#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
fail=[]
for r in csv.DictReader(open(root/'outputs/phase5_v8l_scope_completeness_gates.csv')):
    if r['pass'] not in ('True','true','1'): fail.append(('scope',r))
for r in csv.DictReader(open(root/'outputs/phase5_v8l_certificate_gate_results.csv')):
    if r['gate'] in ('TRUE_DIAGONAL_RANK4_TABLE_PUBLISHED','RADICAL_BII_ZERO','FORM_SPEC_COMPLETE') and r['pass'] not in ('True','true','1'):
        fail.append(('gate',r))
print('PASS' if not fail else 'FAIL', len(fail))
if fail:
    print(fail[:5]); sys.exit(1)
