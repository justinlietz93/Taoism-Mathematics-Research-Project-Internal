# Assumption Lock

## Active inputs

1. The affine model satisfies
   \(y_A=2y_{A-1}+\gamma\) and \(T_A=\lceil y_A\rceil\).
2. \(E_A=y_A-T_A\), and \(c_A=T_A-2T_{A-1}\) for \(A\ge1\).
3. \(\gamma=8+2a\) with \(1/6<a<1/4\).
4. The prior finite trace covers `A=0..10000`; carry transitions use `A=2..10000`.
5. The exact Fibonacci threshold and affine ceiling model are identified only on the prior certified finite range `A=0..10000`.
6. `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is the current Orthad authority.
7. Older Phase 5 ledgers are provenance only.

## Forbidden imports

- No global assertion that the exact Fibonacci threshold equals the affine ceiling model for every `A`.
- No assertion that the specific dyadic orbit is equidistributed or normal.
- No inference of an Orthad chart matrix, primary pairing, transfer map, gauge value, holonomy, FQM class, or Weil projection from operation counts, defects, or primality.
- No use of the older `R/S/T` scheduler as primitive authority.
- No replacement of exact ordered QBL history by count summaries.

## Required status locks

```text
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
```
