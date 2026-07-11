from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from .verification import verify_evidence

CONTROL_SPECS = (
    ("missing_snapshots", "REQUIRED_FILES"),
    ("duplicate_trace_step", "TRACE_UNIQUE_STEPS"),
    ("mutate_word", "EXACT_WORD"),
    ("reset_pair_at_l", "FIRST_L_CARRY"),
    ("reset_phase_at_l", "FIRST_L_CARRY"),
    ("wrong_next_pair", "FIRST_NEXT_DOMAIN_B"),
    ("hardcoded_i", "ACTIVE_AXIS_RECURRENCE"),
    ("fixed_12_pre_l", "ENGINE_EVIDENCE_RECOMPUTED"),
    ("inject_lap_sign", "TRACE_SCHEMA"),
    ("underived_matrix_file", "OUTPUT_SCHEMA_ALLOWLIST"),
    ("projection_file", "OUTPUT_SCHEMA_ALLOWLIST"),
    ("false_pytest_summary", "PYTEST_RESULT_VALID"),
    ("false_notebook_summary", "EXECUTED_NOTEBOOK_COMPLETE"),
    ("false_reproducibility_summary", "REPRODUCIBILITY_COMPARISON"),
    ("remove_missing_equation", "RECURRENCE_HARD_STOP"),
    ("forbidden_live_lexeme", "LIVE_SOURCE_LEXEME_BOUNDARIES"),
)


def _stamp(root: Path) -> str:
    tail = root.name.rsplit("_", 2)[-2:]
    return "T".join(tail)


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in rows))


def mutate(root: Path, name: str) -> None:
    stamp = _stamp(root)
    trace = root / "trace" / f"{stamp}_primitive_trace.jsonl"
    output = root / "outputs"
    if name == "missing_snapshots":
        (output / f"{stamp}_custody_snapshots.json").unlink(); return
    if name == "duplicate_trace_step":
        rows = _read_jsonl(trace); rows.insert(2, dict(rows[1])); _write_jsonl(trace, rows); return
    if name == "mutate_word":
        p = output / f"{stamp}_boundary_results.json"; d = json.loads(p.read_text()); d["word"] = "Q" + d["word"][1:]; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "reset_pair_at_l":
        p = output / f"{stamp}_boundary_results.json"; d = json.loads(p.read_text()); d["after_L"]["pair"] = [1,1]; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "reset_phase_at_l":
        p = output / f"{stamp}_boundary_results.json"; d = json.loads(p.read_text()); d["after_L"]["phase_quarters"] = 0; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "wrong_next_pair":
        p = output / f"{stamp}_boundary_results.json"; d = json.loads(p.read_text()); d["after_first_next_domain_B"]["pair"] = [1,2]; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "hardcoded_i":
        p = output / f"{stamp}_active_axis_trace.json"; d = json.loads(p.read_text()); d["rows"][0]["active_axis"] = "i"; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "fixed_12_pre_l":
        rows = _read_jsonl(trace); rows[0]["available_positions_before"] = 12; _write_jsonl(trace, rows); return
    if name == "inject_lap_sign":
        rows = _read_jsonl(trace); rows[0]["lap_sign"] = 1; _write_jsonl(trace, rows); return
    if name == "underived_matrix_file":
        (output / f"{stamp}_primary_pairing.json").write_text('{"matrix":[[1]]}'); return
    if name == "projection_file":
        (output / f"{stamp}_projection.json").write_text('{"rows":[]}'); return
    if name == "false_pytest_summary":
        p = output / f"{stamp}_test_results.json"; d = json.loads(p.read_text()); d["failed"] = 1; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "false_notebook_summary":
        p = output / f"{stamp}_notebook_execution.json"; d = json.loads(p.read_text()); d["all_code_cells_executed"] = False; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "false_reproducibility_summary":
        p = output / f"{stamp}_reproducibility_comparison.json"; d = json.loads(p.read_text()); d["clean_rebuild_status"] = "FAIL"; d["mismatches"] = ["control"]; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "remove_missing_equation":
        p = output / f"{stamp}_recurrence_assessment.json"; d = json.loads(p.read_text()); d["smallest_missing_equation"] = ""; p.write_text(json.dumps(d, sort_keys=True)); return
    if name == "forbidden_live_lexeme":
        p = root / "src/orthad_v8r/assessment.py"; p.write_text(p.read_text() + "\n# candidate ranking\n"); return
    raise ValueError(name)


def run_controls(root: Path) -> list[dict[str, object]]:
    out = []
    for name, target in CONTROL_SPECS:
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / root.name
            shutil.copytree(root, copy)
            mutate(copy, name)
            gates = verify_evidence(copy, check_manifest=False)
            observed = next((g for g in gates if g["gate"] == target), None)
            fired = observed is not None and observed["passed"] is False
            out.append({"control": name, "target_gate": target, "target_gate_fired": fired, "observed_detail": None if observed is None else observed["detail"]})
    return out
