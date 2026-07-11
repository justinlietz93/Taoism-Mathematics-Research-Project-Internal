from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1048576),b''): h.update(c)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--archive')
    a=ap.parse_args(); root=Path(a.root).resolve()
    m=json.loads((root/'MANIFEST.json').read_text())
    failures=[]
    for e in m['files']:
        p=root/e['path']
        if not p.exists() or p.stat().st_size!=e['size'] or sha256(p)!=e['sha256']:
            failures.append(e['path'])
    conv=root/'inputs/convergence/p5_v8y_primary-pairing-star-phase-compatibility_20260711_162758.zip'
    conv_ok=sha256(conv)=='491ecfffd78ce5ab11e82794381e7579168027892dce7986fb9d4d3507395d27'
    result={'manifest_entries':len(m['files']),'manifest_pass':not failures,'failures':failures,'convergence_hash_pass':conv_ok}
    if a.archive:
        result['archive_sha256']=sha256(Path(a.archive))
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if not failures and conv_ok else 1)
if __name__=='__main__': main()
