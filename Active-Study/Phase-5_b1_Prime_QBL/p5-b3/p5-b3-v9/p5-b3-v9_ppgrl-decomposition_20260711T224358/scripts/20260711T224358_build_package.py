from __future__ import annotations
import argparse,base64,hashlib,json,shutil,subprocess,sys,zipfile
from pathlib import Path
TS='20260711T224358'; PKG_NAME='p5-b3-v9_ppgrl-decomposition_20260711T224358'; FIXED_ZIP_DT=(2026, 7, 11, 22, 43, 58)

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1048576),b''): h.update(c)
    return h.hexdigest()

def stable(x): return json.dumps(x,indent=2,sort_keys=True,ensure_ascii=False)+'\n'

def manifest(root):
    files=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json': files.append({'path':p.relative_to(root).as_posix(),'size':p.stat().st_size,'sha256':sha256(p)})
    (root/'MANIFEST.json').write_text(stable({'package':root.name,'generated_at':TS,'hash_algorithm':'SHA-256','excludes':['MANIFEST.json'],'files':files}),encoding='utf-8')

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
    subprocess.run([sys.executable,str(root/'scripts'/f'{TS}_derive_ppgrl.py'),'--root',str(root)],check=True)
    import nbformat as nbf
    from nbclient import NotebookClient
    src=root/'notebooks'/f'{TS}_ppgrl_decomposition.ipynb'; nb=nbf.read(src,as_version=4)
    NotebookClient(nb,timeout=120,kernel_name='python3',allow_errors=False).execute()
    for c in nb.cells:
        c.metadata.pop('execution',None)
        if c.cell_type=='code':
            for o in c.get('outputs',[]): o.pop('metadata',None)
    exe=root/'notebooks'/f'{TS}_ppgrl_decomposition_executed.ipynb'; nbf.write(nb,exe)
    figdir=root/'figures';
    for p in figdir.glob('*.png'): p.unlink()
    count=0
    for c in nb.cells:
        if c.cell_type!='code': continue
        for o in c.get('outputs',[]): 
            d=o.get('data',{}) if isinstance(o,dict) else {}
            if 'image/png' in d:
                count+=1; (figdir/f'{TS}_claim_{count:02d}.png').write_bytes(base64.b64decode(d['image/png']))
    code_cells=sum(1 for c in nb.cells if c.cell_type=='code')
    assert count==code_cells
    (root/'outputs'/f'{TS}_notebook_summary.json').write_text(stable({'code_cells':code_cells,'figures':count,'all_executed':True,'no_io_inside_notebook':True}),encoding='utf-8')
    manifest(root)
    # Verify before archiving.
    subprocess.run([sys.executable,str(root/'scripts'/f'{TS}_verify_package.py'),'--root',str(root)],check=True)
    out=parent/(root.name+'.zip'); zip_stable(root,out)
    digest=sha256(out); (parent/(out.name+'.sha256')).write_text(digest+'  '+out.name+'\n',encoding='utf-8')
    print(digest)
if __name__=='__main__': main()
