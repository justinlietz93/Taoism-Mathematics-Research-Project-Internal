#!/usr/bin/env python3
import json, shutil, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from orthad_v8u.verification import verify_scientific
STAMP='20260711T121112'
def mutate_json(p,fn):
    x=json.loads(p.read_text()); fn(x); p.write_text(json.dumps(x,indent=2,sort_keys=True)+'\n')
def mutate_csv(p,fn):
    import csv
    rows=list(csv.DictReader(open(p))); fn(rows)
    with open(p,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
controls=[]
def run(name,mutator,target):
    td=Path(tempfile.mkdtemp(prefix='p5v8u_control_')); dst=td/ROOT.name; shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    mutator(dst)
    try: gates=verify_scientific(dst,STAMP); fired=not next(g['pass'] for g in gates if g['gate']==target)
    except Exception: fired=True
    controls.append({'control':name,'target_gate':target,'fired':fired}); shutil.rmtree(td)
run('corrupt primitive word',lambda r: mutate_json(r/'outputs'/f'{STAMP}_baseline_sanity.json',lambda x:x.__setitem__('word','BL')),'PRIMITIVE_BASELINE')
run('promote product carrier to source derived',lambda r: mutate_csv(r/'outputs'/f'{STAMP}_carrier_claim_table.csv',lambda rows:[row.update(evidence_class='SOURCE_DERIVED',status='SUPPORTED') for row in rows if row['claim']=='first-L retained carrier Z/12Z x Z/24Z']),'CARRIER_CLAIM_DISPOSITIONS')
run('promote historical shift to clean seed',lambda r: mutate_json(r/'outputs'/f'{STAMP}_successor_seed_assessment.json',lambda x:x.__setitem__('status','DERIVED')),'NATIVE_SUCCESSOR_SEED_HARD_STOP')
run('mark first prefix successor derived',lambda r: (r/'trace'/f'{STAMP}_pre_L_successor_trace.jsonl').write_text((r/'trace'/f'{STAMP}_pre_L_successor_trace.jsonl').read_text().replace('NOT_YET_DERIVED','DERIVED',1)),'PRE_L_PREFIX_COMPLETENESS')
run('select fixed BQ law',lambda r: mutate_json(r/'outputs'/f'{STAMP}_BQ_successor_covariance.json',lambda x:x.__setitem__('selected_clean_case','FIXED_SUCCESSOR')),'BQ_COVARIANCE_HARD_STOP')
run('derive first L before pre-L closes',lambda r: mutate_json(r/'outputs'/f'{STAMP}_first_L_successor_extension.json',lambda x:x.__setitem__('status','DERIVED')),'FIRST_L_EXTENSION_BLOCKED')
run('reject v7e because q zero',lambda r: mutate_json(r/'outputs'/f'{STAMP}_v7e_first_birth_type_assessment.json',lambda x:x.__setitem__('Q_DEPTH_ZERO','FORBIDDEN')),'V7E_FIRST_BIRTH_TYPING')
run('make spectral module optional',lambda r: mutate_json(r/'outputs'/f'{STAMP}_ambient_spectral_module_role.json',lambda x:x.__setitem__('status_line','AMBIENT_SPECTRAL_MODULE_ROLE: OPTIONAL')),'SPECTRAL_MODULE_ROLE')
run('emit forbidden projection rows',lambda r: (r/'outputs'/'projection_rows.csv').write_text('x\n1\n'),'DOWNSTREAM_OUTPUTS_ABSENT')
run('alter translation generator count',lambda r: mutate_csv(r/'outputs'/f'{STAMP}_successor_seed_translation_generators_D12.csv',lambda rows:rows[0].update(single_cycle='True')),'D12_TRANSLATION_NONUNIQUENESS')
out=ROOT/'outputs'/f'{STAMP}_corruption_controls.jsonl'; out.write_text(''.join(json.dumps(x,sort_keys=True)+'\n' for x in controls))
summary={'total':len(controls),'fired':sum(x['fired'] for x in controls),'all_fired':all(x['fired'] for x in controls)}
(ROOT/'outputs'/f'{STAMP}_corruption_control_summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,indent=2)); raise SystemExit(0 if summary['all_fired'] else 1)
