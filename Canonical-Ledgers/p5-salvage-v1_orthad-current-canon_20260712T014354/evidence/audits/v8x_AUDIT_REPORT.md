# p5_v8x Audit Report

## Verdict

```text
REVISE

PAIRING_FIRST_REALIGNMENT: ADOPT
PRIMITIVE_BASELINE: ADOPT
REPRESENTABILITY_HARD_STOP: ADOPT
FIRST-L MIXED-BLOCK HARD STOP: ADOPT
PAIRING-RANK HARD STOP: ADOPT
REAL CORRUPTION CONTROLS: ADOPT
TREE IMMUTABILITY: ADOPT
PACKAGE INTEGRITY: ADOPT

SOURCE_FORCED_PAIRING_INTERFACE: REVISE
GENERAL Pair(-,-) BIFUNCTOR: REJECT_AS_DERIVED
FIRST-L BLOCK MATRIX SCHEMA: REVISE
SCALAR_VARIANCE_STATUS: REVISE
SOURCE-BINDING VERIFIER: FAIL
NOTEBOOK_SOURCE CERTIFICATE: FAIL
```

## Reproduced package claims

The supplied ZIP and research-document hashes match the response:

```text
ZIP:
6689e6b39d200cfc4fd4f181b85ccda588ce1333665da597f3e48f36e505ef36

document:
417a48354d3a004bf7fd77b8746d0cd2b422380f4177855bfae2338ac04f9885
```

A clean extraction reproduced:

```text
full verifier:            15/15 gates passed
pytest:                   14/14 passed
real corruption controls: 6/6 fired
manifest/archive paths:   exact match
cache or bytecode:        0
verified-tree mutations:  0
```

The primitive baseline remains accepted:

```text
word:                    BQQBBBQBQBBQBBL
floor pair:              (55,89)
floor product:           4895
Q count:                 5
phase witness:           i
after first L:           A=1, pair=(55,89), k=0, j=7
first next-domain pair:  (89,144)
```

## Adopted findings

### A1. Representability is not derived

The package correctly rejects promotion of the primary pairing to

```text
P_t : H_t -> D(H_t)
```

without a representing-dual construction.

### A2. One-sided orthogonality does not force both mixed terms to vanish

The matrix

```text
[[1,1],
 [0,1]]
```

is a valid counterexample in a nonsymmetric bilinear matrix model.

It establishes that the word `orthogonal` must be typed before either mixed term is set to zero.

### A3. Appending one axis does not prove algebraic rank +1

The extension `diag(1,0)` has block size two and algebraic rank one.

This correctly separates:

```text
architectural axis count
argument-object dimension
matrix size
pairing rank
nondegenerate rank
```

### A4. The verifier controls are now real

Each packaged control copies the tree, mutates an artifact, regenerates the manifest, runs the actual verifier, and requires the intended gate to fail.

The full verifier also leaves the checked tree unchanged.

## Findings requiring revision

### F1. The claimed source-forced interface imports a global bifunctor

The source only gives four specific intended descendant expressions:

```text
iota_plus*  P iota_plus
iota_minus* P iota_minus
iota_minus* P iota_plus
iota_plus*  P iota_minus
```

The package promotes this to:

```text
objects A,B in a class C
Pair(A,B)
(f,g)^*: Pair(A,B) -> Pair(A',B')
identity and composition in both slots
```

Those category-wide objects and functorial laws are not stated in the authority.

They are a useful candidate formalization, but they are not yet source-derived.

Corrected status:

```text
SPECIFIC FOUR RESTRICTION/TRANSFER OBLIGATIONS:
    ARCHITECTURAL LAW

GENERAL TWO-SLOT Pair(-,-) PULLBACK SYSTEM:
    ADMISSIBLE CANDIDATE

SOURCE_FORCED PAIRING TYPE:
    NOT_YET_DERIVED
```

### F2. The star symbol is redefined without authority

The package states that `*` means first-slot pullback at this layer.

The written source leaves `*` unresolved. Across the architecture it appears in:

```text
iota* P iota
P -> U* P U
C_t*
historical H=M+iJ
```

It may encode a dual pullback, transpose, adjoint, conjugate transpose, or another involutive operation.

Replacing it with an abstract pullback operation prevents overclaim, but it does not derive the meaning of the source glyph.

### F3. The first-L block matrix is still representation-dependent

The package calls

```text
[[P_t, C_right],
 [C_left, p_new]]
```

the strongest licensed schema.

A literal block matrix requires an additive decomposition or represented matrix model. The package has not derived either.

The source currently forces only these structural obligations:

```text
old pairing content is retained
one new active axis is appended
old/new and new/old relations must be determined
the newborn self-relation must be determined
```

The block display is a candidate presentation of those obligations.

### F4. Scalar/star semantics are not merely downstream

Ordinary-versus-conjugate scalar variance is premature, but the current type problem already contains:

```text
the quarter-turn witness i
the repeated star glyph
the phrase orthogonal axis
historical H=M+iJ
```

The next type step must determine whether `i` is:

```text
a scalar
a complex-structure operator J with J^2=-1
an orientation action
a local descendant label
```

and whether one star law coherently explains restriction, gauge re-expression, and the first-L mixed relation.

Corrected status:

```text
ORDINARY VS CONJUGATE SCALAR VARIANCE:
    PREMATURE

STAR AND QUARTER-TURN SEMANTICS:
    CURRENT TYPE FORK
```

### F5. The source verifier does not bind ledger rows to source text

The verifier checks that each source path exists. It then trusts the formulas copied into the CSV ledger.

It does not verify that the cited section contains the claimed formula.

A direct attack replaced the primary law with:

```text
# CORRUPTED
No pairing, no chart, no transfer statements.
```

After regenerating the manifest, the verifier still returned PASS with 14/14 non-control gates.

Therefore:

```text
SOURCE LEDGER SHAPE: PASS
SOURCE EXCERPT BINDING: FAIL
SOURCE-DERIVED GATES: NOT INDEPENDENTLY CERTIFIED
```

### F6. The notebook source claims are self-seeded

Examples include:

```python
required = {...}
observed = {...}
```

and:

```python
source_states_dual = False
source_states_natural_iso = False
```

The claim cells do not contain or test the governing excerpts. They reproduce the package conclusions as constants.

The matrix counterexamples are computational. The source-type claims are not.

### F7. The abstract evidence classification is too broad

The one-sided-orthogonality and zero-birth results are explicit finite matrix-model counterexamples.

They are valid falsifiers of unconditional claims.

They do not derive the type of the actual Orthad pairing.

Report them as:

```text
CERTIFIED IN AN ADMISSIBLE MATRIX MODEL
```

rather than as a proof of the source-level pairing interface.

## Corrected status boundary

```text
PAIRING_FIRST_REALIGNMENT: PASS
PRIMITIVE_BASELINE: PASS

SPECIFIC CHART/TRANSFER DESCENT OBLIGATIONS:
    ARCHITECTURAL LAW

GENERAL Pair(-,-) PULLBACK SYSTEM:
    ADMISSIBLE CANDIDATE

PAIRING REPRESENTABILITY:
    NOT_YET_DERIVED

STAR SEMANTICS:
    NOT_YET_DERIVED

Q QUARTER-TURN ACTION TYPE:
    NOT_YET_DERIVED

FIRST-L OLD/NEW RELATION:
    NOT_YET_DERIVED

FIRST-L NEW/OLD RELATION:
    NOT_YET_DERIVED

FIRST-L NEWBORN SELF-RELATION:
    NOT_YET_DERIVED

PAIRING RANK LAW:
    NOT_YET_TYPED

EXACT PRIMARY PAIRING TYPE:
    NOT_YET_DERIVED

EXACT PRIMARY PAIRING SEED:
    NOT_YET_DERIVED

Xi_hat_t VALUES:
    NOT_INSTANTIATED

SOURCE EXCERPT BINDING:
    FAIL

REAL CORRUPTION CONTROLS:
    PASS

TERMINAL PROJECTION:
    NOT_RUN
```

## Direction for p5_v8y

The next pass should stop adding generic category structure.

It should determine the concrete compatibility constraints imposed by the repeated `*`, the quarter-turn witness `i`, the word `orthogonal`, the local scalar shorthand, and the historical `H=M+iJ` construction.

The goal is one exact surviving type fork or one exact missing axiom.

The pass must also bind every source-ledger row to the actual source bytes and add a control that corrupts the primary law.
