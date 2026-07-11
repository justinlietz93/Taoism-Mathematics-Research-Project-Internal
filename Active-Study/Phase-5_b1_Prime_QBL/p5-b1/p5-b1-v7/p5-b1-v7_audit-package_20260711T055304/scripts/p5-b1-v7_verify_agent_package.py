#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import shutil
import subprocess
import tempfile
import zipfile

EXPECTED_ZIP = "0181c907c0fbe0e3e502fb72ad06ac13c2f9ab91146f2589a5c670094c7fc94c"
EXPECTED_DOC = "46996ac568f205d6a7cbb200a2c4108e77cec2b3e3b8e13a8aa5ffb854cba8ed"
PACKAGE_NAME = "p5-b1-v7_affine-follower-set-closure_20260711T103100"
DOC_REL = pathlib.Path("docs/QBL_CARRY_AFFINE_FOLLOWER_STRUCTURE_v5.md")


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stream_text(output: dict) -> str:
    text = output.get("text", "")
    if isinstance(text, list):
        return "".join(str(x) for x in text)
    return str(text)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path)
    args = ap.parse_args()

    zpath = args.zip_path.resolve()
    result: dict[str, object] = {
        "zip_path": str(zpath),
        "expected_zip_sha256": EXPECTED_ZIP,
        "actual_zip_sha256": sha256(zpath),
    }
    result["zip_sha256_pass"] = result["actual_zip_sha256"] == EXPECTED_ZIP

    with tempfile.TemporaryDirectory(prefix="p5b1v7-audit-") as td:
        td_path = pathlib.Path(td)
        with zipfile.ZipFile(zpath) as zf:
            zf.extractall(td_path)
        root = td_path / PACKAGE_NAME
        if not root.is_dir():
            raise RuntimeError(f"expected package root missing: {root}")

        manifest = json.loads((root / "MANIFEST.json").read_text())
        listed = sorted(entry["path"] for entry in manifest["files"])
        actual = sorted(
            str(p.relative_to(root))
            for p in root.rglob("*")
            if p.is_file() and p.name != "MANIFEST.json"
        )
        manifest_errors: list[dict[str, object]] = []
        for entry in manifest["files"]:
            p = root / entry["path"]
            if not p.is_file():
                manifest_errors.append({"path": entry["path"], "error": "missing"})
                continue
            size = p.stat().st_size
            digest = sha256(p)
            if size != entry["bytes"] or digest != entry["sha256"]:
                manifest_errors.append(
                    {
                        "path": entry["path"],
                        "error": "mismatch",
                        "actual_bytes": size,
                        "actual_sha256": digest,
                    }
                )

        result.update(
            {
                "manifest_entries": len(listed),
                "actual_nonmanifest_files": len(actual),
                "manifest_path_coverage_pass": listed == actual,
                "manifest_integrity_pass": not manifest_errors,
                "manifest_errors": manifest_errors,
                "document_sha256": sha256(root / DOC_REL),
            }
        )
        result["document_sha256_pass"] = result["document_sha256"] == EXPECTED_DOC

        executed = next((root / "notebooks").glob("*_executed.ipynb"))
        nb = json.loads(executed.read_text())
        code_cells = [c for c in nb["cells"] if c.get("cell_type") == "code"]
        passing = 0
        figures = 0
        for cell in code_cells:
            text = "".join(
                stream_text(o)
                for o in cell.get("outputs", [])
                if o.get("output_type") == "stream"
            )
            if "PASS" in text and "FAIL" not in text:
                passing += 1
            figures += sum(
                1
                for o in cell.get("outputs", [])
                if "image/png" in o.get("data", {})
            )
        result.update(
            {
                "notebook_code_cells": len(code_cells),
                "notebook_passing_cells": passing,
                "notebook_figures": figures,
                "notebook_pass": len(code_cells) == 16 and passing == 16 and figures == 16,
            }
        )

        rebuild_parent = td_path / "rebuild"
        rebuild_parent.mkdir()
        rebuild_root = rebuild_parent / PACKAGE_NAME
        shutil.copytree(root, rebuild_root)
        proc = subprocess.run(
            [
                "python",
                "scripts/20260711T103100_build_package.py",
                "--root",
                ".",
                "--zip",
            ],
            cwd=rebuild_root,
            text=True,
            capture_output=True,
        )
        rebuilt_zip = rebuild_parent / f"{PACKAGE_NAME}.zip"
        result.update(
            {
                "rebuild_returncode": proc.returncode,
                "rebuild_stdout": proc.stdout,
                "rebuild_stderr": proc.stderr,
                "rebuilt_zip_exists": rebuilt_zip.is_file(),
            }
        )
        if rebuilt_zip.is_file():
            result["rebuilt_zip_sha256"] = sha256(rebuilt_zip)
            result["byte_identical_rebuild_pass"] = rebuilt_zip.read_bytes() == zpath.read_bytes()
        else:
            result["byte_identical_rebuild_pass"] = False

    checks = [
        result["zip_sha256_pass"],
        result["manifest_path_coverage_pass"],
        result["manifest_integrity_pass"],
        result["document_sha256_pass"],
        result["notebook_pass"],
        result["rebuild_returncode"] == 0,
        result["byte_identical_rebuild_pass"],
    ]
    result["overall_pass"] = all(checks)

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    return 0 if result["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
