#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
fail=[]
for row in csv.DictReader(open(root/'outputs/phase5_v8k_radical_bii_zero_gate.csv')):
    if row['pass'] not in ('True','true','1'):
        fail.append(('RADICAL_BII_ZERO',row))
for row in csv.DictReader(open(root/'outputs/phase5_v8k_worked_target_certificate.csv')):
    bm=json.loads(row['basis_matrix_json'])
    if not isinstance(bm,list) or any(not isinstance(x,list) for x in bm):
        fail.append(('CERTIFICATE_IS_DATA',row))
for row in csv.DictReader(open(root/'outputs/phase5_v8k_form_spec_complete.csv')):
    if not row.get('diag_units_mod_2D'):
        fail.append(('FORM_SPEC_COMPLETE',row))
print('PASS' if not fail else 'FAIL', len(fail))
if fail:
    for f in fail[:10]: print(f)
    sys.exit(1)
