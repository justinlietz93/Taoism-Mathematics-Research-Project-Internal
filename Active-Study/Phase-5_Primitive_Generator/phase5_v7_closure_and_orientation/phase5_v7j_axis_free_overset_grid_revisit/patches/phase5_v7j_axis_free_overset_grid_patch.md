# Phase 5 v7j Patch Guide

## Patch 1: replace single-lens Orthad language

```text
STALE:
  Orthad is a single matrix/lens.

CORRECTED:
  Orthad is an overset transition/readout structure over retained state.
```

## Patch 2: preserve overlap custody

```text
STALE:
  Projection can sum both charts directly.

CORRECTED:
  Projection must include overlap custody weights or equivalent no-double-counting rules.
```

## Patch 3: boundary handoff must be native

```text
STALE:
  Boundary values may be imposed externally.

CORRECTED:
  Native generation requires boundary handoff from neighboring retained interior state.
```

## Patch 4: scalar closure is insufficient

```text
STALE:
  Scalar closure proves full retained closure.

CORRECTED:
  Vector/tensor component mixing across chart transition needs separate gates.
```

## Patch 5: auxiliary readout separated

```text
STALE:
  An auxiliary basis used for computation is the native carrier.

CORRECTED:
  Auxiliary basis is a readout/projection layer unless it controls retained evolution.
```
