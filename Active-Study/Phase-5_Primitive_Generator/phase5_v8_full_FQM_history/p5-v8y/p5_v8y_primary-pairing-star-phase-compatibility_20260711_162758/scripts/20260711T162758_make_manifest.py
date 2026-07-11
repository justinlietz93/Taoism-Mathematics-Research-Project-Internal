from pathlib import Path
import hashlib,json,sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
entries=[]
for p in sorted(root.rglob('*')):
 if p.is_file() and p.name!='MANIFEST.json': entries.append({'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'MANIFEST.json').write_text(json.dumps({'algorithm':'sha256','entries':entries},indent=2)+'\n')
