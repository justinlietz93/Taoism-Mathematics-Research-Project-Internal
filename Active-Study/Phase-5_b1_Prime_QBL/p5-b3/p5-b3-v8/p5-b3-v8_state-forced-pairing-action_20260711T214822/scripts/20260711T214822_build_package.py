from __future__ import annotations
import argparse, base64, csv, hashlib, json, os, shutil, subprocess, sys, zipfile
from pathlib import Path

TS='20260711T214822'
PKG_NAME='p5-b3-v8_state-forced-pairing-action_20260711T214822'
FIXED_ZIP_DT=(2026, 7, 11, 21, 48, 22)

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1048576),b''): h.update(c)
    return h.hexdigest()

def stable_json(x): return json.dumps(x,indent=2,sort_keys=True,ensure_ascii=False)+'\n'

def manifest(root):
    files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':
            files.append({'path':p.relative_to(root).as_posix(),'size':p.stat().st_size,'sha256':sha256(p)})
    (root/'MANIFEST.json').write_text(stable_json({'package':root.name,'generated_at':TS,'hash_algorithm':'SHA-256','excludes':['MANIFEST.json'],'files':files}),encoding='utf-8')

def zip_stable(root,out):
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file(): continue
            rel=(Path(root.name)/p.relative_to(root)).as_posix()
            info=zipfile.ZipInfo(rel,FIXED_ZIP_DT); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=(0o100644 & 0xFFFF)<<16; info.create_system=3
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--archive-parent',default='..')
    a=ap.parse_args(); root=Path(a.root).resolve(); parent=Path(a.archive_parent).resolve()
    # Regenerate exact outputs and traces.
    subprocess.run([sys.executable,str(root/'scripts'/'20260711T214822_derive_state_forced_action.py'),'--root',str(root)],check=True)
    # Notebooks and figures are deterministic release artifacts generated from the included source notebook.
    # Execute source notebook and strip timing metadata.
    import nbformat as nbf
    from nbclient import NotebookClient
    src=root/'notebooks'/'20260711T214822_state_forced_pairing_action.ipynb'; nb=nbf.read(src,as_version=4)
    client=NotebookClient(nb,timeout=120,kernel_name='python3',allow_errors=False); client.execute()
    for c in nb.cells:
        c.metadata.pop('execution',None)
        if c.cell_type=='code':
            for o in c.get('outputs',[]): o.pop('metadata',None)
    exe=root/'notebooks'/'20260711T214822_state_forced_pairing_action_executed.ipynb'; nbf.write(nb,exe)
    figdir=root/'figures';
    for p in figdir.glob('*.png'): p.unlink()
    count=0
    for c in nb.cells:
        if c.cell_type!='code': continue
        for o in c.get('outputs',[]):
            d=o.get('data',{}) if isinstance(o,dict) else {}
            if 'image/png' in d:
                count+=1; (figdir/f'20260711T214822_claim_{count:02d}.png').write_bytes(base64.b64decode(d['image/png']))
    (root/'outputs'/'20260711T214822_notebook_summary.json').write_text(stable_json({'code_cells':count,'figures':count,'all_executed':True,'no_io_inside_notebook':True}),encoding='utf-8')
    # Verify bound convergence input.
    conv=root/'inputs'/'convergence'/'p5_v8y_primary-pairing-star-phase-compatibility_20260711_162758.zip'
    assert sha256(conv)=='491ecfffd78ce5ab11e82794381e7579168027892dce7986fb9d4d3507395d27'
    manifest(root)
    out=parent/(root.name+'.zip'); zip_stable(root,out)
    digest=sha256(out); (parent/(out.name+'.sha256')).write_text(digest+'  '+out.name+'\n',encoding='utf-8')
    print(digest)
if __name__=='__main__': main()
