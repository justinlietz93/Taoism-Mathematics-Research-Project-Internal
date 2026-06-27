# Protocol Definitions

## Target disposition set

`CLOSED_POSITIVE`: target is positively supported by artifact gates.

`CLOSED_NEGATIVE`: target was tested and rejected; negative result retained.

`SUPERSEDED_WITH_EXPLICIT_REPLACEMENT`: target is replaced by a stronger or corrected target and may not be used in its old form.

`DEFERRED_OUT_OF_PHASE_WITH_REASON`: target is real but outside the finite Phase 5 closure surface.

`BLOCKING_OPEN`: target must be closed, superseded, or explicitly deferred before Phase 5 closure.

## Closure gate

```text
phase5_can_close := blocking_open_count == 0
```

For v7v, `phase5_can_close = false`.
