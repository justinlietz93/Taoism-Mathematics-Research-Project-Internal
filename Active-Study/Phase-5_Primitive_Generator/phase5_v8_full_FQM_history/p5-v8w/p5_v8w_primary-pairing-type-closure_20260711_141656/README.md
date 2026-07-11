# p5_v8w Primary Pairing Type Closure

## Status

See `FINDINGS.md`. The package derives the minimal abstract pairing interface and isolates the scalar-variance fork. It does not instantiate the Orthad.

## Rebuild

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/20260711T141656_rebuild.py .
```

## Verify

```bash
PYTHONDONTWRITEBYTECODE=1 python scripts/20260711T141656_verify.py .
```

## First files

1. `FINDINGS.md`
2. `docs/20260711T141656_PRIMARY_PAIRING_TYPE_CLOSURE.md`
3. `outputs/20260711T141656_pairing_type_source_claim_matrix.csv`
4. `outputs/20260711T141656_pairing_type_elimination_table.csv`
