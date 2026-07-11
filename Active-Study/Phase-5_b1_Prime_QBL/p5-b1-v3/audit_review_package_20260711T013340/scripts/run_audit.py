#!/usr/bin/env python3
"""Run both audit checks and write a combined machine-readable summary."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> None:
    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    outputs = args.root / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    j_out = outputs / "j_derivation_audit.json"
    package_out = outputs / "package_integrity_audit.json"
    run([sys.executable, str(args.root / "scripts" / "audit_j_derivation.py"), "--inputs", str(args.root / "inputs"), "--out", str(j_out)])
    run([sys.executable, str(args.root / "scripts" / "audit_package_integrity.py"), "--inputs", str(args.root / "inputs"), "--out", str(package_out)])
    combined = {
        "status": "REVISE",
        "j_derivation": json.loads(j_out.read_text(encoding="utf-8")),
        "package_integrity": json.loads(package_out.read_text(encoding="utf-8")),
    }
    combined_out = outputs / "combined_audit.json"
    combined_out.write_text(json.dumps(combined, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": combined["status"], "output": str(combined_out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
