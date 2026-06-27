from __future__ import annotations

import csv, json
from dataclasses import asdict
from pathlib import Path
from typing import List

from .events import Q, B, L, P, Event
from .trace import foata_normal_form, same_trace_class
from .coupling import extract_coupling, matrix_signature
from .telemetry import fold_telemetry
from .echo import coupling_echo_gain

DIMS = {"A": 12, "B": 12, "C": 12}
D = 12
SAMPLES = tuple((i % D, (2*i + 1) % D, (3*i + 2) % D) for i in range(1, 49))


def histories() -> dict[str, list[Event]]:
    # H1/H2 differ only by legal swaps of independent local touches.
    h1 = [Q("A"), Q("B"), L("A","B"), Q("C"), L("B","C"), B("A"), L("A","C", sign=-1), P()]
    h2 = [Q("B"), Q("A"), L("A","B"), Q("C"), L("B","C"), B("A"), L("A","C", sign=-1), P()]
    # H3 is constructed to have the same visible checksum as H1 but different retained C.
    h3 = [Q("A"), Q("B"), Q("C"), L("A","B"), B("A"), L("A","C"), L("B","C"), L("B","C", sign=-1), P()]
    # H4 violates the triangle cocycle/holonomy closure.
    h4 = [Q("A"), Q("B"), Q("C"), L("A","B"), P()]
    return {"H1_legal_base": h1, "H2_legal_swap": h2, "H3_same_projection_diff_history": h3, "H4_illegal_cocycle": h4}


def run(out: Path) -> dict[str, object]:
    out.mkdir(parents=True, exist_ok=True)
    hs = histories()
    rows: List[dict[str, object]] = []
    echo_rows: List[dict[str, object]] = []
    telemetry_rows: List[dict[str, object]] = []
    reports = {}
    for name, evs in hs.items():
        nf = foata_normal_form(evs)
        cr = extract_coupling(evs, DIMS)
        tel = fold_telemetry(evs, cr.cocycle_residual)
        er = coupling_echo_gain(cr.C, D, SAMPLES) if cr.admitted else None
        reports[name] = {
            "normal_form": nf.signature(),
            "coupling": asdict(cr),
            "telemetry": tel.as_dict(),
            "echo": asdict(er) if er else None,
        }
        rows.append({
            "history": name,
            "normal_form": nf.signature(),
            "C_signature": matrix_signature(cr.C),
            "pair_values": json.dumps(cr.pair_values, sort_keys=True),
            "visible_projection": cr.visible_projection,
            "holonomy": cr.holonomy,
            "cocycle_residual": cr.cocycle_residual,
            "admitted": cr.admitted,
            "gauge_signature": cr.gauge_signature,
        })
        if er:
            echo_rows.append({"history": name, **asdict(er)})
        telemetry_rows.append({
            "history": name,
            "boundary_spikes": tel.boundary_spikes,
            "cycle_hits": tel.cycle_hits,
            "topology_spikes": tel.topology_spikes,
            "heat": json.dumps(tel.heat, sort_keys=True),
            "excitation": json.dumps(tel.excitation, sort_keys=True),
            "inhibition": json.dumps(tel.inhibition, sort_keys=True),
            "memory": json.dumps(tel.memory, sort_keys=True),
        })
    with (out / "history_coupling_reports.json").open("w") as f:
        json.dump(reports, f, indent=2, sort_keys=True)
    for filename, data in [("history_summary.csv", rows), ("echo_gain.csv", echo_rows), ("telemetry_summary.csv", telemetry_rows)]:
        with (out / filename).open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            w.writeheader(); w.writerows(data)
    h1, h2, h3, h4 = hs["H1_legal_base"], hs["H2_legal_swap"], hs["H3_same_projection_diff_history"], hs["H4_illegal_cocycle"]
    r1, r2, r3, r4 = [extract_coupling(h, DIMS) for h in [h1,h2,h3,h4]]
    e1 = coupling_echo_gain(r1.C, D, SAMPLES)
    e2 = coupling_echo_gain(r2.C, D, SAMPLES)
    e3 = coupling_echo_gain(r3.C, D, SAMPLES)
    gates = {
        "legal_rewrite_invariance": same_trace_class(h1,h2) and matrix_signature(r1.C) == matrix_signature(r2.C),
        "same_projection_different_retained_history": r1.visible_projection == r3.visible_projection and matrix_signature(r1.C) != matrix_signature(r3.C),
        "illegal_cocycle_rejected": not r4.admitted and r4.cocycle_residual != 0,
        "positive_coupling_echo_gain": min(e1.ceg, e2.ceg, e3.ceg) > 0.05,
        "telemetry_flags_bad_history": fold_telemetry(h4, r4.cocycle_residual).topology_spikes == 1,
    }
    result_card = {
        "status": "SMOKE_SUPPORTED_WORTH_PURSUING_NOT_A_THEOREM",
        "global_pass": all(gates.values()),
        "gates": gates,
        "median_admitted_ceg": sorted([e1.ceg, e2.ceg, e3.ceg])[1],
        "max_cocycle_residual_admitted": max(r.cocycle_residual for r in [r1,r2,r3] if r.admitted),
        "negative_control_cocycle_residual": r4.cocycle_residual,
        "interpretation": "VDM-style telemetry plus coupling echo is worth pursuing as a compiler/test layer; it does not replace the external theorem path.",
    }
    with (out / "result_card.json").open("w") as f:
        json.dump(result_card, f, indent=2, sort_keys=True)
    return result_card
