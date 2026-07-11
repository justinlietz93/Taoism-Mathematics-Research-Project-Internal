from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1048576),b''): h.update(c)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.')
    root=Path(ap.parse_args().root).resolve()
    m=json.loads((root/'MANIFEST.json').read_text())
    for row in m['files']:
        p=root/row['path']; assert p.is_file(),row['path']; assert p.stat().st_size==row['size']; assert sha256(p)==row['sha256']
    status=json.loads((root/'outputs'/'STATUS.json').read_text())
    assert status['EARLIEST_MISSING_DATUM']=='STATE_INDEXED_ARGUMENT_AND_PLACEMENT_REALIZATION'
    c=json.loads((root/'outputs'/'CONSTANT_MAP_SMUGGLING_CONTROL.json').read_text())
    assert c['bare_equation_vacuous'] and c['placed_sensitivity'] and not c['constant_constructor_pointwise_fidelity']
    nb=json.loads((root/'outputs'/'20260711T224358_notebook_summary.json').read_text())
    assert nb['code_cells']==nb['figures'] and nb['all_executed']
    print(json.dumps({'manifest_entries':len(m['files']),'notebook_cells':nb['code_cells'],'figures':nb['figures'],'constant_map_rejected':True,'status':'PASS'},indent=2,sort_keys=True))
if __name__=='__main__': main()
