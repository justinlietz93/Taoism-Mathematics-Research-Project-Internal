# Phase 5 v1 — Reweighted-Q Budget Repair Test

Status: `REJECTED_AT_COLLAPSE_CONSISTENCY_AND_BOUNDARY_DIFFERENT_GROWTH`

Phase 5 v1 stays open. This package tests the specific reweighted-Q repair under sealed discipline.

The derived budget law is:

```text
b_r = floor_capacity(r) = 4^r
f(r) = sum_{j<r} b_j = (4^r - 1)/3
Q_budget e_r = exp(i*pi*b_r/2) e_{r+1}
Self(r) = exp(i*pi*f(r)/2)
```

Modulo four, `f(0)=0` and `f(r)=1` for every `r>=1`. The repair therefore does not produce a quadratic self-channel. It collapses to a constant `i` phase after the first occupied orientation.

Collapse consistency:

```text
L1: PASS  -> i/4895
L2: FAIL  -> derived +i/62423800998; expected -i/62423800998
```

The pair-channel was derived only by polarizing the sealed self-channel. No dense block was inserted.

The post-seal comparison fails for `χ12` and `χ8`, but the decisive rejection happens earlier: the repair does not recover the existing diagonal trace at L2.
