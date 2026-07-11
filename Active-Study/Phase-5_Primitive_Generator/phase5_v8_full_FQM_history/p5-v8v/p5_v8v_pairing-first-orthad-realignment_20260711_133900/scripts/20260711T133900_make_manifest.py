#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.json"


def main() -> int:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if "__pycache__" in path.parts or path.suffix == ".pyc" or ".pytest_cache" in path.parts:
            raise RuntimeError(f"cache path present: {rel}")
        entries.append({
            "path": rel,
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        })
    MANIFEST.write_text(json.dumps({"schema": "p5-manifest-v1", "entries": entries}, indent=2) + "\n")
    print(json.dumps({"entries": len(entries)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
