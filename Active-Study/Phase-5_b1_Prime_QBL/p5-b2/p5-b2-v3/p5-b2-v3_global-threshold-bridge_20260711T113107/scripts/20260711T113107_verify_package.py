#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, zipfile
from pathlib import Path


def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--package-root', default='.')
    ap.add_argument('--archive')
    args=ap.parse_args()
    root=Path(args.package_root).resolve()
    man=json.loads((root/'MANIFEST.json').read_text())
    assert man['file_count']==len(man['files'])
    for row in man['files']:
        p=root/row['path']
        assert p.is_file(), row['path']
        assert p.stat().st_size==row['size'], row['path']
        assert sha(p)==row['sha256'], row['path']
    certs=list((root/'outputs').glob('*_global_theorem_certificate.json'))
    assert len(certs)==1
    cert=json.loads(certs[0].read_text())
    assert cert['status']=='PROVED'
    nb=list((root/'notebooks').glob('*_executed.ipynb'))
    assert len(nb)==1
    data=json.loads(nb[0].read_text())
    code=[c for c in data['cells'] if c['cell_type']=='code']
    assert len(code)==12
    for c in code:
        text=''.join(o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o.get('text',[])) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        assert 'PASS' in text and 'FAIL' not in text
    assert len(list((root/'figures').glob('*.png')))==12
    if args.archive:
        arc=Path(args.archive).resolve()
        assert arc.is_file()
        shafile=arc.with_suffix(arc.suffix+'.sha256')
        assert shafile.is_file()
        expected=shafile.read_text().split()[0]
        assert expected==sha(arc)
        with zipfile.ZipFile(arc) as z:
            names=z.namelist()
            assert names==sorted(names)
    print(json.dumps({'status':'PASS','manifest_entries':man['file_count'],'notebook_cells':12,'figures':12,'archive_checked':bool(args.archive)},indent=2))
if __name__=='__main__': main()
