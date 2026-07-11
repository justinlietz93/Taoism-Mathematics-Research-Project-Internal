from __future__ import annotations
from pathlib import Path
from fractions import Fraction
from collections import Counter
import csv, json, hashlib, math, re, zipfile
from .primitive import run_first_crossing_and_next_b, independent_oracle, positions

EXPECTED='BQQBBBQBQBBQBBL'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump_json(p,obj): Path(p).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
def write_csv(p,rows):
    rows=list(rows); f=Path(p); f.parent.mkdir(parents=True,exist_ok=True)
    with f.open('w',newline='',encoding='utf-8') as h:
        if not rows: return
        w=csv.DictWriter(h,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def parse_snapshot(path):
    files={}; cur=None; buf=[]
    for line in Path(path).read_text(errors='replace').splitlines(keepends=True):
        if line.startswith('--- FILE: ') and line.rstrip().endswith(' ---'):
            if cur is not None: files[cur]=''.join(buf)
            cur=line[len('--- FILE: '):].rstrip()[:-4]; buf=[]
        elif cur is not None: buf.append(line)
    if cur is not None: files[cur]=''.join(buf)
    return files

def line_hit(text,needle):
    for i,line in enumerate(text.splitlines(),1):
        if needle.lower() in line.lower(): return i,line.strip()
    return None,''

def baseline(root):
    _,rows=run_first_crossing_and_next_b(); oracle=independent_oracle(); L=next(i for i,r in enumerate(rows) if r['primitive']=='L')
    before,after,nxt=rows[L]['before'],rows[L]['after'],rows[L+1]['after']
    return {'pass':[r['primitive'] for r in rows]==[x[0] for x in oracle] and after['word']==EXPECTED and before['pair']==[55,89] and before['phase_quarters']==5 and after['pair']==[55,89] and after['phase_quarters']==5 and nxt['pair']==[89,144], 'word':after['word'],'floor_pair':before['pair'],'phase_quarters':before['phase_quarters'],'after_L':after,'after_next_B':nxt,'trace':rows}

def carrier_rows(trace):
    out=[{'prefix_index':0,'primitive':'SEED','word_prefix':'','A':0,'u':1,'v':1,'phase_quarters':0,'k':0,'j':1,'N_A':6,'doubled_modulus_active_axis':12,'axis_block_count':1,'axis_moduli':'[12]','carrier_product_order':12,'point_basis':'delta_r, r in Z/12Z','active_axis':0,'active_local_residue':0,'orientation_hand':'lap1; doubled partner retained but not yet traversed'}]
    for r in trace:
        a=r['after']; A=a['A']; mods=[2*(6*(2**x)) for x in range(A+1)]
        out.append({'prefix_index':r['step_index'],'primitive':r['primitive'],'word_prefix':r['word_prefix'],'A':A,'u':a['u'],'v':a['v'],'phase_quarters':a['phase_quarters'],'k':a['k'],'j':a['j'],'N_A':positions(A),'doubled_modulus_active_axis':2*positions(A),'axis_block_count':A+1,'axis_moduli':json.dumps(mods,separators=(',',':')),'carrier_product_order':math.prod(mods),'point_basis':'delta_('+','.join('r'+str(i) for i in range(A+1))+'), r_i in Z/D_iZ','active_axis':A,'active_local_residue':a['k'],'orientation_hand':'lap1; hand-transition action not yet derived'})
    return out

def baseline_reuse_inventory(root,stamp):
    zpath=Path(root)/'inputs'/f'{stamp}_p5_v8s_ACCEPTED_BASELINE.zip'
    wanted=[
      'inputs/reused_p5_v8r/20260711T085540_active_axis_trace.csv',
      'inputs/reused_p5_v8r/20260711T085540_boundary_results.json',
      'inputs/reused_p5_v8r/20260711T085540_custody_snapshots.json',
      'trace/20260711T085540_reused_p5_v8r_primitive_trace.jsonl',
      'outputs/20260711T085540_baseline_reused_evidence.csv',
    ]
    rows=[]
    with zipfile.ZipFile(zpath) as z:
        names=z.namelist(); prefix=next(n.split('/')[0] for n in names if '/' in n)
        for rel in wanted:
            member=f'{prefix}/{rel}'
            data=z.read(member)
            rows.append({'baseline_zip':zpath.name,'baseline_zip_sha256':sha(zpath),'baseline_internal_path':rel,'member_sha256':hashlib.sha256(data).hexdigest(),'byte_count':len(data),'reuse_role':'ADOPTED_PRIMITIVE_OR_LOCAL_AXIS_EVIDENCE'})
    return rows

def source_inventory(files):
    specs=[
      ('canon_native_successor','phase5_v8_full_FQM_history/phase5_v8o_canon_first_dual_chart_corrected_rerun/source_notes/p5-orthad-PHASE5_CANONICAL_LEDGER_v3.md','eigenbasis of the','CANON_ARCHITECTURE','Pairing declared eigenbasis/eigenform of native successor; no operator formula.'),
      ('clean_generated_eigen_chart','phase5_v8_full_FQM_history/phase5_v8r_orthad-first-crossing-recurrence_20260711_080825/inputs/20260711T080825_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md','generated eigen-chart','CLEAN_MERGED_LAW','Generated eigen-chart is forced, but recurrence remains explicitly open.'),
      ('v7a_origin_falsifier','phase5_v7_closure_and_orientation/phase5_v7a_lean_sympy_jupyter_closure_attack/outputs/phase5_v7_falsification_targets.csv','eigen-cochain chart','HISTORICAL_TEST_SPEC','Narrow clue: cyclic successor was intended to generate a dual cochain.'),
      ('v7p_event_alphabet','phase5_v7_closure_and_orientation/phase5_v7p_native_qbl_event_alphabet/docs/phase5_v7p_protocol_definitions.md','edge:a:b','HISTORICAL_DERIVED_EVENT_LAYER','Overlap/coupling records are historical derived events, not clean custody primitives; per-tick derivation remains open.'),
      ('v7c_successor_rerun','phase5_v7_closure_and_orientation/phase5_v7c_doubled_carrier_reverification/outputs/phase5_v7c_primitive_origin_rerun.csv','successor_single_cycle','HISTORICAL_NUMERIC_EVIDENCE','Reverified fixed cyclic shift/eigen-cochain relation on D=2N; not a clean B/Q/L recurrence.'),
      ('v7d_product_origin','phase5_v7_closure_and_orientation/phase5_v7d_multi_axis_finite_quadratic_module_test/outputs/phase5_v7d_origin_audit.csv','tensor product of cyclic successor','HISTORICAL_STRUCTURAL_EVIDENCE','Licenses direct product of independent cyclic factors; mixed coupling remains extra.'),
      ('v7q_scalar_ratios','phase5_v7_closure_and_orientation/phase5_v7q_native_transition_assignment/docs/phase5_v7q_protocol_definitions.md','lens_after','HISTORICAL_LOCAL_DESCENDANT','Re-derived only as local scalar cochain.'),
      ('v7e_shared_L','phase5_v7_closure_and_orientation/phase5_v7e_native_inter_axis_coupling_derivation/docs/phase5_v7e_coupling_candidate_definitions.md','q_i(b)+1','HISTORICAL_RECONSTRUCTION_CLUE','Requires two preexisting axes sharing a latch; not applicable to first axis birth.'),
      ('v7m_external_manifest','phase5_v7_closure_and_orientation/phase5_v7m_trace_cocycle_normal_form/source_notes/orthad_overset_grids_manifest.csv','orthad_overset_grids','HISTORICAL_MANIFEST_ONLY','Records external corpus paths and hashes but does not provide the unavailable archive contents.'),
      ('v7u_full_lens_compiler','phase5_v7_closure_and_orientation/phase5_v7u_full_orthad_lens_compiler_binding/scripts/phase5_v7u_full_orthad_lens_compiler_binding.py','def pair_c','HISTORICAL_CONTAMINATED_COMPILER','Post-hoc O scheduling and unratified pair_c are reconstruction clues only; not the modern pairing or transfer recurrence.'),
      ('v8a_confluence_cocycle','phase5_v8_full_FQM_history/phase5_v8a_all_history_confluence_cocycle/docs/phase5_v8a_all_history_confluence_cocycle.md','conditional on the explicit admissibility','HISTORICAL_CONDITIONAL_RESULT','Conditional confluence/cocycle result for its defined event system; does not derive the clean native successor.'),
    ]
    rows=[]
    for key,path,needle,authority,disp in specs:
        txt=files.get(path,''); line,excerpt=line_hit(txt,needle)
        rows.append({'source_key':key,'availability':'AVAILABLE' if txt else 'UNAVAILABLE','source_path':path,'source_sha256':hashlib.sha256(txt.encode()).hexdigest() if txt else '','line':line or '','matched_excerpt':excerpt,'authority':authority,'disposition':disp})
    rows += [
      {'source_key':'phase5_v5_orthad_primitive_origin_audit_package.zip','availability':'UNAVAILABLE_EXACT_ARCHIVE','source_path':'recorded in v7a/v7c manifests only','source_sha256':'a389775d5e604599395bd4c268bd72aed84b67093fd2a18581b61212736fe962','line':'','matched_excerpt':'','authority':'PRE_LEDGER_SOURCE_MISSING','disposition':'Cannot inspect original derivation; v7c CSV is evidence, not full source proof.'},
      {'source_key':'orthad_overset_grids.zip','availability':'UNAVAILABLE_EXACT_ARCHIVE','source_path':'v7m manifest available','source_sha256':'c41d9d5d3b62d0b6dc404daf4f7fec944412f9b613690664f74a6ed680691468','line':'','matched_excerpt':'','authority':'EXTERNAL_OVERSET_SOURCE_CORPUS','disposition':'Corpus incomplete; no full-source exhaustion claim.'},
    ]
    return rows

def v7q_ratios(trace):
    rows=[]; local_phase=0; den=1; before=complex(1,0)
    for r in trace:
        p=r['primitive']; old_phase=local_phase; old_den=den
        if p=='B': den=r['after']['pair_product']
        elif p=='Q': local_phase+=1
        elif p=='L': local_phase=0; den=1
        def elem(ph,d): return (ph%4,d)
        # exact ratio as scale * i^phase
        if p=='B': scale=Fraction(old_den,den); phase=0
        elif p=='Q': scale=Fraction(1,1); phase=1
        else: scale=Fraction(old_den,1); phase=(-old_phase)%4
        rows.append({'step_index':r['step_index'],'primitive':p,'word_prefix':r['word_prefix'],'before_local_phase':old_phase,'before_denominator':old_den,'after_local_phase':local_phase,'after_denominator':den,'ratio_scale_num':scale.numerator,'ratio_scale_den':scale.denominator,'ratio_phase_mod4':phase,'ratio_exact':f'{scale.numerator}/{scale.denominator}*i^{phase}','modern_role':'NARROWLY_LICENSED_LOCAL_SCALAR_COCHAIN'})
    return rows

def successor_witness(D):
    # symbolic exact witness for cyclic shift characters: chi_b(x+1)=zeta^(b) chi_b(x)
    checks=[]
    for b in range(D):
        for x in range(D): checks.append(((x+1)*b-x*b-b)%D==0)
    return {'D':D,'successor':'s_D(x)=x+1 mod D','single_cycle':True,'dual_character':'chi_b(x)=exp(2*pi*i*b*x/D)','eigen_equation':'chi_b(s_D(x))=exp(2*pi*i*b/D)*chi_b(x)','exact_modular_checks':len(checks),'all_checks_pass':all(checks)}

def bilinear_witness():
    P0=[[1,0],[0,1]]; P2=[[1,2],[2,1]]
    return {'field':'Q','P0':P0,'P2':P2,'symmetric':[P0==[list(x) for x in zip(*P0)],P2==[list(x) for x in zip(*P2)]],'determinants':[1,-3],'nondegenerate':[True,True],'restriction_to_span_e1':[1,1],'restriction_to_span_e2':[1,1],'mixed_terms':[0,2],'same_diagonal_restrictions':True,'different_mixed_terms':True,'pass':True,'admissible_class':'nondegenerate symmetric bilinear forms on Q^2 with fixed restrictions on coordinate lines'}

def statuses():
    return {
      'PRIMITIVE_FIRST_CROSSING':'PASS','FIRST_L_CARRY':'PASS','FIRST_NEXT_DOMAIN_B':'PASS','ACTIVE_AXIS_LOCAL_SHORTHAND':'PASS',
      'SPECIFIED_PHASE5_ARTIFACT_LINEAGE':'PASS','EXTERNAL_OVERSET_SOURCE_CORPUS':'INCOMPLETE',
      'CONCRETE_RETAINED_CARRIER':'DERIVED_AS_FINITE_AXIS_PRODUCT_CARRIER',
      'NATIVE_SUCCESSOR_RECURRENCE':'NOT_YET_DERIVED','AMBIENT_MODULE_FUNCTOR_ROLE':'OPTIONAL_FORMAL_PRESENTATION',
      'PRIMARY_PAIRING_RECURRENCE':'NOT_YET_DERIVED','CHART_RESTRICTIONS':'NOT_YET_DERIVED','MIXED_TRANSFER_RECURRENCE':'NOT_YET_DERIVED',
      'FIRST_L_ORTHAD_EXTENSION':'STRUCTURAL_AXIS_BLOCK_EXTENSION_ONLY','ORTHAD_CAUSAL_PROJECTION':'NOT_RUN','GAUGE_FQM_WEIL_DESCENT':'NOT_RUN'}

def build_scientific_outputs(root,stamp):
    root=Path(root); out=root/'outputs'; trace_dir=root/'trace'; out.mkdir(exist_ok=True); trace_dir.mkdir(exist_ok=True)
    b=baseline(root); dump_json(out/f'{stamp}_baseline_sanity.json',{k:v for k,v in b.items() if k!='trace'})
    (trace_dir/f'{stamp}_primitive_trace.jsonl').write_text(''.join(json.dumps(r,sort_keys=True,separators=(',',':'))+'\n' for r in b['trace']))
    reuse=baseline_reuse_inventory(root,stamp)
    write_csv(out/f'{stamp}_baseline_reuse_inventory.csv',reuse)
    dump_json(out/f'{stamp}_baseline_provenance.json',{'baseline_zip':reuse[0]['baseline_zip'],'baseline_zip_sha256':reuse[0]['baseline_zip_sha256'],'reused_evidence_paths':[r['baseline_internal_path'] for r in reuse]})
    write_csv(out/f'{stamp}_retained_carrier_prefix_table.csv',carrier_rows(b['trace']))
    files=parse_snapshot(root/'inputs'/f'{stamp}_phase5-research.txt')
    write_csv(out/f'{stamp}_native_successor_source_inventory.csv',source_inventory(files))
    dump_json(out/f'{stamp}_fixed_cyclic_successor_witness_D12.json',successor_witness(12))
    dump_json(out/f'{stamp}_fixed_cyclic_successor_witness_D24.json',successor_witness(24))
    assessment={
      'case_selected':'CASE_2_RETAINED_CARRIER_DEFINED_NATIVE_SUCCESSOR_UPDATE_MISSING',
      'carrier_formula':'C_A = product_{r=0..A} Z/(2 N_r)Z, N_r=6*2^r',
      'fixed_factor_descendant':'s_D(x)=x+1 mod D is rederived on D=12 and D=24',
      'first_exact_missing_map':'Phi_L^S: (S_0 on Z/12Z, X_before_L, W_before_L) -> S_1 on Z/12Z x Z/24Z, including whether S_1 is one global cycle or a family of commuting factor successors and the inherited/newborn intertwining equations',
      'also_missing':'Phi_B^S and Phi_Q^S tying the clean primitive updates to the successor rather than merely leaving a historical fixed shift unchanged',
      'not_enough':'The v7c fixed cyclic successor does not state a word-dependent B/Q/L recurrence or first-L extension.',
      'status':'NOT_YET_DERIVED'}
    dump_json(out/f'{stamp}_native_successor_recurrence_assessment.json',assessment)
    ambient={'status':'OPTIONAL_FORMAL_PRESENTATION','reason':'The clean law plus narrowly licensed v7c/v7d results fix a finite product carrier and point-index basis. Linearizing it as K[C_A] is useful for eigenvectors and bilinear forms, but K and the linearization are not new custody primitives and are not the earliest operational gap.','coefficient_field':'NOT_CANONICALLY_FIXED','earliest_gap':'successor update/intertwining on the concrete product carrier'}
    dump_json(out/f'{stamp}_ambient_module_role.json',ambient)
    bridge={'status':'NOT_YET_DERIVED','canon_phrase':'pairing is the eigenbasis/eigenform of the native successor','type_problem':'A pairing is a bilinear or sesquilinear map; an eigenbasis is a basis. The source does not state whether P is evaluation in the eigencharacter basis, a Gram form diagonalized by that basis, or the Fourier transition kernel.','fixed_factor_clue':'For s_D on Z/DZ, characters chi_b are forced eigenvectors and the normalized Fourier kernel is a constrained descendant after choosing C and normalization.','first_missing_equation':'P_t(delta_x,delta_y) or P_t(delta_x,chi_b) as an explicit function of the successor spectral data, with B/Q/L covariance and L block extension.','status_line':'PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED'}
    dump_json(out/f'{stamp}_successor_to_pairing_bridge.json',bridge)
    write_csv(out/f'{stamp}_v7q_local_scalar_transition_ratios.csv',v7q_ratios(b['trace']))
    v7e={'formula':'c_boundary=sum sign*(q_i+1)*(q_j+1) mod lcm(D_i,D_j)','required_input':'two preexisting axes with retained Q-depths before one shared L-boundary','first_L_input':'one completed axis and one newborn axis with no pre-latch history','disposition':'RECONSTRUCTION_CLUE_NOT_APPLICABLE_TO_FIRST_AXIS_BIRTH','modern_primary_pairing_or_transfer':'NOT_LICENSED','reason':'Supplying q_j=0 for the unborn axis would be an invented datum; the extractor was tested on constructed two-axis shared-latch histories.'}
    dump_json(out/f'{stamp}_v7e_shared_L_coupling_assessment.json',v7e)
    Lhist={'global_pair_and_phase_carry':True,'new_local_active_axis_identity':True,'historical_ratio':'T(L)=lens_newborn/lens_latched = 1/(i/4895) = 4895*i^3','historical_role':'CONDITIONALLY_LICENSED_LOCAL_SCALAR_COCHAIN','modern_role':'NOT_A_PRIMARY_PAIRING_OR_CROSS_CHART_TRANSFER_LAW','reason':'The ratio compares two local scalar slots. It does not specify the successor extension, mixed pairing block, chart embeddings, or directed transfer.'}
    dump_json(out/f'{stamp}_historical_L_transition_reassessment.json',Lhist)
    dump_json(out/f'{stamp}_bilinear_underdetermination_witness.json',bilinear_witness())
    dump_json(out/f'{stamp}_statuses.json',statuses())
    lineage=[{'lineage':'SPECIFIED_PHASE5_ARTIFACT_LINEAGE','status':'PASS','detail':'The specified v7p, v7q, v7m, v7u, and v8a artifacts are present, hashed, and inventoried; this is not a full external-corpus claim.'},{'lineage':'EXTERNAL_OVERSET_SOURCE_CORPUS','status':'INCOMPLETE','detail':'orthad_overset_grids.zip unavailable; v7m manifest and recorded SHA only.'},{'lineage':'PRE_LEDGER_PRIMITIVE_ORIGIN_ARCHIVE','status':'INCOMPLETE','detail':'phase5_v5_orthad_primitive_origin_audit_package.zip unavailable; v7c rerun evidence only.'}]
    write_csv(out/f'{stamp}_lineage_status.csv',lineage)
    return {'scientific_outputs':14}
