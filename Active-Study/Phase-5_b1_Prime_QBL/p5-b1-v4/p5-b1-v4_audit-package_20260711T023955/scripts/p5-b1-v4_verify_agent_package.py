#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

EXPECTED_ARCHIVE_SHA256 = "39b8ffb62d90afc09169ea4a863ce3661fae36d89063eb1121ba0438cf0ccbe2"
EXPECTED_DOCUMENT_SHA256 = "87bb9fc406613784f9524464c175b4d42e3fa6fc2d789ba83a17bcab59723ed5"
PACKAGE_NAME = "experiment_package_20260711_064604"
DOCUMENT_RELATIVE = "docs/QBL_CARRY_J_DERIVATION_AND_RESEARCH_BOUNDARY_v2.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_manifest(root: Path) -> dict:
    manifest_path = root / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    recorded = {entry["path"]: entry for entry in manifest["files"]}
    actual = {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file() and path.name != "MANIFEST.json"
    }
    missing = sorted(set(recorded) - set(actual))
    unrecorded = sorted(set(actual) - set(recorded))
    mismatches = []
    for rel in sorted(set(recorded) & set(actual)):
        path = actual[rel]
        entry = recorded[rel]
        size = path.stat().st_size
        digest = sha256(path)
        if size != entry["bytes"] or digest != entry["sha256"]:
            mismatches.append(
                {
                    "path": rel,
                    "expected_bytes": entry["bytes"],
                    "actual_bytes": size,
                    "expected_sha256": entry["sha256"],
                    "actual_sha256": digest,
                }
            )
    return {
        "recorded_files": len(recorded),
        "actual_nonmanifest_files": len(actual),
        "missing": missing,
        "unrecorded": unrecorded,
        "mismatches": mismatches,
        "pass": not missing and not unrecorded and not mismatches,
    }


def inspect_notebooks(root: Path) -> dict:
    source_path = root / "notebooks/20260711T064604_J_Derivation.ipynb"
    executed_path = root / "notebooks/20260711T064604_J_Derivation_executed.ipynb"
    source = json.loads(source_path.read_text(encoding="utf-8"))
    executed = json.loads(executed_path.read_text(encoding="utf-8"))
    source_code = [cell for cell in source["cells"] if cell.get("cell_type") == "code"]
    executed_code = [cell for cell in executed["cells"] if cell.get("cell_type") == "code"]
    counts = [cell.get("execution_count") for cell in executed_code]
    passes = []
    png_counts = []
    for cell in executed_code:
        text_outputs = []
        png_count = 0
        for output in cell.get("outputs", []):
            if output.get("output_type") == "stream":
                text_outputs.extend(output.get("text", []))
            data = output.get("data", {})
            if "image/png" in data:
                png_count += 1
        passes.append(any("PASS" in line for line in text_outputs))
        png_counts.append(png_count)
    return {
        "source_code_cells": len(source_code),
        "executed_code_cells": len(executed_code),
        "execution_counts": counts,
        "all_cells_print_pass": all(passes),
        "png_counts_per_code_cell": png_counts,
        "one_png_per_code_cell": all(count == 1 for count in png_counts),
        "pass": (
            len(source_code) == 10
            and len(executed_code) == 10
            and counts == list(range(1, 11))
            and all(passes)
            and all(count == 1 for count in png_counts)
        ),
    }


def extract_archive(archive: Path, target: Path) -> Path:
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(target)
    root = target / PACKAGE_NAME
    if not root.is_dir():
        raise RuntimeError(f"archive does not contain {PACKAGE_NAME}/")
    return root


def rebuild(root: Path) -> dict:
    command = [sys.executable, "scripts/20260711T064604_build_package.py", "--package-root", "."]
    proc = subprocess.run(command, cwd=root, text=True, capture_output=True)
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "pass": proc.returncode == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--out", type=Path, default=Path("outputs"))
    parser.add_argument("--rebuild", action="store_true")
    args = parser.parse_args()
    archive = args.archive.resolve()
    args.out.mkdir(parents=True, exist_ok=True)

    result = {
        "archive": str(archive),
        "archive_sha256": sha256(archive),
        "expected_archive_sha256": EXPECTED_ARCHIVE_SHA256,
    }
    result["archive_hash_pass"] = result["archive_sha256"] == EXPECTED_ARCHIVE_SHA256

    with tempfile.TemporaryDirectory(prefix="p5-b1-v4-audit-") as tmp:
        root = extract_archive(archive, Path(tmp))
        document = root / DOCUMENT_RELATIVE
        result["document_sha256"] = sha256(document)
        result["expected_document_sha256"] = EXPECTED_DOCUMENT_SHA256
        result["document_hash_pass"] = result["document_sha256"] == EXPECTED_DOCUMENT_SHA256
        result["manifest"] = verify_manifest(root)
        result["notebooks"] = inspect_notebooks(root)
        if args.rebuild:
            result["rebuild"] = rebuild(root)
            if result["rebuild"]["pass"]:
                result["manifest_after_rebuild"] = verify_manifest(root)

    checks = [
        result["archive_hash_pass"],
        result["document_hash_pass"],
        result["manifest"]["pass"],
        result["notebooks"]["pass"],
    ]
    if args.rebuild:
        checks.append(result["rebuild"]["pass"])
        if result["rebuild"]["pass"]:
            checks.append(result["manifest_after_rebuild"]["pass"])
    result["status"] = "PASS" if all(checks) else "FAIL"

    out = args.out / "p5-b1-v4_package-verification.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["status"])
    print(out)
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
