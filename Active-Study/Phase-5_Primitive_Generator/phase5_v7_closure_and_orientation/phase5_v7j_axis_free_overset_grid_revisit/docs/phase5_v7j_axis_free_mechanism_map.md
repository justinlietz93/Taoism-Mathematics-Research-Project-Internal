# Axis-Free Mechanism Map

## Mechanism 1: single chart failure

A spherical polar grid is natural for spherical problems, but the axis/pole structure creates both CFL restrictions and artificial axis-boundary behavior.

Phase 5 mapping:

```text
single chart failure
  -> folded carrier / diagonal-only / projection-collapse warning
```

## Mechanism 2: overset repair

The Yin-Yang grid uses two overlapping low-latitude patches. Neither patch owns the whole sphere. The global object is assembled through overlap.

Phase 5 mapping:

```text
retained state is not owned by one chart
Orthad reads transition structure over the overlap
```

## Mechanism 3: transition matrices

The coordinate transition is fixed and symmetric. Vector quantities also require a component transform.

Phase 5 mapping:

```text
chart transition is lawful structure
component mixing is not scalar overlap
```

## Mechanism 4: ghost-zone handoff

Boundary values are not imposed as artificial angular boundary conditions. They are interpolated from the neighboring chart's interior.

Phase 5 mapping:

```text
boundary handoff should be native/interior-derived
```

## Mechanism 5: retained coefficient maps

The interpolation coefficients are computed once and retained.

Phase 5 mapping:

```text
coupling registry = retained overlap/latch map
```

## Mechanism 6: projection weights

Because regions overlap, scalar integrals require weights to avoid double counting.

Phase 5 mapping:

```text
projection/readout must know overlap custody
```

## Mechanism 7: scalar vs vector conservation

Scalar conservation can be fixed by flux replacement. Momentum is harder because components mix between rotated patches.

Phase 5 mapping:

```text
scalar shadow closure does not imply vector/tensor retained closure
```
