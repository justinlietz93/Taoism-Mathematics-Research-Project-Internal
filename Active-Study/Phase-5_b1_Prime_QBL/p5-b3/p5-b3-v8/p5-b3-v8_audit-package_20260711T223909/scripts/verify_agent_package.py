#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

EXPECTED = "5ffc26e0d38bdf40491492aa9ee427100aad7adddcda61b10585f3aec325c1bb"

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('zip_path', type=Path)
    ap.add_argument('--output', type=Path)
    args=ap.parse_args()
    digest=sha256(args.zip_path)
    failures=[]
    checked=0
    with zipfile.ZipFile(args.zip_path) as z:
        manifest_name=next(n for n in z.namelist() if n.endswith('/MANIFEST.json'))
        root=manifest_name[:-len('MANIFEST.json')]
        manifest=json.loads(z.read(manifest_name))
        for rec in manifest['files']:
            checked += 1
            name=root+rec['path']
            data=z.read(name)
            if len(data)!=rec['size'] or hashlib.sha256(data).hexdigest()!=rec['sha256']:
                failures.append(rec['path'])
    result={
        'zip_sha256':digest,
        'zip_hash_pass':digest==EXPECTED,
        'manifest_entries':checked,
        'manifest_pass':not failures,
        'failures':failures,
    }
    text=json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text+'\n')
    if not result['zip_hash_pass'] or failures:
        raise SystemExit(1)
if __name__=='__main__': main()
