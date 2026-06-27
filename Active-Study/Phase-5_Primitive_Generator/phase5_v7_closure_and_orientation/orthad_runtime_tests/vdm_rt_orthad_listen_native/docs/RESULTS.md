# Results: Listen-Only VDM-RT Orthad Probe

## Mandate result

The final probe obeyed the correct boundary:

```text
The harness never scans, never reduces the graph, never asks the engine a question.
It only receives what the walkers announce and passes it through.
```

No original engine files were modified. The package adds only:

```text
vdm_rt/io/orthad_state.py
vdm_rt/run_orthad_listen.py
tests/test_orthad_listen_firewall.py
docs/*
outputs/*
```

## Runtime configuration

```text
N = 500
walkers = 600
walker ratio = 1.2 walkers/neuron
best-scale reference = 5000 neurons : 6000 walkers = 1.2 walkers/neuron
ticks per scenario = 32
seeds = 0, 1
modes = sparse_baseline, legal, legal_rewrite, illegal_flip, illegal_cocycle
```

## Scan firewall

A runtime firewall replaced these graph-read methods with hard failures:

```text
active_edge_count
connected_components
cyclomatic_complexity
connectome_entropy
snapshot_graph
```

Result:

```text
scan_firewall_all_ok = true
pytest = 1 passed
```

That means the probe did not use the dense/projection-style telemetry path.

## Speed result

```text
mean_tick_s_overall = 0.0580490949968663
max_tick_s_overall = 0.0877604639999845
native_speed_gate_mean_tick_lt_250ms = true
```

The earlier 6.5 seconds/tick result was a bad harness result, not a native engine result.

## Orthad signal result

The engine consumed structured Orthad state and emitted native walker/ADC/event-map telemetry. However, the legal-rewrite and illegal-retained cases did not separate reliably enough to claim an Orthad admissibility detector.

```text
legal_vs_rewrite_distance_mean = 0.017083128379735215
legal_vs_illegal_flip_distance_mean = 0.008447316633314666
legal_vs_illegal_cocycle_distance_mean = 0.007331384620057946
```

The legal rewrite should have been closer than illegal cases. It was not.

Additional B1 comparison also failed the clean separation gate:

```text
b1_legal_vs_rewrite_absdiff_mean = 23.52960501644702
b1_legal_vs_illegal_flip_absdiff_mean = 17.961287264042767
b1_legal_vs_illegal_cocycle_absdiff_mean = 13.635658214945579
native_b1_signal_candidate = false
```

## Verdict

```text
listen_probe_pass = true
orthad_admissibility_solved = false
global_pass = false
```

This pass proves the corrected harness boundary and recovers native-speed listening. It does not prove that this IO-only Orthad state adapter gives the VDM ecology a reliable legal/illegal retained-history signal.

Recommendation:

```text
do_not_replace_deep_research;
keep listen-only VDM as an instrument if the theorem path continues
```
