from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from primitive_custody.application.engine import run_to_first_l_and_next_b
from primitive_custody.application.evidence import (
    EXPECTED_CROSSING_WORD,
    EXPECTED_FLOOR_PAIR,
    EXPECTED_NEXT_PAIR,
    summarize,
)
from primitive_custody.domain.law import capacity, positions
from primitive_custody.orthad.boundary import (
    ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED,
)


STATUS_LINES = {
    "PRIMITIVE_FIRST_CROSSING": "PASS",
    "POST_L_CARRY": "PASS",
    "ORTHAD_CHART_RECURRENCE": "NOT_YET_DERIVED",
    "ORTHAD_CAUSAL_PROJECTION": "NOT_RUN",
    "GAUGE_FQM_WEIL_DESCENT": "NOT_RUN",
}

FORBIDDEN_LIVE_LEXEMES = ("search", "scan", "rank", "test")
LIVE_CODE_PARTS = ("src/primitive_custody/orthad",)
UNLICENSED_TRACE_FIELDS = ("floor_operator", "lap_sign", "lap_relation", "carrier_size")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def verify_manifest(root: Path) -> tuple[bool, str]:
    path = root / "MANIFEST.json"
    if not path.exists():
        return False, "MANIFEST.json missing"
    payload = read_json(path)
    entries = payload.get("files")
    if not isinstance(entries, list):
        return False, "manifest files must be a list"
    expected: dict[str, tuple[int, str]] = {}
    for row in entries:
        rel = row.get("path")
        if not isinstance(rel, str) or rel == "MANIFEST.json":
            return False, "invalid manifest path"
        expected[rel] = (int(row.get("bytes", -1)), str(row.get("sha256", "")))
    actual_paths = sorted(
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file() and path.name != "MANIFEST.json"
    )
    if sorted(expected) != actual_paths:
        missing = sorted(set(expected) - set(actual_paths))
        extra = sorted(set(actual_paths) - set(expected))
        return False, f"manifest path mismatch missing={missing} extra={extra}"
    for rel, (size, digest) in expected.items():
        data = (root / rel).read_bytes()
        if len(data) != size:
            return False, f"byte count mismatch: {rel}"
        if sha256_bytes(data) != digest:
            return False, f"sha mismatch: {rel}"
    return True, "ok"


def _gate(name: str, passed: bool, detail: str, status: str = "PASS") -> dict[str, Any]:
    return {
        "gate": name,
        "passed": bool(passed),
        "declared_status": status if passed else "FAIL",
        "detail": detail,
    }


def source_lexeme_gate(root: Path) -> tuple[bool, str]:
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, FORBIDDEN_LIVE_LEXEMES)) + r")\b", re.IGNORECASE)
    hits: list[str] = []
    for part in LIVE_CODE_PARTS:
        base = root / part
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.py")):
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if pattern.search(line):
                    hits.append(f"{path.relative_to(root)}:{number}:{line.strip()}")
    return (not hits), ("ok" if not hits else "; ".join(hits))


def verify_trace_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    gates: list[dict[str, Any]] = []
    lifted, fresh_records = run_to_first_l_and_next_b()
    fresh_rows = [record.to_dict() for record in fresh_records]

    gates.append(_gate(
        "TRACE_ROW_COUNT",
        len(rows) == len(fresh_rows) == 16,
        f"observed={len(rows)} expected=16",
    ))
    step_ids = [row.get("step_index") for row in rows]
    gates.append(_gate(
        "TRACE_UNIQUE_STEP_INDEX",
        step_ids == list(range(1, 17)),
        f"step_ids={step_ids}",
    ))
    prefixes = [row.get("word_prefix") for row in rows]
    gates.append(_gate(
        "TRACE_UNIQUE_COMPLETE_PREFIXES",
        len(prefixes) == len(set(prefixes)) and all(
            prefixes[index] == "".join(str(r.get("primitive")) for r in rows[: index + 1])
            for index in range(len(rows))
        ),
        "prefixes must be unique and equal executed primitive prefixes",
    ))
    unlicensed = []
    for index, row in enumerate(rows, 1):
        for field in UNLICENSED_TRACE_FIELDS:
            if field in row or field in row.get("before", {}) or field in row.get("after", {}):
                unlicensed.append(f"row={index} field={field}")
    gates.append(_gate(
        "NO_INJECTED_FLOOR_OR_LAP_FIELDS",
        not unlicensed,
        "ok" if not unlicensed else "; ".join(unlicensed),
    ))

    exact_rows = rows == fresh_rows
    gates.append(_gate(
        "TRACE_RECOMPUTES_FROM_SOURCE",
        exact_rows,
        "trace equals a fresh source execution" if exact_rows else "trace differs from fresh source execution",
    ))

    capacity_ok = all(
        row.get("capacity_before") == capacity(int(row["before"]["j"]))
        and row.get("available_positions_before") == positions(int(row["before"]["A"]))
        for row in rows
        if isinstance(row.get("before"), dict)
    )
    gates.append(_gate(
        "CAPACITY_AND_DOMAIN_SIZE_DERIVED",
        capacity_ok,
        "capacity and available positions recomputed from A,j",
    ))

    phase_ok = all(
        row["before"].get("phase_label") == ("1", "i", "-1", "-i")[int(row["before"]["phase_quarters"]) % 4]
        and row["after"].get("phase_label") == ("1", "i", "-1", "-i")[int(row["after"]["phase_quarters"]) % 4]
        for row in rows
        if isinstance(row.get("before"), dict) and isinstance(row.get("after"), dict)
    )
    gates.append(_gate(
        "PHASE_LABEL_DERIVED_FROM_Q_COUNT",
        phase_ok,
        "phase labels match phase_quarters modulo four",
    ))

    return gates


def verify_root(root: Path, *, check_manifest: bool = True) -> dict[str, Any]:
    stamp = read_json(root / "outputs/20260711_072509_run_metadata.json").get("run_stamp")
    trace_path = root / "trace/20260711_072509_primitive_first_crossing_trace.jsonl"
    boundary_path = root / "outputs/20260711_072509_boundary_results.json"
    status_path = root / "outputs/20260711_072509_statuses.json"
    orthad_path = root / "outputs/20260711_072509_orthad_derivation_boundary.json"
    projection_path = root / "outputs/20260711_072509_projection_guard.json"

    gates: list[dict[str, Any]] = []
    if check_manifest:
        ok, detail = verify_manifest(root)
        gates.append(_gate("MANIFEST_INTEGRITY", ok, detail))

    required = [trace_path, boundary_path, status_path, orthad_path, projection_path]
    missing = [str(path.relative_to(root)) for path in required if not path.exists()]
    gates.append(_gate("REQUIRED_EVIDENCE_FILES", not missing, "ok" if not missing else f"missing={missing}"))
    if missing:
        return {"run_stamp": stamp, "gates": gates, "verified": False}

    rows = read_jsonl(trace_path)
    gates.extend(verify_trace_rows(rows))
    boundary = read_json(boundary_path)
    statuses = read_json(status_path)
    orthad = read_json(orthad_path)
    projection = read_json(projection_path)

    fresh_lifted, fresh_records = run_to_first_l_and_next_b()
    fresh_summary = summarize(fresh_records)
    gates.append(_gate(
        "BOUNDARY_EVIDENCE_RECOMPUTED",
        boundary == fresh_summary,
        "boundary JSON equals fresh source summary",
    ))
    gates.append(_gate(
        "EXACT_FIRST_CROSSING_WORD",
        boundary.get("crossing_word") == EXPECTED_CROSSING_WORD,
        f"observed={boundary.get('crossing_word')}",
    ))
    gates.append(_gate(
        "FLOOR_IS_PREDICATE_ONLY",
        boundary.get("floor_reached_before_l") is True
        and "FLOOR" not in str(boundary.get("crossing_word", ""))
        and all(row.get("primitive") in ("B", "Q", "L") for row in rows),
        "L occurs only from floor_reached predicate; FLOOR is absent from word",
    ))
    gates.append(_gate(
        "FLOOR_PAIR_AND_Q_PHASE",
        boundary.get("floor_pair") == list(EXPECTED_FLOOR_PAIR)
        and boundary.get("q_steps") == 5
        and boundary.get("phase_at_boundary") == "i"
        and boundary.get("phase_quarters_at_boundary") == 5,
        f"pair={boundary.get('floor_pair')} q_steps={boundary.get('q_steps')} phase={boundary.get('phase_at_boundary')}",
    ))
    gates.append(_gate(
        "POST_L_PAIR_CARRY",
        boundary.get("post_l_pair") == list(EXPECTED_FLOOR_PAIR),
        f"post_l_pair={boundary.get('post_l_pair')}",
    ))
    gates.append(_gate(
        "POST_L_PHASE_CARRY",
        boundary.get("post_l_phase_quarters") == 5
        and boundary.get("post_l_phase_label") == "i",
        f"post_l_phase_quarters={boundary.get('post_l_phase_quarters')}",
    ))
    gates.append(_gate(
        "POST_L_LOCAL_POSITION_RESET_ONLY",
        boundary.get("post_l_A") == 1
        and boundary.get("post_l_k") == 0
        and boundary.get("post_l_j") == 7,
        f"A={boundary.get('post_l_A')} k={boundary.get('post_l_k')} j={boundary.get('post_l_j')}",
    ))
    gates.append(_gate(
        "FIRST_NEXT_DOMAIN_B",
        boundary.get("first_next_domain_primitive") == "B"
        and boundary.get("first_next_domain_pair") == list(EXPECTED_NEXT_PAIR),
        f"primitive={boundary.get('first_next_domain_primitive')} pair={boundary.get('first_next_domain_pair')}",
    ))

    gates.append(_gate(
        "STATUS_LINES_SEPARATE",
        statuses == STATUS_LINES,
        f"statuses={statuses}",
    ))
    orthad_guard = (
        orthad.get("status") == ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED
        and all(orthad.get(name) is None for name in (
            "primary_pairing", "omega_plus", "omega_minus",
            "transfer_plus_to_minus", "transfer_minus_to_plus",
        ))
    )
    gates.append(_gate(
        "ORTHAD_RECURRENCE_HARD_STOP",
        orthad_guard,
        "all chart objects remain absent under explicit NOT_YET_DERIVED status",
    ))

    matrix_files = list((root / "outputs").glob("*matrix*")) + list((root / "outputs").glob("*omega*"))
    gates.append(_gate(
        "NO_UNDERIVED_MATRIX_EVIDENCE",
        not matrix_files,
        "ok" if not matrix_files else f"unexpected={matrix_files}",
    ))
    projection_files = list((root / "outputs").glob("*channel*")) + list((root / "outputs").glob("*readout*"))
    projection_guard = projection == {
        "status": "NOT_RUN",
        "reason": ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED,
        "channel_addresses": [],
    }
    gates.append(_gate(
        "PROJECTION_REFUSES_UNDERIVED_ORTHAD",
        projection_guard and not projection_files,
        "no projection evidence exists and guard is NOT_RUN",
    ))
    gates.append(_gate(
        "UNIQUE_CHANNEL_ADDRESS_GUARD",
        projection_guard,
        "projection is NOT_RUN; any channel evidence is forbidden until recurrence is derived",
    ))

    lex_ok, lex_detail = source_lexeme_gate(root)
    gates.append(_gate("LIVE_SOURCE_LEXEME_BOUNDARIES", lex_ok, lex_detail))

    forbidden_imports = ("R", "S", "T", "FLOOR")
    word = str(boundary.get("crossing_word", ""))
    gates.append(_gate(
        "PRIMITIVE_ALPHABET_ONLY",
        all(letter in ("B", "Q", "L") for letter in word)
        and not any(token in word for token in forbidden_imports),
        f"word={word}",
    ))

    passed = all(gate["passed"] for gate in gates)
    return {
        "run_stamp": stamp,
        "gates": gates,
        "verified": passed,
        "statuses": statuses,
        "fresh_boundary": fresh_summary,
        "orthad_boundary_status": fresh_lifted.orthad_boundary.status,
    }
