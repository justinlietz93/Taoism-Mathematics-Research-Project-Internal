#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def has(text, phrase): return phrase.lower() in text.lower()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cf000-excerpts', required=True)
    ap.add_argument('--criterion', required=True)
    a=ap.parse_args()
    cf=Path(a.cf000_excerpts).read_text()
    cr=Path(a.criterion).read_text()
    out={
      'cf000_requires_added_internal_determination': has(cf,'adds an internal determination'),
      'cf000_rejects_mere_renaming_or_reparameterization': has(cf,'renaming or reparameterization'),
      'cf000_effective_invariant_stacking_present': has(cf,'effective-invariant stacking') or has(cf,'effective invariant proper'),
      'criterion_requires_fiber_split': has(cr,'fiber split'),
      'criterion_closes_over_finite_paths_and_return_constructions': has(cr,'finite path') and has(cr,'first-return construction'),
      'audit_conclusion': {
        'fiber_split_sufficient_candidate': True,
        'fiber_split_necessity_derived_from_cf000': False,
        'complete_path_closure_safe_as_universal_emergence_test': False,
        'd1_same_layer_articulation_identity': 'NOT_YET_DERIVED',
        'higher_order_descriptive_L_D0_to_D1': 'NOT_YET_DERIVED'
      },
      'warning':'Phrase trace only; mathematical judgment is in AUDIT_RESULTS.md.'
    }
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
