from __future__ import annotations
from pathlib import Path
import json,csv,hashlib,zipfile,tempfile,subprocess,sys,os,shutil,re,xml.etree.ElementTree as ET
from .research import baseline as recompute_baseline, carrier_rows as recompute_carrier_rows, parse_snapshot, source_inventory as recompute_source_inventory, baseline_reuse_inventory as recompute_baseline_reuse, successor_witness, v7q_ratios, bilinear_witness

REQUIRED_STATUS={'PRIMITIVE_FIRST_CROSSING':'PASS','FIRST_L_CARRY':'PASS','FIRST_NEXT_DOMAIN_B':'PASS','ACTIVE_AXIS_LOCAL_SHORTHAND':'PASS','SPECIFIED_PHASE5_ARTIFACT_LINEAGE':'PASS','EXTERNAL_OVERSET_SOURCE_CORPUS':'INCOMPLETE','CONCRETE_RETAINED_CARRIER':'DERIVED_AS_FINITE_AXIS_PRODUCT_CARRIER','NATIVE_SUCCESSOR_RECURRENCE':'NOT_YET_DERIVED','AMBIENT_MODULE_FUNCTOR_ROLE':'OPTIONAL_FORMAL_PRESENTATION','PRIMARY_PAIRING_RECURRENCE':'NOT_YET_DERIVED','CHART_RESTRICTIONS':'NOT_YET_DERIVED','MIXED_TRANSFER_RECURRENCE':'NOT_YET_DERIVED','FIRST_L_ORTHAD_EXTENSION':'STRUCTURAL_AXIS_BLOCK_EXTENSION_ONLY','ORTHAD_CAUSAL_PROJECTION':'NOT_RUN','GAUGE_FQM_WEIL_DESCENT':'NOT_RUN'}

def jload(p): return json.loads(Path(p).read_text())
def stamp(root):
    m=re.search(r'_(\d{8})_(\d{6})$',root.name); return m.group(1)+'T'+m.group(2)
def find_root(ex):
    ds=[p for p in ex.iterdir() if p.is_dir()]; return ds[0] if len(ds)==1 else ex

def run_pytest(root):
    with tempfile.TemporaryDirectory() as td:
        junit=Path(td)/'junit.xml'; env=os.environ.copy(); env['PYTHONDONTWRITEBYTECODE']='1'; env['PYTEST_ADDOPTS']='-p no:cacheprovider'; env['PYTHONPATH']=str(root/'src')
        p=subprocess.run([sys.executable,'-m','pytest','-q','-p','no:cacheprovider','--junitxml',str(junit),str(root/'tests')],cwd=root,env=env,text=True,capture_output=True)
        total=fail=err=skip=0
        if junit.exists():
            x=ET.parse(junit).getroot(); suites=[x] if x.tag=='testsuite' else list(x.findall('testsuite'))
            total=sum(int(s.attrib.get('tests',0)) for s in suites); fail=sum(int(s.attrib.get('failures',0)) for s in suites); err=sum(int(s.attrib.get('errors',0)) for s in suites); skip=sum(int(s.attrib.get('skipped',0)) for s in suites)
        return {'exit_code':p.returncode,'total':total,'failures':fail,'errors':err,'skipped':skip,'stdout':p.stdout[-2000:],'stderr':p.stderr[-2000:]}

def verify_root(root,control_mode=False,zip_path=None):
    root=Path(root); st=stamp(root); gates=[]
    def gate(name,ok,detail): gates.append({'gate':name,'pass':bool(ok),'detail':detail})
    required=[root/'outputs'/f'{st}_baseline_sanity.json',root/'outputs'/f'{st}_baseline_reuse_inventory.csv',root/'outputs'/f'{st}_baseline_provenance.json',root/'outputs'/f'{st}_retained_carrier_prefix_table.csv',root/'outputs'/f'{st}_native_successor_source_inventory.csv',root/'outputs'/f'{st}_native_successor_recurrence_assessment.json',root/'outputs'/f'{st}_statuses.json',root/'proofs'/f'{st}_BILINEAR_UNDERDETERMINATION_PROOF.md']
    gate('REQUIRED_FILES',all(p.exists() for p in required),[p.relative_to(root).as_posix() for p in required if not p.exists()])
    if not all(p.exists() for p in required): return {'pass':False,'gates':gates,'passed':sum(g['pass'] for g in gates),'gate_count':len(gates)}
    b=jload(root/'outputs'/f'{st}_baseline_sanity.json')
    b_recomputed=recompute_baseline(root); b_expected={k:v for k,v in b_recomputed.items() if k!='trace'}
    bp=jload(root/'outputs'/f'{st}_baseline_provenance.json')
    br=list(csv.DictReader(open(root/'outputs'/f'{st}_baseline_reuse_inventory.csv',encoding='utf-8')))
    br_expected=[{k:str(v) for k,v in row.items()} for row in recompute_baseline_reuse(root,st)]
    baseline_reuse_ok=bp.get('baseline_zip_sha256')=='947211aa29891e0f454aac78478fb4e0567301f46e3b2909edfa8ba3e206c502' and br==br_expected and bp.get('reused_evidence_paths')==[r['baseline_internal_path'] for r in br_expected]
    gate('BASELINE_REUSE_PROVENANCE',baseline_reuse_ok,{'provenance':bp,'rows':len(br),'recomputed_rows':len(br_expected)})
    gate('PRIMITIVE_BASELINE',b==b_expected and b.get('pass') and b.get('word')=='BQQBBBQBQBBQBBL' and b.get('floor_pair')==[55,89] and b.get('phase_quarters')==5,b)
    gate('POST_L_CARRY',b['after_L']['pair']==[55,89] and b['after_L']['phase_quarters']==5 and b['after_L']['A']==1 and b['after_L']['k']==0,b['after_L'])
    gate('FIRST_NEXT_DOMAIN_B',b['after_next_B']['pair']==[89,144],b['after_next_B'])
    rows=list(csv.DictReader(open(root/'outputs'/f'{st}_retained_carrier_prefix_table.csv',encoding='utf-8')))
    expected_rows=[{k:str(v) for k,v in row.items()} for row in recompute_carrier_rows(b_recomputed['trace'])]
    keys=[int(r['prefix_index']) for r in rows]
    carrier_ok=rows==expected_rows and len(rows)==17 and len(set(keys))==17 and rows[0]['axis_moduli']=='[12]' and rows[-2]['axis_moduli']=='[12,24]' and rows[-1]['axis_moduli']=='[12,24]'
    gate('CONCRETE_CARRIER_PREFIX_TABLE',carrier_ok,{'rows':len(rows),'unique':len(set(keys)),'recomputed_match':rows==expected_rows,'last':rows[-1] if rows else None})
    inv=list(csv.DictReader(open(root/'outputs'/f'{st}_native_successor_source_inventory.csv',encoding='utf-8')))
    expected_inv=[{k:str(v) for k,v in row.items()} for row in recompute_source_inventory(parse_snapshot(root/'inputs'/f'{st}_phase5-research.txt'))]
    gate('SOURCE_INVENTORY_RECOMPUTED',inv==expected_inv,{'actual_rows':len(inv),'expected_rows':len(expected_inv)})
    copied=[]
    for row in inv:
        path=root/'inputs'/'source_artifacts'/row['source_path']
        if path.exists(): copied.append({'path':row['source_path'],'expected_sha256':row['source_sha256'],'actual_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    gate('SELECTED_SOURCE_ARTIFACT_HASHES',len(copied)>=9 and all(x['expected_sha256']==x['actual_sha256'] for x in copied),copied)
    ids={r['source_key']:r['availability'] for r in inv}
    gate('NATIVE_SUCCESSOR_LINEAGE',all(k in ids for k in ['canon_native_successor','v7p_event_alphabet','v7c_successor_rerun','v7d_product_origin','v7q_scalar_ratios','v7e_shared_L','v7m_external_manifest','v7u_full_lens_compiler','v8a_confluence_cocycle']),ids)
    gate('EXTERNAL_CORPUS_INCOMPLETE',ids.get('orthad_overset_grids.zip')=='UNAVAILABLE_EXACT_ARCHIVE',ids.get('orthad_overset_grids.zip'))
    d12=jload(root/'outputs'/f'{st}_fixed_cyclic_successor_witness_D12.json'); d24=jload(root/'outputs'/f'{st}_fixed_cyclic_successor_witness_D24.json')
    gate('FIXED_SUCCESSOR_D12_RECOMPUTED',d12==successor_witness(12),d12)
    gate('FIXED_SUCCESSOR_D24_RECOMPUTED',d24==successor_witness(24),d24)
    v7q=list(csv.DictReader(open(root/'outputs'/f'{st}_v7q_local_scalar_transition_ratios.csv',encoding='utf-8')))
    v7q_expected=[{k:str(v) for k,v in row.items()} for row in v7q_ratios(b_recomputed['trace'])]
    gate('V7Q_LOCAL_DESCENDANT_RECOMPUTED',v7q==v7q_expected,{'rows':len(v7q),'match':v7q==v7q_expected})
    a=jload(root/'outputs'/f'{st}_native_successor_recurrence_assessment.json')
    gate('SUCCESSOR_HARD_STOP',a.get('status')=='NOT_YET_DERIVED' and 'Phi_L^S' in a.get('first_exact_missing_map',''),a)
    amb=jload(root/'outputs'/f'{st}_ambient_module_role.json')
    gate('AMBIENT_ROLE',amb.get('status')=='OPTIONAL_FORMAL_PRESENTATION',amb)
    br=jload(root/'outputs'/f'{st}_successor_to_pairing_bridge.json')
    gate('PAIRING_BRIDGE_OPEN',br.get('status')=='NOT_YET_DERIVED' and 'pairing' in br.get('type_problem','').lower(),br)
    v7e=jload(root/'outputs'/f'{st}_v7e_shared_L_coupling_assessment.json')
    gate('V7E_SCOPE',v7e.get('disposition')=='RECONSTRUCTION_CLUE_NOT_APPLICABLE_TO_FIRST_AXIS_BIRTH',v7e)
    wit=jload(root/'outputs'/f'{st}_bilinear_underdetermination_witness.json')
    gate('NONDEGENERATE_BILINEAR_WITNESS',wit==bilinear_witness() and wit.get('pass') and wit.get('determinants')==[1,-3] and wit.get('same_diagonal_restrictions') and wit.get('mixed_terms')==[0,2],wit)
    sts=jload(root/'outputs'/f'{st}_statuses.json')
    gate('STATUS_BOUNDARY',all(sts.get(k)==v for k,v in REQUIRED_STATUS.items()),sts)
    current='\n'.join(p.read_text(errors='replace') for p in (root/'tests').glob('*.py'))
    withdrawn=['tau_0 is the smallest gap','O is rejected because it is outside Q/B/L','ambient_retained_module_functor is the earliest']
    gate('NO_WITHDRAWN_CURRENT_TESTS',not any(x in current for x in withdrawn),[x for x in withdrawn if x in current])
    downstream=[p.relative_to(root).as_posix() for p in (root/'outputs').glob('*') if any(k in p.name.lower() for k in ['projection_rows','gauge_result','fqm_result','weil_result','omega_plus_matrix','primary_pairing_matrix'])]
    gate('DOWNSTREAM_CLOSED',not downstream,downstream)
    nb=jload(root/'notebooks'/f'{st}_native_successor_gap_executed.ipynb'); cells=[c for c in nb['cells'] if c['cell_type']=='code']
    gate('EXECUTED_NOTEBOOK_COMPLETE',bool(cells) and all(c.get('execution_count') is not None and c.get('outputs') for c in cells) and not any(o.get('output_type')=='error' for c in cells for o in c.get('outputs',[])),len(cells))
    lean=jload(root/'outputs'/f'{st}_lean_compile_status.json'); gate('LEAN_STATUS_HONEST',lean.get('status') in ['PASS','NOT_RUN_TOOL_UNAVAILABLE','FAIL'],lean)
    test=run_pytest(root); recorded=jload(root/'outputs'/f'{st}_test_results.json')
    gate('PYTEST_ACTUAL',test['exit_code']==0 and test['failures']==0 and test['errors']==0,test)
    gate('PYTEST_COUNT_MATCH',test['total']==recorded.get('total') and recorded.get('exit_code')==0,{'actual':test['total'],'recorded':recorded})
    bad=[p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc' or '.pytest_cache' in p.parts)]
    gate('CACHE_FREE',not bad,bad)
    manifest=jload(root/'MANIFEST.json') if (root/'MANIFEST.json').exists() else {'files':[]}; listed={x['path'] for x in manifest['files']}; actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    gate('MANIFEST_PATH_SET',listed==actual,{'missing':sorted(actual-listed),'extra':sorted(listed-actual)})
    by={x['path']:x for x in manifest['files']}; badhash=[]
    if listed==actual:
        for rel in actual:
            p=root/rel; x=by[rel]
            if p.stat().st_size!=x['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']: badhash.append(rel)
    gate('MANIFEST_HASHES',not badhash,badhash)
    if zip_path:
        with zipfile.ZipFile(zip_path) as z:
            pref=root.name+'/'; zfiles={n[len(pref):] for n in z.namelist() if n.startswith(pref) and not n.endswith('/')}
        gate('ARCHIVE_MANIFEST_PATH_SET',zfiles==actual|{'MANIFEST.json'},{'missing':sorted((actual|{'MANIFEST.json'})-zfiles),'extra':sorted(zfiles-(actual|{'MANIFEST.json'}))})
    if not control_mode:
        cs=root/'outputs'/f'{st}_corruption_control_summary.json'
        c=jload(cs) if cs.exists() else {}
        gate('CORRUPTION_CONTROLS_EXECUTED',c.get('all_fired') is True and c.get('executed_count',0)>0,c)
    return {'pass':all(g['pass'] for g in gates),'passed':sum(g['pass'] for g in gates),'gate_count':len(gates),'gates':gates,'pytest':test}

def verify(path,control_mode=False):
    p=Path(path).resolve()
    if p.suffix=='.zip':
        with tempfile.TemporaryDirectory() as td:
            ex=Path(td); zipfile.ZipFile(p).extractall(ex); root=find_root(ex)
            result=verify_root(root,control_mode=control_mode,zip_path=p); result['zip_sha256']=hashlib.sha256(p.read_bytes()).hexdigest(); return result
    return verify_root(p,control_mode=control_mode)
