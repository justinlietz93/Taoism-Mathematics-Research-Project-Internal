#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import zipfile
from pathlib import Path

EXPECTED_ZIP_SHA = "491ecfffd78ce5ab11e82794381e7579168027892dce7986fb9d4d3507395d27"
EXPECTED_DOC_SHA = "bbba649dcbeff1593afb6d81ca6753253533e6dbe4e2bd8057a7eab1caa5bd46"
CANONICAL_NAME = "p5_v8y_primary-pairing-star-phase-compatibility_20260711_162758.zip"
PACKAGE_ROOT = "p5_v8y_primary-pairing-star-phase-compatibility_20260711_162758"
DOC_REL = "docs/20260711T162758_PRIMARY_PAIRING_STAR_PHASE_COMPATIBILITY.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    package_root = Path(__file__).resolve().parents[1]
    archive = package_root / "inputs" / "convergence" / CANONICAL_NAME
    result: dict[str, object] = {
        "archive": str(archive.relative_to(package_root)),
        "expected_zip_sha256": EXPECTED_ZIP_SHA,
    }

    if not archive.exists():
        result["status"] = "FAIL"
        result["error"] = "archive missing"
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    actual_zip_sha = sha256(archive)
    result["actual_zip_sha256"] = actual_zip_sha
    if actual_zip_sha != EXPECTED_ZIP_SHA:
        result["status"] = "FAIL"
        result["error"] = "archive hash mismatch"
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(td_path)
        root = td_path / PACKAGE_ROOT
        manifest = json.loads((root / "MANIFEST.json").read_text())
        entries = manifest["entries"]
        errors: list[dict[str, object]] = []
        for entry in entries:
            path = root / entry["path"]
            if not path.exists():
                errors.append({"path": entry["path"], "error": "missing"})
                continue
            data = path.read_bytes()
            actual_sha = hashlib.sha256(data).hexdigest()
            if actual_sha != entry["sha256"] or len(data) != entry["bytes"]:
                errors.append({
                    "path": entry["path"],
                    "expected_sha256": entry["sha256"],
                    "actual_sha256": actual_sha,
                    "expected_bytes": entry["bytes"],
                    "actual_bytes": len(data),
                })
        actual_files = {
            str(p.relative_to(root))
            for p in root.rglob("*")
            if p.is_file() and p.name != "MANIFEST.json"
        }
        listed_files = {entry["path"] for entry in entries}
        unlisted = sorted(actual_files - listed_files)
        absent = sorted(listed_files - actual_files)
        doc_sha = sha256(root / DOC_REL)

    result.update({
        "manifest_entries": len(entries),
        "manifest_errors": errors,
        "unlisted_files": unlisted,
        "listed_but_missing": absent,
        "expected_document_sha256": EXPECTED_DOC_SHA,
        "actual_document_sha256": doc_sha,
    })
    passed = not errors and not unlisted and not absent and doc_sha == EXPECTED_DOC_SHA
    result["status"] = "PASS" if passed else "FAIL"
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
