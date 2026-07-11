import csv,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; STAMP='20260711T141656'

def test_source_rows_anchor():
 for r in csv.DictReader(open(ROOT/'outputs'/f'{STAMP}_pairing_type_source_claim_matrix.csv')):
  p=ROOT/r['exact_source_path']; assert p.exists()
  assert hashlib.sha256(p.read_bytes()).hexdigest()==r['source_sha256']
  lines=p.read_text().splitlines(); snippet='\n'.join(lines[int(r['line_start'])-1:int(r['line_end'])])
  assert r['anchor_text'] in snippet
