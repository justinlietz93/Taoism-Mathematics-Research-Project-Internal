from pathlib import Path
import re, csv, json

ROOT = Path('/mnt/data')
PATTERNS = {
    'SHADOW_EXTERNAL': r'\bShadow\b.{0,80}\bexternal\b|\bexternal\b.{0,80}\bShadow\b',
    'NOT_LOADED_INTO_LIFT': r'not loaded into (the )?lift|not loaded into .*lifted',
    'SCALAR_FAILURE_AS_NONCLOSURE': r'scalar .*fail|fails .*scalar|projection .*failure',
    'L_RESETS_Q': r'\bL\b.{0,40}reset|reset.{0,40}\bq\b|reset.{0,40}\btheta\b',
}

def read(path):
    return Path(path).read_text(encoding='utf-8', errors='ignore')

sources = [ROOT/'20260620T085207_ORTHAD_CANON_TIGHTENED_DRAFT_v1_0.md', ROOT/'phase_tao_close_read_notes_v58.txt']
rows=[]
for src in sources:
    txt=read(src)
    for pid, pat in PATTERNS.items():
        c=len(re.findall(pat, txt, flags=re.I|re.S))
        if c:
            rows.append({'source':src.name,'pattern_id':pid,'count':c})
with open('phase3_v6_stale_language_audit_recomputed.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f, fieldnames=['source','pattern_id','count'])
    w.writeheader(); w.writerows(rows)
print(json.dumps({'rows':len(rows)}, indent=2))
