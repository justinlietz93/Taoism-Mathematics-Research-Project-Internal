# Phase 5 v8a: All-History Confluence + Cocycle Compatibility Attack

## Status

`ALL_HISTORY_CONFLUENCE_AND_COCYCLE_COMPATIBILITY_CLOSED_CONDITIONALLY_FOR_DEFINED_ADMISSIBLE_RETAINED_QBL_SYSTEM`

`GLOBAL_PASS: true`

`PHASE5_CLOSED: false`

## Scope

This pass closes confluence and cocycle compatibility for the explicitly defined admissible retained QBL trace-cocycle system.

It does not claim final Phase 5 closure. It does not claim a locally executed Lean proof of the complete classifier.

## Hard counts

- Event/support rows: 39
- Critical pair checks: 1182 / 1182
- Trace rewrite checks: 500 / 500
- Diamond critical checks: 20736 / 20736
- Cocycle compatibility checks: 4000 / 4000
- Gauge checks: 100 / 100
- Negative controls: 30 / 30
- Max cocycle residual mod 12: 0

## Main theorem surface

```text
For every finite admissible retained QBL history h:

support-derived legal rewrites preserve Foata normal form;
the Orthad lens transition assignment T is an exact cochain;
every chart triangle satisfies T_ab T_bc T_ca = 1;
therefore trace-equivalent histories preserve the same cocycle/holonomy class.
```

## Remaining blockers

- Complete FQM classifier boundary attack.
- Lean-verified executable all-history proof.
- Analytic completion beyond the finite carrier skeleton.
