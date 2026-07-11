from __future__ import annotations
import csv, hashlib, json, re, sys, zipfile
from pathlib import Path

STAMP="20260711T085540"
REQUIRED_HEADINGS=["Status","Result","Concrete boundary","What this tests","Files","Boundary of claim"]

def load_json(p): return json.loads(p.read_text())

def verify(root: Path, zip_path: Path|None=None) -> dict:
    gates=[]
    def gate(name, ok, detail): gates.append({"gate":name,"pass":bool(ok),"detail":detail})
    statuses=load_json(root/'outputs'/f'{STAMP}_statuses.json')
    sanity=load_json(root/'outputs'/f'{STAMP}_baseline_sanity.json')
    gate('baseline_sanity', sanity['pass'], sanity)
    gate('primitive_status', statuses['PRIMITIVE_FIRST_CROSSING']=='PASS', statuses['PRIMITIVE_FIRST_CROSSING'])
    lineage=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_source_lineage_inventory.csv',encoding='utf-8')))
    required_lineage={'v7p','v7q','v7m','v7u','v8a'}
    available={r['artifact'] for r in lineage if r['availability']=='AVAILABLE'}
    unavailable={r['artifact'] for r in lineage if r['availability'].startswith('UNAVAILABLE')}
    gate('full_cited_lineage', required_lineage.issubset(available) and 'orthad_overset_grids.zip' in unavailable, {'rows':len(lineage),'available':sorted(available),'unavailable':sorted(unavailable)})
    types=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_orthad_type_status.csv',encoding='utf-8')))
    expected={'H_t ambient retained module','C_t^+ chart module','C_t^- chart module','iota_t^+ embedding','iota_t^- embedding','K pairing codomain','P_t primary pairing','bilinear vs sesquilinear law','symmetry or adjoint law','chart dimensions and bases'}
    gate('typed_boundary_complete', expected.issubset({r['typed_item'] for r in types}), len(types))
    gate('atlas_open', statuses['ORTHAD_ATLAS_TYPE']=='NOT_YET_DERIVED', statuses['ORTHAD_ATLAS_TYPE'])
    scalar=load_json(root/'outputs'/f'{STAMP}_active_scalar_role.json')
    gate('scalar_role', scalar['classification']=='LOCAL_DESCENDANT_ONLY', scalar['classification'])
    overlap=load_json(root/'outputs'/f'{STAMP}_historical_overlap_record_assessment.json')
    gate('O_semantics', overlap['semantic_role']=='DERIVED_OVERLAP_UPDATE' and overlap['modern_per_tick_schedule']=='NOT_YET_DERIVED', overlap['verdict'])
    couplings=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_historical_coupling_formula_audit.csv',encoding='utf-8')))
    verdicts={r['formula']:r['verdict'] for r in couplings}
    gate('T_ab_scope', verdicts.get('T_ab=lens(b)/lens(a)')=='CONDITIONALLY_LICENSED', verdicts)
    gate('pair_c_rejected', verdicts.get('pair_c(ai,aj)')=='REJECTED_WITH_EXACT_DEFECT', verdicts)
    witness=load_json(root/'outputs'/f'{STAMP}_bilinear_underdetermination_witness.json')
    gate('bilinear_witness', witness['pass'] and witness['diagonal_restriction_residual']==0 and witness['mixed_transfer_difference']!=0, witness)
    gap=load_json(root/'outputs'/f'{STAMP}_typed_missing_bridge.json')
    gate('earliest_gap', gap['earliest_missing_object']=='ambient_retained_module_functor', gap['typed_declaration'])
    obligations=load_json(root/'outputs'/f'{STAMP}_first_L_block_obligations.json')
    gate('first_L_boundary', obligations['before_rank']==1 and obligations['after_rank']==2 and obligations['status']=='NOT_YET_DERIVED', obligations)
    forbidden=[p for p in root.rglob('*') if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc' or '.pytest_cache' in p.parts)]
    gate('cache_free', not forbidden, [p.relative_to(root).as_posix() for p in forbidden])
    downstream=[p for p in (root/'outputs').glob('*') if any(x in p.name.lower() for x in ['orthad_matrix','projection_rows','gauge_result','fqm_result','weil_result'])]
    gate('downstream_closed', not downstream, [p.name for p in downstream])
    results=(root/'docs'/f'{STAMP}_RESULTS.md').read_text()
    positions=[]
    for h in REQUIRED_HEADINGS:
        m=re.search(rf'^## {re.escape(h)}$',results,re.M)
        positions.append(m.start() if m else -1)
    gate('results_headings', all(x>=0 for x in positions) and positions==sorted(positions), positions)
    nb=load_json(root/'notebooks'/f'{STAMP}_orthad_atlas_gap_executed.ipynb')
    code=[c for c in nb['cells'] if c['cell_type']=='code']
    gate('executed_notebook', bool(code) and all(c.get('execution_count') is not None and c.get('outputs') for c in code) and not any(o.get('output_type')=='error' for c in code for o in c.get('outputs',[])), len(code))
    lean=load_json(root/'outputs'/f'{STAMP}_lean_compile_status.json')
    gate('lean_status_honest', lean['status'] in {'PASS','NOT_RUN_TOOL_UNAVAILABLE','FAIL'}, lean)
    novelty=load_json(root/'outputs'/f'{STAMP}_novelty_gate.json')
    gate('novelty_required_artifacts', novelty['pass'], novelty)
    manifest=load_json(root/'MANIFEST.json')
    listed={r['path'] for r in manifest['files']}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    gate('manifest_path_set', listed==actual, {'missing':sorted(actual-listed),'extra':sorted(listed-actual)})
    hash_bad=[]
    by={r['path']:r for r in manifest['files']}
    for rel in actual:
        p=root/rel; r=by[rel]
        if p.stat().st_size!=r['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:
            hash_bad.append(rel)
    gate('manifest_hashes', not hash_bad, hash_bad)
    if zip_path is not None:
        with zipfile.ZipFile(zip_path) as z:
            prefix=root.name+'/'
            zip_files={n[len(prefix):] for n in z.namelist() if n.startswith(prefix) and not n.endswith('/')}
        gate('zip_manifest_path_set', zip_files==actual|{'MANIFEST.json'}, {'missing':sorted((actual|{'MANIFEST.json'})-zip_files),'extra':sorted(zip_files-(actual|{'MANIFEST.json'}))})
    return {'pass':all(g['pass'] for g in gates),'gate_count':len(gates),'passed':sum(g['pass'] for g in gates),'gates':gates}

if __name__=='__main__':
    root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    zp=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else None
    result=verify(root,zp)
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['pass'] else 1)
