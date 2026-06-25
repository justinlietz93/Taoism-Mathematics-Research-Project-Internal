#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
claim_path = ROOT / "bridge_claim_dependency_graph_v56.csv"
blocker_path = ROOT / "hard_blocker_decision_matrix_v56.csv"
rows = list(csv.DictReader(open(claim_path, encoding="utf-8")))
blockers = list(csv.DictReader(open(blocker_path, encoding="utf-8")))
ids = {r["claim_id"] for r in rows}
failures = []
for r in rows:
    deps = [d for d in r["depends_on"].split(",") if d]
    missing = [d for d in deps if d not in ids]
    if missing:
        failures.append((r["claim_id"], "missing_dependency", missing))
    if not r["kill_test"].strip():
        failures.append((r["claim_id"], "missing_kill_test", []))
    if not r["next_to_100"].strip():
        failures.append((r["claim_id"], "missing_to_100", []))

blocking = [b for b in blockers if b["blocks_100"] == "yes"]
closed = [r for r in rows if r["status"].startswith("LOCKED") or r["status"].startswith("COMPLETE")]
open_rows = [r for r in rows if r not in closed]

print("PASS" if not failures else "FAIL")
print(f"claims={len(rows)}")
print(f"closed_or_current_locked={len(closed)}")
print(f"open_or_data_pending={len(open_rows)}")
print(f"hard_100_blockers={len(blocking)}")
if failures:
    print(failures)
