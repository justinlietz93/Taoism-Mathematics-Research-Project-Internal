#!/usr/bin/env python3
import argparse,hashlib,json,zipfile
from pathlib import Path

def sha(p):
 h=hashlib.sha256();h.update(p.read_bytes());return h.hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('archive',type=Path);a=ap.parse_args()
 with zipfile.ZipFile(a.archive) as z:
  names=z.namelist();roots={n.split('/')[0] for n in names}
  assert len(roots)==1
  root=next(iter(roots));m=json.loads(z.read(root+'/MANIFEST.json'))
  for row in m['files']:
   b=z.read(root+'/'+row['path']);assert len(b)==row['bytes'];assert hashlib.sha256(b).hexdigest()==row['sha256']
 print(json.dumps({'archive_sha256':sha(a.archive),'manifest_entries':len(m['files']),'PASS':True},indent=2))
if __name__=='__main__':main()
