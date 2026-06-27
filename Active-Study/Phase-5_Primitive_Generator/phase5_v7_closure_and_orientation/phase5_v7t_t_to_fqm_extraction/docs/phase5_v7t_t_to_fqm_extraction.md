# Phase 5 v7t: T-to-FQM Extraction from Native Orthad Transition Records

## Objective

v7t removes the remaining gap between native transition records and finite quadratic module comparison.

Previous state:

```text
QBL support history
  -> transition records T
  -> raw pair couplings C
```

v7t state:

```text
QBL support history
  -> transition records T
  -> finite module presentation
  -> radical gate
  -> 2-primary Jordan-symbol policy
  -> gauge/isometry key
```

## Extraction law

For each admitted history case, axes are read from transition support. Each axis receives a doubled even carrier `D_i` from the retained lens denominators and phase support. Pair transitions contribute to a symmetric bilinear presentation by reducing native pair increments modulo `lcm(D_i,D_j)`.

The resulting object is not the raw matrix. It is the finite module presentation plus its normalized gauge key.

## Gates

1. Every contributing transition must come from a native transition record.
2. Terminal readout records do not mutate the module.
3. The extracted bilinear matrix must be symmetric.
4. Radical-bearing forms are flagged and cannot be promoted as nondegenerate.
5. Even carriers pass through 2-primary Jordan-symbol policy before comparison.
6. Gauge/permutation checks preserve canonical class keys.
7. Negative controls reject illegal mutation, radical collapse, skipped policy, and terminal readout mutation.

## Result

The bounded v7q fixture now produces finite module presentations and stable canonical gauge keys. This is a real bridge from `T` into the FQM layer.

## Boundary

This still does not close full arbitrary retained QBL history classification. It closes the tested extraction protocol from native transition records into FQM presentations.
