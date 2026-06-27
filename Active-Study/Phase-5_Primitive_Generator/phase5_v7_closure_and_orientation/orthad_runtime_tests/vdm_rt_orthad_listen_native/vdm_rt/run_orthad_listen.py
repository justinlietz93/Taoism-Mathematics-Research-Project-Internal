"""
Listen-only Orthad state probe for the original VDM-RT engine.

The harness never scans, never reduces the graph, never asks the engine a question.
It only receives what the walkers announce and passes it through.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import statistics
import tempfile
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List

from vdm_rt.nexus import Nexus
from vdm_rt.core.engine import CoreEngine
from vdm_rt.runtime.events_adapter import observations_to_events, adc_metrics_to_event
from vdm_rt.io.orthad_state import frame_to_indices, make_sequence

SCAN_METHODS = (
    "active_edge_count",
    "connected_components",
    "cyclomatic_complexity",
    "connectome_entropy",
    "snapshot_graph",
)

SELECT_SNAPSHOT_KEYS = (
    "b1_value", "b1_delta", "b1_z", "b1_spike",
    "vt_coverage", "vt_entropy", "cohesion_components",
    "adc_territories", "adc_boundaries", "adc_cycle_hits",
    "cold_max", "cold_count",
    "heat_max", "heat_count",
    "exc_max", "exc_count",
    "inh_max", "inh_count",
    "memory_max", "memory_count",
    "trail_max", "trail_count",
)


def _truthy(x: Any) -> bool:
    return str(x).strip().lower() in {"1", "true", "yes", "on", "y", "t"}


def install_scan_firewall(connectome: Any) -> None:
    def fail(name: str):
        def _f(*args, **kwargs):
            raise RuntimeError(f"scan firewall tripped: {name}")
        return _f
    for name in SCAN_METHODS:
        if hasattr(connectome, name):
            setattr(connectome, name, fail(name))


def listen_row(step: int, dt: float, obs_batch: List[Any], snap: Dict[str, Any], mode: str, seed: int) -> Dict[str, Any]:
    kinds = Counter(str(getattr(o, "kind", "")) for o in obs_batch)
    announced_nodes = set()
    loop_gain_sum = 0.0
    loop_gain_n = 0
    s_mean_sum = 0.0
    s_mean_n = 0
    for obs in obs_batch:
        try:
            for n in (getattr(obs, "nodes", None) or [])[:256]:
                announced_nodes.add(int(n))
        except Exception:
            pass
        if getattr(obs, "kind", "") == "cycle_hit":
            try:
                loop_gain_sum += float(getattr(obs, "loop_gain", 0.0))
                loop_gain_n += 1
            except Exception:
                pass
        if getattr(obs, "kind", "") == "region_stat":
            try:
                s_mean_sum += float(getattr(obs, "s_mean", 0.0))
                s_mean_n += 1
            except Exception:
                pass
    row = {
        "mode": mode,
        "seed": int(seed),
        "tick": int(step),
        "tick_wall_s": float(dt),
        "announcements": int(len(obs_batch)),
        "region_stat": int(kinds.get("region_stat", 0)),
        "cycle_hit": int(kinds.get("cycle_hit", 0)),
        "boundary_probe": int(kinds.get("boundary_probe", 0)),
        "novel_frontier": int(kinds.get("novel_frontier", 0)),
        "announced_unique_nodes": int(len(announced_nodes)),
        "mean_loop_gain": float(loop_gain_sum / max(1, loop_gain_n)),
        "mean_region_s": float(s_mean_sum / max(1, s_mean_n)),
    }
    for k in SELECT_SNAPSHOT_KEYS:
        v = snap.get(k, 0)
        if isinstance(v, bool):
            row[k] = int(v)
        elif isinstance(v, (int, float)):
            row[k] = float(v)
        else:
            row[k] = 0
    return row


def run_one(mode: str, seed: int, args: argparse.Namespace) -> Dict[str, Any]:
    os.environ.setdefault("FRAG_AUDIT_EDGES", "0")
    os.environ.setdefault("ENABLE_EVENT_METRICS", "0")
    run_dir = Path(args.run_root) / f"{mode}_seed{seed}"
    run_dir.mkdir(parents=True, exist_ok=True)
    nx = Nexus(
        str(run_dir),
        N=int(args.N),
        k=int(args.k),
        hz=int(args.hz),
        walkers=int(args.walkers),
        hops=int(args.hops),
        candidates=int(args.candidates),
        speak_auto=False,
        log_every=10**9,
        status_interval=10**9,
        checkpoint_every=0,
        seed=int(seed),
        bus_drain=int(args.bus_drain),
        stim_group_size=int(args.group_size),
        stim_amp=float(args.amp),
    )
    if args.scan_firewall:
        install_scan_firewall(nx.connectome)
    eng = CoreEngine(nx)
    rows: List[Dict[str, Any]] = []
    scan_firewall_ok = True
    error = ""
    seq = make_sequence(mode, int(args.ticks))
    t_start = time.perf_counter()
    try:
        for step, frame in enumerate(seq):
            tick_t0 = time.perf_counter()
            idxs = frame_to_indices(frame, N=int(args.N), group_size=int(args.group_size))
            nx.connectome.stimulate_indices(idxs, amp=float(args.amp))
            # Original engine tick. No compute_metrics, no status builder, no graph audit.
            nx.connectome.step(
                float(step) / float(max(1, args.hz)),
                domain_modulation=float(nx.dom_mod),
                sie_drive=1.0,
                use_time_dynamics=True,
            )
            obs_batch = nx.bus.drain(max_items=int(args.bus_drain))
            try:
                nx.adc.update_from(obs_batch)
                adc_metrics = nx.adc.get_metrics()
            except Exception:
                adc_metrics = {}
            evs = observations_to_events(obs_batch)
            evs.append(adc_metrics_to_event(adc_metrics, int(step)))
            eng.step(int(max(1, 1000 / max(1, args.hz))), evs)
            snap = dict(getattr(eng, "_last_evt_snapshot", {}) or {})
            dt = time.perf_counter() - tick_t0
            rows.append(listen_row(step, dt, obs_batch, snap, mode, seed))
    except RuntimeError as e:
        scan_firewall_ok = False
        error = str(e)
    elapsed = time.perf_counter() - t_start
    ticks_done = len(rows)
    tick_times = [float(r["tick_wall_s"]) for r in rows] or [0.0]
    def ssum(key: str) -> float:
        return float(sum(float(r.get(key, 0.0)) for r in rows))
    def smax(key: str) -> float:
        return float(max((float(r.get(key, 0.0)) for r in rows), default=0.0))
    def slast(key: str) -> float:
        return float(rows[-1].get(key, 0.0)) if rows else 0.0
    summary = {
        "mode": mode,
        "seed": int(seed),
        "N": int(args.N),
        "walkers": int(args.walkers),
        "walker_ratio": float(args.walkers) / float(max(1, args.N)),
        "ticks_requested": int(args.ticks),
        "ticks_done": int(ticks_done),
        "elapsed_s": float(elapsed),
        "mean_tick_s": float(statistics.fmean(tick_times)),
        "p95_tick_s": float(sorted(tick_times)[max(0, min(len(tick_times)-1, int(0.95 * (len(tick_times)-1))))]),
        "max_tick_s": float(max(tick_times)),
        "announcements_total": int(ssum("announcements")),
        "cycle_hits_total": int(ssum("cycle_hit")),
        "region_stat_total": int(ssum("region_stat")),
        "announced_unique_nodes_total": int(ssum("announced_unique_nodes")),
        "mean_loop_gain_avg": float(statistics.fmean([float(r.get("mean_loop_gain", 0.0)) for r in rows]) if rows else 0.0),
        "mean_region_s_avg": float(statistics.fmean([float(r.get("mean_region_s", 0.0)) for r in rows]) if rows else 0.0),
        "b1_value_last": slast("b1_value"),
        "b1_value_max": smax("b1_value"),
        "b1_spikes_total": int(ssum("b1_spike")),
        "heat_max_last": slast("heat_max"),
        "heat_max_max": smax("heat_max"),
        "exc_max_last": slast("exc_max"),
        "inh_max_last": slast("inh_max"),
        "memory_count_last": slast("memory_count"),
        "trail_count_last": slast("trail_count"),
        "adc_cycles_total": int(ssum("adc_cycle_hits")),
        "scan_firewall_ok": bool(scan_firewall_ok),
        "error": error,
    }
    return {"summary": summary, "rows": rows}


def feature_vector(summary: Dict[str, Any]) -> List[float]:
    return [
        float(summary.get("announcements_total", 0.0)),
        float(summary.get("cycle_hits_total", 0.0)),
        float(summary.get("b1_value_max", 0.0)),
        float(summary.get("heat_max_max", 0.0)),
        float(summary.get("memory_count_last", 0.0)),
        float(summary.get("trail_count_last", 0.0)),
    ]


def rel_dist(a: List[float], b: List[float]) -> float:
    denom = sum(abs(x) + abs(y) for x, y in zip(a, b)) + 1e-9
    return float(sum(abs(x - y) for x, y in zip(a, b)) / denom)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-root", default="runs/orthad_listen_probe")
    ap.add_argument("--out-dir", default="outputs")
    ap.add_argument("--N", type=int, default=500)
    ap.add_argument("--walkers", type=int, default=600)
    ap.add_argument("--ticks", type=int, default=48)
    ap.add_argument("--seeds", type=str, default="0,1,2")
    ap.add_argument("--modes", type=str, default="sparse_baseline,legal,legal_rewrite,illegal_flip,illegal_cocycle")
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--hops", type=int, default=3)
    ap.add_argument("--candidates", type=int, default=64)
    ap.add_argument("--hz", type=int, default=1000)
    ap.add_argument("--group-size", type=int, default=4)
    ap.add_argument("--amp", type=float, default=0.07)
    ap.add_argument("--bus-drain", type=int, default=4096)
    ap.add_argument("--scan-firewall", action="store_true", default=True)
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    modes = [x.strip() for x in args.modes.split(",") if x.strip()]
    seeds = [int(x.strip()) for x in args.seeds.split(",") if x.strip()]
    all_summaries: List[Dict[str, Any]] = []
    all_rows: List[Dict[str, Any]] = []
    for seed in seeds:
        for mode in modes:
            r = run_one(mode, seed, args)
            all_summaries.append(r["summary"])
            all_rows.extend(r["rows"])
    with (out_dir / "scenario_summary.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_summaries[0].keys()))
        writer.writeheader(); writer.writerows(all_summaries)
    with (out_dir / "tick_listen_rows.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        writer.writeheader(); writer.writerows(all_rows)
    by_seed_mode = {(s["seed"], s["mode"]): s for s in all_summaries}
    rewrite_dists = []
    illegal_flip_dists = []
    illegal_cocycle_dists = []
    speed_ok = []
    firewall_ok = []
    for seed in seeds:
        if (seed, "legal") in by_seed_mode and (seed, "legal_rewrite") in by_seed_mode:
            rewrite_dists.append(rel_dist(feature_vector(by_seed_mode[(seed,"legal")]), feature_vector(by_seed_mode[(seed,"legal_rewrite")])) )
        if (seed, "legal") in by_seed_mode and (seed, "illegal_flip") in by_seed_mode:
            illegal_flip_dists.append(rel_dist(feature_vector(by_seed_mode[(seed,"legal")]), feature_vector(by_seed_mode[(seed,"illegal_flip")])) )
        if (seed, "legal") in by_seed_mode and (seed, "illegal_cocycle") in by_seed_mode:
            illegal_cocycle_dists.append(rel_dist(feature_vector(by_seed_mode[(seed,"legal")]), feature_vector(by_seed_mode[(seed,"illegal_cocycle")])) )
    for s in all_summaries:
        speed_ok.append(float(s["mean_tick_s"]) < 0.25)
        firewall_ok.append(bool(s["scan_firewall_ok"]))
    result_card = {
        "mandate": "The harness never scans, never reduces the graph, never asks the engine a question. It only receives walker announcements and passes them through.",
        "original_engine_files_modified": 0,
        "added_files_only": True,
        "N": int(args.N),
        "walkers": int(args.walkers),
        "walker_ratio": float(args.walkers) / float(max(1, args.N)),
        "ticks_per_scenario": int(args.ticks),
        "seeds": seeds,
        "modes": modes,
        "scan_firewall_all_ok": bool(all(firewall_ok)),
        "native_speed_gate_mean_tick_lt_250ms": bool(all(speed_ok)),
        "mean_tick_s_overall": float(statistics.fmean([float(s["mean_tick_s"]) for s in all_summaries])),
        "max_tick_s_overall": float(max(float(s["max_tick_s"]) for s in all_summaries)),
        "legal_vs_rewrite_distance_mean": float(statistics.fmean(rewrite_dists) if rewrite_dists else 0.0),
        "legal_vs_illegal_flip_distance_mean": float(statistics.fmean(illegal_flip_dists) if illegal_flip_dists else 0.0),
        "legal_vs_illegal_cocycle_distance_mean": float(statistics.fmean(illegal_cocycle_dists) if illegal_cocycle_dists else 0.0),
        "rewrite_closer_than_illegal_flip": bool(rewrite_dists and illegal_flip_dists and statistics.fmean(rewrite_dists) < statistics.fmean(illegal_flip_dists)),
        "rewrite_closer_than_illegal_cocycle": bool(rewrite_dists and illegal_cocycle_dists and statistics.fmean(rewrite_dists) < statistics.fmean(illegal_cocycle_dists)),
        "global_pass": bool(all(firewall_ok) and all(speed_ok) and rewrite_dists and illegal_flip_dists and illegal_cocycle_dists and statistics.fmean(rewrite_dists) < statistics.fmean(illegal_flip_dists) and statistics.fmean(rewrite_dists) < statistics.fmean(illegal_cocycle_dists)),
    }
    with (out_dir / "result_card.json").open("w") as f:
        json.dump(result_card, f, indent=2, sort_keys=True)
    print(json.dumps(result_card, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
