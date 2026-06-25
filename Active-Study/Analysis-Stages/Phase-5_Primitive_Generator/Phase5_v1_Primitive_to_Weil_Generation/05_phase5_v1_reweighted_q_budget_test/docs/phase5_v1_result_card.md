# Phase 5 v1 — Result Card

```text
STATUS: REJECTED_AT_COLLAPSE_CONSISTENCY_AND_BOUNDARY_DIFFERENT_GROWTH
PHASE5_V1_CLOSED: false
SEALED_BEFORE_COMPARISON: true
HAND_DENSE_BLOCK: forbidden
```

## Generated object

```text
Self_N(r) = exp(i*pi/2 * (4^r - 1)/3)
Pair_N(r,s) = exp(i*pi/2 * (f((r+s) mod N)-f(r)-f(s)))
```

## Located failure

```text
L2 collapse consistency fails:
expected -i/62423800998
derived  +i/62423800998
```

## Verdict

The repair does not generate the Weil generators. It is rejected before a generation claim because it fails to reduce to the existing Orthad diagonal trace.
