#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, hashlib, json, shutil, subprocess, sys, zipfile
from pathlib import Path
import nbformat
from nbclient import NotebookClient

TS='20260711T142511'
FIXED_DT=(2026,7,11,14,25,12)

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def execute_notebook(root):
    src=root/'notebooks'/f'{TS}_Primary_Pairing.ipynb';dst=root/'notebooks'/f'{TS}_Primary_Pairing_executed.ipynb'
    nb=nbformat.read(src,as_version=4)
    NotebookClient(nb,timeout=240,kernel_name='python3',record_timing=False,allow_errors=False).execute(cwd=str(root))
    code=[c for c in nb.cells if c.cell_type=='code']
    if len(code)!=14:raise SystemExit(f'expected 14 code cells, got {len(code)}')
    figdir=root/'figures';figdir.mkdir(exist_ok=True)
    for p in figdir.glob('*'):p.unlink()
    report=[]
    for idx,c in enumerate(nb.cells):
        c['id']=('claim' if c.cell_type=='code' else 'md')+f'-{idx:02d}';c.metadata={}
        if c.cell_type=='code':
            c.execution_count=len([x for x in nb.cells[:idx+1] if x.cell_type=='code'])
            streams=''.join(o.get('text','') for o in c.get('outputs',[]) if o.output_type=='stream')
            imgs=[o.data['image/png'] for o in c.get('outputs',[]) if o.output_type in ('display_data','execute_result') and 'image/png' in o.data]
            if len(imgs)!=1:raise SystemExit(f'cell {c.execution_count} expected one figure, got {len(imgs)}')
            if 'FAIL:' in streams:raise SystemExit(f'cell {c.execution_count} emitted FAIL')
            if 'PASS:' not in streams:raise SystemExit(f'cell {c.execution_count} missing PASS')
            (figdir/f'{TS}_claim_{c.execution_count:02d}.png').write_bytes(base64.b64decode(imgs[0]))
            for o in c.get('outputs',[]):o['metadata']={}
            report.append({'cell':c.execution_count,'pass':True,'status_lines':[line for line in streams.splitlines() if line.startswith(('PASS:','FAIL:'))]})
    nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3'}}
    nbformat.write(nb,dst)
    (root/'outputs'/f'{TS}_notebook_verification.json').write_text(json.dumps({'code_cells':14,'figures':14,'cells':report},indent=2,sort_keys=True)+'\n')

def manifest(root):
    files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':files.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    (root/'MANIFEST.json').write_text(json.dumps({'package':root.name,'timestamp':TS,'hash_algorithm':'sha256','excluded':['MANIFEST.json'],'files':files},indent=2,sort_keys=True)+'\n')

def make_zip(root,out):
    if out.exists():out.unlink()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file():continue
            rel=(Path(root.name)/p.relative_to(root)).as_posix();info=zipfile.ZipInfo(rel,FIXED_DT);info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3;info.external_attr=(0o100644&0xffff)<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package-root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--archive-out',type=Path,required=True);a=ap.parse_args();root=a.package_root.resolve();out=a.archive_out.resolve()
    for d in ['outputs','trace','figures']:
        for p in (root/d).glob('*'):p.unlink()
    ex=root/'notebooks'/f'{TS}_Primary_Pairing_executed.ipynb'
    if ex.exists():ex.unlink()
    subprocess.run([sys.executable,str(root/'scripts'/f'{TS}_derive_primary_pairing.py'),'--package-root',str(root)],check=True)
    execute_notebook(root)
    (root/'outputs'/f'{TS}_build_summary.json').write_text(json.dumps({'derivation':'PASS','notebook_execution':'PASS','figures':14,'deterministic_zip_settings':True,'pairing_recurrence_claimed':False},indent=2,sort_keys=True)+'\n')
    manifest(root);make_zip(root,out);digest=sha(out);Path(str(out)+'.sha256').write_text(f'{digest}  {out.name}\n');print(digest)
if __name__=='__main__':main()
