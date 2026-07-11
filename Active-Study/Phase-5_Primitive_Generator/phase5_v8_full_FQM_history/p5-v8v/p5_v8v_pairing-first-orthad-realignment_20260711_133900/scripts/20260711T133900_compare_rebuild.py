#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260711T133900"

EXCLUSIONS = [
    "MANIFEST.json",
    f"outputs/{STAMP}_pytest_junit.xml",
    f"outputs/{STAMP}_test_results.json",
    f"outputs/{STAMP}_reproducibility_comparison.json",
    f"notebooks/{STAMP}_pairing_first_realign_executed.ipynb",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scientific_paths(root: Path) -> list[Path]:
    paths = []
    for folder in ("outputs", "trace"):
        for path in sorted((root / folder).glob(f"{STAMP}_*")):
            rel = path.relative_to(root).as_posix()
            if rel not in EXCLUSIONS and path.is_file():
                paths.append(path)
    return paths


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="p5_v8v_rebuild_") as temp:
        target = Path(temp) / ROOT.name
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns("MANIFEST.json", "__pycache__", "*.pyc", ".pytest_cache"))
        for path in scientific_paths(target):
            path.unlink()
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["PYTHONPATH"] = str(target / "src")
        proc = subprocess.run(
            [sys.executable, str(target / "scripts" / f"{STAMP}_rebuild.py")],
            cwd=target,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        rows = []
        for original in scientific_paths(ROOT):
            rel = original.relative_to(ROOT)
            rebuilt = target / rel
            rows.append({
                "path": rel.as_posix(),
                "original_sha256": digest(original),
                "rebuilt_sha256": digest(rebuilt) if rebuilt.exists() else None,
                "match": rebuilt.exists() and digest(original) == digest(rebuilt),
            })
        result = {
            "contract": "NORMALIZED_SEMANTIC_REPRODUCIBILITY",
            "rebuild_exit_code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "normalized_exclusions": EXCLUSIONS,
            "artifacts": rows,
            "pass": proc.returncode == 0 and all(row["match"] for row in rows),
        }
        out = ROOT / "outputs" / f"{STAMP}_reproducibility_comparison.json"
        out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps({"pass": result["pass"], "artifacts": len(rows)}, sort_keys=True))
        return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
