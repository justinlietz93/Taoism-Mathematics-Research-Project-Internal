# Phase 3 v4 — Ancient Yi Carry/Lift Closure

Status: `FINITE_CARRY_LIFT_CLOSURE_SUPPORTED`

This package closes the Ancient Yi finite carry/lift target at the retained octal-place carrier layer.

## Result

- LSD-first display examples evaluate exactly.
- The successor/carry rule increments retained value by one.
- Domain completion occurs at all current digits equal to 7.
- Lift opens the next high-place carrier: `77 -> 001`, `777 -> 0001`, `7777 -> 00001`.
- Scalar/display projections are not state-complete.

## Run

```bash
python scripts/phase3_v4_ancient_yi_carry_lift.py --max-k 5
```

## Main files

- `docs/phase3_v4_ancient_yi_carry_lift_closure.md`
- `outputs/phase3_v4_verification_summary.json`
- `outputs/phase3_v4_domain_completion_lift_table.csv`
- `outputs/phase3_v4_64_successor_table.csv`
- `outputs/phase3_v4_projection_loss_witnesses.csv`
- `proofs/Phase3V4AncientYiCarryLift.lean`
- `notebooks/phase3_v4_ancient_yi_carry_lift_closure.ipynb`
