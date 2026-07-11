#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'src'))
from orthad_v8s.verification import verify
zip_path=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else None
result=verify(root,zip_path)
import json
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['pass'] else 1)
