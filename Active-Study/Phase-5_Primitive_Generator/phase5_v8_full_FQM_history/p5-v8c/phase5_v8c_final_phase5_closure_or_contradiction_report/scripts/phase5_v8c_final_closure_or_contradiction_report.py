#!/usr/bin/env python3
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]

ALLOWED = {
    'CLOSED_POSITIVE',
    'CLOSED_NEGATIVE',
    'SUPERSEDED_WITH_EXPLICIT_REPLACEMENT',
    'DEFERRED_OUT_OF_PHASE_WITH_REASON',
    'BLOCKING_OPEN',
}

def read_csv(name):
    with open(ROOT / 'outputs' / name, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    rows = read_csv('final_target_status_matrix.csv')
    bad = [r for r in rows if r['status'] not in ALLOWED]
    blocking = [r for r in rows if r['status'] == 'BLOCKING_OPEN']
    deferrals = read_csv('classifier_deferral_decision_matrix.csv')
    bad_deferrals = [d for d in deferrals if not d['hard_scope_boundary'] or d['hard_scope_boundary'].lower().strip() == 'later theorem surface']
    summary = {
        'target_rows': len(rows),
        'bad_status_rows': len(bad),
        'blocking_open_rows': len(blocking),
        'classifier_deferrals': len(deferrals),
        'bad_deferrals': len(bad_deferrals),
        'phase5_closed': len(bad) == 0 and len(blocking) == 0 and len(bad_deferrals) == 0,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    if not summary['phase5_closed']:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
