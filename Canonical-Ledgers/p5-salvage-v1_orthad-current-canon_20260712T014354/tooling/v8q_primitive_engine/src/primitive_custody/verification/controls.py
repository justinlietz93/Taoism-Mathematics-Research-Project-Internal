from __future__ import annotations

import csv
import json
import shutil
import tempfile
from pathlib import Path
from typing import Callable

from primitive_custody.verification.verifier import verify_root


CONTROL_SPECS = (
    ("manifest_missing_trace", "MANIFEST_INTEGRITY"),
    ("missing_required_file", "REQUIRED_EVIDENCE_FILES"),
    ("duplicate_trace_row", "TRACE_UNIQUE_STEP_INDEX"),
    ("drop_trace_prefix", "TRACE_ROW_COUNT"),
    ("mutate_word_letter", "EXACT_FIRST_CROSSING_WORD"),
    ("reset_pair_after_l", "POST_L_PAIR_CARRY"),
    ("reset_phase_after_l", "POST_L_PHASE_CARRY"),
    ("mutate_next_domain_pair", "FIRST_NEXT_DOMAIN_B"),
    ("hardcode_i_without_q", "PHASE_LABEL_DERIVED_FROM_Q_COUNT"),
    ("fixed_twelve_before_l", "CAPACITY_AND_DOMAIN_SIZE_DERIVED"),
    ("inject_lap_sign", "NO_INJECTED_FLOOR_OR_LAP_FIELDS"),
    ("inject_forbidden_live_lexeme", "LIVE_SOURCE_LEXEME_BOUNDARIES"),
    ("inject_partial_matrix_claim", "NO_UNDERIVED_MATRIX_EVIDENCE"),
    ("inject_duplicate_channel_rows", "PROJECTION_REFUSES_UNDERIVED_ORTHAD"),
)


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))


def _mutate(root: Path, name: str) -> bool:
    trace = root / "trace/20260711_072509_primitive_first_crossing_trace.jsonl"
    boundary = root / "outputs/20260711_072509_boundary_results.json"
    if name == "manifest_missing_trace":
        trace.unlink()
        return True
    if name == "missing_required_file":
        boundary.unlink()
        return True
    if name == "duplicate_trace_row":
        rows = _read_jsonl(trace)
        rows.insert(2, dict(rows[1]))
        _write_jsonl(trace, rows)
        return False
    if name == "drop_trace_prefix":
        rows = _read_jsonl(trace)
        rows.pop(4)
        _write_jsonl(trace, rows)
        return False
    if name == "mutate_word_letter":
        payload = json.loads(boundary.read_text())
        payload["crossing_word"] = "Q" + payload["crossing_word"][1:]
        boundary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return False
    if name == "reset_pair_after_l":
        payload = json.loads(boundary.read_text())
        payload["post_l_pair"] = [1, 1]
        boundary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return False
    if name == "reset_phase_after_l":
        payload = json.loads(boundary.read_text())
        payload["post_l_phase_quarters"] = 0
        payload["post_l_phase_label"] = "1"
        boundary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return False
    if name == "mutate_next_domain_pair":
        payload = json.loads(boundary.read_text())
        payload["first_next_domain_pair"] = [1, 2]
        boundary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return False
    if name == "hardcode_i_without_q":
        rows = _read_jsonl(trace)
        rows[0]["before"]["phase_label"] = "i"
        _write_jsonl(trace, rows)
        return False
    if name == "fixed_twelve_before_l":
        rows = _read_jsonl(trace)
        rows[0]["available_positions_before"] = 12
        _write_jsonl(trace, rows)
        return False
    if name == "inject_lap_sign":
        rows = _read_jsonl(trace)
        rows[0]["lap_sign"] = 1
        _write_jsonl(trace, rows)
        return False
    if name == "inject_forbidden_live_lexeme":
        path = root / "src/primitive_custody/orthad/boundary.py"
        path.write_text(path.read_text() + "\n# search\n")
        return False
    if name == "inject_partial_matrix_claim":
        (root / "outputs/20260711_072509_partial_matrix.json").write_text('{"omega_plus": [[1]]}\n')
        return False
    if name == "inject_duplicate_channel_rows":
        path = root / "outputs/20260711_072509_channel_readout.csv"
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=("address", "value"))
            writer.writeheader()
            writer.writerow({"address": "0", "value": "x"})
            writer.writerow({"address": "0", "value": "x"})
        return False
    raise ValueError(name)


def run_controls(root: Path) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for name, target_gate in CONTROL_SPECS:
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / "package"
            shutil.copytree(root, copy)
            manifest_control = _mutate(copy, name)
            report = verify_root(copy, check_manifest=manifest_control)
            gate = next((row for row in report["gates"] if row["gate"] == target_gate), None)
            fired = gate is not None and gate["passed"] is False
            results.append({
                "control": name,
                "target_gate": target_gate,
                "target_gate_fired": fired,
                "observed_gate": gate,
            })
    return results
