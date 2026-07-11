#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, subprocess, tempfile, zipfile

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('zip_path',type=Path); a=ap.parse_args()
    with tempfile.TemporaryDirectory(prefix='p5v8w_audit_') as td:
        t=Path(td)
        with zipfile.ZipFile(a.zip_path) as zf: zf.extractall(t)
        roots=[p for p in t.iterdir() if p.is_dir()]
        if len(roots)!=1: raise SystemExit('expected one root')
        r=roots[0]; env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
        v=subprocess.run(['python3',str(r/'scripts/20260711T141656_verify.py'),str(r)],capture_output=True,text=True,env=env)
        data=json.loads(v.stdout)
        caches=[p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and ('.pytest_cache' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc')]
        source=(r/'inputs/20260711T141656_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md').read_text()
        result={
          'zip_sha256':sha(a.zip_path),
          'verifier_exit_code':v.returncode,
          'verifier_passed_count':data.get('passed_count'),
          'verifier_failed_count':data.get('failed_count'),
          'cache_created_after_verify':caches,
          'primary_source_contains_two_sided_orthogonality':'two-sided orthogonality' in source,
          'primary_source_contains_contravariant_duality':'contravariant duality' in source,
          'primary_source_phrase_new_orthogonal_axis':'new active orthogonal axis' in source,
        }
        print(json.dumps(result,indent=2))
        return 0 if v.returncode==0 else 1
if __name__=='__main__': raise SystemExit(main())
