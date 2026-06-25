# Obstacle and Design

## Exact obstacle

The agent's target is stronger than a telemetry demo:

```text
arbitrary lifted QBL history
  -> canonical retained history object
  -> unique coupling class up to gauge
  -> product-module Weil-compatible K/G operators
  -> terminal projection
```

The deep-research report did not find a direct off-the-shelf theorem for that exact bridge. It found pieces: trace normal forms, cocycle/holonomy compatibility, and finite quadratic module classification. This repo does not solve that theorem. It asks whether a VDM-style topology runtime can produce useful internal evidence before the theorem pass.

## Cutdown VDM shape

The full `vdm_rt` package is larger than this test needs. The harness keeps the part relevant to dynamic topology:

```text
walkers
  frontier / heat / cycle / random

maps
  cold / heat / trail / excitation / inhibition / memory

events
  vt_touch / edge_transfer / cycle_hit

admission
  discovered transfer map
  triangle cocycle residual
  topology spikes
  coupling echo gain
```

## Overset mapping

```text
chart                    -> graph node
overlap/interface         -> graph edge
retained latch transfer   -> local edge transition value
closed overlap loop       -> cycle residual / holonomy candidate
legal history             -> potential-derived transition: T_ij = p_j - p_i
illegal history           -> one corrupted latch on a cycle edge
visible projection        -> retained potentials mod 2
coupling object           -> discovered oriented transfer matrix
```

Potential-derived transitions close exactly:

```text
T_ij + T_jk + T_ki = 0
```

A corrupted latch leaves a residual and should produce inhibition/topology spikes when a cycle walker discovers it.

## Why CEG is still included

Void walkers discover candidate coupling structure. CEG tests whether the discovered structure improves echo recovery over a no-coupling blind baseline. It is an admission gate, not the discovery mechanism.
