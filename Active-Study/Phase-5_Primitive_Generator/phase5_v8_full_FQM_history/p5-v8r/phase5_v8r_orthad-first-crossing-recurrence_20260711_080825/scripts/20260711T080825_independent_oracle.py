#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from orthad_v8r.oracle import independent_oracle
print(json.dumps(independent_oracle(),indent=2,sort_keys=True))
