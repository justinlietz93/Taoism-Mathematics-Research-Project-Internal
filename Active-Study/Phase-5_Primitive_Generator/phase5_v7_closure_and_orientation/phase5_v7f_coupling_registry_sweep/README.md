# Phase 5 v7f: Coupling Registry Sweep

STATUS: `COUPLING_REGISTRY_SWEEP_SUPPORTED_FOR_BOUNDED_SHARED_LATCH_HISTORIES_FRONTIER_REFINED`

This package sweeps bounded shared-boundary QBL latch histories and extracts native inter-axis coupling values before product-module comparison.

The extractor is sealed first:

```text
c_native = Σ sign_b · (q_i(b)+1) · (q_j(b)+1) mod lcm(D_i,D_j)
```

Then each `c_native` is classified as direct-sum, closure-valid cross coupling, degenerate, or non-representative.

## Result

```text
GLOBAL_PASS: true
PHASE5_CLOSED: false
D_pair_count: 15
registry_rows: 918
property_gate_cases: 29
negative_controls: 23
max_positive_residual: 1.0226784664791497e-12
```

## Frontier

This is a bounded registry sweep, not a full arbitrary-history theorem. It supports native coupling generation for shared-latch histories and maps admissible/degenerate/non-representative classes across tested doubled-axis pairs.
