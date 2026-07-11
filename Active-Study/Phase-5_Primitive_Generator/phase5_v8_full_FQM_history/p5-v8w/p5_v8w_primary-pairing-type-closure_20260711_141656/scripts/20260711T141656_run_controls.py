#!/usr/bin/env python3
from pathlib import Path
import csv,json,os,shutil,subprocess,sys,tempfile
STAMP="20260711T141656"
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]

def wjson(p,o): p.write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def wcsv(p,rows):
 fields=[]
 for r in rows:
  for k in r:
   if k not in fields: fields.append(k)
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

def mutate_claim(r,key):
 p=r/'outputs'/f'{STAMP}_claim_model.json'; d=json.load(open(p)); d['candidate_promotions'][key]=True; wjson(p,d)
def mut1(r): mutate_claim(r,'quadratic_refinement_directly_as_P_t')
def mut2(r): mutate_claim(r,'historical_H_M_plus_iJ_as_P_0')
def mut3(r):
 p=r/'outputs'/f'{STAMP}_initial_axis_object.json'; d=json.load(open(p)); d['one_dimensional_module_forced']=True; wjson(p,d)
def mut4(r):
 p=r/'outputs'/f'{STAMP}_seed_gauge_class_witness.json'; d=json.load(open(p)); d['classification']='RETAINED_GAUGE_CLASS_PROOF'; d['retained_seed_claim']=True; d['raw_presentations']=[{'name':'P1','matrix':[[1]],'rank':1},{'name':'P4','matrix':[[4]],'rank':1}]; wjson(p,d)
def mut5(r):
 p=r/'outputs'/f'{STAMP}_gate_table.csv'; rows=list(csv.DictReader(open(p))); rows[3]['cited_source_ids']=''; rows[3]['pass']='True'; wcsv(p,rows)
def mut6(r):
 p=r/'outputs'/f'{STAMP}_claim_model.json'; d=json.load(open(p)); d['lifted_state_schema']['name']='Xi_hat_t'; d['lifted_state_schema']['instantiated']=True; d['candidate_promotions']['Xi_hat_t_with_null_pairing_chart_transfer']=True; wjson(p,d)
controls=[
 ('promote_quadratic_refinement_directly_to_P','NO_DIRECT_QUADRATIC_PROMOTION',mut1),
 ('promote_historical_H_to_P0','HISTORICAL_H_NOT_SEED',mut2),
 ('axis_count_as_module_dimension','AXIS_OBJECT_BOUNDARY',mut3),
 ('gauge_equivalent_raw_seeds_as_nonuniqueness','GAUGE_WITNESS_INEQUIVALENT',mut4),
 ('hardcode_source_gate_true','SOURCE_GATE_CITATIONS',mut5),
 ('emit_Xi_hat_with_null_fields','XI_HAT_NULL_BOUNDARY',mut6),
]
rows=[]
for name,target,mut in controls:
 with tempfile.TemporaryDirectory(prefix='p5v8w_'+name+'_') as td:
  cr=Path(td)/ROOT.name; shutil.copytree(ROOT,cr,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.pytest_cache'))
  mut(cr)
  env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
  subprocess.run([sys.executable,str(cr/'scripts'/f'{STAMP}_make_manifest.py'),str(cr)],check=True,capture_output=True,text=True,env=env)
  jout=Path(td)/'verify.json'; cmd=[sys.executable,str(cr/'scripts'/f'{STAMP}_verify.py'),str(cr),'--json-out',str(jout),'--skip-pytest']
  cp=subprocess.run(cmd,capture_output=True,text=True,env=env)
  data=json.loads(jout.read_text()) if jout.exists() else {'failed':[]}
  failed=[x['gate'] for x in data.get('failed',[])]
  ev=ROOT/'controls/evidence'/f'{STAMP}_{name}.txt'; ev.parent.mkdir(parents=True,exist_ok=True)
  ev.write_text('COMMAND: '+' '.join(cmd)+'\nEXIT: '+str(cp.returncode)+'\nSTDOUT:\n'+cp.stdout+'\nSTDERR:\n'+cp.stderr)
  rows.append({'mutation':name,'command':' '.join(cmd),'verifier_exit_code':cp.returncode,'failed_gate':target,'actual_failed_gates':failed,'evidence_path':ev.relative_to(ROOT).as_posix(),'pass':cp.returncode!=0 and target in failed})
with (ROOT/'outputs'/f'{STAMP}_corruption_controls.jsonl').open('w') as f:
 for row in rows: f.write(json.dumps(row,sort_keys=True,separators=(',',':'))+'\n')
wjson(ROOT/'outputs'/f'{STAMP}_corruption_control_summary.json',{'controls':len(rows),'passed':sum(r['pass'] for r in rows),'all_pass':all(r['pass'] for r in rows)})
print(json.dumps(rows,indent=2))
raise SystemExit(0 if all(r['pass'] for r in rows) else 1)
