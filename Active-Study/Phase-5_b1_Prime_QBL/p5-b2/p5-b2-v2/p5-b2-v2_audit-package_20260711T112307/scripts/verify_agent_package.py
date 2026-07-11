#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

REPORTED_PACKAGE = "a628db04ab71a59335821754fd0e93388ec783f25e9a46882d46b27a2a31c853"
REPORTED_DOCUMENT = "8657f17a96425a426f8a79a5bf4861cabd20e274c24dc83c0d207c6f8fe330ba"
DOC_REL = "docs/QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v1.md"

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('zip_path')
    ap.add_argument('--output')
    args=ap.parse_args()
    zp=Path(args.zip_path)
    actual_zip=sha_file(zp)
    with zipfile.ZipFile(zp) as zf:
        roots={name.split('/')[0] for name in zf.namelist() if '/' in name}
        if len(roots)!=1:
            raise SystemExit(f'expected one package root, got {roots}')
        root=next(iter(roots))
        manifest=json.loads(zf.read(root+'/MANIFEST.json'))
        listed=set()
        bad=[]
        for row in manifest['files']:
            rel=row['path']; listed.add(rel)
            data=zf.read(root+'/'+rel)
            size=row.get('size',row.get('bytes',row.get('size_bytes')))
            if sha_bytes(data)!=row['sha256'] or (size is not None and len(data)!=size):
                bad.append(rel)
        actual={name[len(root)+1:] for name in zf.namelist() if name.startswith(root+'/') and not name.endswith('/') and name!=root+'/MANIFEST.json'}
        doc_sha=sha_bytes(zf.read(root+'/'+DOC_REL))
        result={
            'status':'PASS' if not bad and actual==listed and doc_sha==REPORTED_DOCUMENT else 'FAIL',
            'reported_package_sha256':REPORTED_PACKAGE,
            'actual_package_sha256':actual_zip,
            'package_hash_matches_report':actual_zip==REPORTED_PACKAGE,
            'reported_document_sha256':REPORTED_DOCUMENT,
            'actual_document_sha256':doc_sha,
            'document_hash_matches_report':doc_sha==REPORTED_DOCUMENT,
            'manifest_entries':manifest['file_count'],
            'manifest_bad_entries':bad,
            'manifest_unlisted_files':sorted(actual-listed),
            'manifest_missing_files':sorted(listed-actual),
            'manifest_pass':not bad and actual==listed,
        }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output: Path(args.output).write_text(text)
    print(text,end='')

if __name__=='__main__': main()
