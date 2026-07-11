# Phase 5 v7m: Trace-Cocycle Normal Form for Admissible QBL History

## Result

```text
STATUS: TRACE_COCYCLE_NORMAL_FORM_PROTOCOL_SUPPORTED_GAUGE_CLASS_TARGET_LOCKED
GLOBAL_PASS: true
PHASE5_CLOSED: false
```

## Corrected theorem target

The target is not raw tensor uniqueness.

The corrected target is:

```text
admissible retained QBL history
  -> trace-normalized history class
  -> overlap / cocycle / holonomy data
  -> finite quadratic module or gauge class
  -> coordinate tensor C only after choosing a basis
```

## Hard results

```text
trace_cases: 12
trace_cases_passed: 12
D_pair_count: 66
registry_rows: 242
property_gate_cases: 125
property_gate_cases_passed: 125
negative_controls: 88
negative_controls_passed: 88
cocycle_checks: 4
cocycle_checks_passed: 4
gauge_checks: 4
gauge_checks_passed: 4
max_property_residual: 1.1368683772161603e-13
```

## What this proves

1. Legal independent swaps preserve the Foata normal form.
2. Legal equivalent histories preserve extracted bounded coupling data.
3. Illegal dependent swaps can change normal form and coupling.
4. Edge cochains admit cocycle/holonomy gates.
5. Local gauge changes preserve cycle holonomy.
6. Product-module polarization gates pass for sampled admissible cases.
7. Raw tensor uniqueness is the wrong target.

## Still open

```text
all admissible retained QBL histories
  -> canonical gauge-class finite quadratic module
```
