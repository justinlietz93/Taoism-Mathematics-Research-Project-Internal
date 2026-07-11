# p5_v8r Orthad first-crossing recurrence

The accepted p5_v8q primitive engine is preserved. The full source set was then checked for a forced pairing-first dual-chart recurrence.

## Rebuild

```bash
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python scripts/20260711T080825_rebuild.py .
PYTHONDONTWRITEBYTECODE=1 python scripts/20260711T080825_make_manifest.py .
```

## Verify from scratch

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python scripts/20260711T080825_verify.py . \
  --zip ../p5_v8r_orthad-first-crossing-recurrence_20260711_080825.zip \
  --sha-file ../p5_v8r_orthad-first-crossing-recurrence_20260711_080825.zip.sha256
```

## Status

```text
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
ACTIVE_AXIS_RECURRENCE: PASS
PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED
ORTHAD_CHART_RECURRENCE: NOT_YET_DERIVED
ORTHAD_RANK_EXTENSION: NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

First audit entry: `FINDINGS.md`.
