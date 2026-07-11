#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''):
            h.update(chunk)
    return h.hexdigest()

p=argparse.ArgumentParser(); p.add_argument('--package-root',type=Path,required=True); p.add_argument('--archive',type=Path,required=True); a=p.parse_args()
root=a.package_root.resolve(); manifest=json.loads((root/'MANIFEST.json').read_text())
errors=[]
for item in manifest['files']:
    path=root/item['path']
    if not path.exists() or sha256(path)!=item['sha256'] or path.stat().st_size!=item['bytes']:
        errors.append(item['path'])
sha_file=a.archive.with_suffix(a.archive.suffix+'.sha256')
reported=sha_file.read_text().split()[0] if sha_file.exists() else None
actual=sha256(a.archive)
result={'manifest_entries':len(manifest['files']),'manifest_errors':errors,'archive_sha256':actual,'reported_sha256':reported,'pass':not errors and actual==reported}
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if result['pass'] else 1)
