# Assumption Lock: p5-b1-v7

## Active affine model

1. `y_A = 2 y_(A-1) + gamma`.
2. `T_A = ceil(y_A)` on the affine model.
3. `E_A = y_A - T_A` and `c_A = T_A - 2 T_(A-1)` for `A >= 1`.
4. `gamma = 8 + 2a`, with `1/6 < a < 1/4`.
5. The current constant satisfies `a > 3/14`, by the included outward interval enclosure.
6. The affine carry language is the language of all interval itineraries of this affine map, not only the imported orbit.

## Accepted affine results inherited into this pass

- exact half-open carry partition;
- exact one-step mass matrix `J` and conditional table `P`;
- forbidden word `989`;
- length-three count `15` at the current constant;
- finite edge comparisons;
- finite outward-rounded boundary certificate on `A=0..10000`.

## Finite imported evidence

The exact Fibonacci threshold and affine ceiling model are identified on `A=0..10000` only by an imported prior finite certificate. This package validates and uses that trace but does not rerun the original Fibonacci-threshold verifier.

## Orthad authority

1. `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is primary.
2. The older canonical ledger is provenance only.
3. Operation counts, parity, defects, and primality do not determine any Orthad chart matrix, gauge value, holonomy, FQM class, or Weil projection.

## Holds not opened in this pass

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
