# 20 — Zagier Squeeze-Dry Pass + Selector/Lens Clarification

Date: 2026-06-23

Resource squeezed in this pass:

- `Modular-Forms/Zagier123ModularForms.pdf`
- Full title: **Elliptic Modular Forms and Their Applications**
- Author: Don Zagier
- PDF pages: 103
- Extracted text lines: 5,447
- Status after this pass: `COMPLETE_FIRST_PASS`

Coverage standard used here:

- Section-by-section sweep completed.
- Main definitions/propositions/theorems relevant to Phase/Tao/Shadow research extracted.
- Q/B/L/Shadow relevance classified.
- Traps and non-matches recorded.
- This is **not** a proof verification of all 29 propositions and quoted theorems.

---

## 0. Clarification: “retained state selects admitted operation”

This phrase should be split into two layers.

### A. QBL selection / custody automation

For the **QBL primitive custody layer**, the phrase is correct:

```text
retained lifted state + current boundary condition
→ determines which operation is admissible next
```

The retained state includes the active coordinates such as:

```text
(A, q=(u,v), theta/kappa/phase, active floor/capacity, word/history)
```

At this level, “retained state selects admitted operation” means:

```text
B can continue only while the current Q-admitted floor/capacity allows it.
Q fires when B is blocked but phase positions remain.
L fires when B and Q are both saturated.
```

This is the **selection automation / primitive custody rule**, not the lens readout rule.

### B. Orthad lens matrix

For the **Orthad lens matrix**, the phrase must be softened:

```text
The lens does not select Q/B/L.
The lens is compiled from the already-accrued Q/B/L word and lifted state.
```

The lens matrix preserves and displays the history:

```text
active axis: updated by Q/B until L
latched axes: frozen completed axes
L: freezes active axis and appends a new active axis
```

So the exact phrasing is:

```text
QBL custody selects admitted operation from retained state.
Orthad lens matrix compiles and preserves the resulting retained channel field.
```

### C. Reunified wording for future notes

Use this instead of the ambiguous sentence:

```text
Retained state governs admissible Q/B/L custody moves;
the Orthad lens compiles the resulting word into active/latched channel structure;
terminal projection reads from that channel structure afterward.
```

This prevents conflating:

```text
operation selection
with
lens readout / Follow projection
```

---

## 1. Resource-level extraction

Zagier’s paper is not a narrow eta note. It is a full survey of classical elliptic modular forms and applications, organized around:

1. Modular group action and modular forms.
2. Eisenstein series and ring structure.
3. Theta series, including unary theta and eta-products.
4. Hecke theory and L-series.
5. Derivatives, quasimodular forms, Rankin-Cohen brackets, differential equations.
6. Complex multiplication, singular moduli, Taylor expansions, CM forms.

For our project, the load-bearing content is:

```text
SL2 action on upper half-plane
PSL2 quotient identification
automorphy factor (cz+d)^k
finite-dimensional computable modular-form spaces
q-expansion as local cusp coordinate
E2 anomaly / quasimodular correction
Dedekind eta product and q^(1/24)
unary theta representation of eta using chi_12 and n^2/24
Serre-Stark theorem: weight 1/2 forms are linear combinations of unary theta series
Rankin-Cohen / derivative correction layer
CM/lacunarity as support-sparsity precedent
```

---

## 2. Section-by-section mechanism extraction

### 2.1 Section 1 — basic definitions

Core mechanics:

```text
H = upper half-plane
SL(2,R) acts by z ↦ (az+b)/(cz+d)
Im(γz) = Im(z)/|cz+d|^2
±γ act identically on H, so PSL(2,R)=SL(2,R)/{±1} is the effective action
modular forms transform by f(γz) = (cz+d)^k f(z)
```

Mechanism value:

```text
SL2 action = state re-coordinate action.
PSL2 quotient = projection loss / sign collapse.
Automorphy factor = carried correction required for coherent projection.
```

Research mapping:

```text
Q: finite action generators later reduce to S/T style grammar.
L: z ↦ -1/z is a domain inversion / re-chart candidate.
Shadow: the transformation factor cannot be discarded if following a channel field.
```

Trap:

```text
Do not say PSL2 is the same as the retained lifted state.
PSL2 is already a quotient where ±I are identified.
For Phase/Orthad comparison, quotienting is projection loss unless the lost sign is externally recovered.
```

### 2.2 Fundamental domain / valence / finite-dimensionality

Zagier develops the fundamental-domain/zero-count logic leading to finite dimensionality of modular-form spaces.

Mechanism value:

```text
A global identity can be proven by checking enough finite data because the space is finite-dimensional.
```

Research mapping:

```text
This supports a later exact-test discipline:
  compare retained channel families in a finite-dimensional modular space;
  do not numerically fit arbitrary q-series.
```

This is important for Follow:

```text
If the Orthad channel field lands in the correct modular/theta space,
then identity checking can become finite and exact, not heuristic.
```

### 2.3 Section 2 — Eisenstein series and the ring M*(SL2Z)

Key extraction:

```text
Eisenstein series generate classical examples.
The ring of modular forms on SL(2,Z) is generated by E4 and E6.
The discriminant Δ is a weight-12 cusp form.
Δ has product structure tied to eta by Δ = η^24.
```

Mechanism value:

```text
A small generator set can produce a full structured function space.
```

Research mapping:

```text
This matches the project pattern:
  small primitive grammar → rich structured projection surface.
```

Trap:

```text
Do not equate E4/E6 with Q/B/L.
The comparison is generator economy and closure, not literal operator identity.
```

### 2.4 E2 and quasimodularity

Key extraction:

```text
E2 almost transforms like a modular form, but has an anomalous correction term.
Correcting E2 by adding a non-holomorphic y-dependent term gives a true transformation behavior.
```

Mechanism value:

```text
Projection-level holomorphy and transformation coherence can conflict.
A correction term may be required to preserve exact transformation law.
```

Research mapping:

```text
This is a strong caution for Shadow Follow:
  a visible q-series may be almost right but missing a carried correction channel.
```

Phase interpretation:

```text
If a projected scalar looks close but fails exact transformation,
check whether the missing object is a retained channel / cocycle / non-holomorphic completion,
not whether the entire lead is false.
```

### 2.5 Section 3 — theta series

Core mechanics:

```text
A quadratic form Q gives theta series Σ q^Q(x).
For m variables, weight is m/2.
Unary theta series are the m=1 case.
Poisson summation supplies transformation behavior.
```

Mechanism value:

```text
Quadratic exponent structure naturally produces modular behavior.
```

Direct Shadow relevance:

```text
The Shadow residual has exponent n^2/24.
This lives naturally in unary theta / half-integral weight territory.
```

### 2.6 Jacobi theta and half-integral weight

Key extraction:

```text
Jacobi theta satisfies two functional equations.
The transformations generate a subgroup commensurable with SL(2,Z).
Theta is a modular form of weight 1/2 on Γ0(4), with character.
```

Mechanism value:

```text
Half-integral weights require multiplier/character discipline.
```

Research mapping:

```text
The sign/support channel cannot be tacked on afterward.
It is part of transformation legality.
```

### 2.7 Eta-products and eta as unary theta

This is the nuclear part for Shadow.

Key extraction:

```text
η(z) = q^(1/24) ∏_{n≥1}(1-q^n)
```

Zagier then gives the theta-series representation:

```text
η(z) = Σ_{n≥1} χ12(n) q^(n^2/24)
```

with character:

```text
χ12(12m ± 1) = +1
χ12(12m ± 5) = -1
χ12(n) = 0 if n is divisible by 2 or 3
```

This is exactly on the Shadow surface:

```text
support: gcd(n,6)=1
sign: χ12(n)
exponent: n^2/24
```

Difference from the project Shadow residual:

```text
Zagier eta has coefficients χ12(n).
Project Shadow residual has χ12(n) * n.
```

So the project residual is not just η. It is likely in the orbit of:

```text
unary theta derivative / weighted theta series / eta-related differential or Jacobi-type channel
```

This is a precise next target.

### 2.8 Mersmann eta-product classification

Key extraction:

```text
There are precisely 14 primitive eta-products that are holomorphic modular forms of weight 1/2.
```

Mechanism value:

```text
Weight-1/2 eta-product possibilities are finite and classifiable.
```

Research mapping:

```text
This blocks vague eta speculation.
If a candidate is an eta-product of weight 1/2, it must fit a finite classification.
```

Useful for future test:

```text
Compare Orthad-projected eta/theta candidates against the finite primitive eta-product list.
```

### 2.9 Serre-Stark theorem

Key extraction:

```text
Every modular form of weight 1/2 is a linear combination of unary theta series.
```

Mechanism value:

```text
Weight-1/2 is not a huge arbitrary search space.
It is controlled by unary theta structure.
```

Research mapping:

```text
This strongly supports keeping Shadow on a unary-theta channel-field track.
```

It also clarifies the role of the `n` factor:

```text
If χ12(n) q^(n²/24) is eta,
then χ12(n)*n*q^(n²/24) must be studied as a weighted unary theta / derivative-like object,
not as a random q-series.
```

### 2.10 Theta series in many variables

Key extraction:

```text
Positive definite quadratic forms yield theta series.
Even unimodular lattices yield modular forms on full SL2Z.
Theta series may fail to distinguish non-isomorphic lattices.
```

Mechanism value:

```text
Projection collision exists: different retained objects can have the same theta projection.
```

Research mapping:

```text
This reinforces the project rule:
  compare retained channel state first;
  scalar/theta projection can identify non-identical objects.
```

### 2.11 Section 4 — Hecke theory and L-series

Key extraction:

```text
Hecke operators organize modular forms into eigenforms.
Eigenforms have L-series with Euler products.
Modular forms connect to algebraic number theory and elliptic curves.
```

Mechanism value:

```text
Operators acting on function spaces extract stable arithmetic channels.
```

Research mapping:

```text
This is downstream from current phase.
Do not use Hecke theory as a primitive baseline yet.
Record it as possible future channel normalization / eigenbasis analysis.
```

### 2.12 Section 5 — derivatives, Rankin-Cohen, quasimodular forms

Key extraction:

```text
Naive derivative of a modular form is generally not modular.
A corrected derivative can transform properly.
Rankin-Cohen brackets combine derivatives into modular forms.
Cohen-Kuznetsov series encodes derivative towers with transformation law.
```

Mechanism value:

```text
Higher-order local change can be retained as a structured tower.
Modular legality can be restored by combining derivative channels in the right grammar.
```

Research mapping:

```text
This is directly relevant to the missing n-factor in the Shadow residual.
A derivative-like operation on q^(n²/24) introduces n²/24, not n.
A Jacobi/unary-theta derivative in an auxiliary variable can introduce n.
Therefore the n factor probably points to an odd theta / Jacobi variable derivative, not ordinary q-differentiation alone.
```

This is the most precise new Shadow instruction from Zagier:

```text
Do not try to get χ12(n)*n by differentiating eta with respect to q alone.
Look for unary theta with an auxiliary z/elliptic variable or odd theta derivative.
```

### 2.13 Section 6 — complex multiplication and lacunarity

Key extraction:

```text
CM modular forms have sparse/lacunary coefficient support.
Some eta powers are CM modular forms only for specific even powers.
Serre’s lacunarity theorem distinguishes CM-type forms by coefficient vanishing density.
```

Mechanism value:

```text
Sparse support is mathematically meaningful, not incidental.
```

Research mapping:

```text
The Shadow support gcd(n,6)=1 is not enough to claim CM/lacunarity,
but it belongs in a world where support patterns can be structural invariants.
```

---

## 3. Direct implications for current research

### 3.1 The Shadow target is strongly supported

The exact surface is no longer merely “modular-looking.” It is in Zagier’s explicit unary theta / eta passage:

```text
η(z) = Σ χ12(n) q^(n²/24)
```

The project’s Shadow reference:

```text
R(q) = Σ χ12(n) * n * q^(n²/24)
```

is therefore one controlled operation away from eta/unary theta.

### 3.2 The missing operation is not arbitrary

The extra coefficient `n` probably demands one of:

```text
1. odd unary theta series;
2. derivative with respect to an auxiliary elliptic/Jacobi variable;
3. weight-3/2 unary theta relation;
4. eta/theta multiplier channel after a specific operator;
5. false/mock/quantum theta boundary variant.
```

Best immediate mathematical target:

```text
Find an object Θ(ζ,τ)=Σ χ12(n) ζ^n q^(n²/24).
Then ∂/∂ζ at ζ=1 yields Σ χ12(n) n q^(n²/24).
```

This is now the cleanest path to the project Shadow residual.

### 3.3 Follow theorem should be formulated at channel level first

Zagier makes it clear that:

```text
transformation behavior
character
weight
cusp behavior
support
```

are all part of the object.

Therefore a terminal scalar coefficient comparison is too late. Follow should compare:

```text
support channel: gcd(n,6)=1
sign channel: χ12
exponent channel: n²/24
weight/multiplier channel: half-integral modular behavior
extra amplitude channel: n
```

### 3.4 Automorphy factor is not cosmetic

The automorphy factor `(cz+d)^k` is the modular-form analogue of a carried correction required for coherent re-charting.

Project mapping:

```text
L / chart handoff cannot discard the carried correction and still expect exact projection.
```

### 3.5 Projection collision warning

Zagier’s many-variable theta discussion includes examples where non-isomorphic lattices can have the same theta series.

Research rule:

```text
Do not infer retained-state equality from q-series equality alone.
```

This supports the Orthad rule:

```text
compare retained lens/channel structure before scalar projection.
```

---

## 4. Q/B/L/Shadow classification after Zagier

### Q

Weak to moderate direct support.

Zagier supplies:

```text
finite group action generators;
S/T modular transformations;
phase-like roots from half-weight multipliers;
finite-dimensional modular spaces.
```

But this is not the primary Q evidence. Yijing/Bagua and QBL internal docs remain stronger for Q.

### B

Indirect support.

Zagier does not supply a B floor-anchor process. But it supplies:

```text
legal coefficient/support refinement in q-series;
finite identity checking by enough coefficients;
cusp vanishing constraints for eta-products;
classification by admissible cusp behavior.
```

This strengthens “admitted operation under constraints,” but not the `(u,v)` floor mechanism directly.

### L

Strong support.

Zagier supplies:

```text
SL2 action / re-coordinate transformation;
S inversion z ↦ -1/z;
automorphy factor carried across charts;
PSL quotient as projection loss;
cusp compactification / boundary behavior.
```

### Shadow

Very strong support.

Zagier supplies the exact family:

```text
eta
unary theta
χ12
q^(n²/24)
weight 1/2
Serre-Stark linear-combination theorem
```

Open gap:

```text
explain the extra coefficient n in the project residual.
```

Best gap-closure route:

```text
Jacobi/elliptic-variable derivative of unary theta.
```

---

## 5. Reunified understanding after this pass

The strongest global similarity has sharpened again:

```text
Retained state governs admissible primitive custody moves.
Lens/channel structure records what happened without collapsing it.
Projection into q-series/modular/theta form happens afterward.
Exact projection requires carrying transformation factors, characters, support conditions, and cusp behavior.
```

The modular-form side now supplies a mature mathematical analogue of the project discipline:

```text
Do not compare raw visible series only.
Track the full transformation law.
Track the character.
Track the multiplier / automorphy factor.
Track cusp legality.
Only then compare coefficients.
```

This is nearly identical in spirit to:

```text
Do not compare scalar output first.
Compare retained Orthad channel field first.
```

---

## 6. New exact work orders generated by Zagier

### Work Order Z1 — Shadow as Jacobi-variable derivative

Define:

```text
Θ12(ζ,τ) = Σ_{gcd(n,6)=1} χ12(n) ζ^n q^(n²/24)
```

Then test:

```text
(ζ ∂/∂ζ Θ12)(ζ,τ)|_{ζ=1}
= Σ χ12(n) n q^(n²/24)
```

This is the project Shadow residual, up to indexing convention and n-domain sign symmetry.

Status: `HIGH_PRIORITY_NEXT_FORMAL_CHECK`

### Work Order Z2 — Identify weight/multiplier of weighted unary theta

Need determine whether the weighted series is:

```text
weight 3/2 unary theta
Jacobi derivative channel
mock/false boundary object
eta derivative relative
```

Status: `OPEN`

### Work Order Z3 — Orthad Follow channel decomposition

Decompose Follow target as:

```text
support: gcd(n,6)=1
sign: χ12(n)
exponent: n²/24
amplitude: n
weight/multiplier: half-integral / derivative channel
```

Then match Orthad lens channels to these before scalar projection.

Status: `OPEN`

### Work Order Z4 — Avoid false eta identity

Record hard prohibition:

```text
Do not say the Shadow residual is η.
η gives χ12(n) q^(n²/24), not χ12(n)*n*q^(n²/24).
```

Correct:

```text
Shadow residual is eta-adjacent / unary-theta-derivative-adjacent.
```

---

## 7. Coverage update

Move:

```text
Modular-Forms/Zagier123ModularForms.pdf
```

from:

```text
MECHANISM_COVERED_NOT_COMPLETE
```

to:

```text
COMPLETE_FIRST_PASS
```

Reason:

```text
Full extracted text swept section-by-section;
Shadow mechanism fully extracted;
modular action / automorphy / theta / eta / derivative / CM relevance classified;
new work orders produced.
```
