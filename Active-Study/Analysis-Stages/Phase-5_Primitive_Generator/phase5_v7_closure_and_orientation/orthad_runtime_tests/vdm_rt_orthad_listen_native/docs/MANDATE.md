# Mandate

The harness never scans, never reduces the graph, never asks the engine a question.

It only receives what the walkers announce and passes it through.

This is not a performance preference. It is the architecture boundary. The walkers are the scan. The announcement stream is retained-state reporting. A graph scan is a terminal projection bolted onto a system that already emits its own state.

Allowed:

```text
structured Orthad state -> deterministic stimulus indices
VDM engine tick -> walker announcements
announcement bus drain -> ADC/event fold
bounded event-map snapshots -> output sink
```

Forbidden:

```text
compute_metrics
active_edge_count
connected_components
cyclomatic_complexity
connectome_entropy
snapshot_graph
per-tick graph status payloads
per-tick map dictionary dumps
```
