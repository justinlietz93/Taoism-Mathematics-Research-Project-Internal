# Arbitrary QBL History Constraints Extracted from Axis-Free Overset Grid

## Constraint A: no single-chart canon

A single local chart cannot be made global by declaration.

## Constraint B: transition maps must be retained

If a state crosses a chart overlap, the transition map is part of the retained history.

## Constraint C: overlap has custody weights

Projection must include overlap weights or it double-counts / loses state.

## Constraint D: boundary handoff must be interior-derived

A native generation claim cannot insert boundary values externally.

## Constraint E: scalar closure is not tensor closure

Scalar quantities can behave well while vector/tensor component mixing remains unresolved.

## Constraint F: auxiliary readout is not native carrier

An auxiliary grid can compute/read a quantity without becoming the native retained state.

## Phase 5 consequence

The arbitrary-history theorem must classify:

```text
QBL word
  -> chart/latch overlap registry
  -> transition maps
  -> projection weights
  -> coupling tensor C
```

and must prove invariance under legal rewrites of the same retained history.
