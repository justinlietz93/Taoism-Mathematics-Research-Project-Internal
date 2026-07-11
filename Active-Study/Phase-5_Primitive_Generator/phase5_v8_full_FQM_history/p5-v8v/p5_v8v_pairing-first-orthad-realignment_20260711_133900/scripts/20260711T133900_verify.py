#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any

STAMP = "20260711T133900"
ROOT_NAME = "p5_v8v_pairing-first-orthad-realignment_20260711_133900"
EXPECTED_WORD = "BQQBBBQBQBBQBBL"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def package_root(path: Path, temp: Path) -> tuple[Path, Path | None, list[str] | None]:
    if path.is_dir():
        return path.resolve(), None, None
    if not zipfile.is_zipfile(path):
        raise ValueError("target is neither a directory nor a ZIP")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        archive.extractall(temp)
    root = temp / ROOT_NAME
    if not root.is_dir():
        raise ValueError(f"ZIP missing expected root {ROOT_NAME}")
    return root, path.resolve(), names


def independent_oracle() -> list[dict[str, Any]]:
    A, u, v, phase, k, j, word = 0, 1, 1, 0, 0, 1, ""
    rows = []
    saw_l = False
    for step in range(1, 101):
        N = 6 * (2**A)
        cap = 2 if j == 1 else 4 if j == 2 else 2 ** (2 * j)
        next_u, next_v = v, u + v
        can_q = k < N - 1
        can_b = next_u * next_v <= cap if can_q else u * v < cap
        primitive = "B" if can_b else "Q" if can_q else "L"
        before = (A, u, v, phase, k, j, word)
        if primitive == "B":
            u, v = next_u, next_v
        elif primitive == "Q":
            phase += 1
            k += 1
            j += 1
        else:
            A += 1
            k = 0
            j = 1 + 6 * ((2**A) - 1)
        word += primitive
        rows.append({"step": step, "primitive": primitive, "before": before, "after": (A, u, v, phase, k, j, word)})
        if primitive == "L":
            saw_l = True
        elif saw_l:
            return rows
    raise RuntimeError("oracle did not terminate")


def verify_manifest(root: Path, archive_names: list[str] | None) -> tuple[bool, dict[str, Any]]:
    manifest = load_json(root / "MANIFEST.json")
    entries = manifest.get("entries", [])
    manifest_paths = {row["path"] for row in entries}
    actual_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name != "MANIFEST.json"
    }
    hashes_ok = True
    bytes_ok = True
    for row in entries:
        path = root / row["path"]
        if not path.is_file():
            hashes_ok = False
            bytes_ok = False
            continue
        hashes_ok = hashes_ok and sha256(path) == row["sha256"]
        bytes_ok = bytes_ok and path.stat().st_size == row["bytes"]
    archive_set_ok = True
    if archive_names is not None:
        archive_files = {
            name[len(ROOT_NAME) + 1 :]
            for name in archive_names
            if name.startswith(ROOT_NAME + "/") and not name.endswith("/")
        }
        archive_set_ok = archive_files == actual_paths | {"MANIFEST.json"}
    return (
        manifest_paths == actual_paths and hashes_ok and bytes_ok and archive_set_ok,
        {
            "manifest_entries": len(entries),
            "actual_files_excluding_manifest": len(actual_paths),
            "path_set_equal": manifest_paths == actual_paths,
            "hashes_ok": hashes_ok,
            "bytes_ok": bytes_ok,
            "archive_path_set_equal": archive_set_ok,
        },
    )


def verify_trace(root: Path) -> tuple[bool, dict[str, Any]]:
    rows = load_jsonl(root / "trace" / f"{STAMP}_custody_trace.jsonl")
    oracle = independent_oracle()
    unique_steps = len({row["step_index"] for row in rows}) == len(rows)
    prefixes = [row["prefix_after"] for row in rows]
    expected_prefixes = [row["after"][6] for row in oracle]
    word = next(prefix for prefix in prefixes if prefix.endswith("L"))
    l_index = next(i for i, row in enumerate(rows) if row["selected_primitive"] == "L")
    before_l = rows[l_index]["before"]
    after_l = rows[l_index]["after"]
    next_b = rows[l_index + 1]["after"]
    checks = {
        "row_count": len(rows) == 16,
        "unique_steps": unique_steps,
        "prefixes_match_oracle": prefixes == expected_prefixes,
        "word": word == EXPECTED_WORD,
        "floor_pair": before_l["pair"] == [55, 89],
        "floor_product": before_l["pair_product"] == 4895,
        "Q_count": before_l["phase_quarters"] == 5,
        "phase_i": before_l["phase_label"] == "i",
        "pair_carry": after_l["pair"] == [55, 89],
        "phase_carry": after_l["phase_quarters"] == 5,
        "k_reset": after_l["k"] == 0,
        "j_after_L": after_l["j"] == 7,
        "next_pair": next_b["pair"] == [89, 144],
        "no_floor_symbol": all(row["selected_primitive"] in {"B", "Q", "L"} for row in rows),
        "local_axis": rows[l_index]["active_axis_before"]["local_shorthand"] == "i/4895",
    }
    return all(checks.values()), checks


def verify_status_and_null_layers(root: Path) -> tuple[bool, dict[str, Any]]:
    statuses = load_json(root / "outputs" / f"{STAMP}_statuses.json")
    causal = load_jsonl(root / "trace" / f"{STAMP}_full_prefix_causal_trace.jsonl")
    required = {
        "FIRST_TRUE_GAP": "PRIMARY_PAIRING_TYPE_SEED_AND_MUTATION",
        "EXACT_PRIMARY_PAIRING_TYPE": "NOT_YET_DERIVED",
        "EXACT_PRIMARY_PAIRING_SEED": "NOT_YET_DERIVED",
        "EXACT_PRIMARY_PAIRING_RECURRENCE": "NOT_YET_DERIVED",
        "EXACT_CHART_MAPS": "NOT_YET_DERIVED",
        "EXACT_DIRECTED_TRANSFERS": "NOT_YET_DERIVED",
        "TERMINAL_PROJECTION": "NOT_RUN",
        "GAUGE_FQM_WEIL_DESCENT": "NOT_RUN",
        "MHD_ORTHAD_READINESS": "NOT_READY",
    }
    status_ok = all(statuses.get(key) == value for key, value in required.items())
    value_fields = [
        "P_t", "P_t_plus_1", "Omega_t_plus", "Omega_t_plus_1_plus",
        "Omega_t_minus", "Omega_t_plus_1_minus", "T_t_plus_to_minus",
        "T_t_plus_1_plus_to_minus", "T_t_minus_to_plus", "T_t_plus_1_minus_to_plus",
    ]
    null_ok = all(row[field]["value"] is None for row in causal for field in value_fields)
    projection_ok = all(row["projection_performed"] is False for row in causal)
    return status_ok and null_ok and projection_ok, {"status_ok": status_ok, "null_layers": null_ok, "no_projection": projection_ok}


def verify_schemas(root: Path) -> tuple[bool, dict[str, Any]]:
    required_csv = {
        f"{STAMP}_typed_state_ledger.csv": {"symbol", "type", "role", "status"},
        f"{STAMP}_source_inventory.csv": {"package_path", "upstream_path", "upstream_sha256", "bytes", "role"},
        f"{STAMP}_provenance_diff.csv": {"package_path", "upstream_path", "upstream_sha256", "bytes", "role"},
        f"{STAMP}_gate_table.csv": {"gate", "evidence_class", "pass", "boundary"},
    }
    details = {}
    ok = True
    for name, columns in required_csv.items():
        path = root / "outputs" / name
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            actual = set(reader.fieldnames or [])
        good = bool(rows) and columns.issubset(actual)
        details[name] = {"rows": len(rows), "columns_ok": good}
        ok = ok and good
    gates = list(csv.DictReader((root / "outputs" / f"{STAMP}_gate_table.csv").open(encoding="utf-8")))
    candidate = [row for row in gates if row["evidence_class"] == "CANDIDATE_FORMALIZATION"]
    candidate_ok = bool(candidate) and all(row["pass"].lower() == "false" for row in candidate)
    details["candidate_not_promoted"] = candidate_ok
    return ok and candidate_ok, details


def verify_controls(root: Path) -> tuple[bool, dict[str, Any]]:
    rows = load_jsonl(root / "outputs" / f"{STAMP}_corruption_controls.jsonl")
    unique = len({row["control"] for row in rows}) == len(rows)
    fired = all(bool(row["target_gate_fired"]) and bool(row["pass"]) for row in rows)
    targets = {row["target_gate"] for row in rows}
    needed = {
        "CANONICAL_WORD", "FIRST_L_CARRY", "NEXT_DOMAIN_B", "ACTIVE_AXIS_LOCAL_SHORTHAND",
        "SUCCESSOR_FIRST_RETIRED", "Z12_LOCAL_TYPE", "PAIRING_TYPE_HARD_STOP",
        "NO_CHART_OR_TRANSFER_VALUES", "NO_PROJECTION", "CONDITIONAL_L_ZERO_MIXED_BIRTH_BLOCK",
        "MHD_READINESS_BOUNDARY",
    }
    return unique and fired and needed.issubset(targets), {"controls": len(rows), "unique": unique, "all_fired": fired, "targets_complete": needed.issubset(targets)}


def verify_notebook(root: Path) -> tuple[bool, dict[str, Any]]:
    import nbformat

    path = root / "notebooks" / f"{STAMP}_pairing_first_realign_executed.ipynb"
    nb = nbformat.read(path, as_version=4)
    code_cells = [cell for cell in nb.cells if cell.cell_type == "code"]
    complete = all(cell.execution_count is not None for cell in code_cells)
    ids = [cell.get("id") for cell in nb.cells]
    stable_ids = len(ids) == len(set(ids)) and all(ids)
    output_ok = True
    for cell in code_cells:
        text = "\n".join(
            output.get("text", "") if output.output_type == "stream" else ""
            for output in cell.outputs
        )
        has_boundary = "claim boundary:" in text
        has_values = "exact values:" in text
        has_pass = "PASS" in text or "FAIL" in text
        has_figure = any(output.output_type in {"display_data", "execute_result"} and "image/png" in output.get("data", {}) for output in cell.outputs)
        output_ok = output_ok and has_boundary and has_values and has_pass and has_figure
    return complete and stable_ids and output_ok, {"code_cells": len(code_cells), "executed": complete, "stable_ids": stable_ids, "claim_outputs_complete": output_ok}


def verify_pytest(root: Path, temp: Path) -> tuple[bool, dict[str, Any]]:
    junit = temp / "pytest.xml"
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(root / "src")
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", f"--junitxml={junit}"],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    suite_root = ET.parse(junit).getroot()
    suite = suite_root if suite_root.tag == "testsuite" else suite_root.find("testsuite")
    counts = {key: int(suite.attrib.get(key, 0)) for key in ("tests", "failures", "errors", "skipped")}
    counts["passed"] = counts["tests"] - counts["failures"] - counts["errors"] - counts["skipped"]
    counts["exit_code"] = proc.returncode
    packaged = load_json(root / "outputs" / f"{STAMP}_test_results.json")
    count_match = all(packaged.get(key) == counts[key] for key in ("tests", "failures", "errors", "skipped", "passed"))
    counts["packaged_count_match"] = count_match
    counts["stdout"] = proc.stdout.strip()
    counts["stderr"] = proc.stderr.strip()
    return proc.returncode == 0 and counts["failures"] == 0 and counts["errors"] == 0 and count_match, counts


def verify_lean(root: Path) -> tuple[bool, dict[str, Any]]:
    source = root / "proofs" / f"{STAMP}_PairingFirstOrthad.lean"
    log = (root / "proofs" / f"{STAMP}_lean_compile.log").read_text(encoding="utf-8")
    lean = shutil.which("lean")
    if lean:
        proc = subprocess.run([lean, str(source)], capture_output=True, text=True, check=False)
        return proc.returncode == 0, {"available": True, "exit_code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    honest = "LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED" in log
    return source.is_file() and honest, {"available": False, "honest_status": honest}


def verify_no_caches_and_forbidden_imports(root: Path, archive_names: list[str] | None) -> tuple[bool, dict[str, Any]]:
    cache_paths = [
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if "__pycache__" in path.parts or path.suffix == ".pyc" or ".pytest_cache" in path.parts
    ]
    if archive_names is not None:
        cache_paths.extend(name for name in archive_names if "__pycache__" in name or name.endswith(".pyc") or ".pytest_cache" in name)
    forbidden = ["sklearn", "scipy.optimize", "networkx", "joblib", "ray", "torch", "tensorflow", "jax", "cupy", "numba.cuda"]
    hits = []
    for path in (root / "src").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        for token in forbidden:
            if f"import {token}" in text or f"from {token}" in text:
                hits.append({"path": path.relative_to(root).as_posix(), "token": token})
    return not cache_paths and not hits, {"cache_paths": sorted(set(cache_paths)), "forbidden_import_hits": hits}


def verify_rebuild_record(root: Path) -> tuple[bool, dict[str, Any]]:
    data = load_json(root / "outputs" / f"{STAMP}_reproducibility_comparison.json")
    return bool(data.get("pass")) and all(row.get("match") for row in data.get("artifacts", [])), {"contract": data.get("contract"), "artifacts": len(data.get("artifacts", [])), "pass": data.get("pass"), "exclusions": data.get("normalized_exclusions", [])}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--expected-zip-sha")
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="p5_v8v_verify_") as temp_name:
        temp = Path(temp_name)
        root, zip_path, archive_names = package_root(args.target, temp)
        gates = []

        def gate(name: str, fn) -> None:
            try:
                passed, detail = fn()
            except Exception as exc:
                passed, detail = False, {"error": f"{type(exc).__name__}: {exc}"}
            gates.append({"gate": name, "pass": bool(passed), "detail": detail})

        gate("MANIFEST_INTEGRITY", lambda: verify_manifest(root, archive_names))
        gate("PRIMITIVE_EVIDENCE", lambda: verify_trace(root))
        gate("STATUS_AND_NULL_LAYER_BOUNDARY", lambda: verify_status_and_null_layers(root))
        gate("OUTPUT_SCHEMAS", lambda: verify_schemas(root))
        gate("CORRUPTION_CONTROLS", lambda: verify_controls(root))
        gate("EXECUTED_NOTEBOOK", lambda: verify_notebook(root))
        gate("PYTEST_ACTUAL_COUNTS", lambda: verify_pytest(root, temp))
        gate("LEAN_STATUS", lambda: verify_lean(root))
        gate("NO_CACHE_AND_FORBIDDEN_IMPORTS", lambda: verify_no_caches_and_forbidden_imports(root, archive_names))
        gate("REBUILD_COMPARISON", lambda: verify_rebuild_record(root))

        if args.expected_zip_sha:
            gate(
                "EXACT_RESPONSE_ZIP_SHA",
                lambda: (
                    zip_path is not None and sha256(zip_path) == args.expected_zip_sha,
                    {"expected": args.expected_zip_sha, "actual": sha256(zip_path) if zip_path else None},
                ),
            )

        passed = all(row["pass"] for row in gates)
        print(json.dumps({"pass": passed, "passed_gates": sum(row["pass"] for row in gates), "total_gates": len(gates), "gates": gates}, indent=2))
        return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
