# Phase 3 v1 — General Shadow Correspondence Sweep

This package opens Phase 3 and executes v1.

## Contents

- `docs/PHASE_3_OUTLINE.md`
- `docs/phase3_v1_general_shadow_correspondence_sweep.md`
- `docs/phase3_v1_result_card.md`
- `outputs/phase3_v1_verification_summary.json`
- `outputs/phase3_v1_result_card.json`
- `outputs/phase3_v1_sweep_summary.csv`
- `outputs/phase3_v1_general_vs_specific.csv`
- `outputs/phase3_v1_coefficient_terms.csv`
- `outputs/phase3_v1_S_kernel_table.csv`
- `outputs/phase3_v1_T_diagonal_table.csv`
- `outputs/phase3_v1_scalar_vs_retained_closure.csv`
- `scripts/phase3_v1_general_shadow_sweep.py`
- `notebooks/phase3_v1_general_shadow_correspondence_sweep.ipynb`
- `proofs/Phase3V1ShadowCorrespondence.lean`
- `patches/phase2_to_phase3_status.patch`

## Result

`CONDITIONAL_CLASS_CLAIM_SUPPORTED_BY_SWEEP`

The χ12 Shadow Residual instance is treated as closed. Phase 3 v1 tests the general unary finite-module pattern and finds that the retained residue/orientation carrier supports the shadow-as-projection-loss correspondence across all tested cases.

## Reproduction

```bash
cd phase3_v1_general_shadow_correspondence
python3 scripts/phase3_v1_general_shadow_sweep.py
```
