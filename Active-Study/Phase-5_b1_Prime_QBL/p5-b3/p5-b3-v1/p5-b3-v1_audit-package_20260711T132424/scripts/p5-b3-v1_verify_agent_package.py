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

import nbformat

EXPECTED_ARCHIVE_SHA = "02b31cd1c48fdfd018bf93c9024ab2256db6e2bcfacde4a8035a13eb81d2e880"
EXPECTED_DOCUMENT_SHA = "8e87b2b0dd6c991bc0d66b2eee51f6f8a4b6c736b96b268e0f51ce50f0dd0fab"
EXPECTED_ROOT = "p5-b3-v1_hierarchical-grammar-lift_20260711T120831"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    archive = args.archive.resolve()
    result: dict[str, object] = {
        "archive": str(archive),
        "expected_archive_sha256": EXPECTED_ARCHIVE_SHA,
        "actual_archive_sha256": sha256(archive),
    }
    result["archive_hash_pass"] = result["actual_archive_sha256"] == EXPECTED_ARCHIVE_SHA

    with tempfile.TemporaryDirectory(prefix="p5b3v1-audit-") as temp_name:
        temp = Path(temp_name)
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(temp)
        root = temp / EXPECTED_ROOT
        if not root.is_dir():
            raise SystemExit(f"missing expected root {EXPECTED_ROOT}")

        manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
        manifest_errors: list[dict[str, object]] = []
        for record in manifest["files"]:
            path = root / record["path"]
            if not path.exists():
                manifest_errors.append({"path": record["path"], "error": "missing"})
                continue
            actual_size = path.stat().st_size
            actual_hash = sha256(path)
            if actual_size != record["bytes"] or actual_hash != record["sha256"]:
                manifest_errors.append({
                    "path": record["path"],
                    "expected_bytes": record["bytes"],
                    "actual_bytes": actual_size,
                    "expected_sha256": record["sha256"],
                    "actual_sha256": actual_hash,
                })
        listed = {record["path"] for record in manifest["files"]}
        actual = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file() and path.name != "MANIFEST.json"
        }
        result["manifest_entries"] = len(manifest["files"])
        result["manifest_errors"] = manifest_errors
        result["manifest_unlisted_files"] = sorted(actual - listed)
        result["manifest_missing_files"] = sorted(listed - actual)
        result["manifest_pass"] = not manifest_errors and actual == listed

        document = root / "docs/QBL_HIERARCHICAL_GRAMMAR_LIFT_v1.md"
        result["actual_document_sha256"] = sha256(document)
        result["expected_document_sha256"] = EXPECTED_DOCUMENT_SHA
        result["document_hash_pass"] = result["actual_document_sha256"] == EXPECTED_DOCUMENT_SHA

        source_nb = nbformat.read(root / "notebooks/20260711T120831_Hierarchical_Grammar_Lift.ipynb", as_version=4)
        executed_nb = nbformat.read(root / "notebooks/20260711T120831_Hierarchical_Grammar_Lift_executed.ipynb", as_version=4)
        source_codes = [cell for cell in source_nb.cells if cell.cell_type == "code"]
        executed_codes = [cell for cell in executed_nb.cells if cell.cell_type == "code"]
        pass_cells = 0
        figure_count = 0
        bad_cells: list[int] = []
        for index, cell in enumerate(executed_codes, 1):
            stream = "".join(
                output.get("text", "")
                for output in cell.get("outputs", [])
                if output.get("output_type") == "stream"
            )
            figures = sum(
                1 for output in cell.get("outputs", [])
                if "image/png" in output.get("data", {})
            )
            figure_count += figures
            if "PASS" in stream and "FAIL" not in stream and figures == 1:
                pass_cells += 1
            else:
                bad_cells.append(index)
        result["source_notebook_code_cells"] = len(source_codes)
        result["executed_notebook_code_cells"] = len(executed_codes)
        result["executed_notebook_pass_cells"] = pass_cells
        result["executed_notebook_figures"] = figure_count
        result["executed_notebook_bad_cells"] = bad_cells
        result["notebook_shape_pass"] = (
            len(source_codes) == 12
            and len(executed_codes) == 12
            and pass_cells == 12
            and figure_count == 12
        )

        # Rebuild under the exact original root name because that name is stored inside the ZIP.
        rebuild_parent = temp / "clean-rebuild"
        rebuild_parent.mkdir()
        rebuild_root = rebuild_parent / EXPECTED_ROOT
        shutil.copytree(root, rebuild_root)
        rebuilt_zip = rebuild_parent / f"{EXPECTED_ROOT}.zip"
        command = [
            sys.executable,
            str(rebuild_root / "scripts/20260711T120831_build_package.py"),
            "--package-root", str(rebuild_root),
            "--archive-out", str(rebuilt_zip),
        ]
        completed = subprocess.run(command, capture_output=True, text=True)
        result["rebuild_returncode"] = completed.returncode
        result["rebuild_stdout"] = completed.stdout
        result["rebuild_stderr"] = completed.stderr
        result["rebuilt_archive_sha256"] = sha256(rebuilt_zip) if rebuilt_zip.exists() else None
        result["byte_identical_rebuild"] = rebuilt_zip.exists() and rebuilt_zip.read_bytes() == archive.read_bytes()

        builder_text = (root / "scripts/20260711T120831_build_package.py").read_text(encoding="utf-8")
        result["builder_executes_notebook"] = "ExecutePreprocessor" in builder_text or "nbconvert" in builder_text
        result["builder_regenerates_figures"] = "figures" in builder_text and "savefig" in builder_text
        result["builder_regenerates_all_outputs"] = False
        result["builder_scope"] = (
            "Runs the derivation script, validates already-executed notebooks, rewrites the manifest, "
            "and reconstructs the deterministic ZIP. It does not execute the notebook or regenerate most figures, traces, or outputs."
        )

    result["overall_integrity_pass"] = all([
        result["archive_hash_pass"],
        result["manifest_pass"],
        result["document_hash_pass"],
        result["notebook_shape_pass"],
        result["byte_identical_rebuild"],
    ])
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["overall_integrity_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
