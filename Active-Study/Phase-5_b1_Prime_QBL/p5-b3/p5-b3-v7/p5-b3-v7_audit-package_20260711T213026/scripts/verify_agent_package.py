#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path

def sha_bytes(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def sha_file(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for x in iter(lambda:f.read(1<<20),b''):h.update(x)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('archive',type=Path);a=ap.parse_args()
 with zipfile.ZipFile(a.archive) as z:
  roots={Path(n).parts[0] for n in z.namelist() if n}
  assert len(roots)==1
  root=next(iter(roots));m=json.loads(z.read(root+'/MANIFEST.json'))
  names={n for n in z.namelist() if n and not n.endswith('/')}
  expected={root+'/'+e['path'] for e in m['files']}|{root+'/MANIFEST.json'}
  bad=[]
  for e in m['files']:
   data=z.read(root+'/'+e['path'])
   if sha_bytes(data)!=e['sha256'] or len(data)!=e['size']:bad.append(e['path'])
  print(json.dumps({'sha256':sha_file(a.archive),'manifest_entries':len(m['files']),'coverage':names==expected,'bad_entries':bad,'pass':names==expected and not bad},indent=2))
if __name__=='__main__':main()
