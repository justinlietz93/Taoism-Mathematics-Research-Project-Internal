# Phase 5 v7r: Finite Quadratic Module Gauge / Isometry Classifier

## Objective

Build the classifier layer required after v7q:

```text
native transition assignment T
  -> cocycle / holonomy data
  -> finite module form
  -> isometry class
  -> coordinate matrix only after basis choice
```

The purpose is to stop treating a raw coupling matrix as the invariant. A raw matrix is a coordinate presentation. The invariant is its gauge/isometry class.

## Model tested

The executable sweep uses small rank-2 finite modules

```text
D_N = (Z/NZ)^2, N in {3,4,5,6,8}
```

with symmetric bilinear representatives `S mod N`.

For a basis change `P in GL(2,Z/NZ)`, the form transforms by

```text
S -> P^T S P mod N
```

The classifier assigns a canonical orbit key:

```text
canon(S) = lexicographic minimum of flatten(P^T S P) over P in GL(2,Z/NZ)
```

Two forms are classified as isometric when their canonical keys agree.

## Gates

1. Gauge invariance: `canon(S) = canon(P^T S P)`.
2. Nonisometry separation: adjacent distinct canonical keys remain distinct.
3. Degeneracy rejection: radical size greater than one is rejected.
4. Coordinate demotion: previous `c_ij` values are treated as coordinate presentations only.
5. 2-primary warning: even `N` is tagged for explicit normalization policy.

## Result

All tested gates passed.

## Boundary

This is not full finite quadratic module classification. It is a small-rank isometry classifier sufficient to lock the Phase 5 correction:

```text
canonical object != raw C
canonical object = gauge/isometry class
```
