#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
STAMP = "20260711T145038"

CONTROLS = [
    {
        "mutation": "promote P:H->D(H) without a representability source",
        "expected_gate": "representability_boundary",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "representability"},
    },
    {
        "mutation": "name scalar variance before a scalar object exists",
        "expected_gate": "scalar_variance_boundary",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "scalar"},
    },
    {
        "mutation": "infer both mixed blocks are zero from one-sided orthogonality",
        "expected_gate": "orthogonality_boundary",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "orthogonality"},
    },
    {
        "mutation": "claim pairing rank +1 with p_new=0",
        "expected_gate": "rank_boundary",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "rank"},
    },
    {
        "mutation": "treat the full Aut(H) as the gauge group without authority",
        "expected_gate": "gauge_boundary",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "gauge"},
    },
    {
        "mutation": "certify candidate elimination from self-reported booleans",
        "expected_gate": "source_inference_mode",
        "target": f"outputs/{STAMP}_claim_model.json",
        "patch": {"kind": "self_report"},
    },
]


def apply_patch(path: Path, kind: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if kind == "representability":
        data["statuses"]["DUALITY_MORPHISM_MODEL"] = "DERIVED"
        data["statuses"]["PAIRING_REPRESENTABILITY"] = "DERIVED"
        data["duality_morphism_model"]["status"] = "DERIVED"
    elif kind == "scalar":
        data["statuses"]["SCALAR_VARIANCE_STATUS"] = "CURRENT"
        data["scalar_variance"]["status"] = "CURRENT"
    elif kind == "orthogonality":
        data["statuses"]["FIRST_L_RIGHT_MIXED_BLOCK"] = "ZERO"
        data["statuses"]["FIRST_L_LEFT_MIXED_BLOCK"] = "ZERO"
        data["first_L"]["right_mixed"] = "ZERO"
        data["first_L"]["left_mixed"] = "ZERO"
    elif kind == "rank":
        data["statuses"]["FIRST_L_PAIRING_RANK_LAW"] = "DERIVED"
        data["first_L"]["pairing_rank_law"] = "DERIVED_PLUS_ONE"
        data["rank_semantics"]["pairing_morphism_rank"] = "DERIVED_PLUS_ONE"
    elif kind == "gauge":
        data["gauge_boundary"]["full_Aut_quotient"] = "DERIVED"
    elif kind == "self_report":
        data["verifier_evidence_mode"] = "SELF_REPORTED_BOOLEAN"
    else:
        raise ValueError(kind)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_one(root: Path, control: dict) -> dict:
    with tempfile.TemporaryDirectory(prefix="p5_v8x_control_") as td:
        copy_root = Path(td) / root.name
        shutil.copytree(root, copy_root)
        target = copy_root / control["target"]
        apply_patch(target, control["patch"]["kind"])
        manifest = copy_root / "scripts" / f"{STAMP}_make_manifest.py"
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        subprocess.run([sys.executable, str(manifest), str(copy_root)], cwd=copy_root, env=env, check=True, text=True, capture_output=True)
        verifier = copy_root / "scripts" / f"{STAMP}_verify.py"
        command = [sys.executable, str(verifier), str(copy_root), "--skip-controls"]
        result = subprocess.run(command, cwd=copy_root, env=env, text=True, capture_output=True)
        expected = f"FAIL_GATE:{control['expected_gate']}"
        fired = result.returncode != 0 and expected in result.stdout
        return {
            "mutation": control["mutation"],
            "command": f"<PYTHON> scripts/{STAMP}_verify.py <TEMP_COPY> --skip-controls",
            "verifier_exit_code": result.returncode,
            "failed_gate": control["expected_gate"] if fired else "UNEXPECTED",
            "evidence_path": control["target"],
            "expected_failure_observed": fired,
            "stdout_excerpt": result.stdout.strip().splitlines()[:3],
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    rows = [run_one(root, control) for control in CONTROLS]
    summary = {
        "total": len(rows),
        "failed_as_required": sum(row["expected_failure_observed"] for row in rows),
        "all_pass": all(row["expected_failure_observed"] for row in rows),
    }
    if args.write:
        output = root / "outputs" / f"{STAMP}_corruption_controls.jsonl"
        output.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
        (root / "outputs" / f"{STAMP}_corruption_control_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("CONTROL_SUMMARY_JSON=" + json.dumps(summary, sort_keys=True))
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
