# Audit Results: p5-b3-v4

## Verdict

```text
REVISE_SCOPE

AUTHORITY-FORCED PAIRING-FIRST ARCHITECTURE: ADOPT
DUALITY-MORPHISM INTERFACE AS CANDIDATE: ADOPT
EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED: ADOPT
EXACT PRIMARY PAIRING SEED: NOT YET DERIVED: ADOPT
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED: ADOPT
ONE-SIDED ORTHOGONALITY CONTROL: ADOPT
LOCAL B/Q DESCENDANTS AND i/4895: ADOPT

TYPE AMBIGUITY PROVED BY MODEL WITNESSES: WITHHOLD
PRIMARY_PAIRING_REALIZATION_AXIOM AS SMALLEST COMPLETE DATUM: REVISE
FIXED-TYPE RANK-ONE SEED UNIQUENESS: NARROW HYPOTHESES REQUIRED

p5-b3 BRANCH STATUS: OPEN
NEXT INTERACTION: p5-b3-v5
```

## Artifact verification

```text
Reported ZIP SHA-256:              PASS
Reported document SHA-256:         PASS
Manifest entries:                  55
Manifest coverage and hashes:      PASS
Notebook cells passing:            15/15
Figures:                           15
Clean rebuild with original root:  PASS
Byte-identical rebuilt ZIP:        PASS
Lean source:                       PRESENT, NOT COMPILED
```

The clean rebuild must preserve the original package-root folder name because that name is part of every ZIP member path. With that condition, the rebuilt archive is byte-identical.

## Adopted mathematical boundary

The package correctly establishes that the current authority forces a pairing-first architecture but does not fix a unique algebraic realization. It also correctly refuses to infer a Hermitian, bilinear, sesquilinear, quadratic, operator-valued, or diagonal complete pairing from downstream or provenance-only material.

The following survive unchanged:

- one retained generative `P_t` precedes charts and transfers;
- both chart restrictions and both directed transfers must descend from that one object;
- `B` and `Q` preserve architectural rank;
- `L` retains the old structure and appends one active axis;
- the meaning of primary-pairing orthogonality is still open;
- one-sided orthogonality does not force both mixed blocks to vanish;
- the local descendant laws are

  \[
  B:a\mapsto a\frac{u}{u+v},
  \qquad
  Q:a\mapsto ia;
  \]

- the first completed local descendant is

  \[
  a_{\mathrm{completed},0}=\frac{i}{4895}.
  \]

## Findings requiring revision

### 1. The claimed model witnesses are not complete models of the forced architecture

The document lists bilinear, sesquilinear, quadratic-with-polarization, and operator-valued examples and concludes:

```text
TYPE AMBIGUITY: PROVED BY MODEL WITNESSES
```

The supplied examples establish only local type alternatives. They do not instantiate all authority-forced clauses. In particular, they do not provide, for every primitive prefix:

- a carrier and rank;
- a complete `P_t`;
- exact `B/Q/L` structural maps;
- old-block retention under `L`;
- chart restrictions and directed transfers derived from the same `P_t`;
- exact-word compatibility.

The notebook’s type-witness cells merely name candidate families or compare rank-one formulas. They do not construct full models.

Correct status:

```text
MULTIPLE PAIRING TYPES NOT EXCLUDED BY CURRENT AUTHORITY: PROVED
TYPE INDEPENDENCE FROM CURRENT AUTHORITY: NOT YET PROVED
```

A genuine independence result requires two complete models satisfying the same authority signature while disagreeing on the disputed type property.

### 2. The proposed realization axiom conflates four different layers

The document calls a 23-field object the “smallest complete” `PRIMARY_PAIRING_REALIZATION_AXIOM`. But Fields 19–23 are not merely type data. They are the missing research results:

```text
B mutation law
Q mutation law
L mutation law
word compatibility
chart-interface compatibility
```

Ratifying those fields would assume the value recurrence and chart descent instead of deriving them.

The dependency must be split into:

```text
PRIMARY_PAIRING_BASE_REALIZATION
PRIMARY_PAIRING_SEED_AND_NORMALIZATION
PRIMARY_PAIRING_MUTATION_LAW
CHART_DESCENT_AND_TRANSFER_LAW
```

The first two may eventually require a canonical source or user ratification. The last two remain theorem targets and must not be silently moved into an axiom package.

The document also has not proved that its checklist is minimal. It is a useful dependency inventory, not a minimality theorem.

### 3. Fixed-type seed uniqueness needs exact algebraic hypotheses

The statement that every one-dimensional bilinear form has shape `alpha*x*y`, or every conjugate-sesquilinear form has shape `alpha*conjugate(x)*y`, requires more than “one-dimensional type.” It needs a declared free rank-one scalar module, a fixed basis, an appropriate commutative unital coefficient system or field, a scalar-valued pairing, and the stated variance convention.

Under those hypotheses, `P(e,e)=1` does force `alpha=1`. The notebook’s equation `alpha=1` checks the final coefficient equation; it does not prove the normal-form theorem.

Correct status:

```text
RANK-ONE SEED COEFFICIENT UNIQUENESS: CONDITIONAL ON EXPLICIT FREE-MODULE HYPOTHESES
```

### 4. The Lean surface is correctly bounded but weaker than the prose

The Lean source proves conditional hypotheses by returning those same hypotheses, gives the nonsymmetric matrix control, and interprets the first word. It does not formalize:

- the complete authority signature;
- two competing full authority models;
- a model-theoretic type-independence theorem;
- the claimed minimality of the proposed realization datum.

The package correctly reports that Lean was unavailable. No formal proof claim should be added.

## Correct disposition

```text
AUTHORITY/REALIZATION BOUNDARY: CLOSED
FULL MODEL-THEORETIC UNDERDETERMINATION: OPEN
STATIC REALIZATION DATUM: OPEN
COMPLETE SEED: OPEN
B/Q/L VALUE RECURRENCE: OPEN
CHART MAPS AND DIRECTED TRANSFERS: OPEN
HIGHER-ORDER DESCRIPTIVE L: OPEN

p5-b3 BRANCH STATUS: OPEN
```
