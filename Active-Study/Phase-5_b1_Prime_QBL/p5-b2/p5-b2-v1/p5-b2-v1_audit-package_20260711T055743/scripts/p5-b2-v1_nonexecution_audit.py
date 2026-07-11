#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESPONSE = ROOT / "inputs" / "p5-b2-v1_AGENT_RESPONSE.txt"
OUTPUT = ROOT / "outputs" / "p5-b2-v1_nonexecution-audit.json"

REQUIRED_ARTIFACT_SIGNALS = {
    "document_link": "Corrected" ,
    "package_name": "p5-b2-v1_global-threshold-bridge_",
    "document_hash": "Document SHA-256",
    "package_hash": "Package SHA-256",
    "binet": "Binet",
    "finite_certificate": "finite certificate",
}


def main() -> int:
    text = RESPONSE.read_text(encoding="utf-8")
    signals = {name: token in text for name, token in REQUIRED_ARTIFACT_SIGNALS.items()}
    executed = all(signals.values())
    result = {
        "interaction_id": "p5-b2-v1",
        "verdict": "PASS_EXECUTED" if executed else "REJECT_NO_EXECUTION",
        "required_signal_checks": signals,
        "branch_1_status": "CLOSED",
        "branch_2_status": "OPEN",
        "next_interaction": "p5-b2-v2",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not executed and result["verdict"] == "REJECT_NO_EXECUTION" else 1


if __name__ == "__main__":
    raise SystemExit(main())
