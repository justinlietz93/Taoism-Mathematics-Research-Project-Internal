# Canon Patch: Do Not Close Phase 5 Yet

Replace any pending final-closure statement with:

```text
Phase 5 remains open until the recovered target ledger has no BLOCKING_OPEN rows.
```

Add the target disposition law and keep `DO_NOT_CLOSE_PHASE5_GATE.json` sealed until all blocking rows are resolved.
