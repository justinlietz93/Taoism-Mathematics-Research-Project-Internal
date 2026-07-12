# Phase 5 v8e External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8e generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings are recorded there.

## What was verified

1. Orbit machinery soundness and completeness (within shape).
   The v8e `act_on_c` union rule was proven correct on paper (merge requires
   pullback equality on generators + polarization, which determines the form;
   every isometry between same-shape family members necessarily passes those
   gates) and then cross-checked by execution: a from-scratch brute-force
   decider testing full pointwise form equality over all group elements
   reproduces the v8e orbit classes exactly on every tested pair.
   Load-bearing instance: (8,8) -> {0,4},{1,7},{2,6},{3,5} from both arms.

2. Cross-shape rigidity (the gap v8e did not test).
   v8e compares presentations only within a fixed shape (D1,D2), but the same
   abstract group can carry two shapes (Z/4 x Z/6 ~= Z/2 x Z/12). If any
   cross-shape isometry existed, the v8e classifier would silently split one
   true class into two, and its completeness claim would be false.
   Exhaustive search over all four same-group alias pairs inside the v8e
   D range found ZERO cross-shape isometries:
     (4,6)/(2,12), (6,8)/(2,24), (4,10)/(2,20), (8,12)/(4,24).

## Findings

- v8e size-2 classifier: VERIFIED on tested range.
- v8e invariant-incompleteness result (CLOSED_NEGATIVE with residual walls):
  independently consistent; the (8,8) c=0 vs c=2 collision is real.
- Cross-shape rigidity: HOLDS EMPIRICALLY, NOT PROVEN. Ledger status:
  CONJECTURED_LEMMA_EMPIRICALLY_GATED. v8e's completeness claim depends on it.

## Obligations created for v8f

1. Prove the cross-shape rigidity lemma (family diagonals q(e_i) = 1/(2 D_i)
   rigidify shape), or extend this exhaustive gate to every alias pair in the
   v8f range and cite the gate in any completeness claim.
2. Connected coupling graph is NOT an isometry invariant: attempt orthogonal
   splitting before booking any component as genuinely rank >= 3.

## How to run

    python3 scripts/v8e_external_audit.py

Exit 0 = check 1 passes. Outputs land in outputs/ as two CSVs. Pure Python,
stdlib only, exact integer arithmetic in the decision path (no floats).
Runtime: ~1-2 min; dominated by the (12,24) and (8,12)/(4,24) searches.
