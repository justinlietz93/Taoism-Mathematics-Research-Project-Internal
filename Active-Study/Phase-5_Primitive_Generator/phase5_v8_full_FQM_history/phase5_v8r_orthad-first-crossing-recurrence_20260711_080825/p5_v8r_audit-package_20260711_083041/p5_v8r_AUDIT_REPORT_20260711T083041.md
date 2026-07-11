# p5_v8r Audit Report

## Verdict

```text
REVISE

PRIMITIVE_FIRST_CROSSING: ADOPT
FIRST_L_CARRY: ADOPT
ACTIVE_AXIS_LOCAL_SHORTHAND: ADOPT
ORTHAD_RECURRENCE_UNDERDETERMINED: ADOPT
SMALLEST_MISSING_EQUATION: REJECT_AS_INCOMPLETE
ABSTRACT_PROOF_CERTIFICATE: REJECT
PACKAGE_INTEGRITY: REVISE
```

The package is a real improvement over `p5_v8q`. It performs the assigned source attack, preserves the accepted primitive engine, emits the three required custody snapshots, compiles the local active-axis shorthand through every prefix, and refuses to invent the primary pairing, chart matrices, transfers, rank extension, or projection.

The broad hard stop is sound: the supplied material does not yet determine a complete pairing-first dual-chart Orthad recurrence. The exact hard-stop certificate is not yet sound. The proposed scalar `tau_t` is introduced before the chart spaces, chart maps, pairing type, and rank-extension blocks have been defined. It therefore cannot yet be called the smallest missing equation.

## Reproduced package results

The exact supplied ZIP hashes to:

```text
5456edffbdc482564904e37aac6565ab39a11036be9959a20935982dc5184556
```

Direct execution reproduced:

```text
internal evidence verifier: 22/22 passed
detached ZIP-hash gate:      1/1 passed
combined verifier surface:   23/23 passed
pytest:                      9 passed
corruption controls:         16/16 target gates fired
response ZIP hash:           matched
```

The primitive evidence is correct:

```text
word through first L: BQQBBBQBQBBQBBL
floor pair:           (55,89)
phase quarters:       5
phase label:          i
post-L state:         A=1, pair=(55,89), k=0, j=7
first next-domain B:  (89,144)
```

The local scalar trace also correctly reaches `i/4895`, latches that value at `L`, and starts the new local slot at `1`.

## Adopted findings

### A1. Primitive custody remains correct

The engine self-selects the exact first crossing from `(1,1)`. It does not consume a supplied word, use `R/S/T`, create a `FLOOR` event, reset the pair, or reset the carried phase.

### A2. The three boundary snapshots are correctly separated

The package emits:

```text
before_first_L
immediately_after_first_L
immediately_after_first_next_domain_B
```

This repairs the one-tick ambiguity in the prior package.

### A3. The local active-axis shorthand is correctly compiled

The recurrence in `src/orthad_v8r/axis.py` computes the historical scalar trace:

```text
B: replace denominator by the new pair product
Q: multiply the local phase factor by i
L: latch the local scalar and open a new local slot at 1
```

This is valid as the local shorthand recorded in the governing law. It is not the primary pairing or either chart.

### A4. The package correctly refuses downstream claims

No primary-pairing matrix, chart matrix, transfer matrix, overlap residual, terminal projection, gauge class, FQM, or Weil action is emitted. This is the correct behavior while the recurrence remains open.

### A5. The broad underdetermination claim is mathematically correct

Chart restrictions alone do not determine mixed transfer data. For example, let

```text
H = K e_plus ⊕ K e_minus
```

and define a family of symmetric bilinear forms `P_c` by

```text
P_c(e_plus,e_plus)   = a_plus
P_c(e_minus,e_minus) = a_minus
P_c(e_plus,e_minus)  = P_c(e_minus,e_plus) = c
```

All `P_c` have the same restrictions to the two one-dimensional chart subspaces, while different values of `c` give different mixed blocks. Some mixed datum is therefore required.

That proves only underdetermination from restrictions. It does not prove that the Orthad gap is exactly one scalar recurrence.

## Findings requiring revision

### F1. `tau_t` is not yet a well-typed smallest missing equation

`src/orthad_v8r/assessment.py:22-26` proposes

```text
tau_t = P_t(iota_plus(e_t), iota_minus(e_t))
tau_(t+1) = Phi_U(X_(t+1), W_(t+1), tau_t)
```

But the same package lists `iota_plus` and `iota_minus` as open. It never defines:

```text
ambient retained module H_t
chart modules C_t^+ and C_t^-
chart bases
embeddings iota_t^+ and iota_t^-
pairing codomain
bilinear versus sesquilinear convention
symmetry or adjoint law
dimension of either chart
```

Until those objects exist, `tau_t` is not typed. It also assumes, without proof, that the relevant mixed block is one-dimensional.

For a chart of dimension greater than one, the missing object is a full mixed map

```text
M_t : C_t^- × C_t^+ -> K
```

or its matrix, not one scalar. At `L`, the new axis also creates old-to-new and new-to-old pairing blocks. One active-axis scalar cannot determine those couplings.

**Required correction:** find the earliest undefined typed object. Do not jump to `tau_t` until one-dimensional chart-active spaces and fixed embeddings have been proved.

### F2. The local scalar is not licensed as a chart restriction

The governing law calls `a_t=i^q/(uv)` an older single-entry shorthand and an active local trace of the larger pairing-first mutation. It does not identify that scalar with `OmegaPlus`, `OmegaMinus`, or either chart restriction.

`FINDINGS.md` and the recurrence assessment slide from:

```text
local active-axis shorthand
```

to:

```text
diagonal chart restriction
```

without a bridge. This imports precisely the single-lens interpretation the modern Orthad correction was meant to avoid.

**Required correction:** classify `a_t` as one of the following, with a source derivation:

```text
chart restriction entry
pairing invariant
local descendant/shorthand only
```

Until then, keep the status name `ACTIVE_AXIS_LOCAL_SHORTHAND`, not `ACTIVE_AXIS_RECURRENCE`.

### F3. The package does not contain the full source lineage it claims to close

The canonical ledger names active finite results from `v7p-v7u` and `v8a`, including transition records, confluence, and cocycle compatibility. The package contains:

```text
the ledger
the merged v2 law
a non-citable single-lens draft
the v7u script and short note
the rejected dual-chart rerun
```

It does not contain the actual `v7p`, `v7q`, or `v8a` source artifacts cited by the ledger. Those are the most likely sources for the transition alphabet and cocycle law.

The valid conclusion is:

```text
THE INCLUDED SOURCE SET DOES NOT FORCE THE RECURRENCE
```

The stronger sentence

```text
THE FULL SOURCE SET DOES NOT FORCE THE RECURRENCE
```

is not certified.

**Required correction:** locate and inspect the cited transition/confluence artifacts, or name them as unavailable inputs. Do not book full-source closure from a ledger summary alone.

### F4. The `O`-event rejection uses the wrong boundary

`assessment.py:31-32` rejects the historical bridge because it adds an `O` event outside the clean QBL alphabet.

That reason is insufficient. The primitive alphabet controls custody. A derived Orthad overlap update may have its own internal record without becoming a primitive letter in the carried word.

The actual defects in the historical v7u implementation are more precise:

1. `build_history()` appends all `O_ij` records after the Q/B/L axis histories rather than updating transfer after every primitive tick.
2. The `pair_c` formula is supplied without a derivation from the clean pairing-first law.
3. The code does not define two chart embeddings and then derive restrictions and transfers from one primary pairing.
4. Its synthetic history generator is not bound to the recovered self-selecting primitive engine.

**Required correction:** classify `O` by semantics, not by its letter. Determine whether it is:

```text
a forbidden custody primitive
a lawful derived overlap record inside each Q/B/L transition
a post-hoc event that cannot serve the recurrence
```

Then audit `T_ab=lens(b)/lens(a)` and `pair_c` separately.

### F5. The abstract proof artifact mimics the claim rather than proving it

`proofs/20260711T080825_OrthadRecurrenceGap.lean` defines four unrelated natural-number fields:

```text
plusRestriction
minusRestriction
plusToMinus
minusToPlus
```

and changes one field while holding two others fixed. It does not define:

```text
an ambient module
subspaces or chart embeddings
a bilinear or sesquilinear form
restriction of one form to two charts
transfer induced by that same form
symmetry, cocycle, or gauge constraints
```

The theorem is a record-level tautology. It does not formalize the stated Orthad underdetermination theorem. Lean being unavailable is not the main defect; the theorem surface itself is too weak.

**Required correction:** either provide the explicit two-dimensional bilinear construction above as the abstract proof, or formalize that construction in Lean. Do not count the current record theorem as the proof.

### F6. The hard-stop verifier certifies a static editorial string

`assess_recurrence()` returns the hard-stop text as constants. The verifier then compares the output JSON to a fresh call of the same function. The tests assert that the same strings contain `tau_0` and `Phi_B/Phi_Q/Phi_L`.

This proves that the report matches the program. It does not prove that the source set lacks a recurrence or that `tau_t` is minimal.

The `16/16` controls similarly detect evidence tampering, not errors in the mathematical source assessment.

**Required correction:** report these gates as report-consistency checks. Add a source-claim matrix that enumerates every historical recurrence candidate, its types, authority, and exact licensing verdict.

### F7. The manifest does not cover every archived file

The exact ZIP contains:

```text
70 file entries
60 manifest entries
9 unmanifested .pyc files
MANIFEST.json itself
```

The manifest generator and verifier explicitly ignore `__pycache__` and `.pyc`, while those files remain in the archive. Therefore `60/60 files verified` is not the package-wide integrity claim it appears to be.

Unmanifested files:

```text
src/orthad_v8r/__pycache__/__init__.cpython-313.pyc
src/orthad_v8r/__pycache__/assessment.cpython-313.pyc
src/orthad_v8r/__pycache__/axis.cpython-313.pyc
src/orthad_v8r/__pycache__/engine.cpython-313.pyc
src/orthad_v8r/__pycache__/evidence.cpython-313.pyc
src/orthad_v8r/__pycache__/law.cpython-313.pyc
src/orthad_v8r/__pycache__/oracle.cpython-313.pyc
src/orthad_v8r/__pycache__/state.cpython-313.pyc
src/orthad_v8r/__pycache__/verification.cpython-313.pyc
```

**Required correction:** remove caches before sealing. Make the manifest path set equal every archived file except `MANIFEST.json`. Make the verifier fail on any unmanifested extra.

### F8. The timestamped results file still violates the required shape

The required headings are:

```text
Status
Result
Concrete boundary
What this tests
Files
Boundary of claim
```

The package instead uses:

```text
Status
Result
Evidence
Controls
Reproducibility
Limitations
```

The information is mostly present, but the relay format was explicitly required.

### F9. The package lacks a novelty report against p5_v8q

The response is clearly not a duplicate, and the package contains new work. However, the outgoing instructions asked for a clean research delta. The package includes no machine-readable changed/added/reused file report against `p5_v8q`.

This is a packaging defect, not a scientific defect.

## Corrected status boundary

### Adopt

```text
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
FIRST_NEXT_DOMAIN_B: PASS
ACTIVE_AXIS_LOCAL_SHORTHAND: PASS
INCLUDED_SOURCE_SET_RECURRENCE_CLOSURE: FAIL
ORTHAD_RECURRENCE: NOT_YET_DERIVED
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

### Revise

```text
EXACT_EARLIEST_MISSING_TYPED_OBJECT
HISTORICAL_T/O_RECORD_LICENSING
ABSTRACT_UNDERDETERMINATION_PROOF
FULL_SOURCE_LINEAGE_COVERAGE
MANIFEST_COMPLETENESS
RESULTS_REPORT_SHAPE
```

### Open

```text
ambient retained module and chart types
chart embeddings
type and seed of the primary pairing
full B/Q/L pairing recurrence
mixed transfer block recurrence
first-L old/new coupling blocks
per-prefix chart restrictions and transfers
overset cocycle on the clean first crossing
terminal projection
gauge/FQM/Weil descent
```

## Direction for p5_v8s

The next pass should not attempt projection. It should determine the earliest typed Orthad gap and audit the historical transition lineage. The main fork is whether the chart atlas itself is still undefined, or whether the atlas is fixed and only its mixed pairing update is missing.
