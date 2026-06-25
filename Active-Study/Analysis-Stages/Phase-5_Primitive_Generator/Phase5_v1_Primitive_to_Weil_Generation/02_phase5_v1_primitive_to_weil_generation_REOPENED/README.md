# Phase 5 v1 — Reopened Orthad Correction

Status: `REOPENED_METHOD_SUSPECT_CORRECTED_TEST_NOT_YET_FORMED`

The original Phase 5 v1 result is preserved under `original_phase5_v1_snapshot/`.

The old verdict is no longer final. It is reclassified as a narrow bare-primitive control because it removed the Orthad and compared raw primitive moves to finished Weil generators at the wrong layer.

Corrected standing:

```text
Original residuals: retained as method-control data.
Corrected falsifier: NOT_TRIGGERED.
Generation verdict: UNTESTED_AFTER_CORRECTION.
Stop point: explicit QBL word + native Orthad terminal projection declaration gate.
```

The next admissible Phase 5 step is not another residual subtraction. It is construction of explicit finite QBL words `W_S` and `W_T`, then Orthad read/lift, then readout-level comparison against the classical Weil generators.
