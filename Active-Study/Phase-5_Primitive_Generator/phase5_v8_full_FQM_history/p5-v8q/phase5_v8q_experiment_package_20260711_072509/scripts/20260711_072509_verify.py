#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
sys.path.insert(0, str(ROOT / "src"))

from primitive_custody.verification.verifier import verify_root

report = verify_root(ROOT, check_manifest=True)
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["verified"] else 1)
