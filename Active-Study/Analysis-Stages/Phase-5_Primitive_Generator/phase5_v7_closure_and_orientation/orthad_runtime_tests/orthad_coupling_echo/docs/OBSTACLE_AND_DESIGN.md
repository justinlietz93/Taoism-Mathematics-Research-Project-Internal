# Obstacle and design

## Source obstacle

Phase 5 v7i/v7j keeps the arbitrary-history theorem open:

```text
arbitrary QBL history class
  -> retained coupling tensor class
  -> admissible / degenerate / nonrepresentative / direct-sum classification
```

The overset-grid revisit sharpened the mechanism constraints:

```text
QBL word
  -> chart/latch overlap registry
  -> transition maps
  -> projection weights
  -> coupling tensor C
  -> invariance under legal rewrites
```

The missing bridge is not whether retained history matters. The missing bridge is whether retained history can be reduced canonically enough to emit a coupling object that survives legal rewrites and detects illegal overlap closure.

## This repo's test

This is a smoke harness, not the final theorem.

It builds a three-chart overset loop:

```text
A -- B
 \  /
  C
```

Each history is a retained event word over local touches and boundary latches. The harness then checks:

1. Cartier-Foata-style trace normal form for legal adjacent swaps.
2. Native pairwise coupling extraction from retained latch history.
3. Triangle cocycle/holonomy residual.
4. VDM-style telemetry fold: heat, excitation, inhibition, memory, boundary spikes, cycle hits, topology spikes.
5. Equal-budget Coupling Echo Gain.

## Admission logic

A candidate C is admitted only when the triangle residual closes:

```text
c_AB + c_BC + c_CA = 0 mod D
```

This is a tiny stand-in for overlap cocycle compatibility. It is intentionally strict enough to reject H4.

## Worth-pursuing criterion

The VDM/overset path is worth pursuing if:

```text
legal rewrites preserve C,
same visible projection can hide different retained C,
illegal cocycle histories are rejected,
extracted C improves echo recovery under equal computational budget,
telemetry flags the bad topology.
```

The deterministic run passes all five gates.
