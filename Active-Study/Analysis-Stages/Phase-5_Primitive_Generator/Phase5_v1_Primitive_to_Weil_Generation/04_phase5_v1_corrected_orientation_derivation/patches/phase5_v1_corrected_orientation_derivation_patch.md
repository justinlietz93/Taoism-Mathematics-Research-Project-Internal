# Phase 5 v1 canon patch

1. Keep degenerate macro suspension.
2. Keep S/T symbol collision ban.
3. Keep Shadow law split.
4. Replace `orientation block may be dense` with:

```text
The orientation block may contain off-diagonal entries only when those entries are computed from Q/B/L accumulation and Orthad read. No dense block may be admitted by permission.
```

5. Add final verdict:

```text
Corrected derivation yields diagonal-only boundary unless a bilinear orientation-pairing rule is derived.
```
