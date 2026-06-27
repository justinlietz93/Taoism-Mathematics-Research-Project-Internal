#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=.
export FRAG_AUDIT_EDGES=0
python -m vdm_rt.run_orthad_listen \
  --run-root runs/final_probe \
  --out-dir outputs \
  --N 500 \
  --walkers 600 \
  --ticks 32 \
  --seeds 0,1 \
  --modes sparse_baseline,legal,legal_rewrite,illegal_flip,illegal_cocycle
pytest -q tests/test_orthad_listen_firewall.py
