#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

EXPECTED_ARCHIVE = "ee18e5d288231722a164843f96f772bb4288e103d1cd5a72ac5526f989fc35b5"
EXPECTED_DOCUMENT = "588f8e1627feda109773610a0854ce49c48052fc85367315bdd60df86ba7814d"
EXPECTED_ROOT = "p5-b3-v3_primary-pairing-recurrence_20260711T142511"
BUILD_SCRIPT = "scripts/20260711T142511_build_package.py"
DOCUMENT = "docs/QBL_PRIMARY_PAIRING_RECURRENCE_v1.md"

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result: dict[str, object] = {}
    result["archive_sha256"] = sha_file(args.archive)
    result["archive_hash_pass"] = result["archive_sha256"] == EXPECTED_ARCHIVE
    with zipfile.ZipFile(args.archive) as z:
        roots = {name.split("/")[0] for name in z.namelist() if name}
        if roots != {EXPECTED_ROOT}:
            raise SystemExit(f"unexpected archive roots: {roots}")
        manifest = json.loads(z.read(f"{EXPECTED_ROOT}/MANIFEST.json"))
        failures = []
        for row in manifest["files"]:
            data = z.read(f"{EXPECTED_ROOT}/{row['path']}")
            if len(data) != row["bytes"] or sha_bytes(data) != row["sha256"]:
                failures.append(row["path"])
        result["manifest_entries"] = len(manifest["files"])
        result["manifest_pass"] = not failures
        result["manifest_failures"] = failures
        doc = z.read(f"{EXPECTED_ROOT}/{DOCUMENT}")
        result["document_sha256"] = sha_bytes(doc)
        result["document_hash_pass"] = result["document_sha256"] == EXPECTED_DOCUMENT
        nb = json.loads(z.read(f"{EXPECTED_ROOT}/notebooks/20260711T142511_Primary_Pairing_executed.ipynb"))
        code = [c for c in nb["cells"] if c["cell_type"] == "code"]
        pass_cells = 0
        figure_cells = 0
        for cell in code:
            streams = "".join(
                "".join(o.get("text", [])) if isinstance(o.get("text", ""), list) else o.get("text", "")
                for o in cell.get("outputs", []) if o.get("output_type") == "stream"
            )
            if "PASS:" in streams and "FAIL:" not in streams:
                pass_cells += 1
            images = [o for o in cell.get("outputs", []) if "image/png" in o.get("data", {})]
            if len(images) == 1:
                figure_cells += 1
        result["notebook_code_cells"] = len(code)
        result["notebook_pass_cells"] = pass_cells
        result["notebook_figure_cells"] = figure_cells
    with tempfile.TemporaryDirectory() as td:
        parent = Path(td)
        with zipfile.ZipFile(args.archive) as z:
            z.extractall(parent)
        root = parent / EXPECTED_ROOT
        rebuilt = parent / "rebuilt.zip"
        proc = subprocess.run(
            [sys.executable, str(root / BUILD_SCRIPT), "--package-root", str(root), "--archive-out", str(rebuilt)],
            text=True, capture_output=True
        )
        result["rebuild_returncode"] = proc.returncode
        result["rebuild_stdout"] = proc.stdout.strip()
        result["rebuild_stderr"] = proc.stderr.strip()
        result["rebuilt_sha256"] = sha_file(rebuilt) if rebuilt.exists() else None
        result["byte_identical_rebuild"] = rebuilt.exists() and rebuilt.read_bytes() == args.archive.read_bytes()
    result["PASS"] = all([
        result["archive_hash_pass"], result["manifest_pass"], result["document_hash_pass"],
        result["notebook_code_cells"] == 14, result["notebook_pass_cells"] == 14,
        result["notebook_figure_cells"] == 14, result["rebuild_returncode"] == 0,
        result["byte_identical_rebuild"]
    ])
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
    if not result["PASS"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
