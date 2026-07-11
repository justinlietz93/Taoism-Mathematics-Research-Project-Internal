# Assumption Lock

## Authority order

1. `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`
2. active canon anchors in `PHASE5_CANONICAL_LEDGER_v3.md`
3. `p5_v8u` audit realignment
4. historical sources only after narrow re-licensing

## Fixed custody law

```text
Xi_t=(A_t,q_t,theta_t,k_t,j_t,W_t)
B > Q > L
j=j_start(A)+k
j_start(A)=1+6(2^A-1)
```

## Written notation controls

Where the image glyph and written notation disagree, the written notation controls.

```text
Primitive custody state:      Xi_t
Fully retained lifted state:  Xi_hat_t
Orthad:                        ⌞Xi_hat_t⌝
```

## Forbidden semantic imports

```text
R/S/T primitive authority
fixed window or 64-tick schedule
externally supplied word
synthetic FLOOR operator
pair reset at L
phase reset at L
post-L-only Orthad
constant lens matrices
independently seeded chart matrices
post-hoc analytical Orthad
search/candidate selection in live custody or readout
projection before halt
imported Weil operator as P_0
finished FQM as P_0
Bloch coordinate as P_0
affine 7/8/9 coordinate as P_0
Z/12Z successor as upstream pairing generator
terminal character as pairing seed
```

## Forbidden Python imports tested

The live source tree must not import:

```text
sklearn
scipy.optimize
networkx
joblib
ray
torch
tensorflow
jax
cupy
numba.cuda
```

## Claim discipline

A candidate formalization is not a derived theorem. Missing pairing, chart, transfer, and projection layers emit no numeric matrices or rows.
