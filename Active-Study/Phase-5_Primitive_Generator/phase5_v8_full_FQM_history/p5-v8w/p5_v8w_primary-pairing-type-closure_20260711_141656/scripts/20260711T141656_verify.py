#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,os,re,subprocess,sys
from pathlib import Path
import nbformat

STAMP='20260711T141656'

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def fail(gate,msg,failed): failed.append({'gate':gate,'detail':msg})

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('root',nargs='?',default=str(Path(__file__).resolve().parents[1])); ap.add_argument('--json-out'); ap.add_argument('--skip-pytest',action='store_true'); args=ap.parse_args()
 root=Path(args.root).resolve(); failed=[]; passed=[]
 def check(gate,cond,msg=''):
  (passed if cond else failed).append({'gate':gate,'detail':msg})
 # source matrix anchors
 sm=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_pairing_type_source_claim_matrix.csv',encoding='utf-8')))
 ids={r['claim_id'] for r in sm}
 required={'SC_PRIMARY','SC_PULLBACKS','SC_Q_QUARTER','SC_L_EXTENSION','SC_GAUGE','SC_FQM_POLARIZATION','SC_LOCAL_AXIS','SC_FIRST_L_BLOCK_TARGET','SC_HIST_HERMITIAN','SC_HIST_FQM_BILINEAR'}
 check('SOURCE_MATRIX_REQUIRED_ROWS',ids==required,f'ids={sorted(ids)}')
 anchors_ok=True
 for r in sm:
  p=root/r['exact_source_path']; ok=p.exists() and h(p)==r['source_sha256']
  if ok:
   lines=p.read_text(encoding='utf-8').splitlines(); a=int(r['line_start']); b=int(r['line_end']); snippet='\n'.join(lines[a-1:b]); ok=r['anchor_text'] in snippet
  anchors_ok &= ok
 check('SOURCE_MATRIX_ANCHORED',anchors_ok,'path/SHA/line anchors')
 # gate citations
 gates=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_gate_table.csv',encoding='utf-8')))
 cite_ok=True
 for g in gates:
  if g['evidence_class']=='SOURCE_DERIVED':
   cited=[x for x in g['cited_source_ids'].split(';') if x]
   if not cited or not all(x in ids for x in cited): cite_ok=False
 check('SOURCE_GATE_CITATIONS',cite_ok,'every SOURCE_DERIVED gate cites anchored rows')
 # claim model boundaries
 cm=json.load(open(root/'outputs'/f'{STAMP}_claim_model.json'))
 check('PAIRING_FIRST_REALIGNMENT',cm['PAIRING_FIRST_REALIGNMENT']=='PASS')
 check('MINIMAL_PAIRING_INTERFACE',cm['MINIMAL_PAIRING_INTERFACE']=='DERIVED' and cm['EXACT_PRIMARY_PAIRING_TYPE']=='NOT_YET_DERIVED')
 check('NO_DIRECT_QUADRATIC_PROMOTION',not cm['candidate_promotions']['quadratic_refinement_directly_as_P_t'])
 check('HISTORICAL_H_NOT_SEED',not cm['candidate_promotions']['historical_H_M_plus_iJ_as_P_0'])
 check('AXIS_COUNT_NOT_MODULE_DIMENSION',not cm['candidate_promotions']['axis_count_as_module_dimension'])
 check('NO_HARDCODED_SOURCE_GATE',not cm['candidate_promotions']['hard_coded_source_gate_without_citation'])
 ls=cm['lifted_state_schema']; nulls=all(ls[k] is None for k in ['pairing','Omega_plus','Omega_minus','T_plus_to_minus','T_minus_to_plus'])
 check('XI_HAT_NULL_BOUNDARY',ls['name']=='lifted_state_schema' and not ls['instantiated'] and nulls and not cm['candidate_promotions']['Xi_hat_t_with_null_pairing_chart_transfer'])
 # axis object
 axis=json.load(open(root/'outputs'/f'{STAMP}_initial_axis_object.json'))
 check('AXIS_OBJECT_BOUNDARY',axis['one_architectural_axis_before_first_L'] and not axis['one_dimensional_module_forced'] and not axis['rank_one_pairing_forced'])
 # elimination table recomputation
 rows=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_pairing_type_elimination_table.csv',encoding='utf-8')))
 def B(x): return x=='True'
 elim_ok=True
 for r in rows:
  c=r['candidate']; v=r['verdict']; extra=B(r['extra_map_required']); forced=B(r['source_forced']); pull=B(r['pullbacks']); mixed=B(r['mixed_blocks'])
  if c=='general morphism H_t -> D(H_t)': exp='DERIVED'
  elif c=='quadratic refinement': exp='RULED_OUT'
  elif extra: exp='REQUIRES_EXTRA_MAP'
  elif pull and mixed and not forced: exp='ADMISSIBLE_BUT_NOT_FORCED'
  else: exp='RULED_OUT'
  elim_ok &= v==exp
 check('PAIRING_TYPE_ELIMINATION',elim_ok,'verdicts recomputed from capability rows')
 # type closure exact fork
 tc=json.load(open(root/'outputs'/f'{STAMP}_primary_pairing_type_closure.json'))
 check('EXACT_TYPE_OPEN',tc['status']=='NOT_YET_DERIVED' and len(tc['surviving_type_fork'])==2 and tc['earliest_missing_axiom'].startswith('SCALAR_VARIANCE_AXIOM'))
 # seed witness: conditional only, and rank witness is inequivalent
 sw=json.load(open(root/'outputs'/f'{STAMP}_seed_gauge_class_witness.json'))
 ranks=[x['rank'] for x in sw['raw_presentations']]
 check('RAW_NONUNIQUENESS_WITNESS',len(set(ranks))==2)
 check('GAUGE_WITNESS_NOT_PROMOTED',sw['classification']=='CONDITIONAL_MODEL_GAUGE_CLASS_WITNESS' and sw['retained_seed_claim'] is False and not cm['candidate_promotions']['gauge_equivalent_raw_seeds_as_nonuniqueness_witness'])
 # detect a deliberately gauge-equivalent 1D bilinear witness if mutated
 if sw.get('classification')=='RETAINED_GAUGE_CLASS_PROOF':
  mats=[x['matrix'][0][0] for x in sw['raw_presentations']]
  ratio=None if mats[0]==0 else mats[1]/mats[0]
  square=False
  if isinstance(ratio,(int,float)) and ratio>=0:
   q=ratio**0.5; square=abs(q-round(q))<1e-12
  check('GAUGE_WITNESS_INEQUIVALENT',not square,f'ratio={ratio}')
 # primitive sanity
 pc=json.load(open(root/'outputs'/f'{STAMP}_primitive_sanity_check.json'))
 check('PRIMITIVE_BASELINE',pc['pass'] and pc['word']=='BQQBBBQBQBBQBBL' and pc['floor_pair']==[55,89] and pc['after_next_B']['pair']==[89,144])
 # notebooks: every code cell complete with PASS/FAIL and one figure
 nb=nbformat.read(root/'notebooks'/f'{STAMP}_pairing_type_closure_executed.ipynb',as_version=4)
 nb_ok=True; code_count=0
 for cell in nb.cells:
  if cell.cell_type!='code': continue
  code_count+=1; texts=[]; imgs=0
  for o in cell.get('outputs',[]):
   if o.output_type=='stream': texts.append(o.get('text',''))
   if o.output_type in ('display_data','execute_result') and 'image/png' in o.get('data',{}): imgs+=1
  joined=''.join(texts); nb_ok &= ('PASS' in joined or 'FAIL' in joined) and 'claim boundary:' in joined and imgs==1 and cell.get('execution_count') is not None
 check('EXECUTED_NOTEBOOK_COMPLETE',nb_ok and code_count==5,f'cells={code_count}')
 # no downstream value outputs
 forbidden=[]
 for p in root.rglob('*'):
  if p.is_file() and any(tok in p.name.lower() for tok in ['chart_matrix','transfer_matrix','projection_rows','weil_action','mhd_field']): forbidden.append(p.relative_to(root).as_posix())
 check('DOWNSTREAM_VALUES_CLOSED',not forbidden,str(forbidden))
 # baseline hashes
 prov=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_baseline_provenance.csv',encoding='utf-8')))
 prov_ok=all((root/r['embedded_path']).exists() and h(root/r['embedded_path'])==r['sha256'] for r in prov)
 check('BASELINE_PROVENANCE',prov_ok)
 # manifest integrity if present
 man=root/'MANIFEST.json'
 if man.exists():
  data=json.load(open(man)); entries={r['path']:r for r in data['files']}
  actual={p.relative_to(root).as_posix():p for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json' and '__pycache__' not in p.parts and p.suffix!='.pyc'}
  m_ok=set(entries)==set(actual) and all(entries[k]['bytes']==actual[k].stat().st_size and entries[k]['sha256']==h(actual[k]) for k in actual)
  check('MANIFEST_INTEGRITY',m_ok,f'manifest={len(entries)} actual={len(actual)}')
  check('NO_CACHE_BYTECODE',not any('__pycache__' in p.parts or '.pytest_cache' in p.parts or p.suffix=='.pyc' for p in root.rglob('*') if p.is_file()))
 # pytest actual counts
 if not args.skip_pytest:
  env=os.environ.copy(); env['PYTHONPATH']=str(root/'src'); env['PYTHONDONTWRITEBYTECODE']='1'
  cp=subprocess.run([sys.executable,'-m','pytest','-q',str(root/'tests')],capture_output=True,text=True,env=env)
  m=re.search(r'(\d+) passed',cp.stdout+cp.stderr)
  check('PYTEST',cp.returncode==0 and m is not None,f'exit={cp.returncode} output={(cp.stdout+cp.stderr).strip()}')
 out={'pass':not failed,'passed':passed,'failed':failed,'passed_count':len(passed),'failed_count':len(failed)}
 if args.json_out: Path(args.json_out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps(out,indent=2,sort_keys=True))
 return 0 if not failed else 1

if __name__=='__main__': raise SystemExit(main())
