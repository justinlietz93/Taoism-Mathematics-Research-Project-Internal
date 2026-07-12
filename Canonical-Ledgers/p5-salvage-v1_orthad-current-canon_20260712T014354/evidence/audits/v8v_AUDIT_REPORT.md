# p5_v8v Audit Report

## Verdict

```text
REVISE

PAIRING_FIRST_BRANCH_REALIGNMENT: ADOPT
PRIMITIVE_CUSTODY_BASELINE: ADOPT
SUCCESSOR_FIRST_RETIREMENT: ADOPT
DOWNSTREAM_HARD_STOP: ADOPT
PACKAGE_INTEGRITY: ADOPT

PAIRING_TYPE_DATUM_AS_EARLIEST_EXACT_OBJECT: REVISE
PAIRING_SEED_NONUNIQUENESS: REVISE
FULL_PREFIX_CAUSAL_CERTIFICATE: REVISE
SOURCE_CLOSURE_CERTIFICATE: REVISE
CORRUPTION_CONTROLS_EXECUTED: FAIL
```

The package follows the ratified dependency order:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

It correctly retires the `Z/12Z` successor as the first gap. It preserves the accepted primitive trace and leaves pairing, charts, transfers, and projection closed.

## Reproduced results

The supplied ZIP hash matches the response:

```text
ae97c9ec1e1cac24ed1a55beacb8267b54ae18a94b4240b6fecd45e8f195a1a8
```

The corrected research document hash also matches:

```text
a0420819e30600f931aa97a635bf19055f7ff9dd458ff0ea66d5ddaec2e8a1be
```

Direct verification reproduced:

```text
exact ZIP verifier: 11/11 passed
pytest:             16/16 passed
manifest entries:   79
archive files:      80 including MANIFEST.json
cache files:        0
```

The accepted primitive evidence remains:

```text
word:                    BQQBBBQBQBBQBBL
floor pair:              (55,89)
floor product:           4895
Q steps:                 5
phase witness:           i
after L:                 A=1, pair=(55,89), k=0, j=7
first next-domain pair:  (89,144)
local shorthand:         i/4895
```

## Adopted findings

### A1. The branch realignment is correct

The package correctly makes the primary pairing upstream of both chart restrictions and both directed transfers.

The fixed successor on `Z/12Z` remains downstream coordinate mathematics. It is not used as the pairing seed or recurrence.

### A2. The pairing hard stop is real

The source set does not currently provide a complete pairing seed or per-letter `B/Q/L` mutation law.

The package correctly emits no pairing, chart, transfer, cocycle, or projection values.

### A3. The state boundary is mostly correct

The package separates:

```text
Xi_t          primitive custody state
Xi_hat_t      fully retained lifted state
⌞Xi_hat_t⌝    Orthad wrapper and reader
```

It also separates the local phase-position index `k` from the architectural pairing-rank counter.

### A4. The downstream boundaries are correct

The package correctly keeps these layers closed:

```text
chart maps
directed transfers
overlap cocycle
terminal projection
gauge/FQM/Weil descent
QBL-to-affine factor map
MHD Orthad application
```

## Findings requiring revision

### F1. `D_P` is a candidate decomposition, not yet the proved earliest exact object

The package names:

```text
D_P = (K, H_0, duality_or_involution, variance, symmetry_law)
```

as the first exact missing object.

This is a useful checklist, but it is a bundle of several missing choices. The package does not determine which component is logically first. It also does not prove that all five components are independent.

The earliest sub-gap may be the retained argument object `H_0`. It may instead be the minimal duality interface needed to state a pullback pairing. The package has not settled that fork.

Corrected status:

```text
PAIRING_TYPE_DATUM_D_P:
    CANDIDATE_DECOMPOSITION

EARLIEST_TYPED_SUBGAP:
    NOT_YET_ISOLATED
```

### F2. The pairing-seed proof establishes raw-presentation nonuniqueness only

The package uses:

```text
P1(x,y)=xy
P2(x,y)=2xy
```

on a one-dimensional rational module.

This proves that the custody tuple alone does not choose one raw formula.

It does not yet prove that two distinct retained pairing seeds exist because:

1. the rational module is not derived from the Orthad architecture;
2. the witness does not implement the required quarter-turn action by `i`;
3. the witness does not include the two chart pullbacks or the first-`L` extension;
4. the allowed gauge group is not fixed;
5. the two forms may become equivalent after a coefficient-field or basis change.

The exact certified statement is:

```text
RAW_PAIRING_PRESENTATION_FROM_CUSTODY_ALONE:
    NONUNIQUE

RETAINED_GAUGE_CLASS_SEED:
    NOT_YET_PROVED_NONUNIQUE
```

The map

```text
eta_P : (Xi_0,W_0,D_P) -> P_0
```

is therefore a candidate seed interface. It is not yet the uniquely isolated next missing map.

### F3. The source-closure claim is under-evidenced

The package includes a five-row historical disposition table. It does not include a complete source-claim matrix for the pairing-type question.

The conclusion that the sources do not distinguish bilinear, sesquilinear, quadratic, operator-valued, or duality-valued forms is plausible. The package does not show the elimination test for each candidate.

The next pass must extract the exact formulas and constraints from:

```text
QBL v2 pairing-first law
the `iota* P iota` pullback shape
the `P -> U* P U` gauge shape
the `C_t*` first-L block shape
the quarter-turn witness i
the historical H=M+iJ result
the downstream FQM polarization
```

It must then state what each formula proves and what it does not prove.

### F4. The corruption controls were not executed

The response reports:

```text
corruption controls: 12/12 fired
```

The package does not perform twelve mutations.

`rebuild.py` writes every control with:

```text
target_gate_fired = True
pass = True
```

`run_controls.py` contains a static list whose `fired` field is also always `True`.

The verifier only checks those stored booleans.

A direct attack confirms the defect:

```text
mutate custody_trace.jsonl
run run_controls.py
result: exit 0, 12/12 fired

run the real verifier on the same mutated copy
result: exit 1
```

The controls are a declared table, not executed falsification tests.

Corrected status:

```text
CORRUPTION_CONTROL_TABLE_PRESENT: PASS
CORRUPTION_CONTROLS_EXECUTED: FAIL
```

### F5. Several source-derived gates are hard-coded

These gates are written as unconditional `True` values:

```text
PAIRING_FIRST_DEPENDENCY
PAIRING_TYPE_HARD_STOP
SUCCESSOR_FIRST_RETIRED
Z12_LOCAL_TYPE
MHD_READINESS_BOUNDARY
```

The verifier checks that the rows exist and that candidate rows remain false. It does not recompute the source reasoning.

These gates certify report consistency, not source truth.

### F6. The full-prefix causal trace is a schema trace, not an Orthad transition certificate

Every pairing, chart, and transfer value is `null`.

The trace correctly records the intended order:

```text
custody advance
-> pairing mutation
-> chart derivation
-> transfer derivation
-> retained next state
```

It does not certify that those mutations occurred.

Corrected status:

```text
ONE_TICK_CAUSAL_ORDER:
    ARCHITECTURAL_SCHEMA_CONFIRMED

ONE_TICK_ORTHAD_COEVOLUTION:
    NOT_YET_INSTANTIATED
```

### F7. `Xi_hat_t` is not instantiated by this package

The package marks the record as `PARTIAL_SCHEMA_ONLY`. That is honest.

The response should distinguish:

```text
ORTHAD EXISTS FROM FIRST PRIMITIVE TICK:
    ARCHITECTURAL LAW

Xi_hat_t VALUES IN THIS PACKAGE:
    NOT_INSTANTIATED
```

A record with null `P`, chart, and transfer fields is not the fully retained lifted state itself.

## Corrected status boundary

```text
PRIMITIVE_CUSTODY: PASS
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
FIRST_NEXT_DOMAIN_B: PASS
ACTIVE_AXIS_LOCAL_SHORTHAND: PASS

PAIRING_FIRST_DEPENDENCY: ADOPT
NATIVE_SUCCESSOR_ON_Z12: DOWNSTREAM_COORDINATE_QUESTION

MINIMAL_PAIRING_INTERFACE: NOT_YET_DERIVED
PAIRING_TYPE_DATUM_D_P: CANDIDATE_DECOMPOSITION
EARLIEST_TYPED_SUBGAP: NOT_YET_ISOLATED

RAW_PAIRING_PRESENTATION_NONUNIQUENESS: PROVED
RETAINED_GAUGE_CLASS_SEED_NONUNIQUENESS: NOT_YET_DERIVED

PRIMARY_PAIRING_SEED: NOT_YET_DERIVED
B_PAIRING_MUTATION: NOT_YET_DERIVED
Q_PAIRING_MUTATION: NOT_YET_DERIVED
L_PAIRING_EXTENSION: NOT_YET_DERIVED

CHART_MAPS: NOT_YET_DERIVED
DIRECTED_TRANSFERS: NOT_YET_DERIVED
ONE_TICK_ORTHAD_COEVOLUTION: NOT_YET_INSTANTIATED
TERMINAL_PROJECTION: NOT_RUN

CORRUPTION_CONTROLS_EXECUTED: FAIL
```

## Direction for p5_v8w

The next pass should close as much of the pairing type as the architecture forces.

It should not introduce another broad abstraction and stop.

The immediate task is to derive the weakest exact pairing interface, eliminate incompatible candidate types, and identify one precise remaining axiom if more than one type survives.

It must also repair the seed nonuniqueness theorem at the gauge-class level and replace the static controls with real mutations.
