#!/usr/bin/env python3
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from orthad_v8u.research import build_outputs
build_outputs(ROOT,'20260711T121112')
print('rebuilt scientific outputs')
