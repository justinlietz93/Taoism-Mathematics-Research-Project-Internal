from pathlib import Path
import json,hashlib,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
m=json.loads((root/'MANIFEST.json').read_text())
for row in m['files']:
    p=root/row['path']
    assert p.is_file(), row['path']
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    assert h==row['sha256'], (row['path'],h,row['sha256'])
ledger=json.loads((root/'ledger/SALVAGE_LEDGER.json').read_text())
assert len(ledger)==65, len(ledger)
assert {r['primary_class'] for r in ledger} <= set('ABCDEF')
assert any(r['id']=='v8m' and r['primary_class']=='C' for r in ledger)
assert any(r['id']=='v8c' and r['primary_class']=='E' for r in ledger)
assert any(r['id']=='v8q' and r['primary_class']=='A' for r in ledger)
print(json.dumps({'manifest_entries':len(m['files']),'ledger_rows':len(ledger),'status':'PASS'},indent=2))
