#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(x for x in root.rglob("*") if x.is_file() and x.name != "MANIFEST.json"):
    rows.append({"path":p.relative_to(root).as_posix(),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
(root/"MANIFEST.json").write_text(json.dumps({"schema":"p5-manifest-v2","file_count":len(rows),"files":rows},indent=2,sort_keys=True)+"\n")
print(len(rows))
