#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

TS="20260711T174605"
PRIOR="6c5109dac6bde39687142a05c474db16f19d698f9d6040c5a07d92a7a0784ac2"

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):
            h.update(chunk)
    return h.hexdigest()

p=argparse.ArgumentParser()
p.add_argument('--package-root',type=Path,required=True)
p.add_argument('--archive',type=Path,required=True)
a=p.parse_args()
root=a.package_root.resolve(); archive=a.archive.resolve()
manifest=json.loads((root/'MANIFEST.json').read_text())
errors=[]
for item in manifest['files']:
    path=root/item['path']
    if not path.exists():
        errors.append({'path':item['path'],'error':'missing'})
    elif path.stat().st_size!=item['bytes'] or sha256(path)!=item['sha256']:
        errors.append({'path':item['path'],'error':'hash_or_size'})
archive_hash=sha256(archive)
sha_file=archive.with_suffix(archive.suffix+'.sha256')
reported=sha_file.read_text().split()[0] if sha_file.exists() else None
prior_path=root/'inputs'/f'{TS}_PRIOR_p5-b3-v5_release.zip'
prior_file=root/'inputs'/f'{TS}_PRIOR_p5-b3-v5_release.zip.sha256'
prior_actual=sha256(prior_path)
prior_reported=prior_file.read_text().split()[0]
result={
    'manifest_entries':len(manifest['files']),
    'manifest_errors':errors,
    'archive_sha256':archive_hash,
    'archive_reported_sha256':reported,
    'archive_hash_match':archive_hash==reported,
    'prior_release_expected_sha256':PRIOR,
    'prior_release_actual_sha256':prior_actual,
    'prior_release_reported_sha256':prior_reported,
    'prior_release_hash_match':prior_actual==prior_reported==PRIOR and len(PRIOR)==64,
}
result['pass']=not errors and result['archive_hash_match'] and result['prior_release_hash_match']
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if result['pass'] else 1)
