# Phase 5 v7t: T-to-FQM Extraction from Native Orthad Transition Records

STATUS: T_TO_FQM_EXTRACTION_SUPPORTED_ON_NATIVE_TRANSITION_RECORD_FIXTURE
GLOBAL_PASS: true
PHASE5_CLOSED: false

This package binds the v7q native transition assignment to the v7r/v7s finite-quadratic-module classifier path.

Pipeline:

```text
native Orthad transition records T
  -> axis support and doubled carriers D_i
  -> pairwise bilinear presentation C_ij mod lcm(D_i,D_j)
  -> radical gate
  -> 2-primary Jordan-symbol policy
  -> canonical gauge/isometry key
```

Hard counts:

```json
{
  "transition_cases": 10,
  "transition_records_processed": 24,
  "module_presentations": 10,
  "property_gates": "40 / 40",
  "gauge_checks": "10 / 10",
  "negative_controls": "7 / 7",
  "unique_fqm_keys": 5,
  "nondegenerate_cases": 4
}
```

Main verdict: Native transition records now feed a finite quadratic module presentation and 2-primary-normalized gauge key; raw C remains coordinate projection.
