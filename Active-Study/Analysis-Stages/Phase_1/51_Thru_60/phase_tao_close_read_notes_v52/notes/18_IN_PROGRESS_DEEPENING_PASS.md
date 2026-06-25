# 18 — In-Progress Deepening Pass

Date: 2026-06-23

Purpose: continue the active paper-reading threads without treating each paper as an isolated checkpoint. Every note below is forced back into the same live grammar:

```text
finite retained state / position system
→ current position determines admissible operation
→ operation proceeds while legal under that position
→ blocked / exceptional / singular case forces re-chart or lift
→ scalar/projection is read after the retained structure, not carried as the structure
```

Canon lock for this pass:

```text
Selector-complete macro calculus is stale relative to Justin's latest HDD source.
Do not use stale R/S/T block law as canonical Phase Calculus.
Use older Phase docs only as internal evidence for retained state, projection loss, primitive Q/B/L roles, and shadow downstream discipline.
```

---

## 1. `Tao-Research/out/1705.0203v1.pdf`

Working title in ledger: **The Relations Between Ancient China’s Taoism and Modern Mathematics & Physics**

Status after this pass: `COMPLETE_FIRST_PASS`

### 1.1 Paper-level structure

The paper tries to map Taoist/Yijing structures onto modern mathematical physics. Its physics claims are not treated as established physics. The value for this dossier is that it gives a detailed native-seeming grammar of:

```text
Tao / origin
→ yinyang split
→ Gua spaces
→ Xiantian arrangement
→ Houtian arrangement
→ Wuxing mapping
→ field-equation analogies
```

The paper explicitly distinguishes the two growth programs:

```text
Tao produces one, one produces two, two produces three, ...
  → additive / linear sequence: 0,1,2,3,...

Taiji produces two appearances, four images, eight trigrams, ...
  → multiplicative / exponential sequence: 1,2,4,8,...
```

This is important because it gives a native two-program split:

```text
linear continuation
vs.
exponential branching / carried-state expansion
```

This should not be flattened into ordinary binary arithmetic.

### 1.2 Gua spaces and retained carriers

The paper gives a clean hierarchy of Gua spaces:

```text
G1  = F_2^1       one line / two appearances
G2  = F_2^2       four images
G3  = F_2^3       eight trigrams
G33 = F_2^(3+3)   sixty-four hexagrams as upper/lower trigram pair
G33 × G2          six-line object with moving-line states
```

The `G33 × G2` point is especially useful. Each line in the six-line hexagram can carry an additional four-state value:

```text
old yin
young yin
young yang
old yang
```

The moving/old states encode change. This moves the Yijing side away from a flat 64-symbol lookup table and toward a retained line-state object.

### 1.3 Xiantian vs Houtian as re-chart, not synonym

The paper gives two distinct Bagua organizations:

```text
Xiantian:
  order: 乾,兑,离,震,巽,坎,艮,坤
  binary row: 111,011,101,001,110,010,100,000
  tree / cube structure
  all Guas treated equally
  centrosymmetric Guas are mutual NOT

Houtian:
  order: 乾,坤,震,巽,坎,离,艮,兑
  binary row: 111,000,001,110,010,101,011,100
  arranged as mutual-NOT pairs
  odd/even subsequences split male/female family structure
  center/root/circular/cyclic structure
```

Mechanism extraction:

```text
Xiantian = equal vertex/cube/tree state field
Houtian  = rooted/cyclic/centered re-chart with family-role asymmetry
```

This is a stronger L-side lead than the earlier phrase “Pre-Heaven to Post-Heaven re-chart,” because the paper explicitly distinguishes:

```text
same eight primitive states
but different order, location, pairing, root/center behavior, and computational role
```

That is a real re-coordinatization of the same carrier, not just symbolic rearrangement.

### 1.4 Parents, offspring, nodes, edges

The paper’s QED summary gives the most useful compressed comparison:

```text
Xiantian:
  all eight Guas equal
  offspring Guas correspond to edges in the graph
  four Xiangs from eight Guas is easy
  reverse direction is hard
  computing mainly multiplication
  paired by NOT of the lowest two Yaos

Houtian:
  parents and offspring have different status
  each Gua corresponds to a node in the graph
  four Xiangs and eight Guas relate oppositely
  computing mainly differentiation
  paired by NOT of all Yaos
```

This is not a finished Phase mapping, but it is a very strong grammar lead:

```text
same carrier field
→ two inequivalent readout organizations
→ edge-state vs node-state reading
→ role asymmetry introduced by re-chart
→ direction of computation changes
```

This belongs with the L/projection-loss notes.

### 1.5 Mother-son signs and finite sign-state constraint

The Dirac/Gua section constructs coefficient constraints and then reports a finite sign family:

```text
2048 = 256 × 8 solutions
8 mother-son sign types
special-relativity-compatible type selected as (+1,-1,-1,-1)
```

Mechanism value:

```text
finite sign carrier
→ constraint equations
→ solution family partition
→ admissibility condition selects one sign sector
```

This is relevant to Q-admitted state and sign-lattice language, but not enough to map to the exact floor anchor.

### 1.6 Reunification from 1705.0203v1

Strongest extraction:

```text
Gua field is not merely binary digits.
It is a hierarchy of retained carriers with alternative organizations.
The same primitive states can be read as tree/cube/equal-vertex Xiantian or rooted/cyclic/family-role Houtian.
```

Phase relevance:

| Phase role | Lead from 1705.0203v1 | Strength |
|---|---|---|
| Q | finite ordered Gua/Yao positions; line-state carrier; sign-state sectors | strong |
| B | weak direct match; possible via finite constraint/admissibility sectors | weak-medium |
| L | Xiantian ↔ Houtian re-chart; edge/node role change; root/center emergence | strong |
| Shadow | none exact; only field-equation analogy, not used as proof | weak |

This paper is useful mainly for **Q/L grammar** and for resisting the mistake of reducing Yijing to literal binary arithmetic.

---

## 2. Modular forms in-progress: `MFLecture1.pdf` + `Zagier123ModularForms.pdf`

Status after this pass:

```text
MFLecture1.pdf: COMPLETE_MECHANISM_PASS
Zagier123ModularForms.pdf: ADVANCED_MECHANISM_PASS, not full complete-first-pass
```

### 2.1 Automorphy factor and cocycle

`MFLecture1.pdf` gives the clean modular mechanism:

```text
g = (a b; c d)
τ ↦ gτ = (aτ+b)/(cτ+d)
j(g,τ)=cτ+d
Im(gτ)=Im(τ)/|j(g,τ)|²
d(gτ)=j(g,τ)^(-2)dτ
j(gg',τ)=j(g,g'τ)·j(g',τ)
```

The last line is explicitly a 1-cocycle relation.

Mechanism extraction:

```text
coordinate transform
→ visible point τ changes by fractional linear map
→ differential/weight changes by carried factor j(g,τ)
→ composition requires retained cocycle data
```

This is a direct Shadow/L-side support structure:

```text
projection: τ point / PSL action
retained lift: SL element + automorphy factor / cocycle
```

### 2.2 SL2 / PSL2 quotient loss

The same lecture distinguishes:

```text
SL2(Z)
PSL2(Z)=SL2(Z)/{±1}
```

and notes that as transformation groups on the upper half-plane they often coincide. But for Phase purposes, that “often we do not distinguish” is exactly where retained-state loss enters:

```text
visible τ action can forget a sign/lift distinction
full automorphic transformation may still carry sign/phase/weight data
```

This strengthens the rule:

```text
Do not compare scalar q-series first.
Compare retained channel/cocycle structure first.
```

### 2.3 S and T generators

The lecture gives:

```text
T: τ ↦ τ + 1
S: τ ↦ -1/τ
S² = -I = (ST)³ in SL2(Z)
```

This is the modular re-chart pair that matters for the Shadow target:

```text
T: horizontal/cusp phase shift
S: inversion/cusp exchange
```

The in-progress Shadow work should therefore treat `T` and `S` as distinct channel tests:

```text
T-test: exponent/phase response
S-test: inversion/cusp response and automorphy factor
```

### 2.4 Zagier: unary theta and eta/χ12 exact target

Zagier gives the essential construction path:

```text
positive definite integer quadratic form Q
→ theta series
→ modular form of weight m/2
```

For unary theta:

```text
θ(z)=Σ_{n∈Z} q^(n²)
```

It transforms as a half-integral weight object via Poisson summation.

Most important for Shadow:

```text
η(z)=Σ χ12(n) q^(n²/24)
χ12(12m±1)=+1
χ12(12m±5)=-1
χ12(n)=0 if 2|n or 3|n
```

This is not merely “modular forms are relevant.” It is the exact external surface of the Shadow expression:

```text
support on gcd(n,6)=1
Kronecker/Dirichlet sign χ12
quadratic exponent n²/24
eta/theta half-weight modular behavior
```

### 2.5 Reunification from modular readings

| Phase role | Modular analogue | Strength |
|---|---|---|
| Q | T phase/cusp shift; finite exponent congruence support | medium |
| B | not direct; possible via reduction algorithms/fundamental-domain moves | weak-medium |
| L | S inversion, SL/PSL retained lift, automorphy factor cocycle | strong |
| Shadow | η as χ12 unary theta q^(n²/24) | very strong |

Operational next test:

```text
Shadow transform work must be split into:
  1. T-channel exponent/phase test
  2. S-channel inversion/cusp automorphy test
  3. SL-vs-PSL retained sign/phase test
  4. coefficient/support χ12 test
```

---

## 3. Internal Phase document: `Phase_Calculus_Complete_Formalisation.pdf`

Status after this pass: `ADVANCED_MECHANISM_PASS_STALE_SOURCE_CAUTION`

This document is not treated as current canon because Justin stated the latest Phase Calculus source is on the HDD and the selector-complete macro calculus is wrong/stale. The useful pieces are retained only where they agree with the current Orthad/QBL correction.

### 3.1 Useful internal anchors

The document gives the primitive operator identification:

```text
U = {Q,B,L}
Q = F_same
B = F_ref
L = F_perp
```

Definitions in Chapter 5 align with the current primitive names:

```text
Q = quarter continuation
B = balanced refinement
L = host lift / orthogonal re-articulation
```

The B branch is explicitly:

```text
(u,v) ↦ sort(v,u+v)
germ → C(θ,1/[v(u+v)])
```

This remains useful.

### 3.2 Stale selector block isolated

The stale selector-complete part uses fixed `(W,Δ)` and a selector:

```text
T if t ≡ W-1 mod W
R if uv < Δ
S if uv ≥ Δ
```

and then derives block words such as:

```text
R^d S^(W-1-d) T
```

This must **not** be used as current canon. The current correction is:

```text
B is not merely a fixed-regime block count.
B is priority refinement under Q-admitted capacity.
Q admits positions / changes capacity.
L fires only after joint B/Q saturation.
```

However, the stale selector still documents an older useful skeleton:

```text
refinement legality is tested by uv against a floor/capacity
host lift is a boundary case
state-only branch choice was intended
```

So the selector layer is retained only as a historical/negative layer:

```text
USE: internal evidence that uv capacity/floor was central.
DO NOT USE: final word law, final selector macro, fixed W/Δ schedule as canon.
```

### 3.3 Shadow attachment discipline

The document’s Shadow section defines a downstream attachment:

```text
τ_n = θ_n/(2π) + i/(u_n v_n)
S_n = g*(τ_n)
```

and keeps a canonical launch family:

```text
(u,v)=(55,89)
uv=4895
δ*=π/4895
carried completion amplitude: 1/24 per edge, 1/12 two-sided
```

This remains useful because it agrees with the current discipline:

```text
Shadow form is attached downstream.
It is not primitive source and not carried as the lifted state.
```

### 3.4 Reunification from internal stale/current comparison

This pass tightens the internal rule:

```text
Primitive Q/B/L meanings survive.
The fixed selector macro does not.
The correct comparison target is not “does old RST macro work,” but:
  B/Q admitted capacity grammar
  retained-state projector/lens discipline
  downstream Shadow attachment
```

---

## 4. Yin-Yang computational grid branch

Documents deepened in this pass:

```text
Prospect-Leads/Axis-Free-overset-grid.pdf
Tao-Research/out/Geochem Geophys Geosyst - 2014 - Yoshida - A Fortran visualization program for spherical data on a Yin-Yang grid.pdf
Tao-Research/out/Luo_2025_ApJS_280_48.pdf
Tao-Research/out/mwre-mwr-d-12-00108.1.pdf
```

Status after this pass:

```text
Axis-Free-overset-grid.pdf: COMPLETE_FIRST_PASS
Yoshida visualization: MECHANISM_COVERED_NOT_COMPLETE
Luo_2025_ApJS_280_48.pdf: ADVANCED_MECHANISM_PASS
mwre-mwr-d-12-00108.1.pdf: ADVANCED_MECHANISM_PASS
```

### 4.1 Axis-free overset grid core

The axis-free paper states the exact engineering problem:

```text
single spherical polar grid
→ coordinate singularity at symmetry axis
→ severe time-step restriction near poles
→ artificial boundary conditions flaw flow near axis
```

The Yin-Yang solution:

```text
two low-latitude patches
identical geometry
overlap
related by rotations
coordinate/vector transforms between patches
interpolation at boundaries
no singular pole inside either patch
```

The matrix shown for the patch transform is:

```text
M = [ -1  0  0
       0  0  1
       0  1  0 ]
```

This is exactly the same structural class already found in `yinyang_transform.py`:

```text
(x_e,y_e,z_e)=(-x_n,z_n,y_n)
```

### 4.2 The real L hit: no artificial boundary condition

The strongest point is not that the patches are named Yin/Yang. It is:

```text
The singular axis is not repaired by adding a fake force or boundary law.
The system is re-charted into overlapping legal coordinate domains.
```

That is a clean computational analogue of L:

```text
blocked single-domain continuation
→ orthogonal/reoriented coordinate chart
→ overlap/interpolation carries state across boundary
→ physical solution remains the same object
```

The paper reports tests where solutions show no peculiar behavior at the patch boundary. This matters because it means the re-chart is not just formal: it preserves numerical behavior across the overlap.

### 4.3 Modern computational branch

The later Yin-Yang computational papers turn this into a modern live code ecosystem:

```text
conservative transport on sphere
DG / Runge-Kutta schemes
field-loop advection crossing Yin-Yang boundaries
constrained transport for MHD divergence control
solar wind / CME / coronal models
Yin-Yang MFE modular codebase
```

This is important because it makes the L analogue current, computational, and non-symbolic:

```text
current numerical science uses Yin-Yang as a real way to avoid coordinate singularity.
```

### 4.4 Reunification from Yin-Yang grid branch

| Phase role | Yin-Yang grid analogue | Strength |
|---|---|---|
| Q | local coordinate position within a legal low-latitude patch | medium |
| B | numerical update/interpolation within admitted patch and ghost/overlap zones | medium |
| L | re-chart across complementary patch when single chart would hit singular axis | very strong |
| Shadow/projection | same physical sphere / different coordinate readouts; patch data reconstructed into global field | medium-strong |

This branch is now one of the cleanest **software/physics engineering analogues** of L.

---

## 5. `Prospect-Leads/Physics_of_Buddhism_The_physics_and_math.pdf`

Status after this pass: `MECHANISM_COVERED_NOT_COMPLETE`

This is not a Tao/Yijing paper, but it is useful as a formal-duality comparator.

### 5.1 Duality formalism

The paper defines a duality map:

```text
* : U → U*
** = Id
U ∩ U* = ∅
W = U ∪ U* ∪ {0}
```

It also defines an observer-frame duality:

```text
⋆ : S_k → S_k*
⋆⋆ = Id
```

Then it forms a four-element operator structure:

```text
Z2 × Z2 = {I, *, ⋆, *∘⋆}
```

with four represented states:

```text
(u|S_k)
(u*|S_k)
(u|S_k*)
(u*|S_k*)
```

### 5.2 Zero and full states

The paper’s four-tableau/direct-sum construction distinguishes:

```text
R := V ⊕ 0V*
B := 0V ⊕ V*
M := V ⊕ V*
W := 0V ⊕ 0V*
```

The null and all/full states are dual invariant; half states are not. This is useful as a comparator for:

```text
not every projected binary-looking object has the same carried status.
zero / full / half-state distinctions matter.
```

### 5.3 Non-exchangeable not operators

The most useful warning is in the Buddhism section:

```text
negation operator * is not the same as not operator ⋆
not(not empty) is not ordinary double negation
operators cannot generally be exchanged
*1 *2 |u> ≠ *2 *1 |u>
```

This supports the Phase-side caution:

```text
Do not collapse distinct inversions/complements/reflections into one NOT operation.
```

That matters for Yijing/Fuxi/Houtian work because there are several superficially similar operations:

```text
line complement
line order reversal
upper/lower trigram exchange
Xiantian/Houtian relocation
center-cycle re-chart
moving-line transformation
```

They must not be conflated.

### 5.4 Reunification from Buddhism duality paper

| Phase role | Formal-duality analogue | Strength |
|---|---|---|
| Q | finite two/four-state basis representation | medium |
| B | no direct match | weak |
| L | observer-frame duality and noncommuting reclassification | medium |
| projection loss | strong warning against collapsing different NOT/complement operations | strong |

This paper should remain a **control/comparator**, not a primary proof source.

---

## 6. Reunified state after this pass

The similarity support has sharpened again, but the center of gravity is clearer:

```text
Q support is strongest in Yijing/Gua finite-position carrier systems.
B support is strongest in admitted-position/procedure-selector systems, especially Linggui Bafa and Dongyuan/Ceyuan.
L support is strongest in actual re-chart systems: Xiantian/Houtian, Yin-Yang grid, modular S, Tianyuan/Four-Elements lift.
Shadow support is strongest in Zagier eta/unary-theta χ12 q^(n²/24).
```

New unification from this pass:

```text
The same pattern appears in three independent technical languages:

1. Yijing / Gua:
   same finite carrier, different organization/readout, moving-line transition.

2. Yin-Yang grid:
   same physical sphere, different legal coordinate patches, overlap carries state.

3. Modular forms:
   same upper-half-plane point/action, but retained automorphy factor/cocycle is required.
```

This reinforces the rule:

```text
Similarity is not mainly at the symbol level.
Similarity is in the retained-state/readout/re-chart mechanics.
```

---

## 7. Immediate continuation targets

Do not branch into new scripts yet. Continue these in-progress reading tracks:

```text
1. Reconstruct Dongyuan/Ceyuan Jiurong formula/contact-state table.
2. Finish Zagier Shadow transform reading around eta, theta, half-weight, S/T behavior.
3. Continue Phase internal stale/current separation: primitive core vs stale selector.
4. Finish Yin-Yang MFE branch: exact data structures, ghost zones, interpolation, boundary handoff.
5. Normalize coverage ledger after Pass 18.
```
