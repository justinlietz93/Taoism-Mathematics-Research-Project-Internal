# p5_v8v Pairing-First Orthad Realignment

This package preserves the accepted primitive custody engine and relocates the first true Orthad gap from a finite successor to the primary pairing type, seed, and per-letter mutation.

## Status

```text
PRIMITIVE_CUSTODY: PASS
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
FIRST_NEXT_DOMAIN_B: PASS
ACTIVE_AXIS_LOCAL_SHORTHAND: PASS

EXACT_PRIMARY_PAIRING_TYPE: NOT_YET_DERIVED
EXACT_PRIMARY_PAIRING_SEED: NOT_YET_DERIVED
EXACT_PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED
EXACT_CHART_MAPS: NOT_YET_DERIVED
EXACT_DIRECTED_TRANSFERS: NOT_YET_DERIVED
TERMINAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
MHD_ORTHAD_READINESS: NOT_READY
```

## First files

1. `FINDINGS.md`
2. `docs/20260711T133900_PAIRING_FIRST_ORTHAD_REALIGNMENT.md`
3. `docs/20260711T133900_primary_pairing_type.md`
4. `trace/20260711T133900_custody_trace.jsonl`
5. `outputs/20260711T133900_gate_table.csv`

## Rebuild

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src \
python3 scripts/20260711T133900_rebuild.py
```

## Verify folder

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/20260711T133900_verify.py .
```

## Verify exact response ZIP

```bash
PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/20260711T133900_verify.py \
  /path/to/p5_v8v_pairing-first-orthad-realignment_20260711_133900.zip \
  --expected-zip-sha <SHA256_FROM_RESPONSE>
```

## Reproducibility contract

```text
NORMALIZED_SEMANTIC_REPRODUCIBILITY
```

Scientific JSON, CSV, JSONL, Markdown derivation, and source notebook content are fixed by the run stamp. Exclusions from byte comparison are the manifest, ZIP container metadata, pytest/JUnit timing, executed-notebook runtime metadata, and detached ZIP hash supplied at verification time.

No `__pycache__`, `.pyc`, or `.pytest_cache` path is included in the sealed package.
