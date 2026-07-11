# Audit Results

## Verdict

```text
REJECT_CURRENT_CANON_FIRST_CLAIM
REBUILD_PRIMITIVE_ENGINE_BEFORE_ORTHAD_CLAIMS
RETAIN_LOCAL_ARITHMETIC_AND_PACKAGE_SCAFFOLD_ONLY
```

## Main result

The package's `12/12` and `global_pass=true` do not audit the recovered first crossing. The package runs `B -> FLOOR -> L` from `(34,55)`, while the governing primitive law derives the ordered first crossing from `(1,1)` as:

```text
B Q Q B B B Q B Q B B Q B B L
```

Replaying that exact word through the package's own operators produces:

```text
character match: 8/12
survival gate: false
```

The passing result therefore depends on replacing the canonical crossing with a different process.

## Specific findings

### 1. Primitive self-selection is absent

`application/experiment.py:8-16` starts at `(34,55)` and directly calls one `B`, `emit_floor_field`, one `L`, and `transport_after_l`. It never calls `Q`. The state has no dimensional counter, local Q-position index, global position index, capacity law, `CanB`, or `CanQ`.

### 2. The floor is replaced by an invented event

`application/crossing.py:7-32` creates a six-row `FLOOR` field and logs `FLOOR` as an event. Under the governing law, the floor is the state where `B` is blocked and `Q` has no remaining position. It is not an operator and does not emit an intermediate field.

### 3. The claimed `i/4895` is not generated

`domain/models.py:20-22` returns `i/uv` for every axis, independent of `phase_mod4`. The passing run executes zero `Q` steps. The real `i/4895` is earned only after the exact five-Q prefix.

### 4. `L` resets the carried pair

`application/compiler.py:107-117` appends a new `AxisState(1,1)`. The clean law carries `(55,89)` through `L`, then the next `B` produces `(89,144)`.

### 5. Rank growth and lap opposition are inserted rather than derived

`CARRIER_SIZE=12` is fixed before `L`, and the lens remains 12-by-12 after `L`. `transport_after_l` creates the second hand with `lap_sign = -1`, while the event log records `lap2=-lap1` as a string. The package does not derive six positions, saturation, dimensional extension, carried phase, and the opposed second lap.

### 6. The lens matrices are not causal to the claimed result

The audit reproduces both failures:

```text
zero both pre-L Omega matrices: survival still passes
zero the entire post-L lens:    survival still passes
```

The final character table is therefore not a terminal projection through the completed Orthad.

### 7. Pairing-first restriction is not certified

The package emits `pairing`, `OmegaPlus`, `OmegaMinus`, and transfer arrays, but does not expose chart maps that mechanically establish both diagonal blocks and both off-diagonal blocks as restrictions of one primary pairing. The second lens contains supported entries that disagree with the primary pairing.

### 8. Gauge, FQM, isometry, and generated Weil descent are absent

The package contains matrix and Gauss-phase vocabulary, but no chart cocycle, holonomy certificate, gauge quotient, FQM presentation, FQM isometry certificate, or Weil action derived from this complete primitive history.

### 9. The verifier can pass destroyed evidence

The standalone verifier returns `global_pass=true` after matrix, ablation, per-channel, and provenance evidence files are emptied. It also accepts twelve duplicates of one valid far-side row. The verifier checks selected values, not evidence completeness and uniqueness.

### 10. Lean proves a table identity, not the crossing

`TransportRelation.lean` defines one refinement from the fixed pair `(34,55)`, inserts a floor parity rule and hand sign, and proves the resulting 12-row character relation by `native_decide`. It does not formalize self-selection, the full word, Q capacity, forced `L`, carry, rank-growing Orthad state, or terminal projection.

## Retained facts

- The package reproduces its own noncanonical model.
- The local arithmetic `(34,55) -> (55,89)` is correct.
- The external character reference is separated into the meta layer.
- The package states several honest nonclaims.
- The existing directory and test scaffold may be reused after the semantic core is replaced.

## Scope

- Proved abstractly: none by this audit beyond direct source-level identities.
- Certified finitely: the decisive replay of `BQQBBBQBQBBQBBL` through the package yields `8/12` and a false survival gate; the two lens-causality ablations still pass; the verifier corruption tests still pass.
- Open: exact dual-chart mutation recurrence, gauge/FQM bridge for the clean crossing, generated Weil action, and any final Shadow Residual or MHD projection claim.
