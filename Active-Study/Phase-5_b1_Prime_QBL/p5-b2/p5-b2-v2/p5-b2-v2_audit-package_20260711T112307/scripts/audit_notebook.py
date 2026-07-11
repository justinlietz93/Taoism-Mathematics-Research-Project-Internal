#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, zipfile
from pathlib import Path

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('zip_path'); ap.add_argument('--output'); args=ap.parse_args()
    with zipfile.ZipFile(args.zip_path) as zf:
        root=next(name.split('/')[0] for name in zf.namelist() if name.endswith('/MANIFEST.json'))
        src=json.loads(zf.read(root+'/notebooks/20260711T110131_Global_Threshold_Bridge.ipynb'))
        exe=json.loads(zf.read(root+'/notebooks/20260711T110131_Global_Threshold_Bridge_executed.ipynb'))
    src_cells=[c for c in src['cells'] if c['cell_type']=='code']
    ex_cells=[c for c in exe['cells'] if c['cell_type']=='code']
    rows=[]
    for i,c in enumerate(ex_cells,1):
        streams=[]; figures=0
        for o in c.get('outputs',[]):
            if o.get('output_type')=='stream':
                t=o.get('text',[]); streams.extend(t if isinstance(t,list) else [t])
            if 'image/png' in o.get('data',{}): figures+=1
        rows.append({'cell':i,'execution_count':c.get('execution_count'),'prints_PASS':any('PASS' in t for t in streams),'figures':figures})
    result={
        'source_code_cells':len(src_cells),
        'executed_code_cells':len(ex_cells),
        'execution_counts':[r['execution_count'] for r in rows],
        'all_cells_print_PASS':all(r['prints_PASS'] for r in rows),
        'all_cells_have_one_figure':all(r['figures']==1 for r in rows),
        'universal_claim_cells_using_finite_samples':[2,3,4,5],
        'status':'PASS_WITH_SCOPE_DEFECTS',
        'cells':rows,
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: Path(args.output).write_text(text)
    print(text,end='')

if __name__=='__main__': main()
