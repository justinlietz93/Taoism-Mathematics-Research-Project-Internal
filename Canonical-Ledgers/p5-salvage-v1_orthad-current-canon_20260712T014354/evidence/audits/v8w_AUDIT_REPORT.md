# p5_v8w Audit Report

## Verdict

```text
REVISE

PAIRING_FIRST_REALIGNMENT: ADOPT
PRIMITIVE_BASELINE: ADOPT
DOWNSTREAM_HARD_STOP: ADOPT
Xi_hat_t SCHEMA BOUNDARY: ADOPT
REAL CORRUPTION CONTROLS: ADOPT
PACKAGE INTEGRITY: ADOPT

MINIMAL_PAIRING_INTERFACE AS DERIVED: REJECT
SCALAR_VARIANCE AS EARLIEST AXIOM: REJECT
L MIXED BIRTH BLOCKS ZERO: REJECT
L PAIRING-RANK LAW AS DERIVED: REJECT
SURVIVING TYPE FORK AS EXHAUSTIVE: REVISE
PAIRING MUTATION TYPE SIGNATURES: REVISE
```

The package is a meaningful advance. It keeps the pairing first, treats the fixed `Z/12Z` successor as downstream, and leaves all Orthad values uninstantiated. Its verification repairs are real.

The central type claim still imports more structure than the primary law provides.

## Reproduced package results

```text
ZIP SHA-256:      73ffcb90075eac0b257f975c9fe4858a36658bd34737f7b96b7970739ceaa251
Document SHA-256: 3c7e7deb5723ba17cdd1a7aa8e529f4e169101bb60c11f2acaf1dd878bb9cc01
Verifier:          22/22 passed
Pytest:            7 passed
Controls runner:   exit 0
Manifest entries:  63
ZIP files:         64 including MANIFEST.json
```

The response hashes match the supplied archive and document.

The accepted primitive trace remains unchanged:

```text
BQQBBBQBQBBQBBL
floor pair (55,89)
floor product 4895
five Q steps
phase witness i
first-L carry preserved
first next-domain pair (89,144)
```

## Adopted findings

### A1. The pairing-first realignment holds

The package preserves the required order:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

It emits no chart, transfer, projection, gauge, FQM, or Weil values.

### A2. The local scalar remains local

`i/4895` remains a local active-axis shorthand. It is not promoted to a pairing or chart entry.

### A3. The controls are now real

Each packaged control copies the package, performs a mutation, regenerates the manifest, runs the actual verifier, and requires the named semantic gate to fail.

### A4. The lifted-state boundary is correct

The package emits `lifted_state_schema`, not `Xi_hat_t`, while the pairing, charts, and transfers are null.

## Defects

### F1. `P_t:H_t->D(H_t)` is a candidate representation, not a source-derived minimum

The primary law gives the intended pullback shapes

```text
iota_a* P_t iota_b
```

and the schematic gauge shape

```text
P -> U* P U.
```

It does not define a contravariant duality functor `D`, an additive category, representability, or currying.

A two-slot pairing can admit pullback in both arguments without first being represented as a morphism `H_t->D(H_t)`. The package therefore proves that the duality-morphism model is sufficient. It does not prove that this model is forced or weakest.

Corrected status:

```text
DUALITY_MORPHISM_MODEL:
    ADMISSIBLE CANDIDATE FORMALIZATION

MINIMAL SOURCE-FORCED PAIRING INTERFACE:
    NOT_YET_DERIVED

EARLIEST MISSING AXIOM:
    PAIRING REPRESENTABILITY / DUALITY AXIOM
```

### F2. Scalar variance cannot be the earliest axiom yet

The proposed scalar-variance axiom uses:

```text
lambda
scalar multiplication
an involution lambda*
a coefficient object
```

None of these has been derived at the clean pairing layer.

The package itself lists the coefficient ring or field as a later choice. It cannot then name ordinary-versus-conjugate scalar action as the first unresolved axiom.

Scalar variance becomes meaningful only after a scalar realization or a star-coefficient object is licensed.

### F3. The zero mixed birth blocks are unearned

The primary law says that `L` appends one new orthogonal active axis. It does not say `two-sided orthogonality`.

The package silently strengthens the source phrase and concludes:

```text
P_(t+1) = block_diag(P_t,p_new).
```

That conclusion fails for a non-symmetric pairing under one-sided orthogonality. For example, with old axis `e1`, new axis `e2`, and matrix

```text
[1 1]
[0 1]
```

`P(e2,e1)=0` but `P(e1,e2)=1`. One mixed block vanishes and the other does not.

Both mixed blocks are zero only after one of these is derived:

```text
two-sided orthogonality
symmetry or Hermitianity plus one-sided orthogonality
an explicit zero-coupling birth law
```

The Lean theorem assumes both mixed blocks are zero. It does not derive that assumption from the architecture.

### F4. Pairing rank is still untyped

The candidate interface is an arbitrary morphism in an additive category. Such a category need not carry a numerical rank.

The package also leaves `p_new` open. If `p_new=0`, block size increases while matrix rank need not increase.

The current source statement `pairing rank increases by one` therefore requires a precise resolution:

```text
rank of the argument object
rank of the pairing morphism
matrix size
architectural axis-block count
```

These are not interchangeable.

Corrected status:

```text
FIRST-L STRUCTURAL AXIS EXTENSION: ADOPT
FIRST-L PAIRING RANK +1: NOT_YET_TYPED
L MIXED BIRTH BLOCKS: NOT_YET_DERIVED
```

### F5. The reported type fork is not exhaustive

The ordinary-dual versus conjugate-dual fork exists only inside the chosen representable scalar model.

The source audit has not eliminated:

```text
nonrepresentable two-slot pairings
duality-valued pairings without a scalar realization
bilinear forms with no symmetry law
sesquilinear forms with no self-adjointness law
left/right-duality variants
```

The package may report the fork as a candidate realization fork. It may not report it as the earliest source-level fork.

### F6. The mutation signatures contain underived inputs

The `Q` signature introduces `J_active`, although the clean law only requires a quarter-turn mutation of active pairing data. The exact carrier of that action is open.

The `L` signature imports a biproduct, two-sided orthogonality, and zero mixed maps.

Corrected status:

```text
B PAIRING MUTATION SHAPE: SAME-OBJECT SCHEMA SUPPORTED
Q PAIRING MUTATION TYPE: NOT_YET_DERIVED
L ARGUMENT-OBJECT EXTENSION SCHEMA: SUPPORTED
L PAIRING MUTATION TYPE: NOT_YET_DERIVED
```

### F7. The seed quotient is also a candidate

The proposed map

```text
eta_P:(Xi_0,W_0)->Pair(H_0,D(H_0))/Aut(H_0)
```

assumes that every automorphism of `H_0` is an admissible gauge transformation. The source only says a lawful basis change may act by `U*PU`.

The gauge subgroup and admissibility law remain open.

### F8. The verifier is not cleanly repeatable

On a fresh extraction, the verifier passes all 22 gates. It checks for cache files before running pytest. Pytest then creates `.pytest_cache`.

The archive is clean at seal time, but the verifier mutates its target and a second run can fail the cache gate. Run pytest with the cache provider disabled or verify in a disposable copy.

### F9. The elimination verifier checks table consistency, not the mathematical elimination

The verifier recomputes each verdict from capability booleans stored in the same CSV. It does not derive those booleans from source formulas.

This is a consistency check. It is not an independent certificate that the candidate list is complete or that the source forces the stated capabilities.

## Corrected status boundary

```text
PAIRING_FIRST_REALIGNMENT: PASS
PRIMITIVE_BASELINE: PASS
REAL_CORRUPTION_CONTROLS: PASS
Xi_hat_t VALUES: NOT_INSTANTIATED

MINIMAL SOURCE-FORCED PAIRING INTERFACE: NOT_YET_DERIVED
DUALITY_MORPHISM MODEL: ADMISSIBLE CANDIDATE
PAIRING REPRESENTABILITY: NOT_YET_DERIVED
SCALAR REALIZATION: NOT_YET_DERIVED
SCALAR VARIANCE: PREMATURE

FIRST-L STRUCTURAL AXIS EXTENSION: PASS
FIRST-L MIXED BIRTH BLOCKS: NOT_YET_DERIVED
FIRST-L PAIRING RANK +1: NOT_YET_TYPED

EXACT PRIMARY PAIRING TYPE: NOT_YET_DERIVED
EXACT PRIMARY PAIRING SEED: NOT_YET_DERIVED
B PAIRING VALUE RECURRENCE: NOT_YET_DERIVED
Q PAIRING TYPE AND RECURRENCE: NOT_YET_DERIVED
L PAIRING TYPE AND RECURRENCE: NOT_YET_DERIVED

CHART MAPS: NOT_YET_DERIVED
DIRECTED TRANSFERS: NOT_YET_DERIVED
TERMINAL PROJECTION: NOT_RUN
```

## Direction for p5_v8x

The next pass should settle two questions before returning to seed values:

1. Does the source force a representable duality morphism, or only a two-slot pullbackable pairing object?
2. What does `new orthogonal axis` mean before symmetry, scalar variance, and pairing rank are defined?

The task must isolate one precise missing axiom at each fork. It must not promote a convenient categorical model into canon.
