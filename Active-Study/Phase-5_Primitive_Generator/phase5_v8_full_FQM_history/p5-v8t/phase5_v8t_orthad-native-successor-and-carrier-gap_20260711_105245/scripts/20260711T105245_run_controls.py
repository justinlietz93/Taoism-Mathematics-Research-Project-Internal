#!/usr/bin/env python3
from pathlib import Path
import sys, shutil, tempfile, json, subprocess, os, csv

root = Path(__file__).resolve().parents[1]
stamp = '20260711T105245'
controls = [
    ('mutate_word', 'PRIMITIVE_BASELINE'),
    ('reset_pair_at_L', 'POST_L_CARRY'),
    ('wrong_next_pair', 'FIRST_NEXT_DOMAIN_B'),
    ('duplicate_carrier_prefix', 'CONCRETE_CARRIER_PREFIX_TABLE'),
    ('corrupt_baseline_hash', 'BASELINE_REUSE_PROVENANCE'),
    ('remove_source_inventory', 'REQUIRED_FILES'),
    ('corrupt_source_hash', 'SOURCE_INVENTORY_RECOMPUTED'),
    ('corrupt_selected_source_artifact', 'SELECTED_SOURCE_ARTIFACT_HASHES'),
    ('promote_external_corpus', 'EXTERNAL_CORPUS_INCOMPLETE'),
    ('corrupt_successor_witness', 'FIXED_SUCCESSOR_D12_RECOMPUTED'),
    ('corrupt_v7q_ratio', 'V7Q_LOCAL_DESCENDANT_RECOMPUTED'),
    ('false_successor_derived', 'SUCCESSOR_HARD_STOP'),
    ('false_ambient_role', 'AMBIENT_ROLE'),
    ('false_pairing_derived', 'PAIRING_BRIDGE_OPEN'),
    ('break_bilinear_witness', 'NONDEGENERATE_BILINEAR_WITNESS'),
    ('promote_v7e', 'V7E_SCOPE'),
    ('corrupt_status', 'STATUS_BOUNDARY'),
    ('corrupt_test_count', 'PYTEST_COUNT_MATCH'),
    ('inject_withdrawn_test', 'NO_WITHDRAWN_CURRENT_TESTS'),
    ('emit_projection', 'DOWNSTREAM_CLOSED'),
    ('unexecute_notebook', 'EXECUTED_NOTEBOOK_COMPLETE'),
]


def detach(path: Path) -> None:
    if path.exists():
        data = path.read_bytes()
        path.unlink()
        path.write_bytes(data)


def rewrite_csv(path: Path, mutate_rows) -> None:
    detach(path)
    rows = list(csv.DictReader(path.open(encoding='utf-8')))
    mutate_rows(rows)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def mutate(package: Path, name: str) -> None:
    out = package / 'outputs'
    if name == 'mutate_word':
        path = out / f'{stamp}_baseline_sanity.json'; detach(path)
        data = json.loads(path.read_text()); data['word'] = 'BL'; path.write_text(json.dumps(data, indent=2))
    elif name == 'reset_pair_at_L':
        path = out / f'{stamp}_baseline_sanity.json'; detach(path)
        data = json.loads(path.read_text()); data['after_L']['pair'] = [1, 1]; path.write_text(json.dumps(data, indent=2))
    elif name == 'wrong_next_pair':
        path = out / f'{stamp}_baseline_sanity.json'; detach(path)
        data = json.loads(path.read_text()); data['after_next_B']['pair'] = [1, 2]; path.write_text(json.dumps(data, indent=2))
    elif name == 'duplicate_carrier_prefix':
        path = out / f'{stamp}_retained_carrier_prefix_table.csv'; detach(path)
        lines = path.read_text().splitlines(); lines.append(lines[-1]); path.write_text('\n'.join(lines) + '\n')
    elif name == 'corrupt_baseline_hash':
        path = out / f'{stamp}_baseline_provenance.json'; detach(path)
        data = json.loads(path.read_text()); data['baseline_zip_sha256'] = '0' * 64; path.write_text(json.dumps(data, indent=2))
    elif name == 'remove_source_inventory':
        (out / f'{stamp}_native_successor_source_inventory.csv').unlink()
    elif name == 'corrupt_source_hash':
        rewrite_csv(out / f'{stamp}_native_successor_source_inventory.csv', lambda rows: rows[0].__setitem__('source_sha256', '0' * 64))
    elif name == 'corrupt_selected_source_artifact':
        path = package / 'inputs' / 'source_artifacts' / 'phase5_v7_closure_and_orientation' / 'phase5_v7q_native_transition_assignment' / 'docs' / 'phase5_v7q_protocol_definitions.md'
        detach(path); path.write_text(path.read_text() + '\nCORRUPTED_CONTROL\n')
    elif name == 'promote_external_corpus':
        def promote(rows):
            for row in rows:
                if row['source_key'] == 'orthad_overset_grids.zip':
                    row['availability'] = 'AVAILABLE'
        rewrite_csv(out / f'{stamp}_native_successor_source_inventory.csv', promote)
    elif name == 'corrupt_successor_witness':
        path = out / f'{stamp}_fixed_cyclic_successor_witness_D12.json'; detach(path)
        data = json.loads(path.read_text()); data['all_checks_pass'] = False; path.write_text(json.dumps(data, indent=2))
    elif name == 'corrupt_v7q_ratio':
        rewrite_csv(out / f'{stamp}_v7q_local_scalar_transition_ratios.csv', lambda rows: rows[0].__setitem__('ratio_phase_mod4', '3'))
    elif name == 'false_successor_derived':
        path = out / f'{stamp}_native_successor_recurrence_assessment.json'; detach(path)
        data = json.loads(path.read_text()); data['status'] = 'DERIVED'; path.write_text(json.dumps(data, indent=2))
    elif name == 'false_ambient_role':
        path = out / f'{stamp}_ambient_module_role.json'; detach(path)
        data = json.loads(path.read_text()); data['status'] = 'DERIVED'; path.write_text(json.dumps(data, indent=2))
    elif name == 'false_pairing_derived':
        path = out / f'{stamp}_successor_to_pairing_bridge.json'; detach(path)
        data = json.loads(path.read_text()); data['status'] = 'DERIVED'; path.write_text(json.dumps(data, indent=2))
    elif name == 'break_bilinear_witness':
        path = out / f'{stamp}_bilinear_underdetermination_witness.json'; detach(path)
        data = json.loads(path.read_text()); data['P2'] = data['P0']; data['mixed_terms'] = [0, 0]; data['pass'] = False; path.write_text(json.dumps(data, indent=2))
    elif name == 'promote_v7e':
        path = out / f'{stamp}_v7e_shared_L_coupling_assessment.json'; detach(path)
        data = json.loads(path.read_text()); data['disposition'] = 'MODERN_PRIMARY_TRANSFER'; path.write_text(json.dumps(data, indent=2))
    elif name == 'corrupt_status':
        path = out / f'{stamp}_statuses.json'; detach(path)
        data = json.loads(path.read_text()); data['NATIVE_SUCCESSOR_RECURRENCE'] = 'DERIVED'; path.write_text(json.dumps(data, indent=2))
    elif name == 'corrupt_test_count':
        path = out / f'{stamp}_test_results.json'; detach(path)
        data = json.loads(path.read_text()); data['total'] = 999; path.write_text(json.dumps(data, indent=2))
    elif name == 'inject_withdrawn_test':
        (package / 'tests' / 'test_withdrawn_injected.py').write_text('# tau_0 is the smallest gap\ndef test_x(): assert True\n')
    elif name == 'emit_projection':
        (out / f'{stamp}_projection_rows.csv').write_text('x\n1\n')
    elif name == 'unexecute_notebook':
        path = package / 'notebooks' / f'{stamp}_native_successor_gap_executed.ipynb'; detach(path)
        data = json.loads(path.read_text()); data['cells'][-1]['execution_count'] = None; data['cells'][-1]['outputs'] = []; path.write_text(json.dumps(data, indent=2))
    else:
        raise ValueError(name)


def refresh_manifest(package: Path) -> None:
    manifest = package / 'MANIFEST.json'
    if manifest.exists():
        manifest.unlink()
    subprocess.run([sys.executable, str(package / 'scripts' / f'{stamp}_make_manifest.py'), str(package)], check=True, timeout=60, capture_output=True, text=True)


selected = set(sys.argv[1:]) if len(sys.argv) > 1 else {name for name, _ in controls}
processed = []
for name, target in controls:
    if name not in selected:
        continue
    temp_root = Path(tempfile.mkdtemp(prefix='p5v8t-control-', dir='/mnt/data'))
    package = temp_root / root.name
    try:
        subprocess.run(['cp', '-al', str(root), str(package)], check=True, timeout=30, capture_output=True, text=True)
        mutate(package, name)
        refresh_manifest(package)
        env = os.environ.copy(); env['PYTHONDONTWRITEBYTECODE'] = '1'; env['PYTHONPATH'] = str(package / 'src')
        try:
            proc = subprocess.run([sys.executable, str(package / 'scripts' / f'{stamp}_verify.py'), str(package), '--control-mode'], cwd=package, env=env, text=True, capture_output=True, timeout=120)
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            proc = type('P', (), {'returncode': 124, 'stdout': exc.stdout or '', 'stderr': exc.stderr or 'verifier timeout'})()
            timed_out = True
        try:
            result = json.loads(proc.stdout)
        except Exception:
            result = {'gates': [], 'parse_error': str(proc.stdout)[-1000:]}
        gate = next((item for item in result.get('gates', []) if item['gate'] == target), None)
        fired = bool(gate and not gate['pass'] and proc.returncode != 0 and not timed_out)
        row = {'mutation': name, 'target_gate': target, 'verifier_exit_code': proc.returncode, 'observed_failure': gate, 'fired': fired, 'timed_out': timed_out, 'stderr': str(proc.stderr)[-1000:]}
        evidence = root / 'outputs' / 'control_evidence' / f'{stamp}_{name}.json'
        evidence.write_text(json.dumps(row, indent=2) + '\n')
        processed.append(row)
    finally:
        subprocess.run(['rm', '-rf', str(temp_root)], check=False, timeout=30)

rows = []
for name, _ in controls:
    evidence = root / 'outputs' / 'control_evidence' / f'{stamp}_{name}.json'
    if evidence.exists():
        row = json.loads(evidence.read_text()); row['evidence_path'] = evidence.relative_to(root).as_posix(); rows.append(row)
(root / 'outputs' / f'{stamp}_corruption_controls.jsonl').write_text(''.join(json.dumps(row, sort_keys=True) + '\n' for row in rows))
summary = {'expected_count': len(controls), 'executed_count': len(rows), 'fired_count': sum(row['fired'] for row in rows), 'all_fired': len(rows) == len(controls) and all(row['fired'] for row in rows)}
(root / 'outputs' / f'{stamp}_corruption_control_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
raise SystemExit(0 if processed and all(row['fired'] for row in processed) else 1)
