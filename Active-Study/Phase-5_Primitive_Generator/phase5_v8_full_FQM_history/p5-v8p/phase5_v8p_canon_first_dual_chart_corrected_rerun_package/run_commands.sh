#!/usr/bin/env bash
set -euo pipefail
python -m pip install -e '.[dev]'
python scripts/run_experiment.py
python scripts/verify_evidence.py .
pytest -q
