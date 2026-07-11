# p5_v8x: Pairing Representability and First-L Rank Law

This package narrows the primary-pairing boundary without instantiating the Orthad.

## Result

The written architecture forces one primary **two-slot pairing object** with contravariant restriction in both arguments. It does not force a scalar-valued form or a represented morphism `P:H->D(H)`.

The first `L` preserves the old pairing sector and appends one architectural axis, but the source does not type orthogonality as left, right, or two-sided. Neither mixed block is therefore certified zero. The architectural axis count rises `1 -> 2`; algebraic pairing rank remains untyped.

## Rebuild

```bash
python3 scripts/20260711T145038_rebuild.py .
```

## Verify from scratch

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/20260711T145038_verify.py .
```

Pytest is run with its cache provider disabled. The verifier leaves the checked tree unchanged.

## Audit order

1. `FINDINGS.md`
2. `docs/20260711T145038_PAIRING_REPRESENTABILITY_AND_L_RANK_LAW.md`
3. `outputs/20260711T145038_pairing_representability_source_ledger.csv`
4. `outputs/20260711T145038_first_L_mixed_block_cases.json`
5. `outputs/20260711T145038_pairing_rank_semantics.csv`
