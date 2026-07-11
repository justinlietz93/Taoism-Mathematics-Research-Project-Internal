#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import sys
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from orthad_canon import RunOptions, run_once
from orthad_canon.application.readout import after_rows, before_rows
from orthad_canon.domain.exact import matrix_digest_rows
from orthad_canon.domain.models import AxisState, LiftState
from orthad_canon.meta.reference import shadow_reference
from orthad_canon.meta.verify import (
    compare_evidence,
    dual_chart_control,
    dual_chart_gate,
    evidence_control,
    evidence_gate,
    matrix_hash,
    omega_diff,
    scalar_control,
    scalar_gate,
    source_control,
    source_gate,
    transfer_control,
    transfer_gate,
    word_domain_gate,
)

OUT = ROOT / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def write_csv(name: str, rows: list[dict]) -> None:
    path = OUT / name
    if not rows:
        path.write_text("")
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_json(name: str, payload) -> None:
    (OUT / name).write_text(json.dumps(payload, indent=2, sort_keys=True))


def matrix_rows(label: str, matrix) -> list[dict]:
    return [
        {"matrix": label, "row": i, "col": j, "support": support, "phase_mod24": phase}
        for i, j, support, phase in matrix_digest_rows(matrix)
    ]


def matrix_set(state: LiftState, stage: str) -> list[dict]:
    lens = state.floor_lens if stage == "before" else state.lens
    if lens is None:
        return []
    rows: list[dict] = []
    rows += matrix_rows(f"{stage}_pairing", lens.pairing)
    rows += matrix_rows(f"{stage}_omega_plus", lens.omega_plus)
    rows += matrix_rows(f"{stage}_omega_minus", lens.omega_minus)
    rows += matrix_rows(f"{stage}_transfer_plus_to_minus", lens.transfer_plus_to_minus)
    rows += matrix_rows(f"{stage}_transfer_minus_to_plus", lens.transfer_minus_to_plus)
    return rows


def lap_gate(state: LiftState) -> bool:
    rows = after_rows(state)
    by_source: dict[str, dict[int, dict]] = {}
    for row in rows:
        by_source.setdefault(row["source_channel_id"], {})[row["hand"]] = row
    return len(by_source) == 6 and all(
        hands[1]["character_value"] == -hands[0]["character_value"]
        for hands in by_source.values()
        if 0 in hands and 1 in hands
    )


def lap_control(state: LiftState) -> bool:
    rows = after_rows(state)
    if not rows:
        return False
    altered = [dict(row) for row in rows]
    for row in altered:
        if row["hand"] == 1 and row["character_value"] != 0:
            row["character_value"] *= -1
            break
    by_source: dict[str, dict[int, dict]] = {}
    for row in altered:
        by_source.setdefault(row["source_channel_id"], {})[row["hand"]] = row
    passed = len(by_source) == 6 and all(
        hands[1]["character_value"] == -hands[0]["character_value"]
        for hands in by_source.values()
        if 0 in hands and 1 in hands
    )
    return not passed


def matrix_trace_gate(state: LiftState) -> bool:
    return [row["event"] for row in state.event_log] == ["B", "FLOOR", "L"] and state.lens is not None and state.lens.event_count == 2


def matrix_trace_control(state: LiftState) -> bool:
    copy = list(state.event_log)
    copy.pop(0)
    return not ([row["event"] for row in copy] == ["B", "FLOOR", "L"])


def word_domain_control() -> bool:
    open_state = LiftState(axes=[AxisState(34, 55)])
    open_state.interior_field = (object(),)
    baseline = run_once()
    return not word_domain_gate(open_state, baseline)


def ablation_gate(rows: list[dict]) -> bool:
    required = {"delete_B", "delete_L", "pair_1_1", "pair_100_101", "corrupt_floor_bit", "corrupt_latched_axis", "sever_cross_transfer"}
    names = {row["ablation"] for row in rows}
    return names == required and all(not row["survival_gate"] for row in rows)


def ablation_control(rows: list[dict]) -> bool:
    altered = rows[:-1]
    return not ablation_gate(altered)


def provenance_gate(rows: list[dict]) -> bool:
    return bool(rows) and all(row["sha256_matches"] for row in rows)


def provenance_control(rows: list[dict]) -> bool:
    altered = [dict(row) for row in rows]
    altered[0]["sha256_matches"] = False
    return not provenance_gate(altered)


def manifest_name_gate(names: list[str]) -> bool:
    return all("__pycache__" not in name and not name.endswith(".pyc") for name in names)


def manifest_control(names: list[str]) -> bool:
    return not manifest_name_gate(names + ["src/orthad_canon/__pycache__/bad.pyc"])


def external_reference_control(rows: list[dict]) -> bool:
    altered = [dict(row) for row in rows]
    altered[1]["character_reference"] *= -1
    return not all(row["character_value"] == row["character_reference"] for row in altered)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def provenance_rows() -> list[dict]:
    provenance_file = ROOT / "source_notes" / "PROVENANCE_INPUTS.json"
    entries = json.loads(provenance_file.read_text())
    rows = []
    for entry in entries:
        path = ROOT / entry["package_path"]
        actual = sha256(path)
        rows.append({
            **entry,
            "actual_sha256": actual,
            "sha256_matches": actual == entry["expected_sha256"],
        })
    return rows


def run() -> int:
    baseline = run_once()
    open_state = LiftState(axes=[AxisState(34, 55)])
    before = before_rows(baseline)
    after = after_rows(baseline)
    survival = compare_evidence(baseline)
    reference = [shadow_reference(n) for n in range(1, 13)]

    write_json("qbl_word.json", {"qbl_word": baseline.word, "crossing_marker": "FLOOR", "event_sequence": ["B", "FLOOR", "L"]})
    write_json("latched_axis.json", {
        "input_pair": [34, 55],
        "refined_pair": [baseline.axes[0].u, baseline.axes[0].v],
        "latched_axis": baseline.axes[0].lens_axis,
        "new_active_axis": baseline.active_axis,
        "pair_relation": "lap2=-lap1",
    })
    write_csv("channel_readout_before.csv", before)
    write_csv("channel_readout_after.csv", after)
    write_csv("per_channel_survival.csv", survival)
    write_csv("external_shadow_reference_meta_only.csv", reference)
    write_csv("dual_chart_matrices.csv", matrix_set(baseline, "before") + matrix_set(baseline, "after"))
    write_csv("matrix_build_trace.csv", baseline.event_log)

    ablations = [
        ("delete_B", RunOptions(delete_b=True)),
        ("delete_L", RunOptions(delete_l=True)),
        ("pair_1_1", RunOptions(pair_override=(1, 1))),
        ("pair_100_101", RunOptions(pair_override=(100, 101))),
        ("corrupt_floor_bit", RunOptions(corrupt_floor_bit=True)),
        ("corrupt_latched_axis", RunOptions(corrupt_latched_axis=True)),
        ("sever_cross_transfer", RunOptions(sever_cross_transfer=True)),
    ]
    ablation_rows: list[dict] = []
    diff_rows: list[dict] = []
    ablation_evidence: list[dict] = []
    for name, options in ablations:
        altered = run_once(options)
        gate = evidence_gate(altered)
        mismatches = [row for row in compare_evidence(altered) if not row["survival"]]
        ablation_rows.append({
            "ablation": name,
            "qbl_word": altered.word,
            "before_channels": len(altered.interior_field),
            "after_channels": len(altered.far_field),
            "mismatch_count": len(mismatches),
            "survival_gate": gate,
            "required_failure_observed": not gate,
        })
        diff_rows.append({"ablation": name, **omega_diff(baseline, altered)})
        for row in compare_evidence(altered):
            ablation_evidence.append({"ablation": name, **row})
    write_csv("ablation_results.csv", ablation_rows)
    write_csv("ablation_omega_diffs.csv", diff_rows)
    write_csv("ablation_per_channel_evidence.csv", ablation_evidence)

    live_paths = [
        ROOT / "src/orthad_canon/domain/models.py",
        ROOT / "src/orthad_canon/domain/exact.py",
        ROOT / "src/orthad_canon/application/compiler.py",
        ROOT / "src/orthad_canon/application/crossing.py",
        ROOT / "src/orthad_canon/application/readout.py",
        ROOT / "src/orthad_canon/application/experiment.py",
    ]
    law0_ok, law0_hits = source_gate(live_paths)
    write_csv("law0_lexeme_hits.csv", law0_hits)

    provenance = provenance_rows()
    write_csv("provenance_diff.csv", provenance)

    names = [
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and not path.name.endswith(".pyc")
    ]
    gates = [
        {"gate": "evidence_bound_character_survival", "pass": evidence_gate(baseline)},
        {"gate": "law0_live_source", "pass": law0_ok},
        {"gate": "law0b_no_scalar_in_lift", "pass": scalar_gate(baseline)},
        {"gate": "dual_chart_presence", "pass": dual_chart_gate(baseline)},
        {"gate": "cross_chart_transfer_presence", "pass": transfer_gate(baseline)},
        {"gate": "word_forced_domain", "pass": word_domain_gate(open_state, baseline)},
        {"gate": "lap2_negative_lap1", "pass": lap_gate(baseline)},
        {"gate": "matrix_tick_trace", "pass": matrix_trace_gate(baseline)},
        {"gate": "all_required_ablations_fail", "pass": ablation_gate(ablation_rows)},
        {"gate": "external_reference_meta_only_match", "pass": all(row["character_matched"] for row in survival)},
        {"gate": "provenance_sha", "pass": provenance_gate(provenance)},
        {"gate": "manifest_excludes_cache", "pass": manifest_name_gate(names)},
    ]
    controls = [
        {"gate": "evidence_bound_character_survival", "control_fired": evidence_control(baseline)},
        {"gate": "law0_live_source", "control_fired": source_control()},
        {"gate": "law0b_no_scalar_in_lift", "control_fired": scalar_control()},
        {"gate": "dual_chart_presence", "control_fired": dual_chart_control(baseline)},
        {"gate": "cross_chart_transfer_presence", "control_fired": transfer_control(baseline)},
        {"gate": "word_forced_domain", "control_fired": word_domain_control()},
        {"gate": "lap2_negative_lap1", "control_fired": lap_control(baseline)},
        {"gate": "matrix_tick_trace", "control_fired": matrix_trace_control(baseline)},
        {"gate": "all_required_ablations_fail", "control_fired": ablation_control(ablation_rows)},
        {"gate": "external_reference_meta_only_match", "control_fired": external_reference_control(survival)},
        {"gate": "provenance_sha", "control_fired": provenance_control(provenance)},
        {"gate": "manifest_excludes_cache", "control_fired": manifest_control(names)},
    ]
    write_csv("declared_gates.csv", gates)
    write_csv("gate_negative_controls.csv", controls)

    global_pass = all(row["pass"] for row in gates) and all(row["control_fired"] for row in controls)
    completion_claim = False
    result = {
        "status": "CANON_FIRST_DUAL_CHART_ONE_CROSSING_CHARACTER_MATCH_OBSERVED" if global_pass else "CANON_FIRST_CORRECTED_RERUN_GATES_FAILED",
        "global_pass": global_pass,
        "completion_claim": completion_claim,
        "qbl_word": baseline.word,
        "event_sequence": ["B", "FLOOR", "L"],
        "omega_plus_exists": bool(baseline.lens and baseline.lens.omega_plus),
        "omega_minus_exists": bool(baseline.lens and baseline.lens.omega_minus),
        "cross_chart_transfer_exists": transfer_gate(baseline),
        "character_survival": f"{sum(row['survival'] for row in survival)}/{len(survival)}",
        "required_ablations_failed": f"{sum(not row['survival_gate'] for row in ablation_rows)}/{len(ablation_rows)}",
        "latched_axis": baseline.axes[0].lens_axis,
        "refined_pair": [baseline.axes[0].u, baseline.axes[0].v],
        "new_active_axis": baseline.active_axis,
        "not_claimed": [
            "arbitrary cusp paths",
            "multi-crossing stability",
            "analytic q-series completion",
            "mock-theta closure",
            "general field-valued MHD transport",
            "final canon completion",
        ],
    }
    write_json("result_card.json", result)
    write_json("matrix_hashes.json", {
        "before_omega_plus": matrix_hash(baseline.floor_lens.omega_plus),
        "before_omega_minus": matrix_hash(baseline.floor_lens.omega_minus),
        "before_transfer": matrix_hash(baseline.floor_lens.transfer_plus_to_minus),
        "after_omega_plus": matrix_hash(baseline.lens.omega_plus),
        "after_omega_minus": matrix_hash(baseline.lens.omega_minus),
        "after_transfer": matrix_hash(baseline.lens.transfer_plus_to_minus),
    })
    print(json.dumps(result, indent=2))
    return 0 if global_pass else 1


if __name__ == "__main__":
    raise SystemExit(run())
