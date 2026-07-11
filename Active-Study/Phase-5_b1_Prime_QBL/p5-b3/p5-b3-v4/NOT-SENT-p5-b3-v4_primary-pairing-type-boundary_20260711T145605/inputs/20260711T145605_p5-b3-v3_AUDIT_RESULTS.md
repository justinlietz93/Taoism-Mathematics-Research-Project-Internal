# Audit Results: p5-b3-v3

## Verdict

```text
REVISE_SCOPE

EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED                ADOPT
EXACT PRIMARY PAIRING SEED: NOT YET DERIVED                ADOPT
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED          ADOPT
LOCAL B/Q ACTIVE-AXIS RECURRENCES: PROVED                  ADOPT
FIRST-DOMAIN ACTIVE WITNESS i/4895: PROVED                 ADOPT
CARRY INDEXING CORRECTION: PROVED                          ADOPT

MINIMAL DUALITY-MORPHISM INTERFACE: CANDIDATE, NOT FORCED
EARLIEST MISSING LAW = SCALAR_VARIANCE_AXIOM: REJECT
RAW SEED NONUNIQUENESS AS A SEPARATE THEOREM: WITHHOLD
TWO-SIDED ZERO MIXED BLOCKS AT L: CONDITIONAL ONLY

p5-b3 BRANCH STATUS: OPEN
NEXT INTERACTION: p5-b3-v4
```

## Package integrity

The reported archive SHA-256 and document SHA-256 are correct. All 49 manifest entries verify. The source and executed notebooks contain 14 code cells, and all 14 executed cells emit a PASS line and one figure. A clean rebuild performed under the original package-root basename reproduces the returned ZIP byte for byte.

## Findings

### 1. The hard stop is correct

The current authority gives primitive custody, the exact local active-axis shorthand, fixed architectural rank under `B` and `Q`, rank increase under `L`, and the dependency direction from the primary pairing to chart restrictions and directed transfers. It does not give enough value laws to recover a unique full `P_t`.

The following statuses are therefore sound:

```text
EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED
EXACT PRIMARY PAIRING SEED: NOT YET DERIVED
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
EXACT CHART MAPS: NOT YET DERIVED
EXACT DIRECTED TRANSFERS: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
```

### 2. `P_t : H_t -> D(H_t)` is a useful candidate interface, not a forced minimum

A scalar bilinear or sesquilinear pairing can be curried into a map from a carrier to a dual or anti-dual. This makes

\[
P_t:H_t\to D(H_t)
\]

a clean common interface for those two realizations.

The authority does not yet supply the assumptions needed to prove that every lawful primary pairing must have this form. In particular, it does not define:

- a scalar module or linear carrier;
- a scalar-valued codomain;
- additivity or linearity in either argument;
- a contravariant duality functor;
- a categorical biproduct;
- a polarization law if the primitive object is quadratic;
- an operator-valued pairing rule.

The contextual extract already proposed the duality-morphism interface. Repeating it does not convert it into a necessity theorem. The correct status is:

```text
DUALITY-MORPHISM INTERFACE: LAWFUL CANDIDATE REALIZATION
MINIMALITY / NECESSITY FROM CURRENT AUTHORITY: NOT YET DERIVED
```

### 3. Scalar variance is not the earliest missing law

“Ordinary versus conjugate scalar variance” is meaningful only after a scalar carrier, scalar action, involution or conjugation, codomain, and linearity convention have been fixed.

The package itself says the coefficient ring, concrete carrier, module-dimension identification, and exact pairing type are open. It therefore cannot place `SCALAR_VARIANCE_AXIOM` before those choices.

The earliest missing item is a broader datum, such as:

```text
PRIMARY_PAIRING_REALIZATION_AXIOM
```

It must define at least:

```text
carrier and scalar/coefficient system
pairing codomain
duality or adjoint operation
linearity/additivity and scalar variance
symmetry or adjoint law, if any
meaning of rank and orthogonality
```

Only inside a scalar realization does the ordinary-versus-conjugate variance fork become the next question.

### 4. The seed witness proves type ambiguity, not seed nonuniqueness within one type

The two examples

\[
P_{\mathrm{bil}}(x,y)=xy,
\qquad
P_{\mathrm{sesq}}(x,y)=\overline{x}y
\]

live under different scalar-variance types. Their agreement at `(1,1)` and disagreement at `(i,1)` proves that the local normalization does not choose the pairing type.

It does not provide two different seeds of one fixed type. On a fixed one-dimensional carrier with a fixed basis and normalization `P(e,e)=1`, either candidate type may have a unique rank-one seed.

The safe split is:

```text
FULLY TYPED SEED FROM CURRENT AUTHORITY: NOT YET DERIVED
TYPE AMBIGUITY UNDER LOCAL NORMALIZATION: PROVED
SEED NONUNIQUENESS AFTER TYPE IS FIXED: NOT YET PROVED
```

### 5. The two zero `L` mixed blocks are conditional

The authority says that `L` appends a new orthogonal active axis and retains the old pairing block. But the package leaves the pairing type and symmetry/adjoint law open.

Before those laws are fixed, “orthogonal” has no unique algebraic meaning. For a nonsymmetric bilinear pairing, left and right orthogonality can differ. One mixed block may vanish while the opposite block remains nonzero. Both zero blocks follow only from a two-sided `P`-orthogonal birth axiom or from a symmetry/Hermitian law plus one-sided orthogonality.

Therefore:

```text
L ARCHITECTURAL RANK EXTENSION: DERIVED
OLD RETAINED BLOCK PRESERVATION: DERIVED AT THE ARCHITECTURAL LEVEL
TWO-SIDED ZERO MIXED BIRTH BLOCKS: CONDITIONAL ON A PAIRING-ORTHOGONALITY AXIOM
EXACT L VALUE RECURRENCE: NOT YET DERIVED
```

The notebook correctly calls its matrix calculation “conditional,” but the research document later promotes the zero blocks to an unconditional result.

### 6. The accepted local scalar results are exact

With

\[
a_t=\frac{i^{\#_Q(W_t)}}{u_tv_t},
\]

the primitive updates give

\[
B:\quad a_{t+1}=a_t\frac{u}{u+v},
\qquad
Q:\quad a_{t+1}=ia_t.
\]

Replaying

```text
B Q Q B B B Q B Q B B Q B B L
```

reaches `(u,v)=(55,89)`, five quarter turns, and

\[
a_{\mathrm{completed},0}=\frac{i}{4895}.
\]

These are local descendants. They do not determine the full primary pairing.

### 7. Several PASS cells encode assumptions rather than test them

Notebook cells 3, 5, 8, 10, and 14 do not independently establish the corresponding authority-level claims:

- Cell 3 assigns Boolean values to the proposed interface requirements and then checks that they are all true.
- Cell 5 lists unfixed data and counts the list.
- Cells 8 and 14 construct block matrices with or without zero mixed entries after assuming a particular orthogonality interpretation.
- Cell 10 inserts a free mixed coefficient but does not show that both resulting matrices arise from lawful mutations.

These cells are useful illustrations. Their labels should be `CONDITIONAL CHECK` or `MODEL WITNESS`, not theorem-level PASS results.

### 8. The Lean file is an interface encoding, not a formal derivation

The Lean source defines structures whose Boolean fields are set to `true` and proves the fields are `true` by reduction. It also defines the endpoint witness directly as `(0,1,4895)`.

That accurately records intended data, but it does not derive block orthogonality or the active endpoint from the primitive law. The existing boundary remains correct:

```text
LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
```

The next version should call these declarations and conditional lemmas, not a formal theorem surface proving the missing pairing facts.
