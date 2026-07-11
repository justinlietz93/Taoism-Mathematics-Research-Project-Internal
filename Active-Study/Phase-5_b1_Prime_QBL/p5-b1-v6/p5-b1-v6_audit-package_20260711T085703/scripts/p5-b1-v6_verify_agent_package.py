#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import PurePosixPath

EXPECTED_ZIP_SHA256 = "2b21db666b26273b0ba945b0f9a855bf074596ac6a67237f2e571ad7e29fb3af"
EXPECTED_DOC_SHA256 = "b3b75959831fd868b98672eb17eacabc0c4d59432107e371dffe9b9fad4c814b"
DOC_NAME = "docs/QBL_CARRY_AFFINE_LANGUAGE_STRUCTURE_v4.md"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    raw = open(args.zip_path, "rb").read()
    report = {
        "zip_sha256": sha256(raw),
        "expected_zip_sha256": EXPECTED_ZIP_SHA256,
        "zip_hash_pass": sha256(raw) == EXPECTED_ZIP_SHA256,
    }

    with zipfile.ZipFile(args.zip_path) as zf:
        files = [n for n in zf.namelist() if not n.endswith("/")]
        roots = {PurePosixPath(n).parts[0] for n in files}
        if len(roots) != 1:
            raise SystemExit("archive must have exactly one root directory")
        root = next(iter(roots))
        manifest_path = f"{root}/MANIFEST.json"
        manifest = json.loads(zf.read(manifest_path))
        entries = manifest["files"]
        issues = []
        listed = set()
        for e in entries:
            rel = e["path"]
            listed.add(rel)
            name = f"{root}/{rel}"
            try:
                data = zf.read(name)
            except KeyError:
                issues.append({"type": "missing", "path": rel})
                continue
            if len(data) != e["bytes"]:
                issues.append({"type": "bytes", "path": rel})
            if sha256(data) != e["sha256"]:
                issues.append({"type": "sha256", "path": rel})
        actual = {
            str(PurePosixPath(n).relative_to(root))
            for n in files
            if n != manifest_path
        }
        doc = zf.read(f"{root}/{DOC_NAME}")
        nb = json.loads(zf.read(f"{root}/notebooks/20260711T083401_Affine_Language_executed.ipynb"))
        code_cells = [c for c in nb["cells"] if c.get("cell_type") == "code"]
        passes = 0
        pngs = 0
        errors = []
        for index, cell in enumerate(code_cells, 1):
            text_parts = []
            for out in cell.get("outputs", []):
                if out.get("output_type") == "stream":
                    text = out.get("text", "")
                    text_parts.append("".join(text) if isinstance(text, list) else str(text))
                if "data" in out and "image/png" in out["data"]:
                    pngs += 1
                if out.get("output_type") == "error":
                    errors.append(index)
            text = "".join(text_parts)
            if "PASS" in text and "FAIL" not in text:
                passes += 1
        report.update({
            "root": root,
            "manifest_entries": len(entries),
            "actual_nonmanifest_files": len(actual),
            "manifest_issues": issues,
            "manifest_missing_entries": sorted(actual - listed),
            "manifest_extra_entries": sorted(listed - actual),
            "manifest_pass": not issues and actual == listed,
            "document_sha256": sha256(doc),
            "expected_document_sha256": EXPECTED_DOC_SHA256,
            "document_hash_pass": sha256(doc) == EXPECTED_DOC_SHA256,
            "notebook_code_cells": len(code_cells),
            "notebook_pass_cells": passes,
            "notebook_png_outputs": pngs,
            "notebook_error_cells": errors,
            "notebook_pass": len(code_cells) == 15 and passes == 15 and pngs == 15 and not errors,
        })

    report["overall_pass"] = all([
        report["zip_hash_pass"],
        report["manifest_pass"],
        report["document_hash_pass"],
        report["notebook_pass"],
    ])
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(payload, end="")
    if args.json_out:
        open(args.json_out, "w", encoding="utf-8").write(payload)
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
