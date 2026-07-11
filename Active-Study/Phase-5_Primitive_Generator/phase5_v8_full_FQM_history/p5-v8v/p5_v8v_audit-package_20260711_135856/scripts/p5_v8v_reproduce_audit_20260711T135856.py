#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT_NAME = "p5_v8v_pairing-first-orthad-realignment_20260711_133900"
STAMP = "20260711T133900"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path", type=Path)
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="p5_v8v_audit_") as td:
        temp = Path(td)
        with zipfile.ZipFile(args.zip_path) as zf:
            zf.extractall(temp)
        root = temp / ROOT_NAME

        verifier = subprocess.run(
            [
                "python3",
                str(root / "scripts" / f"{STAMP}_verify.py"),
                str(args.zip_path.resolve()),
                "--expected-zip-sha",
                sha256(args.zip_path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        attacked = temp / "attacked"
        shutil.copytree(root, attacked)
        trace_path = attacked / "trace" / f"{STAMP}_custody_trace.jsonl"
        lines = trace_path.read_text(encoding="utf-8").splitlines()
        first = json.loads(lines[0])
        first["prefix_after"] = "X"
        lines[0] = json.dumps(first, separators=(",", ":"))
        trace_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        controls = subprocess.run(
            ["python3", str(attacked / "scripts" / f"{STAMP}_run_controls.py")],
            cwd=attacked,
            capture_output=True,
            text=True,
            check=False,
        )
        attacked_verifier = subprocess.run(
            ["python3", str(attacked / "scripts" / f"{STAMP}_verify.py"), str(attacked)],
            cwd=attacked,
            capture_output=True,
            text=True,
            check=False,
        )

        result = {
            "zip_sha256": sha256(args.zip_path),
            "clean_verifier_exit_code": verifier.returncode,
            "clean_verifier_output": json.loads(verifier.stdout),
            "control_disconnect_attack": {
                "mutation": "first custody prefix_after changed to X",
                "run_controls_exit_code": controls.returncode,
                "run_controls_stdout": controls.stdout.strip(),
                "real_verifier_exit_code": attacked_verifier.returncode,
            },
        }
        print(json.dumps(result, indent=2))
        return 0 if verifier.returncode == 0 and controls.returncode == 0 and attacked_verifier.returncode != 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
