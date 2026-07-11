# Assumption Lock

## Active affine model

1. `y_A = 2 y_(A-1) + gamma`.
2. `T_A = ceil(y_A)` on the affine model.
3. `E_A = y_A - T_A` and `c_A = T_A - 2 T_(A-1)` for `A >= 1`.
4. `gamma = 8 + 2a` with `1/6 < a < 1/4`.
5. The current constant also satisfies `a > 3/14`, established by the included outward interval enclosure.
6. The affine carry language means the set of all interval itineraries of this affine map, not only the one imported orbit.

## Finite imported evidence

1. The prior finite trace covers exactly `A=0..10000`.
2. The exact Fibonacci threshold and affine ceiling model are identified on that range by an imported prior finite certificate.
3. This package validates the trace structure, carries, transition counts, and affine interval membership. It does not rerun the original exact Fibonacci-threshold verifier.

## Orthad authority

1. `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is the current authority.
2. The older Phase 5 canonical ledger is provenance only.
3. Ordered QBL history is retained state; counts are not a substitute for the ordered word.

## Forbidden upgrades

- Do not infer global `T_A=ceil(y_A)` for the exact Fibonacci threshold from the finite trace.
- Do not call the imported specific orbit equidistributed or normal.
- Do not infer a chart matrix, gauge value, holonomy, FQM class, or Weil projection from counts, defects, oddness, or primality.
- Do not describe `P` as a first-order Markov presentation.
- Do not describe `M` as the full carry language.
- Do not describe `K` as the maximal-entropy measure of the actual affine carry coding.
- Do not transfer mixing of the pairwise edge envelope to the actual affine carry language.

## Required holds

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
ACTUAL CARRY LANGUAGE MIXING: NOT YET DERIVED
```
