import csv,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def norm(lines):
 lines=[x.rstrip() for x in lines]
 while lines and lines[0]=='': lines.pop(0)
 while lines and lines[-1]=='': lines.pop()
 return '\n'.join(lines)

def test_source_binding():
 rows=list(csv.DictReader(open(ROOT/'outputs'/'20260711T162758_source_bound_claim_ledger.csv')))
 assert len(rows)==12
 for r in rows:
  p=ROOT/r['source_path']; ex=norm(p.read_text().splitlines()[int(r['start_line'])-1:int(r['end_line'])])
  assert hashlib.sha256(p.read_bytes()).hexdigest()==r['source_file_sha256']
  assert hashlib.sha256(ex.encode()).hexdigest()==r['excerpt_sha256']
  assert r['required_formula'] in ex

def test_boundaries():
 c=json.loads((ROOT/'outputs'/'20260711T162758_result_card.json').read_text())
 assert c['STAR SEMANTICS']=='NOT_YET_DERIVED'
 assert c['GENERAL Pair(-,-) BIFUNCTOR']=='ADMISSIBLE_CANDIDATE'
 assert c['HERMITIAN DIAGONAL PROMOTION OF i/(uv)']=='REJECTED'
 assert c['FIRST_L_BLOCK_MATRIX']=='CANDIDATE_PRESENTATION_ONLY'
 assert c['Xi_hat_t VALUES']=='NOT_INSTANTIATED'
 assert c['TERMINAL PROJECTION']=='NOT_RUN'

def test_math_outputs():
 h=json.loads((ROOT/'outputs'/'20260711T162758_hermitian_diagonal_obstruction.json').read_text()); assert h['uv']==4895 and not h['conjugation_fixed']
 m=json.loads((ROOT/'outputs'/'20260711T162758_first_L_mixed_relation_cases.json').read_text())['counterexample']['matrix']; assert m[1][0]==0 and m[0][1]!=0
