#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
# The full verifier is embedded in phase5_v8m_generate_package.py; rerun generation to reproduce gates.
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
rows=list(csv.DictReader(open(root/'outputs'/'phase5_v8m_sectionV_verifier_results.csv')))
fail=[r for r in rows if r['certificate_verified']!='True']
print('rows',len(rows),'failures',len(fail))
sys.exit(1 if fail else 0)
