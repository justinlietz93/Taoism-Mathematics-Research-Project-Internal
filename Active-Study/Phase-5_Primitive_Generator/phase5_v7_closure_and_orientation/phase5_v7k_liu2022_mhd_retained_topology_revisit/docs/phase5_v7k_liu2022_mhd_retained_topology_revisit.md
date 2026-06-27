# Phase 5 v7k: Liu 2022 MHD Revisit for Retained Topology and Projection Discipline

## Status

`RETAINED_TOPOLOGY_ANALOGUE_CONFIRMED_ARBITRARY_HISTORY_CLASSIFICATION_STILL_OPEN`

## Purpose

This pass re-enters Liu 2022 after the corrected Phase 5 canon: doubled carrier, overset Orthad, product-module coupling, and the open arbitrary QBL history classification problem.

## Paper mechanism extracted

The paper builds a data-constrained MHD simulation of a filament-sigmoid system in AR 11520. The relevant structure is not merely the visible filament/sigmoid image. The relevant object is the retained 3D magnetic topology: MFR, HFT, null point, overlying field, high-Q boundaries, and reconnection-driven connectivity change.

## Phase 5 mapping

The strongest mapping is:

```text
retained 3D MHD topology
  -> retained lifted state

HFT / null point
  -> branch/latch boundary where custody changes

overlying reconnection P1->P3
  -> endpoint/custody reassignment

tether-cutting at HFT
  -> branch separation: high branch erupts, low branch remains

synthetic AIA images
  -> downstream projection from retained state
```

## What this does not prove

This does not prove the arbitrary QBL history classification theorem. It supports the need for such a theorem. The unresolved problem is still:

```text
arbitrary QBL history
  -> canonical retained axes
  -> canonical boundary events
  -> canonical coupling tensor C
```

## Caveats preserved

- The requested data/animations are not available in this pass.
- The initial model is already unstable and lacks the slow-rise phase.
- The simulation does not include optically thin radiative cooling and does not form prominence condensation.
- The authors do not rule out alternative double-decker/partial eruption interpretations.

## Conclusion

Liu 2022 is strong support for the *kind* of retained-topology / projection discipline Phase 5 needs. It is not a closure proof.
