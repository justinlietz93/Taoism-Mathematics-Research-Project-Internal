#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd()
rows=[]
for path in sorted(root.rglob('*')):
    if path.is_file() and path.name!='MANIFEST.json' and '__pycache__' not in path.parts and path.suffix!='.pyc':
        rows.append({'path':path.relative_to(root).as_posix(),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(root/'MANIFEST.json').write_text(json.dumps({'schema_version':1,'files':rows},indent=2,sort_keys=True)+'\n')
print(len(rows))
