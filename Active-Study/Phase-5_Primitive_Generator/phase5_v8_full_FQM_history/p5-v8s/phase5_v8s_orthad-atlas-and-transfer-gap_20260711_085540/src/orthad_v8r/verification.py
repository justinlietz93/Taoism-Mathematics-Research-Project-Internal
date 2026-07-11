from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from .assessment import assess_recurrence
from .axis import compile_active_axis
from .engine import run_first_crossing_and_next_b
from .evidence import EXPECTED_NEXT_WORD, EXPECTED_WORD, boundary_summary, snapshots
from .oracle import independent_oracle

ALLOWED_OUTPUTS = {
    "boundary_results.json", "custody_snapshots.json", "active_axis_trace.csv",
    "active_axis_trace.json", "recurrence_assessment.json", "overset_consistency.json",
    "statuses.json", "source_constraint_table.csv", "test_results.json",
    "control_results.csv", "control_results.json", "gate_results.csv", "gate_results.json",
    "notebook_execution.json", "lean_compile_status.json", "reproducibility_comparison.json",
    "source_provenance.csv", "build_environment.json",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def gate(name: str, passed: bool, detail: str) -> dict[str, object]:
    return {"gate": name, "passed": bool(passed), "detail": detail}


def verify_manifest(root: Path) -> tuple[bool, str]:
    manifest = load_json(root / "MANIFEST.json")
    expected = {row["path"]: row for row in manifest["files"]}
    actual = {}
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != "MANIFEST.json" and "__pycache__" not in path.parts and path.suffix != ".pyc":
            rel = path.relative_to(root).as_posix()
            actual[rel] = {"bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    if set(expected) != set(actual):
        return False, f"path-set mismatch missing={sorted(set(expected)-set(actual))} extra={sorted(set(actual)-set(expected))}"
    for rel, got in actual.items():
        row = expected[rel]
        if row["bytes"] != got["bytes"] or row["sha256"] != got["sha256"]:
            return False, f"mismatch={rel}"
    return True, f"{len(actual)}/{len(actual)} files verified"


def verify_zip_hash(zip_path: Path, sha_path: Path) -> tuple[bool, str]:
    expected = sha_path.read_text().strip().split()[0]
    actual = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    return actual == expected, f"expected={expected} actual={actual}"


def _trace_schema(row: dict[str, Any]) -> bool:
    exact = {
        "step_index", "primitive", "before", "after", "can_b_before", "can_q_before",
        "floor_reached_before", "capacity_before", "available_positions_before",
        "next_pair_before", "next_pair_product_before", "word_prefix"
    }
    return set(row) == exact and row["primitive"] in ("B", "Q", "L")


def verify_evidence(root: Path, check_manifest: bool = True) -> list[dict[str, object]]:
    g: list[dict[str, object]] = []
    ts = root.name.split("_")[-2] + "_" + root.name.split("_")[-1]
    compact = ts.replace("_", "T")
    trace_path = root / "trace" / f"{compact}_primitive_trace.jsonl"
    output = root / "outputs"
    required = [
        trace_path,
        output / f"{compact}_boundary_results.json",
        output / f"{compact}_custody_snapshots.json",
        output / f"{compact}_active_axis_trace.json",
        output / f"{compact}_recurrence_assessment.json",
        output / f"{compact}_statuses.json",
        output / f"{compact}_test_results.json",
        output / f"{compact}_control_results.json",
        output / f"{compact}_notebook_execution.json",
        output / f"{compact}_lean_compile_status.json",
        output / f"{compact}_reproducibility_comparison.json",
    ]
    g.append(gate("REQUIRED_FILES", all(p.is_file() for p in required), f"present={sum(p.is_file() for p in required)}/{len(required)}"))
    if not all(p.is_file() for p in required):
        return g
    rows = load_jsonl(trace_path)
    g.append(gate("TRACE_SCHEMA", len(rows) == 16 and all(_trace_schema(row) for row in rows), f"rows={len(rows)}"))
    g.append(gate("TRACE_UNIQUE_STEPS", [r["step_index"] for r in rows] == list(range(1, 17)), "step indices 1..16"))
    g.append(gate("TRACE_PREFIXES", all(r["word_prefix"] == "".join(x["primitive"] for x in rows[:i+1]) for i, r in enumerate(rows)), "all prefixes complete"))
    fresh_state, fresh_records = run_first_crossing_and_next_b()
    fresh_rows = [r.to_dict() for r in fresh_records]
    g.append(gate("ENGINE_EVIDENCE_RECOMPUTED", rows == fresh_rows, "trace equals fresh engine run"))
    oracle = independent_oracle()
    oracle_projection = [{k: r[k] for k in ("step_index","primitive","word_prefix","capacity_before","available_positions_before")} for r in oracle]
    engine_projection = [{k: r[k] for k in ("step_index","primitive","word_prefix","capacity_before","available_positions_before")} for r in rows]
    g.append(gate("INDEPENDENT_ORACLE_MATCH", oracle_projection == engine_projection, "oracle and engine agree on 16 steps"))
    boundary = load_json(output / f"{compact}_boundary_results.json")
    g.append(gate("EXACT_WORD", boundary["word"] == EXPECTED_WORD, f"word={boundary['word']}"))
    g.append(gate("FIRST_FLOOR_BOUNDARY", boundary["floor_pair"] == [55,89] and boundary["floor_product"] == 4895 and boundary["q_steps"] == 5 and boundary["phase_at_boundary"] == "i", str(boundary)))
    g.append(gate("FIRST_L_CARRY", boundary["after_L"]["pair"] == [55,89] and boundary["after_L"]["phase_quarters"] == 5 and boundary["after_L"]["A"] == 1 and boundary["after_L"]["k"] == 0 and boundary["after_L"]["j"] == 7, str(boundary["after_L"])))
    g.append(gate("FIRST_NEXT_DOMAIN_B", boundary["first_next_domain_primitive"] == "B" and boundary["after_first_next_domain_B"]["pair"] == [89,144] and boundary["after_first_next_domain_B"]["word"] == EXPECTED_NEXT_WORD, str(boundary["after_first_next_domain_B"])))
    snaps = load_json(output / f"{compact}_custody_snapshots.json")
    g.append(gate("THREE_NAMED_SNAPSHOTS", set(snaps) == {"before_first_L","immediately_after_first_L","immediately_after_first_next_domain_B"}, f"keys={sorted(snaps)}"))
    axis = load_json(output / f"{compact}_active_axis_trace.json")
    fresh_axis = [r.to_dict() for r in compile_active_axis(fresh_records)]
    g.append(gate("ACTIVE_AXIS_RECURRENCE", axis["rows"] == fresh_axis and axis["rows"][13]["active_axis"] == "i/4895" and axis["rows"][14]["latched_axis"] == "i/4895" and axis["rows"][14]["active_axis"] == "1", "Domain-0 shorthand and L mutation recomputed"))
    assessment = load_json(output / f"{compact}_recurrence_assessment.json")
    fresh_assessment = assess_recurrence().to_dict()
    g.append(gate("RECURRENCE_HARD_STOP", assessment == fresh_assessment and assessment["primary_pairing_status"] == "NOT_YET_DERIVED", assessment["smallest_missing_equation"]))
    statuses = load_json(output / f"{compact}_statuses.json")
    expected_statuses = {
        "PRIMITIVE_FIRST_CROSSING":"PASS",
        "FIRST_L_CARRY":"PASS",
        "ACTIVE_AXIS_RECURRENCE":"PASS",
        "PRIMARY_PAIRING_RECURRENCE":"NOT_YET_DERIVED",
        "ORTHAD_CHART_RECURRENCE":"NOT_YET_DERIVED",
        "ORTHAD_RANK_EXTENSION":"NOT_YET_DERIVED",
        "ORTHAD_CAUSAL_PROJECTION":"NOT_RUN",
        "GAUGE_FQM_WEIL_DESCENT":"NOT_RUN",
    }
    g.append(gate("SEPARATE_STATUS_LINES", statuses == expected_statuses, str(statuses)))
    produced = {p.name.replace(compact + "_", "") for p in output.iterdir() if p.is_file()}
    g.append(gate("OUTPUT_SCHEMA_ALLOWLIST", produced == ALLOWED_OUTPUTS, f"outputs={sorted(produced)}"))
    forbidden_live = re.compile(r"\b(candidate|ranking|scan|score|best)\b", re.IGNORECASE)
    live_hits = []
    for path in sorted((root / "src/orthad_v8r").glob("*.py")):
        if path.name in {"verification.py", "controls.py"}:
            continue
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if forbidden_live.search(line):
                live_hits.append(f"{path.name}:{number}:{line.strip()}")
    g.append(gate("LIVE_SOURCE_LEXEME_BOUNDARIES", not live_hits, "no forbidden live-path lexemes" if not live_hits else str(live_hits)))
    tests = load_json(output / f"{compact}_test_results.json")
    g.append(gate("PYTEST_RESULT_VALID", tests["exit_status"] == 0 and tests["failed"] == 0 and tests["passed"] == tests["collected"] and tests["collected"] > 0, str(tests)))
    controls = load_json(output / f"{compact}_control_results.json")
    g.append(gate("ALL_CONTROLS_FIRE", controls["fired"] == controls["total"] and controls["total"] > 0, f"{controls['fired']}/{controls['total']}"))
    notebook = load_json(output / f"{compact}_notebook_execution.json")
    g.append(gate("EXECUTED_NOTEBOOK_COMPLETE", notebook["all_code_cells_executed"] is True and notebook["pass_outputs"] == notebook["code_cells"], str(notebook)))
    reproducibility = load_json(output / f"{compact}_reproducibility_comparison.json")
    repro_ok = reproducibility.get("clean_rebuild_status") == "PASS" and reproducibility.get("mismatches", []) == []
    g.append(gate("REPRODUCIBILITY_COMPARISON", repro_ok, str(reproducibility)))
    lean = load_json(output / f"{compact}_lean_compile_status.json")
    lean_ok = lean["status"] in {"COMPILED_PASS", "NOT_COMPILED_TOOL_UNAVAILABLE"} and lean["formal_proof_claimed"] is False
    g.append(gate("LEAN_STATUS_HONEST", lean_ok, str(lean)))
    if check_manifest:
        ok, detail = verify_manifest(root)
        g.append(gate("MANIFEST_INTEGRITY", ok, detail))
    return g


def parse_pytest(output: str, exit_status: int) -> dict[str, object]:
    passed = failed = skipped = errors = 0
    match = re.search(r"(?P<count>\d+) passed", output)
    if match: passed = int(match.group("count"))
    match = re.search(r"(?P<count>\d+) failed", output)
    if match: failed = int(match.group("count"))
    match = re.search(r"(?P<count>\d+) skipped", output)
    if match: skipped = int(match.group("count"))
    match = re.search(r"(?P<count>\d+) error", output)
    if match: errors = int(match.group("count"))
    return {"exit_status": exit_status, "passed": passed, "failed": failed, "skipped": skipped, "errors": errors, "collected": passed + failed + skipped + errors}
