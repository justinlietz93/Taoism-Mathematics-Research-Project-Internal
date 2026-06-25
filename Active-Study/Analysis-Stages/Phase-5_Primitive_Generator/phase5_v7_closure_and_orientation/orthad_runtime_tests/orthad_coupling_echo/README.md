# Orthad Coupling Echo

Status: `SMOKE_SUPPORTED_WORTH_PURSUING_NOT_A_THEOREM`

This repo tests whether the VDM/void-walker topology-telemetry idea is worth pursuing for the Phase 5 arbitrary-history blocker.

It does **not** prove the final theorem:

```text
arbitrary QBL history -> canonical coupling tensor up to gauge
```

It builds a tiny falsifiable overset arena where retained QBL-like history is normalized, reduced into a pairwise coupling candidate, instrumented with VDM-style topology telemetry, and tested by equal-budget echo recovery.

## Why this exists

The Phase 5 v7i/v7j frontier says the open bridge is:

```text
QBL word
  -> chart/latch overlap registry
  -> transition maps
  -> projection weights
  -> coupling tensor C
  -> invariance under legal rewrites
```

This package supplies a first machine test for that bridge.

## Run

```bash
python -m orthad_coupling_echo.run_experiment --out outputs
```

or after install:

```bash
orthad-coupling-echo --out outputs
```

## Main result

The included deterministic run produced:

```text
GLOBAL_PASS: true
legal_rewrite_invariance: PASS
same_projection_different_retained_history: PASS
illegal_cocycle_rejected: PASS
positive_coupling_echo_gain: PASS
telemetry_flags_bad_history: PASS
```

Median Coupling Echo Gain over admitted positive histories: see `outputs/result_card.json`.

## Interpretation

This is enough to keep the VDM/overset path alive as an experimental compiler layer. It is not enough to sideline external theory permanently. The recommended path is:

```text
VDM telemetry discovers candidate latch/cycle structure.
Coupling Echo tests whether the extracted C carries recoverable information.
Trace/cocycle/FQM theory still supplies the theorem layer.
```
