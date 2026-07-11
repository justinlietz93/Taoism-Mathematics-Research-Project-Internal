#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
from orthad_v8s.analysis import rebuild
rebuild(root)
print("REBUILD: PASS")
