#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name=='MANIFEST.json': continue
    rel=p.relative_to(root).as_posix()
    if '__pycache__' in rel or rel.endswith('.pyc'): continue
    rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'MANIFEST.json').write_text(json.dumps({'schema':'path-bytes-sha256-v1','files':rows},indent=2,sort_keys=True)+'\n')
print(len(rows))
