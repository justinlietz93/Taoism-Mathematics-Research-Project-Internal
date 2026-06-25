# Phase 3 v4 — Ancient Yi Carry/Lift Closure

## Claim

Ancient Yi octal-place tables instantiate a retained finite carrier with an ordered place-symbol state, least-significant-first readout, local successor/carry refinement, all-7 finite-domain completion, and lift into a higher place-domain.

## Retained state

```text
state_k = (d0, d1, ..., d{k-1}),  di ∈ {0,...,7}
value(state_k) = Σ_i d_i 8^i
```

## Internal successor

```text
increment d0
if di overflows 7, reset di = 0 and carry to d{i+1}
if d{k-1} overflows 7, append new high place d_k = 1
```

## Closure result

The finite domain of k places has `8^k` states. Its last retained carrier is `(7,7,...,7)`. The next state is `(0,0,...,0,1)`.

Displayed LSD-first:

```text
7      -> 01
77     -> 001
777    -> 0001
7777   -> 00001
```

## Gate result

```text
GLOBAL_PASS = true
```

## What is proved here

- LSD-first examples evaluate exactly to the extracted values.
- The successor/carry rule increments retained value by one.
- All-7 completion forces higher-place opening.
- Scalar value, low digit, and raw display are not state-complete projections.

## Falsification target

A machine-readable Ancient Yi row falsifies this closure if it contradicts the LSD-first normalized examples, the successor/carry value law, or the all-7 completion-to-lift rule.
