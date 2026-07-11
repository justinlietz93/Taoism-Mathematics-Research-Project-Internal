#!/usr/bin/env python3
import hashlib, json, tempfile, zipfile
from pathlib import Path

ZIP = Path('/mnt/data/p5_v8u_orthad-successor-seed-and-prefix-covariance_20260711_121112(2).zip')
EXPECTED_WORD = 'BQQBBBQBQBBQBBL'

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

with tempfile.TemporaryDirectory(prefix='p5_v8u_realign_') as td:
    td = Path(td)
    with zipfile.ZipFile(ZIP) as zf:
        zf.extractall(td)
    roots = [p for p in td.iterdir() if p.is_dir()]
    if len(roots) != 1:
        raise SystemExit('expected one package root')
    root = roots[0]
    statuses = json.loads(next((root/'outputs').glob('*_statuses.json')).read_text())
    trace_path = next((root/'trace').glob('*_primitive_trace.jsonl'))
    trace = [json.loads(line) for line in trace_path.read_text().splitlines() if line.strip()]
    lrow = next(row for row in trace if row['primitive'] == 'L')
    next_b = trace[trace.index(lrow)+1]
    findings = (root/'FINDINGS.md').read_text()
    results = next((root/'docs').glob('*_RESULTS.md')).read_text()
    successor_doc = next((root/'docs').glob('*_successor_seed_derivation.md')).read_text()
    report = {
        'archive_sha256': sha256(ZIP),
        'primitive_word': lrow['after']['word'],
        'primitive_word_pass': lrow['after']['word'] == EXPECTED_WORD,
        'first_L_pair': lrow['after']['pair'],
        'first_L_phase_quarters': lrow['after']['phase_quarters'],
        'first_L_k': lrow['after']['k'],
        'first_L_j': lrow['after']['j'],
        'first_next_domain_pair': next_b['after']['pair'],
        'successor_first_markers': {
            'findings_alpha_empty_open': 'alpha_empty' in findings,
            'results_first_gap_carrier_equivariance': 'first clean gap is the carrier-address/equivariance bridge' in results,
            'successor_doc_first_missing_alpha': 'The first missing object is' in successor_doc and 'alpha_empty' in successor_doc,
            'status_native_successor_seed_open': statuses.get('NATIVE_SUCCESSOR_SEED') == 'NOT_YET_DERIVED',
            'status_primary_pairing_only_broad': statuses.get('PRIMARY_PAIRING_RECURRENCE') == 'NOT_YET_DERIVED',
        },
        'pairing_first_artifacts_present': {
            'primary_pairing_type_doc': any((root/'docs').glob('*primary_pairing_type*')),
            'primary_pairing_seed_doc': any((root/'docs').glob('*primary_pairing_seed*')),
            'B_pairing_mutation_doc': any((root/'docs').glob('*B_pairing_mutation*')),
            'Q_pairing_mutation_doc': any((root/'docs').glob('*Q_pairing_mutation*')),
            'L_pairing_extension_doc': any((root/'docs').glob('*L_pairing_extension*')),
            'full_prefix_causal_trace': any((root/'trace').glob('*full_prefix_causal_trace*')),
        },
        'realignment_verdict': 'RETYPE_P5_V8U_AS_PRIOR_NEGATIVE_CONTEXT',
        'first_true_gap': 'PRIMARY_PAIRING_TYPE_SEED_AND_PER_LETTER_MUTATION',
        'z12_successor_status': 'DOWNSTREAM_COORDINATE_QUESTION',
    }
    out = Path('/mnt/data/p5_v8u_audit-package_20260711_131911/outputs/p5_v8u_REALIGNMENT_REPRODUCTION_20260711T131911.json')
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report, indent=2, sort_keys=True))
