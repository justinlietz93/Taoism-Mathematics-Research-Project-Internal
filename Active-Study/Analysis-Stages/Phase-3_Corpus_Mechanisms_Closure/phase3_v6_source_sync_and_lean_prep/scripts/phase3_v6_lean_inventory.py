from pathlib import Path
import csv, re
root = Path('lean')
rows=[]
for p in root.rglob('*.lean'):
    txt=p.read_text(encoding='utf-8', errors='ignore')
    rows.append({'path':str(p),'loc':len(txt.splitlines()),'sorry_count':txt.count('sorry'),'axiom_count':len(re.findall(r'\baxiom\b', txt))})
with open('phase3_v6_lean_inventory_recomputed.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=['path','loc','sorry_count','axiom_count'])
    w.writeheader(); w.writerows(rows)
print('lean files', len(rows))
