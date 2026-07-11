#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

EXPECTED_SHA = "5456edffbdc482564904e37aac6565ab39a11036be9959a20935982dc5184556"
ROOT_NAME = "p5_v8r_orthad-first-crossing-recurrence_20260711_080825"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_path", type=Path)
    args = parser.parse_args()
    zip_path = args.zip_path.resolve()
    result: dict[str, object] = {
        "zip_sha256": sha256(zip_path),
        "zip_hash_matches_response": sha256(zip_path) == EXPECTED_SHA,
    }

    with zipfile.ZipFile(zip_path) as archive:
        prefix = ROOT_NAME + "/"
        archived = {
            name[len(prefix):]
            for name in archive.namelist()
            if name.startswith(prefix) and not name.endswith("/")
        }
        manifest = json.loads(archive.read(prefix + "MANIFEST.json"))
        listed = {row["path"] for row in manifest["files"]}
        extras = sorted(archived - listed - {"MANIFEST.json"})
        result["zip_file_entries"] = len(archived)
        result["manifest_entries"] = len(listed)
        result["unmanifested_extras"] = extras

        with tempfile.TemporaryDirectory() as directory:
            archive.extractall(directory)
            root = Path(directory) / ROOT_NAME
            env = dict(**__import__("os").environ)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            env["PYTHONPATH"] = str(root / "src")
            # Run the package verifier before any tool can create unsealed cache files.
            verify = subprocess.run(
                [sys.executable, str(root / "scripts/20260711T080825_verify.py"), str(root)],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )
            pytest = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )
            result["pytest_exit"] = pytest.returncode
            result["pytest_output"] = pytest.stdout.strip()
            result["verifier_exit"] = verify.returncode
            try:
                result["verifier"] = json.loads(verify.stdout)
            except json.JSONDecodeError:
                result["verifier_stdout"] = verify.stdout
                result["verifier_stderr"] = verify.stderr

            assessment_text = (root / "src/orthad_v8r/assessment.py").read_text()
            lean_text = (root / "proofs/20260711T080825_OrthadRecurrenceGap.lean").read_text()
            result["assessment_is_literal_report"] = "missing = (" in assessment_text and "tau_0" in assessment_text
            result["lean_uses_bilinear_form"] = "Bilinear" in lean_text or "LinearMap" in lean_text
            result["lean_uses_independent_record_fields"] = "structure PairingData" in lean_text and "plusToMinus : Nat" in lean_text

    print(json.dumps(result, indent=2, sort_keys=True))
    failures = []
    if not result["zip_hash_matches_response"]:
        failures.append("zip hash")
    if result["pytest_exit"] != 0:
        failures.append("pytest")
    if result["verifier_exit"] != 0:
        failures.append("verifier")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
