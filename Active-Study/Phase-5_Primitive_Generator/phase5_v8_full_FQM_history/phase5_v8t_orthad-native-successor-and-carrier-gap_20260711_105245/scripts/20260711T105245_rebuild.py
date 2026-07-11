#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'src'))
from orthad_v8t.research import build_scientific_outputs
print(build_scientific_outputs(root,'20260711T105245'))
