#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, zipfile
from pathlib import Path
import nbformat
from nbclient import NotebookClient

TS='20260711T145605'
FIXED_DT=(2026,7,11,14,56,6)
RECOGNIZED=('PASS','FAIL','MODEL WITNESS','CONDITIONAL CHECK','STATUS')


def sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()


def dump(path:Path,obj):path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')


def execute_notebook(root:Path):
    src=root/'notebooks'/f'{TS}_Primary_Pairing_Type_Boundary.ipynb'
    dst=root/'notebooks'/f'{TS}_Primary_Pairing_Type_Boundary_executed.ipynb'
    nb=nbformat.read(src,as_version=4)
    nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.11'}}
    for i,c in enumerate(nb.cells):
        c['id']=('md' if c.cell_type=='markdown' else 'claim')+f'-{i:02d}';c.metadata={}
    NotebookClient(nb,timeout=240,kernel_name='python3',record_timing=False,allow_errors=False).execute(cwd=str(root))
    figdir=root/'figures';figdir.mkdir(exist_ok=True)
    for p in figdir.glob('*'):p.unlink()
    code_cells=[c for c in nb.cells if c.cell_type=='code']
    if len(code_cells)!=15:raise SystemExit(f'expected 15 code cells, got {len(code_cells)}')
    report=[]
    for ci,c in enumerate(code_cells,1):
        texts=[];images=[]
        for out in c.get('outputs',[]):
            if out.output_type=='stream':texts.append(out.get('text',''))
            elif out.output_type in ('execute_result','display_data'):
                data=out.get('data',{})
                if 'text/plain' in data:texts.append(data['text/plain'])
                if 'image/png' in data:images.append(data['image/png'])
        joined='\n'.join(texts)
        if not any(token in joined for token in RECOGNIZED):raise SystemExit(f'cell {ci} has no recognized status')
        if 'FAIL' in joined:raise SystemExit(f'cell {ci} failed')
        if len(images)!=1:raise SystemExit(f'cell {ci} expected one figure, got {len(images)}')
        import base64
        fp=figdir/f'{TS}_claim_{ci:02d}.png';fp.write_bytes(base64.b64decode(images[0]))
        report.append({'cell':ci,'status_line':next((line for line in joined.splitlines() if any(t in line for t in RECOGNIZED)),''),'figure':fp.name})
        c.metadata={}
        c.execution_count=ci
    nb.metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.11'}}
    nbformat.write(nb,dst)
    dump(root/'outputs'/f'{TS}_notebook_verification.json',{'code_cells':len(code_cells),'figures':len(report),'cells':report,'all_executed':True})
    return len(code_cells),len(report)


def build_manifest(root:Path):
    files=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.name=='MANIFEST.json':continue
        rel=p.relative_to(root).as_posix()
        files.append({'path':rel,'sha256':sha(p),'size':p.stat().st_size})
    manifest={'schema':'qbl-experiment-manifest-v1','package':root.name,'hash_rule':'all package files except MANIFEST.json','files':files}
    dump(root/'MANIFEST.json',manifest)
    return manifest


def make_zip(root:Path,out:Path):
    if out.exists():out.unlink()
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file():continue
            rel=(Path(root.name)/p.relative_to(root)).as_posix()
            info=zipfile.ZipInfo(rel,FIXED_DT);info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3;info.external_attr=(0o100644&0xffff)<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package-root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--archive',type=Path);a=ap.parse_args();root=a.package_root.resolve();archive=(a.archive.resolve() if a.archive else root.parent/(root.name+'.zip'))
    # Remove generated artifacts before rerun.
    for p in [root/'MANIFEST.json',root/'notebooks'/f'{TS}_Primary_Pairing_Type_Boundary_executed.ipynb']:
        if p.exists():p.unlink()
    subprocess.run([sys.executable,str(root/'scripts'/f'{TS}_derive_type_boundary.py'),'--package-root',str(root)],check=True)
    cells,figures=execute_notebook(root)
    summary={'package':root.name,'derivation':'PASS','notebook_cells':cells,'figures':figures,'branch_status':'OPEN','lean_status':'LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED'}
    dump(root/'outputs'/f'{TS}_build_summary.json',summary)
    manifest=build_manifest(root)
    make_zip(root,archive)
    digest=sha(archive)
    Path(str(archive)+'.sha256').write_text(f'{digest}  {archive.name}\n')
    print(json.dumps({'archive':str(archive),'sha256':digest,'manifest_entries':len(manifest['files']),'notebook_cells':cells,'figures':figures,'PASS':True},indent=2))

if __name__=='__main__':main()
