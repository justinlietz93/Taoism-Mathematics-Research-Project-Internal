#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
files=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='MANIFEST.json':
        files.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'MANIFEST.json').write_text(json.dumps({'schema':'p5-experiment-manifest-v1','root':root.name,'files':files},indent=2,sort_keys=True)+'\n')
print(len(files))
