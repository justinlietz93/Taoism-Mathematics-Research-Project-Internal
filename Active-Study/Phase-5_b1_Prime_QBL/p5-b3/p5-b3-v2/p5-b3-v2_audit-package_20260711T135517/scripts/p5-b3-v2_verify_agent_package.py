#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('archive',type=Path)
    ap.add_argument('--expected-zip-sha256',required=True)
    ap.add_argument('--expected-document-sha256',required=True)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--skip-rebuild',action='store_true')
    args=ap.parse_args()
    zpath=args.archive.resolve()
    result={'archive':str(zpath),'checks':{},'errors':[]}
    actual_zip=sha256(zpath)
    result['archive_sha256']=actual_zip
    result['checks']['archive_sha256']=actual_zip==args.expected_zip_sha256
    with tempfile.TemporaryDirectory(prefix='p5b3v2_audit_') as td:
        t=Path(td)
        with zipfile.ZipFile(zpath) as z:
            z.extractall(t)
            roots=sorted({Path(n).parts[0] for n in z.namelist() if n and not n.startswith('__MACOSX')})
        if len(roots)!=1:
            result['errors'].append(f'expected one package root, found {roots}')
            root=t
        else:
            root=t/roots[0]
        manifest_path=root/'MANIFEST.json'
        if not manifest_path.exists():
            result['errors'].append('MANIFEST.json missing')
            manifest={'files':[]}
        else:
            manifest=json.loads(manifest_path.read_text())
        entries=manifest.get('files',[])
        result['manifest_entries']=len(entries)
        manifest_errors=[]
        listed=[]
        for e in entries:
            rel=e['path']; listed.append(rel); p=root/rel
            if not p.exists(): manifest_errors.append({'path':rel,'error':'missing'}); continue
            b=p.read_bytes(); h=hashlib.sha256(b).hexdigest()
            if len(b)!=e['bytes']: manifest_errors.append({'path':rel,'error':'bytes','actual':len(b),'expected':e['bytes']})
            if h!=e['sha256']: manifest_errors.append({'path':rel,'error':'sha256','actual':h,'expected':e['sha256']})
        actual=sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json')
        unlisted=sorted(set(actual)-set(listed)); extra=sorted(set(listed)-set(actual))
        result['manifest_errors']=manifest_errors
        result['manifest_unlisted']=unlisted
        result['manifest_extra']=extra
        result['checks']['manifest']=not manifest_errors and not unlisted and not extra and len(entries)==48
        doc=root/'docs'/'QBL_HIERARCHICAL_GRAMMAR_FACTOR_SCOPE_v2.md'
        doc_hash=sha256(doc) if doc.exists() else None
        result['document_sha256']=doc_hash
        result['checks']['document_sha256']=doc_hash==args.expected_document_sha256
        srcnbs=list((root/'notebooks').glob('*Factor_Scope.ipynb'))
        exnbs=list((root/'notebooks').glob('*Factor_Scope_executed.ipynb'))
        if len(exnbs)==1:
            nb=json.loads(exnbs[0].read_text())
            code=[c for c in nb.get('cells',[]) if c.get('cell_type')=='code']
            pass_cells=0; images=0
            for c in code:
                text='\n'.join(''.join(o.get('text',[])) if isinstance(o.get('text'),list) else str(o.get('text','')) for o in c.get('outputs',[]))
                if 'PASS' in text: pass_cells+=1
                for o in c.get('outputs',[]):
                    if 'image/png' in o.get('data',{}): images+=1
            result['notebook']={'code_cells':len(code),'pass_cells':pass_cells,'inline_png_outputs':images}
            result['checks']['notebook']=len(code)==13 and pass_cells==13 and images==13
        else:
            result['checks']['notebook']=False
            result['errors'].append(f'executed notebook count={len(exnbs)}')
        figs=list((root/'figures').glob('*.png'))
        result['figures']=len(figs)
        result['checks']['figures']=len(figs)==13
        if not args.skip_rebuild and roots:
            rebuild_parent=t/'rebuild'
            rebuild_parent.mkdir()
            copied=rebuild_parent/roots[0]
            shutil.copytree(root,copied)
            rebuilt_zip=rebuild_parent/(roots[0]+'.zip')
            builders=list((copied/'scripts').glob('*_build_package.py'))
            if len(builders)!=1:
                result['checks']['rebuild']=False
                result['errors'].append('builder not uniquely found')
            else:
                proc=subprocess.run([sys.executable,str(builders[0]),'--package-root',str(copied),'--archive-out',str(rebuilt_zip)],capture_output=True,text=True,timeout=300)
                result['rebuild_stdout']=proc.stdout
                result['rebuild_stderr']=proc.stderr
                result['rebuild_returncode']=proc.returncode
                if proc.returncode==0 and rebuilt_zip.exists():
                    rebuilt_hash=sha256(rebuilt_zip)
                    result['rebuilt_archive_sha256']=rebuilt_hash
                    result['checks']['rebuild']=rebuilt_hash==actual_zip and rebuilt_zip.read_bytes()==zpath.read_bytes()
                else:
                    result['checks']['rebuild']=False
        else:
            result['checks']['rebuild']='SKIPPED'
    result['status']='PASS' if all(v is True or v=='SKIPPED' for v in result['checks'].values()) and not result['errors'] else 'FAIL'
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text,end='')
    return 0 if result['status']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
