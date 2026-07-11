#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
STAMP = "20260711T145038"


class GateFailure(Exception):
    def __init__(self, gate: str, detail: str):
        super().__init__(detail)
        self.gate = gate
        self.detail = detail


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, gate: str, detail: str) -> None:
    if not condition:
        raise GateFailure(gate, detail)


def source_rows(root: Path) -> dict[str, dict[str, str]]:
    path = root / "outputs" / f"{STAMP}_pairing_representability_source_ledger.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    ids = {row["source_id"] for row in rows}
    require(len(rows) == len(ids), "source_ledger", "duplicate source_id")
    required = {"S01_LIFTED_STATE", "S02_PAIRING_FIRST", "S03_FOUR_PULLBACKS", "S05_Q_QUARTER_TURN", "S06_L_EXTENSION", "S08_GAUGE_SHAPE", "S09_FQM_POLARIZATION", "S11_AUDIT_RETYPE"}
    require(required <= ids, "source_ledger", f"missing rows: {sorted(required - ids)}")
    for row in rows:
        require(row["exact_source_path"], "source_ledger", f"missing path for {row['source_id']}")
        require(row["section_or_lines"], "source_ledger", f"missing location for {row['source_id']}")
        require(row["authority"], "source_ledger", f"missing authority for {row['source_id']}")
        require((root / row["exact_source_path"]).exists(), "source_ledger", f"missing source file for {row['source_id']}")
    return {row["source_id"]: row for row in rows}


def check_source_inference(root: Path, rows: dict[str, dict[str, str]], claim: dict) -> None:
    rules = load_json(root / "outputs" / f"{STAMP}_inference_rules.json")
    by_id = {rule["rule_id"]: rule for rule in rules}
    require(claim["verifier_evidence_mode"] == "SOURCE_ROWS_PLUS_EXPLICIT_INFERENCE_RULES", "source_inference_mode", "self-reported inference mode")
    for rid in ["R01_TWO_SLOT_PULLBACK", "R02_NO_REPRESENTABILITY", "R03_SCALAR_DOWNSTREAM", "R04_L_MIXED_OPEN", "R05_RANK_UNTYPED"]:
        require(rid in by_id, "source_inference_mode", f"missing inference rule {rid}")
        rule = by_id[rid]
        require(rule["evidence_class"] == "SOURCE_DERIVED", "source_inference_mode", f"wrong evidence class {rid}")
        require(all(p in rows for p in rule["premises"]), "source_inference_mode", f"unresolved premise {rid}")
    text = rows["S03_FOUR_PULLBACKS"]["literal_formula"]
    require("iota_-^* P iota_+" in text and "iota_+^* P iota_-" in text, "source_interface", "two mixed pullbacks absent")
    iface = claim["source_forced_interface"]
    require(iface["name"] == "two_slot_pullback_pairing_system", "source_interface", "wrong interface")
    require(iface["scalar_object_required"] is False and iface["duality_object_required"] is False, "source_interface", "extra structure promoted")


def check_representability(claim: dict) -> None:
    statuses = claim["statuses"]
    require(statuses["DUALITY_MORPHISM_MODEL"] == "ADMISSIBLE_CANDIDATE", "representability_boundary", "duality model promoted")
    require(statuses["PAIRING_REPRESENTABILITY"] == "NOT_YET_DERIVED", "representability_boundary", "representability promoted")
    rep = claim["duality_morphism_model"]
    require(rep["status"] == "ADMISSIBLE_CANDIDATE", "representability_boundary", "candidate status changed")
    missing = rep["missing_axiom"]
    require("natural isomorphism" in missing and "Pair(A,H)" in missing and "Hom(A,D(H))" in missing, "representability_boundary", "representability axiom incomplete")


def check_scalar(claim: dict) -> None:
    require(claim["statuses"]["SCALAR_VARIANCE_STATUS"] == "DOWNSTREAM", "scalar_variance_boundary", "scalar variance promoted")
    deps = set(claim["scalar_variance"]["dependencies"])
    required = {"coefficient object K", "scalar action on H_t", "involution/star on K", "pairing compatibility"}
    require(required <= deps, "scalar_variance_boundary", "scalar dependencies incomplete")


def check_orthogonality(root: Path, claim: dict) -> None:
    first_l = claim["first_L"]
    require(first_l["right_mixed"] == "NOT_YET_DERIVED", "orthogonality_boundary", "right mixed block promoted")
    require(first_l["left_mixed"] == "NOT_YET_DERIVED", "orthogonality_boundary", "left mixed block promoted")
    cases = load_json(root / "outputs" / f"{STAMP}_first_L_mixed_block_cases.json")
    matrix = cases["counterexample"]["matrix"]
    require(matrix == [[1, 1], [0, 1]], "orthogonality_boundary", "counterexample changed")
    require(matrix[1][0] == 0 and matrix[0][1] == 1, "orthogonality_boundary", "counterexample does not separate sides")


def rank2(matrix: list[list[int]]) -> int:
    if all(v == 0 for row in matrix for v in row):
        return 0
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return 2 if det != 0 else 1


def check_rank(root: Path, claim: dict) -> None:
    require(claim["statuses"]["FIRST_L_PAIRING_RANK_LAW"] == "NOT_YET_TYPED", "rank_boundary", "rank law promoted")
    require(claim["rank_semantics"]["architectural_axis_count"] == "DERIVED", "rank_boundary", "axis count lost")
    require(claim["rank_semantics"]["pairing_morphism_rank"] == "NOT_YET_TYPED", "rank_boundary", "morphism rank promoted")
    example = load_json(root / "outputs" / f"{STAMP}_rank_zero_birth_counterexample.json")
    matrix = example["extended_matrix_with_p_new_zero"]
    require(len(matrix) == 2 and len(matrix[0]) == 2, "rank_boundary", "block size example invalid")
    require(rank2(matrix) == 1 and example["new_algebraic_rank"] == 1, "rank_boundary", "rank counterexample invalid")


def check_gauge(root: Path, claim: dict) -> None:
    gauge = claim["gauge_boundary"]
    require(gauge["full_Aut_quotient"] == "ADMISSIBLE_MODEL_NOT_DERIVED", "gauge_boundary", "full Aut quotient promoted")
    artifact = load_json(root / "outputs" / f"{STAMP}_seed_gauge_quotient_boundary.json")
    require(artifact["full_Aut_H_quotient"] == "ADMISSIBLE_MODEL_NOT_DERIVED", "gauge_boundary", "gauge artifact promoted")


def check_lifted_boundary(claim: dict) -> None:
    schema = claim["lifted_state_schema"]
    require(schema["name"] == "lifted_state_schema", "lifted_schema_boundary", "wrong schema name")
    require(schema["Xi_hat_t_emitted"] is False, "lifted_schema_boundary", "Xi_hat_t emitted")
    for key in ["pairing", "omega_plus", "omega_minus", "transfer_plus_to_minus", "transfer_minus_to_plus"]:
        require(schema[key] is None, "lifted_schema_boundary", f"non-null {key}")
    require(claim["statuses"]["Xi_hat_t VALUES"] == "NOT_INSTANTIATED", "lifted_schema_boundary", "status inconsistent")


def check_downstream(claim: dict) -> None:
    downstream = claim["downstream"]
    expected = {
        "chart_values": "NOT_EMITTED",
        "transfer_values": "NOT_EMITTED",
        "projection": "NOT_RUN",
        "gauge_quotient": "NOT_CONSTRUCTED",
        "FQM": "NOT_RUN",
        "Weil": "NOT_RUN",
        "affine": "NOT_RUN",
        "MHD": "NOT_RUN",
    }
    require(downstream == expected, "downstream_boundary", "downstream layer opened")


def check_primitive(root: Path) -> None:
    data = load_json(root / "outputs" / f"{STAMP}_primitive_sanity_check.json")
    require(data["pass"] is True, "primitive_baseline", "primitive sanity failed")
    require(data["word"] == "BQQBBBQBQBBQBBL", "primitive_baseline", "wrong word")
    require(data["floor_pair"] == [55, 89] and data["floor_product"] == 4895, "primitive_baseline", "wrong floor")
    require(data["Q_steps"] == 5 and data["phase_witness"] == "i", "primitive_baseline", "wrong phase")
    after_l = data["after_L"]
    require((after_l["A"], after_l["u"], after_l["v"], after_l["k"], after_l["j"]) == (1, 55, 89, 0, 7), "primitive_baseline", "wrong L carry")
    after_b = data["after_next_B"]
    require([after_b["u"], after_b["v"]] == [89, 144], "primitive_baseline", "wrong next B")


def check_notebooks(root: Path) -> None:
    source = root / "notebooks" / f"{STAMP}_pairing_representability_and_rank.ipynb"
    executed = root / "notebooks" / f"{STAMP}_pairing_representability_and_rank_executed.ipynb"
    require(source.exists() and executed.exists(), "notebook_complete", "notebooks missing")
    nb = load_json(executed)
    code_cells = [cell for cell in nb["cells"] if cell["cell_type"] == "code"]
    require(code_cells, "notebook_complete", "no code cells")
    for index, cell in enumerate(code_cells, start=1):
        require(cell.get("execution_count") is not None, "notebook_complete", f"cell {index} not executed")
        outputs = cell.get("outputs", [])
        text = "".join("".join(out.get("text", [])) if isinstance(out.get("text"), list) else str(out.get("text", "")) for out in outputs)
        require("PASS" in text and "claim boundary" in text.lower(), "notebook_complete", f"cell {index} missing claim output")
        figures = sum(1 for out in outputs if out.get("output_type") == "display_data" and "image/png" in out.get("data", {}))
        require(figures == 1, "notebook_complete", f"cell {index} figure count {figures}")


def run_pytest(root: Path) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    collect = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"],
        cwd=root, env=env, text=True, capture_output=True,
    )
    require(collect.returncode == 0, "pytest", collect.stdout + collect.stderr)
    match = re.search(r"(\d+) tests? collected", collect.stdout + collect.stderr)
    require(match is not None, "pytest", "unable to parse collected test count")
    collected = int(match.group(1))
    run = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=root, env=env, text=True, capture_output=True,
    )
    require(run.returncode == 0, "pytest", run.stdout + run.stderr)
    match = re.search(r"(\d+) passed", run.stdout + run.stderr)
    require(match is not None, "pytest", "unable to parse passed test count")
    passed = int(match.group(1))
    require(passed == collected, "pytest", f"passed {passed} collected {collected}")
    return {"collected": collected, "passed": passed, "exit_code": run.returncode}


def check_manifest(root: Path) -> None:
    manifest_path = root / "MANIFEST.json"
    require(manifest_path.exists(), "manifest", "manifest missing")
    manifest = load_json(manifest_path)
    listed = {entry["path"]: entry for entry in manifest["entries"]}
    actual = {}
    for path in root.rglob("*"):
        if not path.is_file() or path.name == "MANIFEST.json":
            continue
        rel = path.relative_to(root).as_posix()
        require("__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"} and ".pytest_cache" not in path.parts, "manifest", f"cache present {rel}")
        actual[rel] = path
    require(set(listed) == set(actual), "manifest", f"path-set mismatch missing={sorted(set(actual)-set(listed))} extra={sorted(set(listed)-set(actual))}")
    for rel, path in actual.items():
        data = path.read_bytes()
        entry = listed[rel]
        require(entry["bytes"] == len(data), "manifest", f"byte mismatch {rel}")
        require(entry["sha256"] == hashlib.sha256(data).hexdigest(), "manifest", f"hash mismatch {rel}")


def run_controls(root: Path) -> dict:
    script = root / "scripts" / f"{STAMP}_run_controls.py"
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run([sys.executable, str(script), str(root), "--check"], cwd=root, env=env, text=True, capture_output=True)
    require(result.returncode == 0, "controls", result.stdout + result.stderr)
    match = re.search(r"CONTROL_SUMMARY_JSON=(\{.*\})", result.stdout)
    require(match is not None, "controls", "control summary missing")
    summary = json.loads(match.group(1))
    require(summary["failed_as_required"] == summary["total"] and summary["total"] > 0, "controls", "not all controls fired")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--skip-controls", action="store_true")
    parser.add_argument("--skip-manifest", action="store_true")
    parser.add_argument("--skip-pytest", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    gates: list[str] = []
    try:
        claim = load_json(root / "outputs" / f"{STAMP}_claim_model.json")
        rows = source_rows(root); gates.append("source_ledger")
        check_source_inference(root, rows, claim); gates.extend(["source_inference_mode", "source_interface"])
        check_representability(claim); gates.append("representability_boundary")
        check_scalar(claim); gates.append("scalar_variance_boundary")
        check_orthogonality(root, claim); gates.append("orthogonality_boundary")
        check_rank(root, claim); gates.append("rank_boundary")
        check_gauge(root, claim); gates.append("gauge_boundary")
        check_lifted_boundary(claim); gates.append("lifted_schema_boundary")
        check_downstream(claim); gates.append("downstream_boundary")
        check_primitive(root); gates.append("primitive_baseline")
        check_notebooks(root); gates.append("notebook_complete")
        pytest_result = None
        if not args.skip_pytest:
            pytest_result = run_pytest(root); gates.append("pytest")
        controls_result = None
        if not args.skip_controls:
            controls_result = run_controls(root); gates.append("controls")
        if not args.skip_manifest:
            check_manifest(root); gates.append("manifest")
        print(json.dumps({"status": "PASS", "gates": gates, "gate_count": len(gates), "pytest": pytest_result, "controls": controls_result}, sort_keys=True))
        return 0
    except GateFailure as exc:
        print(f"FAIL_GATE:{exc.gate}")
        print(exc.detail)
        return 1
    except Exception as exc:
        print("FAIL_GATE:unhandled")
        print(repr(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
