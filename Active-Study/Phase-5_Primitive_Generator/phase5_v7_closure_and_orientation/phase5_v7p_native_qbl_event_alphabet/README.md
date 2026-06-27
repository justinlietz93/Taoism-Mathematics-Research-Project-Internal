# Phase 5 v7p: Native QBL Event Alphabet and Support-Derived Independence

STATUS: `NATIVE_SUPPORT_DERIVED_EVENT_ALPHABET_SUPPORTED_ON_TESTED_QBL_HISTORY_MODEL`

GLOBAL_PASS: true  
PHASE5_CLOSED: false

## Result

v7p replaces hand-labeled event admissibility with a native support-derived rule.

```text
Q/B/L primitive effects
  -> read/write/birth support tokens
  -> independence/dependence relation
  -> legal trace rewrites
  -> Foata normal form
  -> retained coupling/contact signature checks
```

## Hard counts

```json
{
  "alphabet_rows": 5,
  "independence_rows": 64,
  "trace_cases": 10,
  "trace_cases_passed": 10,
  "rewrite_checks": 3,
  "rewrite_checks_passed": 3,
  "coupling_gates": 10,
  "coupling_gates_passed": 10,
  "negative_controls": 4,
  "negative_controls_passed": 4,
  "claim_rows": 5,
  "frontier_rows": 4,
  "falsification_targets": 5
}
```

## Main boundary

This pass does not close arbitrary QBL history classification. It closes the first missing protocol layer: the event alphabet and legal commutation relation are now derived from retained support rather than hand labels.
