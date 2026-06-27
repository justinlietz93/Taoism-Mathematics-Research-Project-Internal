# Phase 5 v7y Protocol Definitions

## Admitted start

```text
(u0,v0) is admitted iff:
  u0 > 0
  v0 > 0
  gcd(u0,v0) = 1
```

## B ladder

```text
B(u,v) = (v, u+v)
```

## Inverse ladder

```text
B^{-1}(u,v) = (v-u, u)
```

This inverse is applied only to terminal states known to lie on an admitted B trajectory.

## Continuant law

```text
B^k(u0,v0) = (F_(k-1)u0 + F_k v0, F_k u0 + F_(k+1)v0)
```

## Projection collision rule

A terminal readout key is not state-complete if two starts collide under a projection key while inverse recovery separates them.

## Closure disposition values

```text
CLOSED_POSITIVE
CLOSED_NEGATIVE
SUPERSEDED_WITH_EXPLICIT_REPLACEMENT
DEFERRED_OUT_OF_PHASE_WITH_REASON
BLOCKING_OPEN
```
