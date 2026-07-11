#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
STAMP = "20260711T145038"
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
ENV = dict(os.environ)
ENV["PYTHONDONTWRITEBYTECODE"] = "1"


def call(command: list[str], capture: bool = False) -> subprocess.CompletedProcess[str]:
    kwargs = {"cwd": ROOT, "env": ENV, "text": True, "check": True}
    if capture:
        kwargs.update({"stdout": subprocess.PIPE, "stderr": subprocess.PIPE})
    else:
        kwargs.update({"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL})
    return subprocess.run(command, **kwargs)


def clean_caches() -> None:
    for cache in list(ROOT.rglob("__pycache__")) + list(ROOT.rglob(".pytest_cache")):
        if cache.is_dir():
            shutil.rmtree(cache)
    for pyc in list(ROOT.rglob("*.pyc")) + list(ROOT.rglob("*.pyo")):
        pyc.unlink()


clean_caches()
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_generate.py")])
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_make_notebook.py")])
collect = call([sys.executable, "-m", "pytest", "--collect-only", "-q", "-p", "no:cacheprovider"], capture=True)
execute = call([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"], capture=True)
collected_match = re.search(r"(\d+) tests? collected", collect.stdout + collect.stderr)
passed_match = re.search(r"(\d+) passed", execute.stdout + execute.stderr)
if not collected_match or not passed_match:
    raise SystemExit("pytest count parse failed")
test_result = {
    "exit_code": execute.returncode,
    "collected": int(collected_match.group(1)),
    "passed": int(passed_match.group(1)),
    "cache_provider_disabled": True,
}
(ROOT / "outputs" / f"{STAMP}_test_results.json").write_text(json.dumps(test_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_make_manifest.py"), str(ROOT)])
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_run_controls.py"), str(ROOT), "--write"])
clean_caches()
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_make_manifest.py"), str(ROOT)])
call([sys.executable, str(ROOT / "scripts" / f"{STAMP}_verify.py"), str(ROOT)])
print(json.dumps({"status": "REBUILD_AND_VERIFY_PASS", "root": str(ROOT), "tests": test_result}, sort_keys=True))
