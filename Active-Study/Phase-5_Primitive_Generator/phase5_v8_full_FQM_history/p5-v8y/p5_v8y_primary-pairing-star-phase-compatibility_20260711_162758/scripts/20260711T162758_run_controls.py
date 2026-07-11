from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile
STAMP='20260711T162758'

def make_manifest(root):
    entries=[]
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json':
            entries.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (root/'MANIFEST.json').write_text(json.dumps({'algorithm':'sha256','entries':entries},indent=2)+'\n')

def mutate_card(root,key,value):
    p=root/'outputs'/f'{STAMP}_result_card.json'
    data=json.loads(p.read_text())
    data[key]=value
    p.write_text(json.dumps(data,indent=2)+'\n')

def replace_primary_law(root):
    p=root/'inputs'/f'{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md'
    old='The primary pairing is generative.'
    text=p.read_text()
    assert old in text
    p.write_text(text.replace(old,'UNRELATED TEXT.',1))

def change_iota_excerpt(root):
    p=root/'inputs'/f'{STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md'
    old=r'\Omega_t^+=\iota_+^*P_t\iota_+,'
    text=p.read_text()
    assert old in text
    p.write_text(text.replace(old,'BROKEN_IOTA_EXPRESSION,',1))

CONTROLS=[
    ('replace_primary_law','SOURCE_BOUND_CLAIM_LEDGER',replace_primary_law),
    ('change_iota_excerpt','SOURCE_BOUND_CLAIM_LEDGER',change_iota_excerpt),
    ('promote_pair_bifunctor','GENERAL_PAIR_BIFUNCTOR_BOUNDARY',lambda r:mutate_card(r,'GENERAL Pair(-,-) BIFUNCTOR','DERIVED')),
    ('promote_iuv_to_hermitian_diagonal','HERMITIAN_DIAGONAL_BOUNDARY',lambda r:mutate_card(r,'HERMITIAN DIAGONAL PROMOTION OF i/(uv)','DERIVED')),
    ('assume_block_matrix_without_decomposition','FIRST_L_MATRIX_BOUNDARY',lambda r:mutate_card(r,'FIRST_L_BLOCK_MATRIX','DERIVED')),
    ('hardcode_star_as_derived','STAR_SEMANTICS_BOUNDARY',lambda r:mutate_card(r,'STAR SEMANTICS','DERIVED')),
]

def copy_function(src,dst):
    p=Path(src)
    # Immutable large provenance files are hard-linked; every mutated claim/source file is copied.
    if p.suffix.lower() in {'.zip','.png'}:
        os.link(src,dst)
        return dst
    return shutil.copy2(src,dst)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root')
    ap.add_argument('--record',action='store_true')
    args=ap.parse_args()
    root=Path(args.root).resolve()
    env=os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE']='1'
    env['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
    results=[]
    evidence={}
    for name,target_gate,mutation in CONTROLS:
        with tempfile.TemporaryDirectory(prefix=f'p5_v8y_{name}_') as td:
            copy=Path(td)/root.name
            shutil.copytree(root,copy,copy_function=copy_function,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.pytest_cache'))
            mutation(copy)
            make_manifest(copy)
            command=[sys.executable,str(copy/'scripts'/f'{STAMP}_verify.py'),str(copy),'--skip-controls','--control-mode']
            proc=subprocess.run(command,capture_output=True,text=True,env=env,timeout=30)
            try:
                report=json.loads(proc.stdout)
                failed=report.get('failed_gates',[])
            except Exception:
                report={'parse_error':proc.stdout[-1000:]}
                failed=[]
            passed=proc.returncode!=0 and target_gate in failed
            normalized_command=f"python <TEMP_PACKAGE>/scripts/{STAMP}_verify.py <TEMP_PACKAGE> --skip-controls --control-mode"
            row={
                'mutation':name,
                'command':normalized_command,
                'verifier_exit_code':proc.returncode,
                'failed_gate':target_gate,
                'evidence_path':f'outputs/control_evidence/{name}.json',
                'pass':passed,
                'observed_failed_gates':failed,
            }
            results.append(row)
            evidence[name]={'control':row,'verifier_report':report,'stderr':proc.stderr}
    summary={'pass':all(r['pass'] for r in results),'count':len(results),'results':results}
    if args.record:
        evdir=root/'outputs'/'control_evidence'
        evdir.mkdir(parents=True,exist_ok=True)
        for name,payload in evidence.items():
            (evdir/f'{name}.json').write_text(json.dumps(payload,indent=2)+'\n')
        with open(root/'outputs'/f'{STAMP}_corruption_controls.jsonl','w') as f:
            for row in results:
                f.write(json.dumps(row,sort_keys=True)+'\n')
        (root/'outputs'/f'{STAMP}_corruption_control_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return 0 if summary['pass'] else 1

if __name__=='__main__':
    raise SystemExit(main())
