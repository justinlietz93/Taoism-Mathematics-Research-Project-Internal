#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,zipfile
from pathlib import Path

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):return sha_bytes(Path(p).read_bytes())

def main():
 ap=argparse.ArgumentParser();ap.add_argument('archive');a=ap.parse_args();archive=Path(a.archive)
 with zipfile.ZipFile(archive) as z:
  names=z.namelist();root=names[0].split('/')[0];m=json.loads(z.read(root+'/MANIFEST.json'))
  failures=[]
  for row in m['files']:
   name=root+'/'+row['path'];data=z.read(name)
   if sha_bytes(data)!=row['sha256'] or len(data)!=row['size']:failures.append(row['path'])
  if failures:raise SystemExit('manifest failures: '+repr(failures))
 print(json.dumps({'archive_sha256':sha(archive),'manifest_entries':len(m['files']),'PASS':True},indent=2))
if __name__=='__main__':main()
