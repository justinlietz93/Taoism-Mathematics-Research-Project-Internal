#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1<<20),b''): h.update(c)
 return h.hexdigest()
m=json.loads((root/'MANIFEST.json').read_text())
for row in m['files']:
 p=root/row['path']; assert p.exists(),row['path']; assert sha(p)==row['sha256'],row['path']
print('PASS',m['file_count'])
