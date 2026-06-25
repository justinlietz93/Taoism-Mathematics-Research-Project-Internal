import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT/'sources'/'full_table.csv').read_text(encoding='utf-8').splitlines()))
failures = []
for r in rows:
    d = int(r['decimal'])
    bits = ''.join(str((d >> i) & 1) for i in range(6))
    oct_lsd = f'{d % 8}{d // 8}'
    if bits != r['six_line_binary_top_to_bottom_source_order']:
        failures.append({'decimal': d, 'gate': 'binary_lsd'})
    if oct_lsd != r['yi_octal_lsd_first_two_place']:
        failures.append({'decimal': d, 'gate': 'octal_lsd'})
print(json.dumps({'rows': len(rows), 'failures': failures, 'global_pass': not failures}, indent=2, ensure_ascii=False))
