#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys, zipfile
from pathlib import Path

EXPECTED_ZIP = "c3c91e37e7d970f8f89bf3db086fb64dc658e1e1e1c77fb3666f6aed80405b9b"
EXPECTED_DOC = "00c9d0068dad1b45ddb7cd71dcf1d8695c1fcbc64d3e3f2563bf36bafc5b5a16"
DOC_REL = "docs/QBL_PRIMARY_PAIRING_TYPE_BOUNDARY_v2.md"

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_agent_package.py <archive.zip>")
    archive = Path(sys.argv[1])
    raw = archive.read_bytes()
    failures: list[str] = []
    if sha(raw) != EXPECTED_ZIP:
        failures.append("archive_sha256")
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        root = names[0].split("/")[0]
        manifest = json.loads(z.read(f"{root}/MANIFEST.json"))
        manifest_paths = {row["path"] for row in manifest["files"]}
        actual_paths = {
            name[len(root)+1:]
            for name in names
            if name.startswith(root + "/") and not name.endswith("/") and name != f"{root}/MANIFEST.json"
        }
        if manifest_paths != actual_paths:
            failures.append("manifest_coverage")
        for row in manifest["files"]:
            data = z.read(f"{root}/{row['path']}")
            if len(data) != row["size"] or sha(data) != row["sha256"]:
                failures.append(f"manifest:{row['path']}")
        if sha(z.read(f"{root}/{DOC_REL}")) != EXPECTED_DOC:
            failures.append("document_sha256")
        nb = json.loads(z.read(f"{root}/notebooks/20260711T145605_Primary_Pairing_Type_Boundary_executed.ipynb"))
        code = [c for c in nb["cells"] if c["cell_type"] == "code"]
        if len(code) != 15:
            failures.append("notebook_cell_count")
        figures = [n for n in names if n.startswith(f"{root}/figures/") and n.endswith(".png")]
        if len(figures) != 15:
            failures.append("figure_count")
    result = {
        "archive_sha256": sha(raw),
        "document_sha256": EXPECTED_DOC,
        "manifest_entries": len(manifest["files"]),
        "notebook_code_cells": len(code),
        "figures": len(figures),
        "failures": failures,
        "PASS": not failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
