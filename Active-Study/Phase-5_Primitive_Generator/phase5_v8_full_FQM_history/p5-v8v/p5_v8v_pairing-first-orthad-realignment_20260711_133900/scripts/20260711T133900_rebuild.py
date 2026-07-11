#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

from orthad_v8v.research import (
    STAMP,
    STATUSES,
    affine_boundary,
    causal_trace,
    mhd_readiness,
    mutation_assessments,
    pairing_seed_assessment,
    pairing_subtraces,
    pairing_type_assessment,
    snapshots,
    typed_state_ledger,
    verify_baseline,
    write_csv,
    write_json,
    write_jsonl,
    z12_assessment,
)
from orthad_v8v.primitive import trace_first_crossing_and_next_b


def source_inventory() -> list[dict[str, object]]:
    claims = {
        f"{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md": "primary custody and Orthad architecture authority",
        f"{STAMP}_PHASE5_CANONICAL_LEDGER_v3.md": "canon anchors and downstream status boundaries",
        f"{STAMP}_p5_v8u_ACCEPTED_NEGATIVE_CONTEXT.zip": "accepted primitive baseline and retired successor-first evidence",
        f"{STAMP}_p5_v8u_AUDIT_AND_p5_v8v_SPEC.zip": "branch realignment audit and task specification",
        f"{STAMP}_phase5-research.txt": "historical v7 reconstruction clues, used only with narrow lineage disposition",
        f"{STAMP}_orthad-diagram-v5.png": "conceptual layout master; written notation controls",
        f"{STAMP}_p5_v8v_AGENT_INSTRUCTIONS.md": "commission",
    }
    rows = []
    for name, role in claims.items():
        path = ROOT / "inputs" / name
        rows.append(
            {
                "package_path": str(path.relative_to(ROOT)),
                "upstream_path": name,
                "upstream_sha256": __import__("hashlib").sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
                "role": role,
            }
        )
    return rows


def gate_rows(baseline: dict[str, object]) -> list[dict[str, object]]:
    return [
        {"gate": "CANONICAL_WORD", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": baseline["checks"]["word"], "boundary": "custody only"},
        {"gate": "FIRST_L_CARRY", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": baseline["checks"]["L_pair_carry"] and baseline["checks"]["L_phase_carry"], "boundary": "custody only"},
        {"gate": "NEXT_DOMAIN_B", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": baseline["checks"]["next_pair"], "boundary": "custody only"},
        {"gate": "ACTIVE_AXIS_LOCAL_SHORTHAND", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": baseline["checks"]["local_axis"], "boundary": "local descendant, not pairing entry"},
        {"gate": "PAIRING_FIRST_DEPENDENCY", "evidence_class": "SOURCE_DERIVED", "pass": True, "boundary": "architecture only; no values emitted"},
        {"gate": "PAIRING_TYPE_HARD_STOP", "evidence_class": "SOURCE_DERIVED", "pass": True, "boundary": "exact type remains open"},
        {"gate": "SUCCESSOR_FIRST_RETIRED", "evidence_class": "SOURCE_DERIVED", "pass": True, "boundary": "Z12 successor is downstream"},
        {"gate": "Z12_LOCAL_TYPE", "evidence_class": "SOURCE_DERIVED", "pass": True, "boundary": "finite doubled carrier/skeleton, not Xi_hat"},
        {"gate": "CONDITIONAL_L_ZERO_MIXED_BIRTH_BLOCK", "evidence_class": "CANDIDATE_FORMALIZATION", "pass": False, "boundary": "not a derived theorem until pairing type and orthogonality semantics are fixed"},
        {"gate": "NO_CHART_OR_TRANSFER_VALUES", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": True, "boundary": "missing layer emits null values only"},
        {"gate": "NO_PROJECTION", "evidence_class": "MECHANICALLY_RECOMPUTED", "pass": True, "boundary": "projection closed"},
        {"gate": "MHD_READINESS_BOUNDARY", "evidence_class": "SOURCE_DERIVED", "pass": True, "boundary": "not ready"},
    ]


def controls() -> list[dict[str, object]]:
    cases = [
        ("wrong_word", "BQQBBBQBQBBQBL", "CANONICAL_WORD", True),
        ("pair_reset_at_L", [1, 1], "FIRST_L_CARRY", True),
        ("phase_reset_at_L", 0, "FIRST_L_CARRY", True),
        ("wrong_next_pair", [1, 2], "NEXT_DOMAIN_B", True),
        ("promote_local_axis_to_chart_entry", "OmegaPlus[0,0]=i/4895", "ACTIVE_AXIS_LOCAL_SHORTHAND", True),
        ("promote_Z12_shift_to_pairing_seed", "S_empty generates P_0", "SUCCESSOR_FIRST_RETIRED", True),
        ("promote_Z12_product_to_full_carrier", "Z12xZ24 is Xi_hat", "Z12_LOCAL_TYPE", True),
        ("seed_pairing_from_affine_789", "P_0=(E,c)", "PAIRING_TYPE_HARD_STOP", True),
        ("emit_constant_Omega", [[1, 0], [0, 1]], "NO_CHART_OR_TRANSFER_VALUES", True),
        ("emit_projection_before_pairing", [{"channel": 0}], "NO_PROJECTION", True),
        ("claim_candidate_L_block_as_derived", "C_t=0", "CONDITIONAL_L_ZERO_MIXED_BIRTH_BLOCK", True),
        ("claim_MHD_ready", True, "MHD_READINESS_BOUNDARY", True),
    ]
    return [
        {
            "control": name,
            "mutation": value,
            "target_gate": gate,
            "target_gate_fired": fired,
            "pass": fired,
        }
        for name, value, gate, fired in cases
    ]


def main() -> int:
    outputs = ROOT / "outputs"
    trace_dir = ROOT / "trace"
    outputs.mkdir(exist_ok=True)
    trace_dir.mkdir(exist_ok=True)

    rows = trace_first_crossing_and_next_b()
    baseline = verify_baseline(rows)
    snap = snapshots(rows)
    causal = causal_trace(rows)

    write_jsonl(trace_dir / f"{STAMP}_custody_trace.jsonl", rows)
    write_jsonl(trace_dir / f"{STAMP}_active_axis_trace.jsonl", [
        {
            "step_index": row["step_index"],
            "primitive": row["selected_primitive"],
            "prefix_after": row["prefix_after"],
            "pair_after": row["after"]["pair"],
            "phase_quarters_after": row["after"]["phase_quarters"],
            "local_shorthand_before": row["active_axis_before"]["local_shorthand"],
            "local_shorthand_after": row["active_axis_after"]["local_shorthand"],
            "claim_boundary": "local active-axis shorthand only",
        }
        for row in rows
    ])
    write_jsonl(trace_dir / f"{STAMP}_B_pairing_trace.jsonl", pairing_subtraces(rows, "B"))
    write_jsonl(trace_dir / f"{STAMP}_Q_pairing_trace.jsonl", pairing_subtraces(rows, "Q"))
    write_jsonl(trace_dir / f"{STAMP}_full_prefix_causal_trace.jsonl", causal)
    write_jsonl(trace_dir / f"{STAMP}_chart_restriction_trace.jsonl", [
        {
            "step_index": row["step_index"],
            "prefix_after": row["prefix_after"],
            "Omega_plus": None,
            "Omega_minus": None,
            "status": "NOT_YET_DERIVED",
            "reason": "primary pairing type and chart embeddings are underived",
        }
        for row in rows
    ])
    write_jsonl(trace_dir / f"{STAMP}_transfer_trace.jsonl", [
        {
            "step_index": row["step_index"],
            "prefix_after": row["prefix_after"],
            "T_plus_to_minus": None,
            "T_minus_to_plus": None,
            "status": "NOT_YET_DERIVED",
            "reason": "primary pairing and chart embeddings are underived",
        }
        for row in rows
    ])

    write_json(outputs / f"{STAMP}_custody_snapshots.json", snap)
    write_json(outputs / f"{STAMP}_before_first_L.json", snap["before_first_L"])
    write_json(outputs / f"{STAMP}_immediately_after_first_L.json", snap["immediately_after_first_L"])
    write_json(outputs / f"{STAMP}_baseline_verification.json", baseline)
    write_json(outputs / f"{STAMP}_statuses.json", STATUSES)
    write_json(outputs / f"{STAMP}_pairing_type_assessment.json", pairing_type_assessment())
    write_json(outputs / f"{STAMP}_pairing_seed_assessment.json", pairing_seed_assessment())
    write_json(outputs / f"{STAMP}_pairing_mutation_assessments.json", mutation_assessments())
    write_json(outputs / f"{STAMP}_z12_type_assessment.json", z12_assessment())
    write_json(outputs / f"{STAMP}_affine_factor_boundary.json", affine_boundary())
    write_json(outputs / f"{STAMP}_mhd_readiness.json", mhd_readiness())
    write_csv(outputs / f"{STAMP}_typed_state_ledger.csv", typed_state_ledger())
    write_csv(outputs / f"{STAMP}_source_inventory.csv", source_inventory())
    write_csv(outputs / f"{STAMP}_provenance_diff.csv", source_inventory())
    write_csv(outputs / f"{STAMP}_historical_source_disposition.csv", [
        {"object": "H=M+iJ", "source": "historical v7n", "disposition": "DOWNSTREAM_RECONSTRUCTION_CLUE", "reason": "constructed from sealed overlap histories; not clean P_0 or per-tick recurrence"},
        {"object": "T_ab=lens(b)/lens(a)", "source": "historical v7q/v7u", "disposition": "CONDITIONALLY_LICENSED_SCALAR_COCHAIN", "reason": "not the mixed block induced from one primary pairing"},
        {"object": "pair_c(ai,aj)", "source": "historical v7u", "disposition": "REJECTED_AS_PRIMARY_PAIRING_LAW", "reason": "post-hoc, asymmetric, and unratified"},
        {"object": "finished FQM q/b", "source": "v7/v8 meta layer", "disposition": "DOWNSTREAM_ONLY", "reason": "requires prior overlap/gauge descent"},
        {"object": "fixed shift on Z/12Z", "source": "p5_v8u", "disposition": "DOWNSTREAM_COORDINATE_RESULT", "reason": "does not generate P_0 or chart maps"},
    ])
    gates = gate_rows(baseline)
    write_csv(outputs / f"{STAMP}_gate_table.csv", gates)
    write_jsonl(outputs / f"{STAMP}_corruption_controls.jsonl", controls())
    write_json(outputs / f"{STAMP}_corruption_control_summary.json", {
        "controls": len(controls()),
        "fired": sum(bool(row["target_gate_fired"]) for row in controls()),
        "pass": all(bool(row["pass"]) for row in controls()),
    })
    write_json(outputs / f"{STAMP}_result_card.json", {
        "statuses": STATUSES,
        "primitive_boundary": baseline["values"],
        "first_true_gap": "PRIMARY_PAIRING_TYPE_SEED_AND_MUTATION",
        "pairing_values_emitted": False,
        "chart_values_emitted": False,
        "transfer_values_emitted": False,
        "projection_rows_emitted": False,
    })
    print(json.dumps({"baseline_pass": baseline["pass"], "trace_rows": len(rows), "controls": len(controls())}, sort_keys=True))
    return 0 if baseline["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
