# Shadow Residual v60 Completion Package

Status: `CLOSED_MULTIPLIER_SURFACE / RETAINED_ORIENTATION_CHANNEL`

This package completes the remaining v59 task:

- builds the two-orientation Shadow channel,
- embeds it in the exact residue-vector unary-theta derivative parent,
- exhibits the weight-3/2 S/T multiplier system,
- confirms the coefficient-stripped shadow is eta,
- preserves the v58 scalar obstruction as correct.

## Main files

- `docs/v60_shadow_residual_multiplier_completion.md` — theorem-grade result note.
- `docs/v60_repo_patch_instructions.md` — direct replacement text for stale v58/v59 rows.
- `scripts/shadow_residual_multiplier_v60.py` — SymPy/mpmath verification script.
- `outputs/v60_verification_summary.json` — PASS ledger.
- `outputs/v60_completion_result_card.json` — status/result card.
- `outputs/v60_orientation_residue_coefficients.csv` — coefficient channel table.
- `outputs/v60_S_matrix_weight_half.csv` — exact weight-1/2 S matrix entries.
- `outputs/v60_S_matrix_weight_three_half.csv` — exact weight-3/2 S matrix entries.
- `outputs/v60_T_multiplier_diagonal.csv` — exact T multipliers.
- `proofs/ShadowResidualV60.lean` — Lean theorem surface.
- `notebooks/shadow_residual_multiplier_v60.ipynb` — notebook audit, no file I/O required.
- `MANIFEST_SHA256SUMS.txt` — package integrity manifest.

## Pass signature

```text
GLOBAL_PASS: true
eta coefficient check: PASS
orientation projection check: PASS
chi eta multiplier check: PASS
numeric S/T transform check: PASS
```
