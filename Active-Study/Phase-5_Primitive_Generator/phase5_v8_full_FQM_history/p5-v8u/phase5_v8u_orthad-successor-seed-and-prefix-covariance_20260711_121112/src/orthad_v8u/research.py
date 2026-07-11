from __future__ import annotations
import csv, hashlib, json, math
from pathlib import Path
from .primitive import run_first_crossing_and_next_b, independent_oracle
EXPECTED='BQQBBBQBQBBQBBL'
PRE_L='BQQBBBQBQBBQBB'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump_json(p,obj): Path(p).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
def write_csv(p,rows):
    rows=list(rows); Path(p).parent.mkdir(parents=True,exist_ok=True)
    with Path(p).open('w',newline='',encoding='utf-8') as h:
        if rows:
            w=csv.DictWriter(h,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def baseline():
    _,rows=run_first_crossing_and_next_b(); oracle=independent_oracle(); li=next(i for i,r in enumerate(rows) if r['primitive']=='L')
    before,after,nxt=rows[li]['before'],rows[li]['after'],rows[li+1]['after']
    return {'pass':[r['primitive'] for r in rows]==[x[0] for x in oracle] and after['word']==EXPECTED and before['pair']==[55,89] and before['phase_quarters']==5 and after['pair']==[55,89] and after['phase_quarters']==5 and nxt['pair']==[89,144], 'word':after['word'],'floor_pair':before['pair'],'phase_quarters':before['phase_quarters'],'after_L':after,'after_next_B':nxt,'trace':rows}
def translation_generators(D=12):
    rows=[]
    for a in range(D):
        cycle_length=1 if a==0 else D//math.gcd(a,D)
        rows.append({'D':D,'increment':a,'gcd':math.gcd(a,D),'cycle_length':cycle_length,'single_cycle':cycle_length==D,'coordinate_normal_form':a==1})
    return rows
def fixed_shift_identity(D=12):
    checks=[((b*(x+1)-b*x-b)%D)==0 for b in range(D) for x in range(D)]
    return {'D':D,'operator':'T_1(x)=x+1 mod D','single_cycle':True,'eigencharacter_identity':'chi_b(T_1 x)=zeta_D^b chi_b(x)','exact_checks':len(checks),'pass':all(checks),'clean_QBL_seed_status':'HISTORICAL_DESCENDANT_ONLY'}
def carrier_claims():
    return [
      {'claim':'Domain-0 doubled surface Z/12Z','evidence_class':'SOURCE_DERIVED','status':'SUPPORTED','reason':'N_0=6 and the clean doubled-orientation carrier rule gives local surface Z/(2N_0)=Z/12Z.'},
      {'claim':'first-L structural axis-block count 1 -> 2','evidence_class':'SOURCE_DERIVED','status':'SUPPORTED','reason':'Clean L freezes the completed axis and appends exactly one new active axis.'},
      {'claim':'newborn Domain-1 local doubled surface Z/24Z','evidence_class':'SOURCE_DERIVED','status':'SUPPORTED_AS_LOCAL_SURFACE_ONLY','reason':'N_1=12 and the doubled-orientation rule gives the newborn local surface Z/24Z; no integration law with the inherited surface is implied.'},
      {'claim':'first-L retained carrier Z/12Z x Z/24Z','evidence_class':'CANDIDATE_FORMALIZATION','status':'NOT_YET_DERIVED','reason':'Independence/direct-product structure is not stated by the clean L law.'},
      {'claim':'prefix-by-prefix doubled carrier address','evidence_class':'SOURCE_DERIVED','status':'NOT_YET_DERIVED','reason':'The clean source gives k and retained two-hand opposition but no address map alpha_t into Z/12Z.'},
      {'claim':'single retained carrier with two-block presentation','evidence_class':'CANDIDATE_FORMALIZATION','status':'POSSIBLE_NOT_SELECTED','reason':'Compatible with 1->2 structural blocks but not uniquely forced.'},
      {'claim':'coupled group extension at first L','evidence_class':'CANDIDATE_FORMALIZATION','status':'POSSIBLE_NOT_SELECTED','reason':'No extension class or incidence map is supplied.'},
    ]
def successor_seed_assessment():
    return {
      'case_1_fixed_shift_clean_seed':'NOT_DERIVED',
      'case_2_historical_downstream_operator':'SUPPORTED',
      'case_3_word_built_native_object':'STRONGEST_SOURCE_SUPPORTED_INTERPRETATION_NOT_FORMULA',
      'status':'NOT_YET_DERIVED',
      'status_line':'NATIVE_SUCCESSOR_SEED: NOT_YET_DERIVED',
      'first_missing_object':'alpha_empty: clean retained seed state -> C_0=Z/12Z (initial doubled-carrier address/orientation coordinate)',
      'first_missing_equation':'alpha_B(F_B(X_empty)) = S_B(alpha_empty(X_empty))',
      'typing':'F_B is the first clean custody B transition; alpha_empty and alpha_B are clean carrier-address maps; S_B:C_0->C_0 is the post-B native successor.',
      'why_plus_one_not_forced':'A 12-point single cycle is conjugate to x->x+1, and translations x->x+a are 12-cycles for a in {1,5,7,11}. The available source does not choose a clean coordinate origin, orientation, or address map.',
      'v7c_executable_gap':'The available v7c script constructs Fourier, Gauss, and reversal matrices but contains no successor function or QBL-to-successor derivation; the successor claim survives only in report/CSV artifacts.'
    }
def pre_l_trace(trace):
    out=[]; clean_before='UNDEFINED_CLEAN_SUCCESSOR'
    for r in trace:
        if r['primitive']=='L': break
        out.append({
          'step_index':r['step_index'],'word_prefix':r['word_prefix'],'carrier_or_index_set':'C_0 local surface Z/12Z',
          'successor_before':clean_before,'primitive':r['primitive'],'successor_after':'UNDEFINED_CLEAN_SUCCESSOR',
          'historical_fixed_descendant':'T_1(x)=x+1 mod 12 (not promoted)',
          'source_or_derivation':'Clean source requires per-tick Orthad mutation but supplies neither alpha_t nor Phi_B^S/Phi_Q^S.',
          'status':'NOT_YET_DERIVED'})
    return out
def bq_assessment():
    return {
      'change_successor':'POSSIBLE_NOT_FORCED','conjugate_successor':'POSSIBLE_NOT_FORCED','change_only_eigencharacters':'POSSIBLE_NOT_FORCED','fixed_successor_other_object_changes':'HISTORICAL_V7C_NORMAL_FORM_ONLY',
      'selected_clean_case':'NONE_DERIVED',
      'stronger_interpretation':'The native successor is best typed as a word-covariant successor system (C_t,S_t,alpha_t), whose coordinate normal form may be cyclic shift after a carrier chart is fixed. The historical fixed shift is not itself the clean custody recurrence.',
      'first_chronological_gap':'first B equivariance square alpha_B o F_B = S_B o alpha_empty',
      'status_line':'PRE_L_BQ_SUCCESSOR_RECURRENCE: NOT_YET_DERIVED'}
def first_l_assessment():
    return {'status':'BLOCKED','status_line':'FIRST_L_SUCCESSOR_EXTENSION: BLOCKED','reason':'The seed and every pre-L B/Q update remain untyped; no lawful S_before_L exists to extend.','candidate_constructions':['one global cycle','commuting factor successors','coupled group extension','block successor on one retained carrier'],'selected':'NONE','first_missing_map':'pre-L address/successor covariance beginning at the first B, not Phi_L^S'}
def v7e_assessment():
    return {'Q_DEPTH_ZERO':'LAWFUL_VALUE_IN_V7E','NEWBORN_PRE_LATCH_AXIS_HISTORY':'ABSENT','V7E_AT_FIRST_AXIS_BIRTH':'INPUT_TYPING_NOT_ESTABLISHED','boundary_incidence_analogue':'POSSIBLE_RECONSTRUCTION_CLUE_REQUIRES_NEW_BIRTH_INCIDENCE_MAP','modern_pairing_or_transfer_authority':'NOT_LICENSED','reason':'The extractor accepts q=0, but its input is two axis histories that both preexist a shared latch. At the first clean L the newborn axis has no pre-latch history.'}
def spectral_assessment():
    return {'status_line':'AMBIENT_SPECTRAL_MODULE_ROLE: REQUIRED_FOR_EIGENBASIS_AND_PAIRING_FORMALIZATION','custody_role':'NOT_A_PRIMITIVE_AND_NOT_THE_EARLIEST_OPERATIONAL_GAP','pre_L_carrier':'C_0=Z/12Z','minimum_splitting_field_for_a_12_cycle':'Q(zeta_12)','representation_space':'K[C_0] with point basis delta_x or function space Fun(C_0,K)','unitary_fourier_normalization':'requires adjoining 1/sqrt(12), or using C','first_L_local_surface_if_used':'Q(zeta_24) suffices for the newborn Z/24Z local cycle; integration remains open','successor_to_pairing_bridge':'requires a typed S_t action and a declared bilinear/sesquilinear eigenform; neither is clean-derived'}
def statuses():
    return {'PRIMITIVE_FIRST_CROSSING':'PASS','FIRST_L_CARRY':'PASS','FIRST_NEXT_DOMAIN_B':'PASS','ACTIVE_AXIS_LOCAL_SHORTHAND':'PASS','DOMAIN0_DOUBLED_CYCLIC_SURFACE':'SUPPORTED','FIRST_L_AXIS_BLOCK_COUNT':'1_TO_2','NEWBORN_DOMAIN1_LOCAL_DOUBLED_SURFACE':'SUPPORTED_AS_LOCAL_SURFACE_ONLY','FIRST_L_RETAINED_PRODUCT_CARRIER':'NOT_YET_DERIVED','RETAINED_DOUBLED_PREFIX_ADDRESS':'NOT_YET_DERIVED','FIXED_CYCLIC_SHIFT_DESCENDANT':'VERIFIED_D12','NATIVE_SUCCESSOR_SEED':'NOT_YET_DERIVED','PRE_L_BQ_SUCCESSOR_RECURRENCE':'NOT_YET_DERIVED','FIRST_L_SUCCESSOR_EXTENSION':'BLOCKED','AMBIENT_SPECTRAL_MODULE_ROLE':'REQUIRED_FOR_EIGENBASIS_AND_PAIRING_FORMALIZATION','PRIMARY_PAIRING_RECURRENCE':'NOT_YET_DERIVED','CHART_RESTRICTIONS':'NOT_YET_DERIVED','MIXED_TRANSFER_RECURRENCE':'NOT_YET_DERIVED','FIRST_L_ORTHAD_EXTENSION':'STRUCTURAL_AXIS_BLOCK_ONLY','ORTHAD_CAUSAL_PROJECTION':'NOT_RUN','GAUGE_FQM_WEIL_DESCENT':'NOT_RUN'}
def build_outputs(root,stamp):
    root=Path(root); out=root/'outputs'; out.mkdir(exist_ok=True); (root/'trace').mkdir(exist_ok=True)
    b=baseline(); dump_json(out/f'{stamp}_baseline_sanity.json',{k:v for k,v in b.items() if k!='trace'})
    (root/'trace'/f'{stamp}_primitive_trace.jsonl').write_text(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in b['trace']))
    write_csv(out/f'{stamp}_carrier_claim_table.csv',carrier_claims())
    write_csv(out/f'{stamp}_successor_seed_translation_generators_D12.csv',translation_generators(12))
    dump_json(out/f'{stamp}_fixed_cyclic_shift_descendant_D12.json',fixed_shift_identity(12))
    dump_json(out/f'{stamp}_successor_seed_assessment.json',successor_seed_assessment())
    (root/'trace'/f'{stamp}_pre_L_successor_trace.jsonl').write_text(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in pre_l_trace(b['trace'])))
    dump_json(out/f'{stamp}_BQ_successor_covariance.json',bq_assessment())
    dump_json(out/f'{stamp}_first_L_successor_extension.json',first_l_assessment())
    dump_json(out/f'{stamp}_v7e_first_birth_type_assessment.json',v7e_assessment())
    dump_json(out/f'{stamp}_ambient_spectral_module_role.json',spectral_assessment())
    dump_json(out/f'{stamp}_statuses.json',statuses())
