#!/usr/bin/env python3
import csv, json
from pathlib import Path

ALLOWED = {
    'CLOSED_POSITIVE',
    'CLOSED_NEGATIVE',
    'SUPERSEDED_WITH_EXPLICIT_REPLACEMENT',
    'DEFERRED_OUT_OF_PHASE_WITH_REASON',
    'BLOCKING_OPEN',
}

def validate_ledger(path: str) -> dict:
    rows = list(csv.DictReader(open(path, newline='')))
    bad = [r for r in rows if r['status'] not in ALLOWED]
    blocking = [r for r in rows if r['status'] == 'BLOCKING_OPEN']
    empty_next = [r for r in rows if not r.get('next_action')]
    return {
        'rows': len(rows),
        'bad_status_rows': len(bad),
        'blocking_open_rows': len(blocking),
        'empty_next_action_rows': len(empty_next),
        'phase5_can_close': len(blocking) == 0,
        'pass': len(bad) == 0 and len(empty_next) == 0 and len(blocking) > 0,
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    result = validate_ledger(str(root / 'outputs' / 'open_targets_master_ledger.csv'))
    print(json.dumps(result, indent=2))
