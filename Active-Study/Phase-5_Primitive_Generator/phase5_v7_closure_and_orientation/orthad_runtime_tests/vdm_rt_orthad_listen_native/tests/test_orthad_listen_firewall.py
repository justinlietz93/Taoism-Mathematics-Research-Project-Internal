import json
import os
import subprocess
import sys
from pathlib import Path


def test_listen_probe_scan_firewall(tmp_path):
    root = Path(__file__).resolve().parents[1]
    out = tmp_path / "out"
    run_root = tmp_path / "runs"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root)
    env["FRAG_AUDIT_EDGES"] = "0"
    cmd = [
        sys.executable, "-m", "vdm_rt.run_orthad_listen",
        "--run-root", str(run_root),
        "--out-dir", str(out),
        "--N", "120",
        "--walkers", "144",
        "--ticks", "8",
        "--seeds", "0",
        "--modes", "legal,legal_rewrite,illegal_flip,illegal_cocycle",
    ]
    subprocess.check_call(cmd, cwd=str(root), env=env)
    card = json.loads((out / "result_card.json").read_text())
    assert card["scan_firewall_all_ok"] is True
    assert card["original_engine_files_modified"] == 0
    assert card["walker_ratio"] == 1.2
