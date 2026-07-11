#!/usr/bin/env python3
import csv, hashlib, json, os, shutil, sys, tempfile, zipfile
from pathlib import Path

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load_root(arg):
    p=Path(arg)
    if p.is_dir(): return p,None
    td=Path(tempfile.mkdtemp(prefix='p5v8u_verify_'))
    with zipfile.ZipFile(p) as z: z.extractall(td)
    roots=[x for x in td.iterdir() if x.is_dir()]
    if len(roots)!=1: raise SystemExit('ZIP must contain one root')
    return roots[0],td
root,tmp=load_root(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
sys.path.insert(0,str(root/'src'))
from orthad_v8u.verification import verify_scientific,run_pytest
gates=verify_scientific(root,'20260711T121112')
cp,xml=run_pytest(root,'20260711T121112')
gates.append({'gate':'PYTEST_EXIT_STATUS','pass':cp.returncode==0,'evidence_class':'MECHANICALLY_RECOMPUTED','detail':{'returncode':cp.returncode,'stdout':cp.stdout[-2000:],'stderr':cp.stderr[-2000:]}})
# Notebook executed gate.
nb=json.loads((root/'notebooks'/'20260711T121112_successor_seed_and_covariance_executed.ipynb').read_text())
nb_ok=all(c.get('execution_count') is not None for c in nb['cells'] if c.get('cell_type')=='code') and any(c.get('outputs') for c in nb['cells'] if c.get('cell_type')=='code')
gates.append({'gate':'EXECUTED_NOTEBOOK_COMPLETE','pass':nb_ok,'evidence_class':'MECHANICALLY_RECOMPUTED','detail':{'code_cells':sum(c.get('cell_type')=='code' for c in nb['cells'])}})
# Manifest exact set and content.
man=json.loads((root/'MANIFEST.json').read_text()); entries={e['path']:e for e in man['files']}
actual={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts and p.suffix!='.pyc'}
manifest_ok=set(entries)==set(actual) and all(entries[k]['bytes']==actual[k].stat().st_size and entries[k]['sha256']==sha(actual[k]) for k in actual)
gates.append({'gate':'MANIFEST_INTEGRITY','pass':manifest_ok,'evidence_class':'MECHANICALLY_RECOMPUTED','detail':{'manifest_entries':len(entries),'actual_entries':len(actual)}})
cache=list(root.rglob('__pycache__'))+list(root.rglob('*.pyc'))
gates.append({'gate':'NO_CACHE_BYTECODE','pass':not cache,'evidence_class':'MECHANICALLY_RECOMPUTED','detail':[str(p) for p in cache]})
# Controls summary must be all fired, count dynamic.
ctrl=json.loads((root/'outputs'/'20260711T121112_corruption_control_summary.json').read_text())
gates.append({'gate':'CORRUPTION_CONTROLS','pass':ctrl['total']>0 and ctrl['fired']==ctrl['total'],'evidence_class':'MECHANICALLY_RECOMPUTED','detail':ctrl})
passed=sum(g['pass'] for g in gates)
print(json.dumps({'passed':passed,'total':len(gates),'gates':gates},indent=2))
if tmp: shutil.rmtree(tmp)
raise SystemExit(0 if passed==len(gates) else 1)
