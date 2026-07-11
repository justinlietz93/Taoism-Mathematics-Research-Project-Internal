#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, re, sys, zipfile
from pathlib import Path

EXPECTED_NAME = "p5_v8s_orthad-atlas-and-transfer-gap_20260711_085540.zip"
DECLARED_SHA = "947211aa29891e0f454aac78478fb4e0567301f46e3b2909edfa8ba3e206c502"

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def main(zp: Path) -> None:
    actual_sha=sha256(zp)
    with zipfile.ZipFile(zp) as z:
        files=[n for n in z.namelist() if not n.endswith('/')]
        root=files[0].split('/')[0]
        manifest=json.loads(z.read(root+'/MANIFEST.json'))
        listed={r['path'] for r in manifest['files']}
        rel={n[len(root)+1:] for n in files if n.startswith(root+'/')}-{'MANIFEST.json'}
        controls=list(csv.DictReader(z.read(root+'/outputs/20260711T085540_corruption_controls.csv').decode().splitlines()))
        stale=z.read(root+'/tests/test_recurrence_boundary.py').decode()
        claim_matrix=z.read(root+'/outputs/20260711T085540_source_claim_matrix.csv').decode()
        type_boundary=z.read(root+'/docs/20260711T085540_orthad_type_boundary.md').decode(errors='replace')
        proof=z.read(root+'/proofs/20260711T085540_BILINEAR_UNDERDETERMINATION_PROOF.md')
        first_l=z.read(root+'/docs/20260711T085540_first_L_block_obligations.md')
        result={
            'zip_name':zp.name,
            'declared_sha256':DECLARED_SHA,
            'actual_sha256':actual_sha,
            'hash_match':actual_sha==DECLARED_SHA,
            'archive_file_entries':len(files),
            'manifest_entries':len(listed),
            'manifest_path_match':listed==rel,
            'corruption_control_rows':len(controls),
            'response_claimed_controls':16,
            'control_count_match':len(controls)==16,
            'stale_tau_test': 'tau_0' in stale,
            'stale_old_O_rejection_test': 'old_o_event_bridge_rejected' in stale,
            'native_successor_in_claim_matrix': bool(re.search(r'native successor',claim_matrix,re.I)),
            'native_successor_in_type_boundary': bool(re.search(r'native successor',type_boundary,re.I)),
            'proof_has_backspace': b'\x08' in proof,
            'first_L_doc_has_backspace': b'\x08' in first_l,
        }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit(f'usage: {sys.argv[0]} /path/to/{EXPECTED_NAME}')
    main(Path(sys.argv[1]).resolve())
