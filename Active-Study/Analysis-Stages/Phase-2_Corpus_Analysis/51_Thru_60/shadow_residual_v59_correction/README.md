# Shadow Residual v59 correction package

This package corrects the v58 Shadow Residual verdict while preserving the v58 obstruction proof.

## Files

- `docs/v59_shadow_residual_correction.md` — full replacement note and exact target replacements.
- `patches/v58_to_v59_shadow_residual_targeted.patch` — direct patch map for stale rows/blocks.
- `proofs/ShadowResidualV59.lean` — Lean 4 proof surface for finite retained-orientation / scalar-cancellation claims.
- `notebooks/shadow_residual_eta_sympy_v59.ipynb` — Jupyter + SymPy audit, executed, no notebook file IO.
- `scripts/shadow_residual_eta_sympy_v59.py` — script that emits coefficient and summary artifacts.
- `outputs/shadow_residual_eta_summary_v59.json` — PASS/FAIL summary from the SymPy audit.
- `outputs/shadow_residual_eta_coefficients_v59.csv` — finite coefficient table through `t^1600`.
- `outputs/shadow_row_status_v59.csv` — row-level status replacements.
- `MANIFEST_SHA256SUMS.txt` — SHA-256 manifest.

## Pass signature

The SymPy audit reports:

- eta positive-half coefficient check: PASS through `t^1600`.
- scalar bilateral Jacobi derivative cancellation: PASS on symmetric windows `[1, 5, 12, 37, 89, 144]`.
- positive-half Shadow Residual nonzero: PASS.
- bilateral `n^0` normalization equals `2 ×` positive half: PASS.
- two-orientation channel carries what scalar projection erases: PASS.

## Corrected status

`Shadow Residual` is no longer classified as `EXTERNAL_REFERENCE_NOT_LOADED`.

Correct status:

```text
RETAINED_ORIENTATION_CHANNEL / QUANTUM_MODULAR / EXPLICIT_MULTIPLIER_PENDING
```

No closure-as-accomplished claim is made. The remaining finite task is the explicit two-orientation vector-valued multiplier/completion with eta as shadow.
