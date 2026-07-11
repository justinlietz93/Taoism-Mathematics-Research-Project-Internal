#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, tempfile, zipfile
from pathlib import Path

def main():
 ap=argparse.ArgumentParser();ap.add_argument('archive',type=Path);a=ap.parse_args()
 with tempfile.TemporaryDirectory() as td:
  with zipfile.ZipFile(a.archive) as z:z.extractall(td)
  roots=[p for p in Path(td).iterdir() if p.is_dir()];assert len(roots)==1;root=roots[0]
  texts={str(p.relative_to(root)):p.read_text(errors='ignore') for p in root.rglob('*') if p.is_file() and p.suffix in {'.md','.py','.json','.csv','.jsonl','.lean'}}
  joined='\n'.join(texts.values())
  notebook=next(root.glob('notebooks/*_Primary_Pairing_BQL_Action_Boundary.ipynb')).read_text(errors='ignore')
  deriv=next(root.glob('scripts/*_derive_bql_action_boundary.py')).read_text(errors='ignore')
  findings={
   'state_forced_principle_present': 'STATE-FORCED DERIVATION PRINCIPLE' in joined or 'State-Forced Derivation Principle' in joined,
   'complete_coupled_state_transition_defined': bool(re.search(r'widehat.*X.*to.*widehat',joined,re.I)),
   'b_countermodel_is_label_dictionary': "models={'metadata_mutation'" in notebook,
   'q_countermodel_is_label_dictionary': "models={'slot_1'" in notebook,
   'realization_witness_is_names_only': "candidates=['abstract','duality morphism','bilinear','sesquilinear']" in notebook,
   'boundary_independence_uses_arbitrary_sequences': "class_a=['x']" in deriv and "class_b=[f'y{i%3}'" in deriv,
   'coordinate_equivalence_test_present': bool(re.search(r'(coordinate|gauge).*equiv',joined,re.I)),
  }
  findings['pass_state_forced_burden']=findings['state_forced_principle_present'] and not any(findings[k] for k in ['b_countermodel_is_label_dictionary','q_countermodel_is_label_dictionary','realization_witness_is_names_only','boundary_independence_uses_arbitrary_sequences'])
  print(json.dumps(findings,indent=2,sort_keys=True))
if __name__=='__main__':main()
