#!/usr/bin/env python3
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
import sys,json
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'src'))
from orthad_v8t.verification import verify
path=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root
control='--control-mode' in sys.argv
r=verify(path,control_mode=control)
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['pass'] else 1)
