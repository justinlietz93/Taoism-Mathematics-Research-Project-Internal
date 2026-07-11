#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for x in iter(lambda:f.read(1<<20),b''):h.update(x)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('archive',type=Path);ap.add_argument('--expected');a=ap.parse_args();digest=sha(a.archive)
 if a.expected and digest!=a.expected:raise SystemExit(f'hash mismatch: {digest} != {a.expected}')
 with zipfile.ZipFile(a.archive) as z:
  roots={Path(n).parts[0] for n in z.namelist() if n}
  if len(roots)!=1:raise SystemExit('archive must have one package root')
  root=next(iter(roots));m=json.loads(z.read(root+'/MANIFEST.json'))
  bad=[]
  for e in m['files']:
   data=z.read(root+'/'+e['path'])
   if sha_bytes(data)!=e['sha256'] or len(data)!=e['size']:bad.append(e['path'])
  if bad:raise SystemExit('manifest failures: '+repr(bad))
 print(json.dumps({'archive':str(a.archive),'sha256':digest,'manifest_entries':len(m['files']),'manifest_verified':True},indent=2))
if __name__=='__main__':main()
