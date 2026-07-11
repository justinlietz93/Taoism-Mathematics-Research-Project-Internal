#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, hashlib, json, shutil, subprocess, sys, zipfile
from pathlib import Path
import nbformat
from nbclient import NotebookClient

TS='20260711T134500'
FIXED_DT=(2026,7,11,13,45,0)

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def execute_notebook(root):
    src=root/'notebooks'/f'{TS}_Factor_Scope.ipynb'; dst=root/'notebooks'/f'{TS}_Factor_Scope_executed.ipynb'
    nb=nbformat.read(src,as_version=4)
    client=NotebookClient(nb,timeout=180,kernel_name='python3',record_timing=False,allow_errors=False)
    client.execute(cwd=str(root))
    for idx,c in enumerate(nb.cells):
        c['id']=f'claim-{idx+1:02d}' if c.cell_type=='code' else f'md-{idx+1:02d}'
        c.metadata={}
        if c.cell_type=='code':
            c.execution_count=idx+1
            for o in c.get('outputs',[]): o['metadata']={}
    nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3'}}
    nbformat.write(nb,dst)
    figdir=root/'figures';
    for p in figdir.glob('*'):p.unlink()
    codecells=[c for c in nb.cells if c.cell_type=='code']
    if len(codecells)!=13:raise SystemExit('expected 13 code cells')
    report=[]
    for i,c in enumerate(codecells,1):
        streams=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        imgs=[o.data['image/png'] for o in c.outputs if o.output_type in ('display_data','execute_result') and 'image/png' in o.data]
        if len(imgs)!=1:raise SystemExit(f'cell {i}: expected one figure, got {len(imgs)}')
        if 'FAIL:' in streams:raise SystemExit(f'cell {i}: failure output')
        (figdir/f'{TS}_claim_{i:02d}.png').write_bytes(base64.b64decode(imgs[0]))
        report.append({'cell':i,'has_pass':('PASS' in streams),'status_lines':[line for line in streams.splitlines() if ':' in line]})
    (root/'outputs'/f'{TS}_notebook_verification.json').write_text(json.dumps({'code_cells':13,'figures':13,'cells':report},indent=2,sort_keys=True)+'\n')

def manifest(root):
    files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':files.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    obj={'package':root.name,'timestamp':TS,'hash_algorithm':'sha256','excluded':['MANIFEST.json'],'files':files}
    (root/'MANIFEST.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def make_zip(root,out):
    if out.exists():out.unlink()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file():continue
            rel=(Path(root.name)/p.relative_to(root)).as_posix(); info=zipfile.ZipInfo(rel,FIXED_DT); info.compress_type=zipfile.ZIP_DEFLATED; info.create_system=3; info.external_attr=(0o100644&0xffff)<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--package-root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--archive-out',type=Path,required=True); a=ap.parse_args(); root=a.package_root.resolve(); out=a.archive_out.resolve()
    for p in (root/'outputs').glob('*'):p.unlink()
    for p in (root/'trace').glob('*'):p.unlink()
    executed=root/'notebooks'/f'{TS}_Factor_Scope_executed.ipynb'
    if executed.exists():executed.unlink()
    subprocess.run([sys.executable,str(root/'scripts'/f'{TS}_derive_factor_scope.py'),'--package-root',str(root)],check=True)
    execute_notebook(root)
    (root/'outputs'/f'{TS}_build_summary.json').write_text(json.dumps({'derivation':'PASS','notebook_execution':'PASS','figures':13,'archive_deterministic_settings':True},indent=2,sort_keys=True)+'\n')
    manifest(root); make_zip(root,out); digest=sha(out); Path(str(out)+'.sha256').write_text(f'{digest}  {out.name}\n')
    print(digest)
if __name__=='__main__':main()
