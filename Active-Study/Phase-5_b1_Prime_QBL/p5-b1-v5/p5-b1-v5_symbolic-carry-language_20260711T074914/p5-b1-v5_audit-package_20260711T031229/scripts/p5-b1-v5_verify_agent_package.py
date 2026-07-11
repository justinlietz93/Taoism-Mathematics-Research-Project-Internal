#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, tempfile, zipfile
from pathlib import Path

EXPECTED_ZIP = "94fe453557d0185418cfcd8a67d20646e4fe4754f3a6be0466b1a75517236577"
EXPECTED_DOC = "c1e7c50beff37b7186e07f67a6c84ead07a3e5839de9652414e13cea0fca91f6"
DOC_REL = "docs/QBL_CARRY_J_DERIVATION_AND_SYMBOLIC_BOUNDARY_v3.md"

def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument('zip_path', type=Path); ap.add_argument('--json-out', type=Path)
    args=ap.parse_args(); result={}
    result['zip_sha256']=sha(args.zip_path); result['zip_hash_pass']=result['zip_sha256']==EXPECTED_ZIP
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(args.zip_path) as z: z.extractall(td)
        roots=[p for p in Path(td).iterdir() if p.is_dir()]
        if len(roots)!=1: raise RuntimeError(f'expected one root, found {roots}')
        root=roots[0]
        manifest=json.loads((root/'MANIFEST.json').read_text())
        listed={r['path']:r for r in manifest['files']}
        actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
        bad=[]
        for rel,r in listed.items():
            p=root/rel; data=p.read_bytes()
            if len(data)!=r['bytes'] or hashlib.sha256(data).hexdigest()!=r['sha256']: bad.append(rel)
        result.update(manifest_entries=len(listed), actual_nonmanifest_files=len(actual), manifest_missing=sorted(actual-set(listed)), manifest_extra=sorted(set(listed)-actual), manifest_bad=bad)
        result['manifest_pass']=not result['manifest_missing'] and not result['manifest_extra'] and not bad
        result['document_sha256']=sha(root/DOC_REL); result['document_hash_pass']=result['document_sha256']==EXPECTED_DOC
        nb=json.loads(next((root/'notebooks').glob('*_executed.ipynb')).read_text())
        cells=[c for c in nb['cells'] if c.get('cell_type')=='code']
        checks=[]
        for c in cells:
            text=''; png=0
            for o in c.get('outputs',[]):
                if o.get('output_type')=='stream':
                    t=o.get('text',''); text += ''.join(t) if isinstance(t,list) else t
                if 'image/png' in o.get('data',{}): png+=1
            checks.append({'execution_count':c.get('execution_count'),'pass':('PASS' in text and 'FAIL' not in text),'png_count':png})
        result['notebook_code_cells']=len(cells); result['notebook_checks']=checks
        result['notebook_pass']=len(cells)==13 and [x['execution_count'] for x in checks]==list(range(1,14)) and all(x['pass'] and x['png_count']==1 for x in checks)
    result['overall_pass']=all(result[k] for k in ('zip_hash_pass','manifest_pass','document_hash_pass','notebook_pass'))
    text=json.dumps(result,indent=2)+"\n"; print(text,end='')
    if args.json_out: args.json_out.write_text(text)
    if not result['overall_pass']: raise SystemExit(1)
if __name__=='__main__': main()
