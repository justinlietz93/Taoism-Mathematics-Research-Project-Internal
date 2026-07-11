#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def build_manifest(root: Path) -> dict:
    entries = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.json":
            continue
        rel = path.relative_to(root).as_posix()
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"} or ".pytest_cache" in path.parts:
            raise SystemExit(f"cache file present: {rel}")
        data = path.read_bytes()
        entries.append({
            "path": rel,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
        })
    return {
        "schema": "p5-v8x-manifest-v1",
        "excludes": ["MANIFEST.json"],
        "entries": entries,
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    manifest = build_manifest(root)
    (root / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"manifest_entries": len(manifest["entries"]), "root": str(root)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
