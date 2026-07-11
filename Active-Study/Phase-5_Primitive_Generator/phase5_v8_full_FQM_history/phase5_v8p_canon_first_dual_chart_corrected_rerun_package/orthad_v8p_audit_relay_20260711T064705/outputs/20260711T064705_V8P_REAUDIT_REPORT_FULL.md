# Re-audit: v8p corrected dual-chart rerun against the recovered primitive custody and Orthad law

## Disposition

```text
REJECT_CANON_FIRST_CLAIM
REVOKE_GLOBAL_PASS
REVOKE_FINITE_BL_TRANSPORT_STATUS
RETAIN_NONCANONICAL_TABLE_REPRODUCTION_ONLY
```

The result changes materially from the first independent audit.

The earlier audit correctly found that the emitted lenses were non-causal, the second lens was not represented as a proved restriction of the primary pairing, the exact `i/4895` datum was not load-bearing, one directed transfer phase was unused, the verifier trusted precomputed evidence, and the Lean theorem surface was overstated.

That audit was still too generous because it accepted `BL` as a meaningful finite crossing scaffold. Under the recovered primitive law, the package does not execute the first crossing at all.

The first crossing from `(1,1)` is:

```text
B Q Q B B B Q B Q B B Q B B L
```

The package executes:

```text
B FLOOR L
```

where `FLOOR` is an invented intermediate event rather than a primitive letter or merely the saturation condition.

## Decisive replay

I replayed the recovered first-domain primitive word through the package's own `apply_b`, `apply_q`, `emit_floor_field`, `apply_l`, and `transport_after_l` functions.

```text
correct primitive word: BQQBBBQBQBBQBBL
package character result: 8/12
package survival gate: false
```

The package's advertised `12/12` result exists only when the five required `Q` operations and the preceding eight `B` operations are omitted.

This is the central finding. The package is not a damaged implementation of the correct first crossing. Its passing result depends on replacing the crossing with a different process.

## D1. Primitive self-selection is absent

The canonical primitive state requires at least:

```text
A     dimensional/domain counter
q     carried pair
θ     carried phase
k     local phase-position index
j     global phase-position index
W     exact ordered primitive history
```

The package's `LiftState` contains none of the dimensional or phase-capacity state needed to determine the next letter. There is no `CanB`, `CanQ`, domain capacity, or saturation predicate.

`run_once` externally calls one `B`, an invented `FLOOR` procedure, and one `L`:

```python
pair = ... else (34, 55)
state = LiftState(axes=[AxisState(pair[0], pair[1])])
apply_b(state)
emit_floor_field(state)
apply_l(state)
transport_after_l(state)
```

Source: `src/orthad_canon/application/experiment.py:8-17`.

`apply_q` exists as an unused helper but is never called by the experiment. The state does not self-select anything.

## D2. The package starts near the floor instead of deriving the floor

The true evolution begins at `(1,1)` and derives `(55,89)` through the complete ordered word.

The package starts at `(34,55)` and performs only the final local refinement:

```text
(34,55) -> (55,89)
```

That arithmetic step is correct as a local fact. It is not the first crossing. It omits the exact prefix that determines the phase, the floor admission, the latched axis, and every Orthad mutation before the boundary.

## D3. The claimed `i/4895` axis is not derived

In the passing baseline:

```text
Q operations executed: 0
frozen phase_mod4:      0
reported axis:          i/4895
```

The `i` is emitted because `AxisState.lens_axis` is hard-coded as:

```python
return f"i/{self.uv}"
```

for every phase value. The property reports `i/4895` at phase `0`, `1`, `2`, or `3`.

Source: `src/orthad_canon/domain/models.py:16-22`.

In the actual first crossing, five `Q` operations produce phase `i` at the floor. The package reports the same label without executing those operations.

## D4. `L` resets the carried pair instead of carrying it

The recovered law says `L` increments the dimensional counter and carries `(55,89)` and the phase into the new domain. The next `B` must be:

```text
(55,89) -> (89,144)
```

The package does:

```python
state.axes.append(AxisState(1, 1))
state.active_axis += 1
```

Source: `src/orthad_canon/application/compiler.py:107-117`.

Observed replay:

```text
active pair immediately after L: (1,1)
package's next B:                (1,2)
required next B:                 (89,144)
```

The code confuses a new local lens entry initialized to identity with a reset of the carried arithmetic custody state.

## D5. The six-to-twelve lift is inserted, not generated

The package hard-codes:

```python
CARRIER_SIZE = 12
OVERLAP_SIZE = 6
```

before any `L` occurs.

Both the pre-`L` and post-`L` lenses are already `12 x 12`:

```text
before L: 12 x 12
after L:  12 x 12
```

`L` does not grow matrix rank. It rebuilds another fixed `12 x 12` matrix and then `transport_after_l` duplicates six source channels into two hands, inserting `lap_sign = +1/-1` directly.

The relation `lap2=-lap1` is also written into the event log as a string. It is not derived from the carried five-Q phase history, because that history is absent from the passing run.

Therefore the package does not demonstrate:

```text
six positions
-> forced L
-> new dimension
-> carried phase
-> opposed second lap
-> twelve-position retained carrier
```

It begins with twelve addresses and applies a hand sign formula.

## D6. `FLOOR` is an invented intermediate field-emission stage

The floor is the state where `B` is blocked and `Q` has no remaining position. It is not an operator and does not emit a six-channel field during custody.

The package inserts:

```python
emit_floor_field(state)
```

between `B` and `L`, records an event named `FLOOR`, reads transfer entries, applies an invented `floor_bit = uv % 2`, and creates `InteriorChannel.orientation_value` rows.

Source: `src/orthad_canon/application/crossing.py:7-32`.

This is a separate synthetic computation that replaces continued lifted state evolution. Its `corrupt_floor_bit` ablation tests a package-invented bit, not the recovered primitive floor law.

## D7. The matrices are not the retained Orthad

The package creates arrays named:

```text
PrimaryPairing
OmegaPlus
OmegaMinus
TransferPlusToMinus
TransferMinusToPlus
```

but their existence does not establish the Orthad.

### No tick-by-tick retained construction

`_pairing(axis, ...)` rebuilds every `12 x 12` array from the current pair, `phase_mod4`, and a Boolean `lifted` flag. It does not retain the axis stack or derive the next matrices from the full prior Orthad state.

### No rank growth at `L`

The custody axis list grows to two entries, but the matrix object has no axis-stack rank. Its shape remains `12 x 12`.

### The passing projection does not use the two lenses

Reproduced controls:

```text
zero both pre-L Omega matrices:     still 12/12
zero the entire post-L lens:        still 12/12
```

The floor field reads only pre-`L` transfer entries. The far field then reads the already-created interior field plus `frozen_shift_mod6`. The post-`L` pairing, both post-`L` lenses, and both post-`L` transfers are not used for the final result.

### The primary-pairing restriction claim remains unproved

On the 121 supported `OmegaMinus` entries, 94 differ from the corresponding primary-pairing entries. A chart pullback or orientation-conjugation map might make a lawful relation possible, but none is represented or certified.

## D8. The exact retained history is collapsed

The matrix compiler sees only:

```text
(u,v)
phase modulo 4
lifted Boolean
```

It does not see the dimensional counter, local position, global position, exact Q count, full axis stack, or exact word prefix as causal inputs.

Different lifted histories that share the same reduced signature compile to the same arrays. This violates the requirement that the Orthad geometry be built by the exact ordered history.

The previously found collision remains:

```text
canonical label: i/4895
alternate label: i/77
all emitted matrices and fields identical
both produce the package's 12/12 result
```

## D9. Gauge, FQM, isometry, and Weil projection are not implemented here

The package cites earlier earned anchors and includes a `_gauss_phase` formula. It does not construct or verify:

```text
chart transition cocycle
gauge equivalence class
holonomy from the complete primitive history
finite quadratic module presentation
FQM isometry
Weil representation generated by this first-crossing Orthad
terminal projection through that generated structure
```

Those may remain valid results in earlier packages. They are not instantiated or bound to this package's synthetic `BL` computation.

## D10. The final output is not projection through the compiled Orthad

The claimed far-side result is produced by:

```python
residue = (source.basis_slot + 6 * hand + shift) % 12
lap_sign = 1 if hand == 0 else -1
character_value = source.orientation_value * lap_sign
```

Source: `src/orthad_canon/application/crossing.py:35-54`.

That is direct arithmetic duplication from a six-seat intermediate table. It is not a terminal projection through the completed primary pairing, both chart restrictions, and cross-chart transfers.

## D11. Verifier and proof defects remain

The first audit's verifier findings reproduce:

```text
empty matrix evidence + empty ablation evidence + empty provenance evidence:
    standalone verifier exits 0 with global_pass=true

twelve duplicates of one valid far-side row:
    standalone verifier exits 0 with global_pass=true
```

The Lean file still proves a finite formula over:

```text
one pair refinement
floorBit
shift6
hand sign
chi12 lookup
```

It does not define the recovered primitive trace, `Q` capacity, forced `L`, pair/phase carry, rank-growing dual-chart Orthad, gauge/FQM bridge, or terminal projection. The statement in the response that Lean states the actual finite B/L transport relation is false.

# Audit of the agent's response

| Agent statement | Revised verdict | Reason |
|---|---|---|
| `global_pass: true` | **Reject** | Only true for the synthetic `BL` model; correct word replay is `8/12`. |
| `QBL word: BL` | **False** | The first crossing word is `BQQBBBQBQBBQBBL`. |
| `crossing: B -> FLOOR -> L` | **False architecture** | `FLOOR` is a state condition, not an emitted operator or field stage. |
| `(34,55)->(55,89)` | **Retain as local arithmetic only** | It is the final local refinement, not the full crossing. |
| `latched axis: i/4895` | **Not certified** | No `Q` executes; `i` is hard-coded in the label property. |
| `new active axis: 1` | **Misrepresented in code** | A new lens slot may begin at identity, but custody pair and phase must carry; code resets pair to `(1,1)`. |
| `both word-built matrices emitted` | **Names emitted; claim false** | Arrays are rebuilt from reduced current state, not retained from the exact word; rank does not grow. |
| `7/7 load-bearing controls` | **Internal controls only** | They test the synthetic model and omit the decisive Q/order/carry controls. |
| `verifier recomputes evidence` | **Partial and insufficient** | It accepts absent matrix/ablation/provenance evidence and duplicate output coverage. |
| `Lean states the actual finite B/L transport relation` | **False** | It proves an invented one-B parity/shift identity without Q, L state evolution, lenses, or projection. |
| `completion_claim: false` | **True** | The explicit final-completion nonclaim is honest. |
| package hash/tests/manifest | **Retain** | These reproduce for the package as written. |

# Change to the first independent audit

## Findings retained

The old D1-D6 remain valid:

- lenses not causal;
- `OmegaMinus` restriction not represented;
- exact axis not load-bearing;
- reverse transfer phase unused;
- verifier not evidence-bound;
- Lean surface overstated.

## Findings strengthened

The exact-axis defect is stronger than a modular collision: the package reports `i/4895` without any `Q` history.

The lens-causality defect is stronger than a missing connection after `L`: the package never executes the canonical primitive history and never grows Orthad rank.

The doubled-carrier defect is stronger than an incomplete proof: twelve is hard-coded before `L` and the second hand is inserted arithmetically.

## Prior retained status revoked

The earlier status:

```text
FINITE_BL_TRANSFER_SEAT_CHARACTER_MATCH_OBSERVED
```

should be revoked because `BL` is not a lawful first-crossing history and the output fails when the correct history is replayed.

The narrow statement still supported is:

```text
A deterministic noncanonical one-B parity/shift table reproduces chi12 on 12 labeled residues under its own formulas.
```

This is a software fact, not an Orthad transport result.

# Repair boundary

This package should not be repaired by wiring the existing arrays more tightly into `transport_after_l`. That would preserve the wrong primitive object.

A valid rerun must begin below this package:

```text
1. Implement the primitive custody state A,q,theta,k,j,W.
2. Derive B/Q/L from strict priority B>Q>L.
3. Reproduce the exact first word from (1,1).
4. Carry q and theta across L; only increment A and restart local k.
5. Attach the primary pairing, both chart restrictions, and both transfers to every primitive prefix.
6. Make L extend their retained rank rather than rebuild a fixed 12x12 carrier.
7. Keep all structure in the lift until the run halts.
8. Apply one terminal projection through the completed Orthad.
9. Compare that result to chi12 only in the meta layer.
```

The exact all-prefix pairing/chart/transfer recurrence remains `NOT YET DERIVED` in the clean law. It must be derived before another package can honestly claim the Orthad is implemented.

# Reproduction artifacts

- `reaudit_v8p_against_clean_qbl.py`
- `V8P_REAUDIT_RESULTS_v2.json`

Subject ZIP SHA-256:

```text
906787a686458477fefc8e042832682aa3f3ba8c232667d235a15512c3273e75
```
