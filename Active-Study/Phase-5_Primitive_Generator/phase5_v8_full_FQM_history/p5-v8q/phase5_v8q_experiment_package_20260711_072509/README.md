# Canon First Experiment: clean primitive custody boundary

This package replaces the old semantic core rather than repairing it.

The old implementation omitted the custody variables, self-selection law, five required `Q` steps, eight preceding `B` refinements, pair/phase carry, and exact word history. Repairing it would preserve misleading interfaces whose meanings do not survive the recovered law. The clean engine reuses only the valid balanced-refinement arithmetic and generic packaging conventions.

## Rebuild

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python scripts/20260711_072509_rebuild.py .
```

## Verify from scratch

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python scripts/20260711_072509_verify.py .
```

## Statuses

```text
PRIMITIVE_FIRST_CROSSING: PASS
POST_L_CARRY: PASS
ORTHAD_CHART_RECURRENCE: NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

See `FINDINGS.md` and `docs/20260711_072509_RESULTS.md`.
