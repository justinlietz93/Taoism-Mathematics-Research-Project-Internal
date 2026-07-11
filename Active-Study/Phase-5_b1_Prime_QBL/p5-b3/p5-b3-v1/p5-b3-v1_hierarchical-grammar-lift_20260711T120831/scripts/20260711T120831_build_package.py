#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys, zipfile
from pathlib import Path

FIXED_DT=(2026,7,11,12,8,32)

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''): h.update(b)
    return h.hexdigest()

def write_manifest(root):
    files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':
            files.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    obj={'package':root.name,'timestamp':'20260711T120831','hash_algorithm':'sha256','excluded':['MANIFEST.json'],'files':files}
    (root/'MANIFEST.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def make_zip(root,out):
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file(): continue
            rel=(Path(root.name)/p.relative_to(root)).as_posix()
            i=zipfile.ZipInfo(rel,FIXED_DT); i.compress_type=zipfile.ZIP_DEFLATED; i.external_attr=(0o100644&0xffff)<<16; i.create_system=3
            z.writestr(i,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--package-root',type=Path,default=Path(__file__).resolve().parents[1]); ap.add_argument('--archive-out',type=Path,required=True)
    a=ap.parse_args(); root=a.package_root.resolve(); out=a.archive_out.resolve()
    subprocess.run([sys.executable,str(root/'scripts/20260711T120831_derive_factor.py'),'--package-root',str(root)],check=True)
    # The source and executed notebooks are fixed, no-I/O proof companions. Verify their required shape.
    import nbformat
    for name in ['20260711T120831_Hierarchical_Grammar_Lift.ipynb','20260711T120831_Hierarchical_Grammar_Lift_executed.ipynb']:
        nb=nbformat.read(root/'notebooks'/name,as_version=4)
        codes=[c for c in nb.cells if c.cell_type=='code']
        if len(codes)!=12: raise SystemExit(f'{name}: expected 12 code cells')
        if 'executed' in name:
            for c in codes:
                text=''.join(o.get('text','') for o in c.get('outputs',[]) if o.get('output_type')=='stream')
                figs=sum(1 for o in c.get('outputs',[]) if 'image/png' in o.get('data',{}))
                if 'PASS' not in text or 'FAIL' in text or figs!=1: raise SystemExit(f'bad executed cell {c.id}')
    write_manifest(root); make_zip(root,out)
    digest=sha(out); Path(str(out)+'.sha256').write_text(f'{digest}  {out.name}\n',encoding='utf-8')
    print(digest)
if __name__=='__main__': main()
