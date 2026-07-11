from __future__ import annotations
import csv, json, os, subprocess, sys, tempfile
from pathlib import Path
from .research import baseline, carrier_claims, translation_generators, fixed_shift_identity, successor_seed_assessment, pre_l_trace, bq_assessment, first_l_assessment, v7e_assessment, spectral_assessment, statuses

def jload(p): return json.loads(Path(p).read_text())
def csvload(p): return list(csv.DictReader(open(p,encoding='utf-8')))
def jsonl(p): return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
def verify_scientific(root,stamp):
    root=Path(root); out=root/'outputs'; trace=root/'trace'; gates=[]
    def gate(name,ok,klass,detail): gates.append({'gate':name,'pass':bool(ok),'evidence_class':klass,'detail':detail})
    b=jload(out/f'{stamp}_baseline_sanity.json'); rb=baseline()
    gate('PRIMITIVE_BASELINE',b=={k:v for k,v in rb.items() if k!='trace'} and b['pass'],'MECHANICALLY_RECOMPUTED',b)
    claims=csvload(out/f'{stamp}_carrier_claim_table.csv')
    expected=carrier_claims(); gate('CARRIER_CLAIM_DISPOSITIONS',claims==[{k:str(v) for k,v in r.items()} for r in expected],'SOURCE_DERIVED',claims)
    prod=next(r for r in claims if r['claim']=='first-L retained carrier Z/12Z x Z/24Z')
    gate('PRODUCT_CARRIER_REMAINS_CANDIDATE',prod['evidence_class']=='CANDIDATE_FORMALIZATION' and prod['status']=='NOT_YET_DERIVED','CANDIDATE_FORMALIZATION',prod)
    addr=next(r for r in claims if r['claim']=='prefix-by-prefix doubled carrier address')
    gate('PREFIX_ADDRESS_REMAINS_OPEN',addr['status']=='NOT_YET_DERIVED','SOURCE_DERIVED',addr)
    trans=csvload(out/f'{stamp}_successor_seed_translation_generators_D12.csv')
    recomputed=[{k:str(v) for k,v in r.items()} for r in translation_generators(12)]
    gate('D12_TRANSLATION_NONUNIQUENESS',trans==recomputed and sum(r['single_cycle']=='True' for r in trans)==4,'MECHANICALLY_RECOMPUTED',{'single_cycle_count':sum(r['single_cycle']=='True' for r in trans)})
    fixed=jload(out/f'{stamp}_fixed_cyclic_shift_descendant_D12.json')
    gate('FIXED_SHIFT_IDENTITY',fixed==fixed_shift_identity(12) and fixed['clean_QBL_seed_status']=='HISTORICAL_DESCENDANT_ONLY','MECHANICALLY_RECOMPUTED',fixed)
    seed=jload(out/f'{stamp}_successor_seed_assessment.json')
    gate('NATIVE_SUCCESSOR_SEED_HARD_STOP',seed==successor_seed_assessment() and seed['status']=='NOT_YET_DERIVED','SOURCE_DERIVED',seed)
    pre=jsonl(trace/f'{stamp}_pre_L_successor_trace.jsonl'); exp=pre_l_trace(rb['trace'])
    gate('PRE_L_PREFIX_COMPLETENESS',pre==exp and len(pre)==14 and pre[-1]['word_prefix']=='BQQBBBQBQBBQBB','MECHANICALLY_RECOMPUTED',{'rows':len(pre)})
    gate('NO_PRE_L_FALSE_DERIVATION',all(r['status']=='NOT_YET_DERIVED' and r['successor_after']=='UNDEFINED_CLEAN_SUCCESSOR' for r in pre),'SOURCE_DERIVED',{'rows':len(pre)})
    bq=jload(out/f'{stamp}_BQ_successor_covariance.json'); gate('BQ_COVARIANCE_HARD_STOP',bq==bq_assessment(),'SOURCE_DERIVED',bq)
    fl=jload(out/f'{stamp}_first_L_successor_extension.json'); gate('FIRST_L_EXTENSION_BLOCKED',fl==first_l_assessment() and fl['status']=='BLOCKED','SOURCE_DERIVED',fl)
    v7e=jload(out/f'{stamp}_v7e_first_birth_type_assessment.json'); gate('V7E_FIRST_BIRTH_TYPING',v7e==v7e_assessment() and v7e['Q_DEPTH_ZERO']=='LAWFUL_VALUE_IN_V7E','SOURCE_DERIVED',v7e)
    spec=jload(out/f'{stamp}_ambient_spectral_module_role.json'); gate('SPECTRAL_MODULE_ROLE',spec==spectral_assessment(),'SOURCE_DERIVED',spec)
    st=jload(out/f'{stamp}_statuses.json'); gate('STATUS_BOUNDARY',st==statuses(),'SOURCE_DERIVED',st)
    forbidden=[]
    for pat in ['OmegaPlus','OmegaMinus','TransferPlusToMinus','TransferMinusToPlus','projection_rows','pairing_matrix']:
        forbidden += list(root.rglob(f'*{pat}*'))
    gate('DOWNSTREAM_OUTPUTS_ABSENT',not forbidden,'MECHANICALLY_RECOMPUTED',[str(p) for p in forbidden])
    return gates

def run_pytest(root,stamp):
    root=Path(root); xml=Path(tempfile.mkdtemp(prefix='p5v8u_pytest_'))/f'{stamp}_pytest_junit.xml'
    env={**os.environ,'PYTHONPATH':str(root/'src'),'PYTHONDONTWRITEBYTECODE':'1'}
    cp=subprocess.run([sys.executable,'-m','pytest','-q','-p','no:cacheprovider','--junitxml',str(xml),str(root/'tests')],cwd=root,env=env,text=True,capture_output=True)
    return cp,xml
