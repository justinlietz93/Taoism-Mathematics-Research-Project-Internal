# v7r Protocol Definitions

## Coordinate presentation

A matrix `C` or `S` written after choosing a basis of the finite module.

## Gauge / basis change

For rank-2 `D_N=(Z/NZ)^2`, a legal frame change is any `P in GL(2,Z/NZ)`.

## Isometry action

```text
S' = P^T S P mod N
```

## Canonical orbit key

```text
canon(S) = min_{P in GL(2,Z/NZ)} flatten(P^T S P mod N)
```

## Nondegeneracy

A form is admitted only when its radical is trivial. In the rank-2 square case this is equivalent to `det(S)` being a unit modulo `N`.

## 2-primary policy marker

Even `N` forms are tagged. v7r does not claim final Jordan normalization for the 2-primary sector.
