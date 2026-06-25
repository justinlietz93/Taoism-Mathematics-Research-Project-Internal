# Phase 5 v7j: Axis-Free Overset Grid Revisit for Arbitrary QBL History

Status: `OVERSET_GRID_MECHANISM_REENTRY_COMPLETED_ARBITRARY_HISTORY_CONSTRAINTS_EXTRACTED`

This package re-reads the Axis-Free / Yin-Yang overset grid paper under the corrected Phase 5 canon.

## Main result

The paper is a strong operational analogue for overset Orthad behavior:

```text
bad single chart
  -> overlapping legal charts
  -> fixed chart transition
  -> ghost-zone handoff
  -> retained interpolation/weight maps
  -> projection discipline
```

## Main caution

It does not close arbitrary QBL history classification.

It gives constraints for the next normal-form pass.

## Run

```bash
python scripts/phase5_v7j_axis_free_overset_grid_revisit.py
```

## Contents

- `docs/`: mechanism map, result card, frontier note
- `outputs/`: CSV/JSON extraction tables
- `sealed/`: source/check hashes sealed before Phase Calculus extension
- `scripts/`: reproducibility script
- `notebooks/`: no-IO notebook
- `proofs/`, `lean/`: Lean proof surface for local extension
