#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, tempfile, zipfile
from pathlib import Path

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--archive',type=Path,required=True); a=ap.parse_args()
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(a.archive) as z: z.extractall(td)
        root=next(p for p in Path(td).iterdir() if p.is_dir())
        doc=(root/'docs/QBL_DOMAIN_PROPER_EFFECTIVE_INVARIANT_v1.md').read_text()
        lpath=next((root/'outputs').glob('*_descriptive_L_test.csv'))
        rows=list(csv.DictReader(lpath.open()))
        by={r['requirement']:r for r in rows}
        checks={
            'd1_explicitly_induced_first_return_map': 'induced first-return map' in doc or 'induced return map' in doc,
            'd1_label_derived_from_d0_history': 'c_A=\\nu(q_A)-2\\nu(q_{A-1})' in doc or 'c_A=nu(q_A)-2' in doc,
            'no_symbolwise_map_used_as_novelty_certificate': 'No symbol map' in doc or 'no symbol map' in doc,
            'd1_saturation_only_defined': 'This criterion does not assert that the current finite descriptors saturate D1' in doc,
            'csv_marks_criterion_stated_as_pass': by.get('same-layer saturation criterion independent',{}).get('verdict')=='PASS',
            'document_claims_descriptive_l_proved': 'HIGHER-ORDER DESCRIPTIVE L: PROVED' in doc,
        }
        findings=[]
        if checks['d1_explicitly_induced_first_return_map'] and checks['d1_label_derived_from_d0_history']:
            findings.append('D1 is proved as an induced return invariant derived from D0 paths and history.')
        if checks['no_symbolwise_map_used_as_novelty_certificate']:
            findings.append('Failure of a one-letter map does not exclude variable-length same-layer recoding.')
        if checks['d1_saturation_only_defined'] and checks['csv_marks_criterion_stated_as_pass']:
            findings.append('The package counts a stated saturation criterion as a passed saturation premise.')
        if checks['document_claims_descriptive_l_proved']:
            findings.append('The descriptive-L theorem exceeds the proved irreducibility and saturation bridges.')
        result={
            'checks':checks,
            'findings':findings,
            'recommended_status':{
                'D1_INDUCED_RETURN_INVARIANT':'PROVED',
                'D1_DOMAIN_PROPER_EFFECTIVE_INVARIANT':'NOT YET DERIVED',
                'HIGHER_ORDER_DESCRIPTIVE_L':'NOT YET DERIVED',
            }
        }
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
