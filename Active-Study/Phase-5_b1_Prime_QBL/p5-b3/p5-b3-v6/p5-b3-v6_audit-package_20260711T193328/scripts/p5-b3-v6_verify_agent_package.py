#!/usr/bin/env python3
import argparse, hashlib, json, os, shutil, subprocess, tempfile, zipfile
from pathlib import Path

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--archive', required=True)
    a=ap.parse_args()
    archive=Path(a.archive).resolve()
    expected='9a849f82c2b96a174b104fc589ca50e1f71ab88dabd05c03f65034ca4554488a'
    out={'archive_sha256':sha(archive),'expected_sha256':expected}
    out['archive_hash_match']=out['archive_sha256']==expected
    with tempfile.TemporaryDirectory() as td:
        td=Path(td)
        with zipfile.ZipFile(archive) as z: z.extractall(td)
        roots=[p for p in td.iterdir() if p.is_dir()]
        if len(roots)!=1: raise SystemExit('expected one package root')
        root=roots[0]
        manifest=json.loads((root/'MANIFEST.json').read_text())
        errors=[]
        listed=set()
        for rec in manifest['files']:
            p=root/rec['path']; listed.add(rec['path'])
            if not p.is_file(): errors.append(f"missing:{rec['path']}"); continue
            if p.stat().st_size!=rec['bytes']: errors.append(f"bytes:{rec['path']}")
            if sha(p)!=rec['sha256']: errors.append(f"sha:{rec['path']}")
        actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
        if actual!=listed:
            errors.append('coverage mismatch')
        out['manifest_entries']=len(manifest['files'])
        out['manifest_errors']=errors
        nb=list((root/'notebooks').glob('*_executed.ipynb'))
        figs=list((root/'figures').glob('*.png'))
        if nb:
            data=json.loads(nb[0].read_text())
            code=[c for c in data['cells'] if c.get('cell_type')=='code']
            passed=0
            for c in code:
                text='\n'.join(o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o.get('text',[])) for o in c.get('outputs',[]))
                if 'PASS' in text and 'FAIL' not in text: passed+=1
            out['notebook_code_cells']=len(code); out['notebook_pass_cells']=passed
        out['figures']=len(figs)
        # Rebuild under the original root basename.
        parent=td/'rebuild'; parent.mkdir()
        work=parent/root.name
        shutil.copytree(root, work)
        rebuilt=parent/(root.name+'.zip')
        build=next((work/'scripts').glob('*_build_package.py'))
        cp=subprocess.run(['python',str(build),'--package-root',str(work),'--archive',str(rebuilt)],capture_output=True,text=True)
        out['build_returncode']=cp.returncode
        out['rebuilt_sha256']=sha(rebuilt) if rebuilt.exists() else None
        out['byte_identical_rebuild']=rebuilt.exists() and rebuilt.read_bytes()==archive.read_bytes()
    out['pass']=out['archive_hash_match'] and not out['manifest_errors'] and out.get('notebook_code_cells')==12 and out.get('notebook_pass_cells')==12 and out.get('figures')==12 and out['byte_identical_rebuild']
    print(json.dumps(out,indent=2,sort_keys=True))
    raise SystemExit(0 if out['pass'] else 1)
if __name__=='__main__': main()
