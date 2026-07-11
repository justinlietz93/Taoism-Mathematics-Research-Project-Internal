#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, tempfile, zipfile
from pathlib import Path

EXPECTED_ACTUAL = "6c5109dac6bde39687142a05c474db16f19d698f9d6040c5a07d92a7a0784ac2"
REPORTED = "6c5109dac6bde39687142a05c474db16f19d698f9d6040c5a07d92a7a0784ac"
EXPECTED_DOC = "97a149261ad5653b097157d532e2dd0f2218985dd8c17c776c003961983884ea"

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--archive', type=Path, required=True)
    args=ap.parse_args()
    archive=args.archive.resolve()
    actual=sha256_bytes(archive.read_bytes())
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(archive) as z:
            z.extractall(td)
        roots=[p for p in Path(td).iterdir() if p.is_dir()]
        if len(roots)!=1:
            raise SystemExit('expected one package root')
        root=roots[0]
        manifest=json.loads((root/'MANIFEST.json').read_text())
        errors=[]
        listed=set()
        for item in manifest['files']:
            p=root/item['path']; listed.add(item['path'])
            if not p.is_file(): errors.append({'path':item['path'],'error':'missing'}); continue
            h=sha256_bytes(p.read_bytes())
            if h!=item['sha256'] or p.stat().st_size!=item['bytes']:
                errors.append({'path':item['path'],'error':'hash_or_size'})
        actual_files={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
        coverage=sorted(actual_files.symmetric_difference(listed))
        doc=root/'docs/QBL_DOMAIN_PROPER_EFFECTIVE_INVARIANT_v1.md'
        figures=list((root/'figures').glob('*.png'))
        result={
            'archive_sha256':actual,
            'archive_matches_actual_expected':actual==EXPECTED_ACTUAL,
            'reported_sha256':REPORTED,
            'reported_hash_length':len(REPORTED),
            'reported_hash_valid_sha256_length':len(REPORTED)==64,
            'reported_matches_archive':REPORTED==actual,
            'document_sha256':sha256_bytes(doc.read_bytes()),
            'document_hash_pass':sha256_bytes(doc.read_bytes())==EXPECTED_DOC,
            'manifest_entries':len(manifest['files']),
            'manifest_errors':errors,
            'manifest_coverage_difference':coverage,
            'figures':len(figures),
            'pass_internal':actual==EXPECTED_ACTUAL and not errors and not coverage and sha256_bytes(doc.read_bytes())==EXPECTED_DOC and len(figures)==12,
            'pass_response_integrity':REPORTED==actual and len(REPORTED)==64,
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result['pass_internal'] else 1

if __name__=='__main__':
    raise SystemExit(main())
