# Canon Checkpoints

## Current enforced rules

- Orthad has no candidates and no scalar output.
- Q and B mutate the active axis in place.
- B is the exact mediant update `(u,v) -> sort(v,u+v)`.
- Q is exact quarter continuation, `theta += π/2`.
- L latches exactly one active axis and opens exactly one new axis.
- L carries the accumulated phase and does not reset the lifted state.
- Rank grows by one per L.
- External Shadow Residual is not loaded into the lift.

## Gate trace

See `trace_logs/20260620T113500_canon_gate_trace.jsonl`.
