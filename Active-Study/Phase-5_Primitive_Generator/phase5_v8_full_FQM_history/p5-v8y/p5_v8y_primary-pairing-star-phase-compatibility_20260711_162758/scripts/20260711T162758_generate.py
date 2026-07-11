from __future__ import annotations
import csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
import importlib.util
_model_path=Path(__file__).parent/f'20260711T162758_model.py'
_spec=importlib.util.spec_from_file_location('p5v8y_model',_model_path)
_model=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_model)
for _name in dir(_model):
    if not _name.startswith('_'): globals()[_name]=getattr(_model,_name)

def write_csv(path, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def main():
    ledger=build_source_ledger(ROOT)
    write_csv(ROOT/'outputs'/'20260711T162758_source_bound_claim_ledger.csv',ledger)
    (ROOT/'outputs'/'20260711T162758_source_excerpt_hashes.json').write_text(json.dumps({r['claim_key']:{'excerpt_sha256':r['excerpt_sha256'],'source_file_sha256':r['source_file_sha256'],'line_range':[r['start_line'],r['end_line']]} for r in ledger},indent=2))
    write_csv(ROOT/'outputs'/'20260711T162758_star_semantics_table.csv',star_semantics_rows())
    write_csv(ROOT/'outputs'/'20260711T162758_star_phase_candidate_compatibility.csv',candidate_rows())
    (ROOT/'outputs'/'20260711T162758_hermitian_diagonal_obstruction.json').write_text(json.dumps(hermitian_obstruction(),indent=2))
    (ROOT/'outputs'/'20260711T162758_first_L_mixed_relation_cases.json').write_text(json.dumps(first_L_relations(),indent=2))
    (ROOT/'outputs'/'20260711T162758_result_card.json').write_text(json.dumps(result_card(),indent=2))
    provenance=[]
    for p in [ROOT/'inputs'/'20260711T162758_p5_v8x_ACCEPTED_BASELINE.zip',ROOT/'inputs'/'20260711T162758_p5_v8x_AUDIT_AND_p5_v8y_TASK.zip',ROOT/'inputs'/'20260711T162758_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md',ROOT/'inputs'/'20260711T162758_v7n_finite_orthad_qgt_jm_split.md']:
        provenance.append({'path':str(p.relative_to(ROOT)),'sha256':sha256_file(p),'bytes':p.stat().st_size})
    write_csv(ROOT/'outputs'/'20260711T162758_provenance.csv',provenance)
if __name__=='__main__': main()
