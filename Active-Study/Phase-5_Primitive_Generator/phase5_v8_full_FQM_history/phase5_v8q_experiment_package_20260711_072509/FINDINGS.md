# Findings

## Repair decision

A clean primitive engine is safer and simpler than repairing the old implementation. The old engine's public objects encoded the rejected semantics: externally staged `BL`, synthetic `FLOOR`, pair reset, constant twelve-address carrier, and noncausal matrices. Reusing those objects would require redefining nearly every field and operation. Only the exact balanced refinement `(u,v)->(v,u+v)` and neutral package scaffolding survive.

## Proved abstractly

- The custody transition is deterministic once `X=(A,q,theta,k,j,W)` and the strict priority `B>Q>L` are fixed.
- `FLOOR` is unnecessary as an operation: saturation is the predicate `not CanB and not CanQ`.
- `L` changes `A` and local `k` only; pair and phase are carried.

These statements are implemented directly from the primary source. A Lean attack is included, but Lean was unavailable in the build environment, so no compiled formal-proof claim is made.

## Certified finitely

- The engine self-selects `BQQBBBQBQBBQBBL` from `(1,1)`.
- The boundary pair is `(55,89)` with product `4895`.
- Five `Q` steps produce phase quarter count `5`, hence visible phase `i`.
- After `L`: `A=1`, pair `(55,89)`, phase quarter count `5`, `k=0`, `j=7`.
- The first next-domain primitive is `B`, producing `(89,144)`.
- Every trace prefix, capacity, local/global position, predicate, and transition is emitted as machine data.
- Corruption controls fire for missing files, duplicate rows, word mutation, pair reset, phase reset, hard-coded `i`, fixed twelve positions before `L`, injected lap signs, partial matrix evidence, duplicate channel evidence, and broken lexical boundaries.

## Open

The provided source is not sufficient to derive exact per-tick chart maps. Section 13 gives the pairing-first restriction equations but explicitly says the exact chart-map recurrence remains a formalization obligation. Therefore:

```text
ORTHAD_CHART_RECURRENCE: NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

No constant matrices, chart labels, channel field, Shadow Residual comparison, character result, gauge class, FQM, Weil action, Bloch sphere, or MHD claim is emitted.
