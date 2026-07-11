#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT_NAME = "p5_v8x_pairing-representability-and-l-rank-law_20260711_145038"
STAMP = "20260711T145038"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(cmd, cwd, env):
    return subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)

def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <p5_v8x.zip>")
        return 2

    zip_path = Path(sys.argv[1]).resolve()
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    with tempfile.TemporaryDirectory(prefix="p5_v8x_audit_") as td:
        td_path = Path(td)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(td_path)
        root = td_path / ROOT_NAME

        clean = run(
            [sys.executable, str(root / "scripts" / f"{STAMP}_verify.py"), str(root)],
            root,
            env,
        )

        attacked = td_path / "attacked"
        shutil.copytree(root, attacked)
        law = attacked / "inputs" / f"{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md"
        law.write_text("# CORRUPTED\nNo pairing, chart, or transfer law remains.\n", encoding="utf-8")

        manifest = run(
            [sys.executable, str(attacked / "scripts" / f"{STAMP}_make_manifest.py"), str(attacked)],
            attacked,
            env,
        )

        attack = run(
            [
                sys.executable,
                str(attacked / "scripts" / f"{STAMP}_verify.py"),
                str(attacked),
                "--skip-controls",
            ],
            attacked,
            env,
        )

        result = {
            "zip_sha256": sha256(zip_path),
            "clean_verifier_exit_code": clean.returncode,
            "clean_verifier_stdout": clean.stdout.strip(),
            "source_binding_attack": {
                "manifest_exit_code": manifest.returncode,
                "verifier_exit_code": attack.returncode,
                "verifier_stdout": attack.stdout.strip(),
            },
        }
        print(json.dumps(result, indent=2))
        return 0 if clean.returncode == 0 and manifest.returncode == 0 and attack.returncode == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
