# What Changed

The original engine was left intact. No original VDM-RT engine/runtime dynamics file was edited.

## Added

```text
vdm_rt/io/orthad_state.py
vdm_rt/run_orthad_listen.py
tests/test_orthad_listen_firewall.py
docs/MANDATE.md
docs/RESULTS.md
outputs/result_card.json
outputs/scenario_summary.csv
outputs/tick_listen_rows.csv
```

## Not changed

```text
core/sparse_connectome.py
core/engine/core_engine.py
core/cortex/*
core/adc.py
core/void_b1.py
runtime/events_adapter.py
runtime/loop/main.py
runtime/stepper.py
runtime/telemetry.py
```

## IO replacement

The language/decoder path is not used. Structured Orthad frames are converted directly into deterministic stimulus indices:

```text
OrthadFrame
  visible symbols
  retained symbols
  -> deterministic BLAKE2 index groups
  -> connectome.stimulate_indices(...)
```

No lexicon, phrase bank, speaker, decoder, or autonomous language output participates in the probe.

## Listen-only output

The output side drains the native announcement bus and folds only event-derived signals:

```text
bus.drain(...)
adc.update_from(observations)
observations_to_events(observations)
CoreEngine.step(...)
eng._last_evt_snapshot bounded event-map fields
```

It does not call `CoreEngine.snapshot()` because that method uses `compute_metrics()`.
