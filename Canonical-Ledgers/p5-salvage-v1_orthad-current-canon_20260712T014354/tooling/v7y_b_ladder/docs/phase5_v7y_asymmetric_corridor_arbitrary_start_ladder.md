# Phase 5 v7y: Asymmetric Corridor / Arbitrary Start Ladder

## Status

`ASYMMETRIC_CORRIDOR_ARBITRARY_START_LADDER_CLOSED_POSITIVE_ON_RETAINED_UNIMODULAR_B_MODEL`

## Target

Recover and close the earlier asymmetric ladder target:

```text
B refinement must work over arbitrary admitted corridor starts,
not only the canonical Fibonacci origin path.
```

## Native ladder law tested

```text
B(u,v) = (v, u+v)
```

For depth `k`:

```text
B^k(u0,v0) = (F_(k-1)u0 + F_k v0, F_k u0 + F_(k+1)v0)
```

with the identity case handled at `k=0`.

## Closure result

```text
CLOSED_POSITIVE:
  asymmetric corridor / arbitrary start ladder
  arbitrary 1/n starts
  arbitrary coprime asymmetric starts
```

## Why it matters

The old risk was that the corridor mechanism was accidentally only the Fibonacci origin path. v7y rejects that. The B ladder is a unimodular transport on the retained pair. The canonical origin is one admitted start, not the whole mechanism.

## Main gates

```text
continuant matrix law
integer inverse recovery
coprime/gcd preservation
unimodular wedge preservation
projection collision separation
negative controls
```

## Hard counts

```json
{
  "phase": "Phase 5 v7y",
  "title": "Asymmetric Corridor / Arbitrary Start Ladder",
  "status": "ASYMMETRIC_CORRIDOR_ARBITRARY_START_LADDER_CLOSED_POSITIVE_ON_RETAINED_UNIMODULAR_B_MODEL",
  "global_pass": true,
  "phase5_closed": false,
  "start_cases": 96,
  "depth_max": 12,
  "b_ladder_records": 1248,
  "continuant_matrix_checks_passed": "1248/1248",
  "inverse_recovery_checks_passed": "1248/1248",
  "unimodular_wedge_checks_passed": "1260/1260",
  "projection_collision_witnesses": 40,
  "negative_controls_passed": "8/8",
  "canonical_reachable_starts": 8,
  "noncanonical_admitted_starts": 88,
  "one_over_n_starts": 22,
  "asymmetric_arbitrary_starts": 66,
  "closed_positive_targets": [
    "asymmetric corridor / arbitrary start ladder",
    "B refinement from arbitrary 1/n and asymmetric coprime starts"
  ],
  "closed_negative_targets": [
    "collapse arbitrary start to Fibonacci origin",
    "terminal projection signature is state-complete"
  ],
  "still_open": [
    "mock-theta FQM matching",
    "all-history confluence + cocycle proof",
    "full FQM classification boundary attack"
  ]
}
```

## Boundary

This does not close mock-theta matching, all-history confluence, or full FQM classification. It closes the arbitrary-start ladder target.
