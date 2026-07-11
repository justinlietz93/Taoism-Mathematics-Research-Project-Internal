#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
required=[
 root/'outputs'/'20260711T141656_claim_model.json',
 root/'outputs'/'20260711T141656_pairing_type_source_claim_matrix.csv',
 root/'outputs'/'20260711T141656_pairing_type_elimination_table.csv',
 root/'outputs'/'20260711T141656_primitive_sanity_check.json',
]
for p in required:
    if not p.exists(): raise SystemExit(f'missing {p}')
print(json.dumps({'status':'REBUILD_INPUTS_PRESENT','artifacts':len(required),'sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in required}},indent=2))
