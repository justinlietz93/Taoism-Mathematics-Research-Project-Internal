from pathlib import Path
import argparse,csv,hashlib,json,os,re,subprocess,sys
STAMP='20260711T162758'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def norm(lines):
    lines=[x.rstrip() for x in lines]
    while lines and lines[0]=='': lines.pop(0)
    while lines and lines[-1]=='': lines.pop()
    return '\n'.join(lines)

def add(g,name,ok,detail,evidence_class='MECHANICALLY_RECOMPUTED'):
    g.append({'gate':name,'pass':bool(ok),'detail':detail,'evidence_class':evidence_class})

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root',nargs='?',default='.')
    ap.add_argument('--skip-controls',action='store_true')
    ap.add_argument('--control-mode',action='store_true')
    args=ap.parse_args()
    root=Path(args.root).resolve()
    gates=[]

    manifest=json.loads((root/'MANIFEST.json').read_text())
    listed={e['path'] for e in manifest['entries']}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
    add(gates,'MANIFEST_PATH_SET',listed==actual,{'listed':len(listed),'actual':len(actual)})
    bad=[]
    for e in manifest['entries']:
        p=root/e['path']
        if not p.exists() or p.stat().st_size!=e['bytes'] or sha(p)!=e['sha256']:
            bad.append(e['path'])
    add(gates,'MANIFEST_HASHES',not bad,bad[:10])

    rows=list(csv.DictReader(open(root/'outputs'/f'{STAMP}_source_bound_claim_ledger.csv')))
    source_fail=[]
    for row in rows:
        p=root/row['source_path']
        if not p.exists():
            source_fail.append({'claim':row['claim_key'],'reason':'source_missing'})
            continue
        lines=p.read_text().splitlines()
        start,end=int(row['start_line']),int(row['end_line'])
        if start<1 or end<start or end>len(lines):
            source_fail.append({'claim':row['claim_key'],'reason':'line_range_invalid'})
            continue
        excerpt=norm(lines[start-1:end])
        checks={
            'source_file_sha':sha(p)==row['source_file_sha256'],
            'excerpt_sha':hashlib.sha256(excerpt.encode()).hexdigest()==row['excerpt_sha256'],
            'excerpt_bytes':excerpt==row['normalized_exact_excerpt'],
            'required_formula':row['required_formula'] in excerpt,
        }
        if not all(checks.values()):
            source_fail.append({'claim':row['claim_key'],'checks':checks})
    add(gates,'SOURCE_BOUND_CLAIM_LEDGER',len(rows)>=1 and not source_fail,{'rows':len(rows),'failures':source_fail},'SOURCE_DERIVED')

    card=json.loads((root/'outputs'/f'{STAMP}_result_card.json').read_text())
    add(gates,'PAIRING_FIRST_REALIGNMENT',card.get('PAIRING_FIRST_REALIGNMENT')=='PASS',card.get('PAIRING_FIRST_REALIGNMENT'),'SOURCE_DERIVED')
    add(gates,'LOCAL_SIGNATURE_BOUNDARY',card.get('SOURCE-FORCED LOCAL SIGNATURE')=='DERIVED',card.get('SOURCE-FORCED LOCAL SIGNATURE'),'SOURCE_DERIVED')
    add(gates,'GENERAL_PAIR_BIFUNCTOR_BOUNDARY',card.get('GENERAL Pair(-,-) BIFUNCTOR')=='ADMISSIBLE_CANDIDATE',card.get('GENERAL Pair(-,-) BIFUNCTOR'),'CANDIDATE_FORMALIZATION')
    add(gates,'STAR_SEMANTICS_BOUNDARY',card.get('STAR SEMANTICS')=='NOT_YET_DERIVED',card.get('STAR SEMANTICS'),'SOURCE_DERIVED')
    add(gates,'Q_ACTION_BOUNDARY',card.get('Q QUARTER-TURN ACTION TYPE')=='NOT_YET_DERIVED',card.get('Q QUARTER-TURN ACTION TYPE'),'SOURCE_DERIVED')
    add(gates,'HERMITIAN_DIAGONAL_BOUNDARY',card.get('HERMITIAN DIAGONAL PROMOTION OF i/(uv)')=='REJECTED',card.get('HERMITIAN DIAGONAL PROMOTION OF i/(uv)'),'MECHANICALLY_RECOMPUTED')
    add(gates,'FIRST_L_MATRIX_BOUNDARY',card.get('FIRST_L_BLOCK_MATRIX')=='CANDIDATE_PRESENTATION_ONLY',card.get('FIRST_L_BLOCK_MATRIX'),'CANDIDATE_FORMALIZATION')
    add(gates,'PAIRING_TYPE_BOUNDARY',card.get('EXACT PRIMARY PAIRING TYPE')=='NOT_YET_DERIVED',card.get('EXACT PRIMARY PAIRING TYPE'),'SOURCE_DERIVED')
    add(gates,'SEED_BOUNDARY',card.get('EXACT PRIMARY PAIRING SEED')=='NOT_YET_DERIVED',card.get('EXACT PRIMARY PAIRING SEED'),'SOURCE_DERIVED')
    add(gates,'LIFTED_STATE_BOUNDARY',card.get('Xi_hat_t VALUES')=='NOT_INSTANTIATED' and card.get('TERMINAL PROJECTION')=='NOT_RUN',{'Xi_hat_t':card.get('Xi_hat_t VALUES'),'projection':card.get('TERMINAL PROJECTION')},'SOURCE_DERIVED')

    obstruction=json.loads((root/'outputs'/f'{STAMP}_hermitian_diagonal_obstruction.json').read_text())
    expected_num=2
    expected_den=obstruction['uv']
    observed_num=obstruction.get('difference_im_numerator')
    observed_den=obstruction.get('difference_im_denominator')
    add(gates,'HERMITIAN_OBSTRUCTION_RECOMPUTED',obstruction['uv']!=0 and obstruction['conjugation_fixed'] is False and observed_num==expected_num and observed_den==expected_den,{'expected_fraction':[expected_num,expected_den],'actual_fraction':[observed_num,observed_den]})

    mixed=json.loads((root/'outputs'/f'{STAMP}_first_L_mixed_relation_cases.json').read_text())
    matrix=mixed['counterexample']['matrix']
    add(gates,'ONE_SIDED_ORTHOGONALITY_COUNTEREXAMPLE',matrix[1][0]==0 and matrix[0][1]!=0,{'matrix':matrix})

    if not args.control_mode:
        import nbformat
        nb=nbformat.read(root/'notebooks'/f'{STAMP}_star_phase_compatibility_executed.ipynb',as_version=4)
        code_cells=[cell for cell in nb.cells if cell.cell_type=='code']
        claim_cells=code_cells[1:]
        complete=all(cell.execution_count is not None and cell.outputs for cell in code_cells)
        figure_cells=all(any(getattr(out,'output_type',None)=='display_data' and 'image/png' in getattr(out,'data',{}) for out in cell.outputs) for cell in claim_cells)
        add(gates,'EXECUTED_NOTEBOOK',complete and figure_cells,{'code_cells':len(code_cells),'claim_cells_with_figures':sum(any(getattr(out,'output_type',None)=='display_data' and 'image/png' in getattr(out,'data',{}) for out in cell.outputs) for cell in claim_cells)})

        env=os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE']='1'
        env['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
        proc=subprocess.run([sys.executable,'-m','pytest','-q','-p','no:cacheprovider',str(root/'tests')],capture_output=True,text=True,env=env)
        match=re.search(r'(\d+) passed',proc.stdout+proc.stderr)
        add(gates,'PYTEST',proc.returncode==0 and match is not None,{'exit':proc.returncode,'passed':int(match.group(1)) if match else 0,'tail':(proc.stdout+proc.stderr)[-500:]})

    if not args.skip_controls:
        env=os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE']='1'
        env['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
        proc=subprocess.run([sys.executable,str(root/'scripts'/f'{STAMP}_run_controls.py'),str(root)],capture_output=True,text=True,env=env,timeout=180)
        try:
            controls=json.loads(proc.stdout)
        except Exception:
            controls={'pass':False,'parse_error':proc.stdout[-500:]}
        add(gates,'REAL_SOURCE_CORRUPTION_CONTROLS',proc.returncode==0 and controls.get('pass') is True,{'exit':proc.returncode,'count':controls.get('count'),'stderr':proc.stderr[-300:]})

    result={'pass':all(g['pass'] for g in gates),'gates':gates,'failed_gates':[g['gate'] for g in gates if not g['pass']]}
    print(json.dumps(result,indent=2))
    return 0 if result['pass'] else 1

if __name__=='__main__':
    raise SystemExit(main())
