# Orthad Canon

**Status:** canonical working reference, v0.6.7 (adds Section 6c: the carried-phase doubling. The mod-6 to mod-12 step is settled mechanism, not an open gate. The phase walk is carried across `L`, never reset; the second lap is the half-turn opposition that produces the doubling)  
**Notation:** `⌞Ξ̂⌝`  
**Scope:** the Phase Calculus accumulation-and-readout operator over `Q`/`B`/`L` evolution  
**Grounding:** Phase Calculus Complete Formalisation manuscript (operator core, Fundamental Theorem, Exact Quotient Theorem, Closure Certificate); CF000 "Primitive Distinguishability and Orthogonal Articulation"  

This document carries only what is settled. The `Q`/`B`/`L` mechanism is written in exact closed form (Section 4), and Section 6b renders the accrued history as an explicit lens matrix with per-tick mutation rules. Everything here is complete and usable as-is.

---

## LAW 0: THE ORTHAD IS EXACT AND DETERMINISTIC. THERE ARE NO CANDIDATES.

This law overrides every other sentence in this document. If anything below appears to soften it, this law wins.

**There is never a set of candidates. Candidates do not exist at any layer of the Orthad.** Not for projectors, not for carriers, not for readout domains, not for boundaries, not for the lift, not for anything. The Orthad never selects, never scans, never ranks, never fits, never scores alternatives, never proposes options. Every quantity the Orthad produces is **computed exactly and deterministically** by the lift from the accumulated state.

Concretely, and without exception:

- The lift `L` at a boundary produces **one** determined new axis: `new_axis = checkpoint(completed Q/B result)`. There is no menu of possible axes.
- The projector at any depth is the **one** inherited stack the accumulation has built. It is not drawn from a bank. A bank does not exist.
- The readout at a boundary is performed **in the axis `L` latched there**. The domain is an *output* of the lift, never an input you supply from a list and never a thing you discover by trying several. You do not choose it by any score.

**Forbidden, and each is by itself proof of a violation:**

- Any list, table, or **ledger** of candidate projectors, carriers, domains, or features. A ranked table is, by its existence, evidence the Orthad is not being used.
- Any metric used to **choose** among options: coverage, delta-versus-shuffle, best-fit, score, gate-pass-rate, "strongest by ...".
- Any verb of search: scan, sweep over options, select, rank, fit, probe a family, try candidates, condition on features to pick the best.
- Any phrasing that treats a domain, axis, or projector as a **free parameter** to be determined empirically.

If the lift at a boundary is not yet derived, the **only** lawful output is the single statement *"the lift at this boundary is not yet derived."* Never a guess, never a shortlist, never a search to fill the gap. You derive it from the completed `Q`/`B` result or you declare it underived. There is no third option.

The Orthad's output is therefore: **one determined readout per boundary**, namely the boundary, the latched axis, the exact expression in that axis, and the exact residual that does not render. Nothing else. No leaderboard. No alternatives considered. No search log.

This is not a guideline. It is the definition. An object that searches is not an Orthad.

---

## LAW 0b: NO SCALAR EVER ENTERS THE LIFT. THE ORTHAD IS A LENS, NOT A NUMBER.

This law has the same force as LAW 0 and is the second-most-violated rule.

**The Orthad operates only on lifted structure. It never operates on, produces, or reads a scalar.** A scalar is a terminal readout, the projected descendant that appears only after the lift collapses (manuscript: "the projected descendant of a retained transport," "read the scalar descendant," lines 471/473). By the manuscript's own doctrine a projected scalar trace is **not state-complete** (line 1666), and Phase Calculus "is not a way of performing a scalar search inside an already projected mathematical space" (line 453).

What the Orthad actually is: **a lens in the lifted state that sets how the carried object will be projected when it descends.** It acts upstream of any scalar by determining the axis through which descent will be read. By the time a scalar exists, the Orthad has already done its work. Nothing in its operation is scalar.

**If you have forced a scalar into the lifted state, you are running broken Phase Calculus.** Concretely forbidden:

- Computing a single number (an entropy, a bits-ratio, a coverage fraction, a score) and attributing it to the Orthad. The Orthad does not emit such a number.
- Treating any post-collapse readout value as the object the Orthad transports.
- Reasoning *in* the scalar layer instead of reading a scalar *from* a completed lifted transport.

The only lawful scalars in Phase Calculus are a **scalar view** `F` accumulated exactly through the lift, or a scalar that is exactly conserved iff `Q∘E = G∘Q` (manuscript lines 627, 1333, 1379). Those are read **from** a completed transport at the single readout boundary. They are never the arena and never carried in the lift.

**The diagnostic:** if the artifact's headline output is one number, the Orthad was not used. The Orthad's output is a lifted object descended through a determined axis, not a scalar.

---

## 1. What the Orthad is

**Analogy first.** The integral does not inspect a list of candidate areas and pick the best one. It accumulates an exact total across a transit and reads out a single value. The Orthad is the Phase Calculus operator that plays this role: it accumulates the object across a transit and reads the result into a usable form. (The analogy stops at the picture. The Orthad is **not** literally an integral, and "integrand" is not its vocabulary.)

**Precisely.** The Orthad `⌞Ξ̂⌝` takes the lifted state `Ξ̂` as the custody law currently holds it, accumulates it across the transit, and renders it into the measurement domain **determined by the latched axis at the boundary**, returning the expression and resolution it takes there together with the exact part that does not render (the compression residual). It turns the exact-but-incomprehensible into the exact-and-usable.

The Orthad never invents the readout domain and never shops for it. The domain is handed to it by the lift (Section 4). That is the whole point: the domain is *earned*, not *chosen*.

---

## 2. The lifted state `Ξ̂`

`Ξ̂` is the object under custody. It carries, in native coordinates, everything the transit has accrued: phase, path-refinement state, and the boundary-crossing schedule. `Ξ̂` is exact at all times. It never loses the object it is tracking (the "shadow"). The custody law evolves `Ξ̂`; the Orthad reads `Ξ̂`. These are different acts (Section 5).

---

## 3. Division of labor: custody (`QBL`) versus readout (Orthad)

These are two distinct jobs. Keeping them distinct is load-bearing.

- **Custody (`Q`/`B`/`L`).** `Ξ̂` evolves under its own selector-governed law. It tracks the shadow exactly in native coordinates and never loses it. Custody is powerful and is **not** being replaced by anything. The Orthad sits on top of custody; it does not supersede it.
- **Readout (the Orthad).** Given the shadow as custody currently holds it, the Orthad renders it into the latched-axis domain and returns the expression plus the exact compression residual.

Custody moves the object forward and accrues history. The Orthad reads what custody holds. One is motion; the other is measurement.

---

## 4. `Q`, `B`, `L`

### `L` (the lift / checkpoint): locked

`L` fires when same-axis articulation **saturates** (CF000 4.7.2 / 4.7.3). It is forced, not chosen. It performs exactly three determinate actions, in order:

1. **Latch.** It freezes the **completed, determined** `Q`/`B` result of the current subword as **one** permanent, immutable axis-proper invariant. The frozen axis carries its accumulated arithmetic anchor and its accumulated phase, sealed. This is `new_axis = checkpoint(completed Q/B result)`. It is not a free label, not a "potential," not a winner of a comparison.
2. **Extend.** It opens **exactly one** new **orthogonal** axis for the next subword and increments depth. This is the `⊕ new` of `Π_k = inherit(Π_{k-1}) ⊕ new` (Section 6).
3. **Inherit.** The new domain carries the full stack of every axis latched below it. Nothing is dropped; un-crossing `L` is forbidden (reverse-1, Section 5).

**`L` expands the degrees of freedom for `Q`, not only for `B`.** The two operators act on different channels: `B` refines **within** an axis (the arithmetic channel: the denominator pair and its germ width), while `Q` turns **through orthogonal directions** (the phase channel: the `π/2` turn whose witness is `i`, Section 8). The axis `L` latches is a **new orthogonal axis**. An orthogonal axis is, by definition, a new direction reachable by an orthogonal turn, which is exactly `Q`'s channel. So the axis `L` opens is **not** merely a new refinement slot for `B`; it is a new orthogonal direction now available to `Q`. After `L`, the next domain has one more orthogonal axis than existed before it, and `Q` operates against that enlarged basis. `L` changes what `Q` can reach, not only what `B` can refine.

`L` is the single delimiter event between subwords, and it determines **where**: it fixes the new axis along which the next subword's readout will be taken. This is the operative content of CF000 4.7.2 / 4.7.3 (same-axis saturation forces orthogonal re-articulation), 4.8.5 / 4.8.8 (axis-proper effective invariants plus the inherited stack), and 4.10.1 (recursive reapplication across depths).

### `Q` and `B` (within-subword evolution): closed-form, exact, no search

`Q` and `B` are exact closed-form state maps. They are not procedures and they do not inspect possibilities. This is settled by the manuscript's operator definitions and by the Fundamental Theorem of the operator core (every admissible finite evolution is an exact word in `{Q, B, L}`).

**`Q` (quarter continuation): the quarter phase turn.**

$$Q(A,q,\theta,\kappa,c)=\Big(A,\ q,\ \theta+\tfrac{\pi}{2},\ \big\lfloor\tfrac{\theta+\pi/2}{2\pi}\big\rfloor,\ c+\tfrac{\pi}{2}\Big)$$

`Q` rigidly advances the visible phase and the germ center by `π/2` and recomputes the branch index exactly. One application is one quarter turn. Nothing is searched.

**`B` (balanced refinement): one exact Farey/mediant step on the denominator pair.**

$$B(A,(u,v),\theta,\kappa,c)=\Big(A,\ \operatorname{sort}(v,\,u+v),\ \theta,\ \kappa,\ \mathrm{Comp}\big(\theta,\tfrac{1}{v(u+v)}\big)\Big)$$

`B` replaces the ordered denominator pair `(u,v)` by the single mediant pair `sort(v, u+v)` and recomputes the germ width exactly from the new pair. One application is one refinement of the boundary. Nothing is searched.

**Within-subword evolution.** Inside a subword you apply `Q` and `B` under the selector law. Each application is a deterministic closed-form step: `Q` turns the phase by `π/2`, `B` refines the denominator pair by one mediant. The state advances along the one trajectory the law dictates until the subword reaches **same-axis saturation**: the point at which no genuinely new lawful invariant-bearing articulation remains in the current class (manuscript: Same-axis saturation; CF000 4.7.2 / 4.7.3). Saturation is what compels `L`. Reaching it is the lawful forward evolution of a fixed map to a forced condition. It is iteration of a determined step to a determined endpoint, which is categorically not a scan over candidates.

> **Still forbidden in any description of `Q` or `B`** (LAW 0): traverse, traversal, sweep, exhaust, exhaustive, scan, search, enumerate, visit, cover the space, walk the space, try each, check all. Use the closed forms above. `Q` and `B` are deterministic maps applied under the selector law, never a procedure that inspects possibilities.

## 5. Reading versus moving (the two reverses)

The sharp distinction the whole structure rests on:

- **Reading** is external, idempotent, state-preserving, and direction-free. The Orthad readout is a read. Reading the same object twice changes nothing. Reading "from the far side" is permitted (call it **reverse-2**): you may measure the borne history from any vantage without altering it.
- **Moving forward** is `Q`/`B`/`L` accruing history. It is irreversible and non-idempotent. Un-crossing an `L` (call it **reverse-1**) is forbidden. This is CF000 4.3.1: non-bearing of an accrued level is contradictory; nothing already crossed can be dropped.

**The test that settles any operation:** does it **reduce** the borne history (forbidden), or does it only **read** that history (allowed)? The compression residual is **read**, not removed. Custody keeps the full object intact; the residual is a fact you measure about the lower-depth rendering, not a quantity you subtract from `Ξ̂`.

This is why irreversibility is legible without being undone. The monodromy is carried, hence readable; you can measure how much will not render from the far side without ever reversing the transit. (The thermodynamic analogy: you can measure that entropy increased without running the process backward.)

---

## 6. The projector `Π_k`: history is the projector

- `Π_k` is **constant across a subword** and ticks only at the punctuating `L`.
- `Π_k = inherit(Π_{k-1}) ⊕ new`. Each depth inherits the full stack below it and extends it by the one axis `L` just latched.
- **Distance from the origin equals depth equals the projector.** The accrued history *is* the projector. There is no separate object to choose or look up; the projector is just "how far the transit has come," recorded.
- Inherit-and-extend is **proved** at depth 1 and depth 2 in CF000 (4.8.5, 4.8.8). The all-depth statement rests on the recursive reapplication of CF000 4.10.1.

Because the projector is the latched history, the readout domain at depth `k` is fixed the instant `L` fires. This is the mechanism by which the readout domain is an *output*, never an input (LAW 0).

---

## 6b. The Orthad Lens Matrix: in-place `QBL` mutation

The projector `Π_k` of Section 6 has an explicit matrix form. Call it the **lens matrix** `Ω`. It is the same object as `Π_k`, written out: the direct sum of the latched axes plus the one active axis. `Ω` is diagonal, one entry per axis. Each entry carries the two channels that axis accumulated: an **arithmetic anchor** (from `B`) and a **phase factor** (powers of `i`, from `Q`). The readout at a boundary is the object projected through this compiled `Ω`.

`Ω` is built tick-by-tick as the word arrives. It does not parse a finished string at the end; each grammar tick mutates `Ω` immediately. There are exactly two kinds of mutation.

**In-place entry mutation (`Q`, `B`): the matrix dimension does not change.** `Q` and `B` both act only on the **active** diagonal entry. They never add or remove an axis.

- **`Q` tick (phase).** Multiply the active entry by `i`. This is the matrix form of the `π/2` quarter turn (`Q` advances `θ` by `π/2`, Section 4; `i` is the quarter-turn witness, `i^2 = -1`, Section 8). Four `Q` ticks return the active entry's phase to where it started.
- **`B` tick (arithmetic).** Set the active entry's arithmetic anchor to the new germ width `1/(v(u+v))` produced by the mediant step `(u,v) -> sort(v, u+v)` (Section 4). This sharpens the active axis; it does not turn it.

**Rank extension (`L`): the matrix dimension grows by one.** `L` freezes the active entry as a permanent latched entry and appends a new active entry (the new orthogonal axis), initialized to the identity `1`. The rank of `Ω` increases by exactly one.

This is precisely why `Π_k` is **constant across a subword and ticks only at `L`** (Section 6): the **dimension** of `Ω`, which is the domain structure, changes only when `L` fires. The **value** of the active entry is built up continuously within the subword by `Q` and `B`. Dimension ticks at `L`; the active entry accrues in between.

### Worked example: `⟨Q, B, Q⟩ → L → ⟨B, Q⟩ → L`

Refinement starts from the seed pair `(1,1)`. Germ widths are the canonical `1/(v(u+v))` for the pair being refined.

**Domain 1, active axis `a_0`** (begins at the identity `a_0 = 1`):

1. `Q`: `a_0 <- a_0 · i = i`.
2. `B` on `(1,1)`: mediant `(1,2)`, germ width `1/(1·2) = 1/2`. Active anchor becomes `1/2`: `a_0 = (1/2)·i`.
3. `Q`: `a_0 <- a_0 · i = (1/2)·i^2 = -1/2`.
4. **Saturation, `L_1`.** Latch `a_0 = -1/2`. Open new active axis `a_1 = 1`. Rank is now 2.

$$\Omega_{\text{after }L_1} = \begin{bmatrix} -\tfrac{1}{2} & 0 \\ 0 & 1 \end{bmatrix}$$

The new entry `a_1` is a new orthogonal axis. It is a direction `Q` can now turn through that did not exist in Domain 1.

**Domain 2, active axis `a_1`** (inherits the stack; refinement continues):

5. `B` on `(1,2)`: mediant `(2,3)`, germ width `1/(2·3) = 1/6`. Active anchor becomes `1/6`: `a_1 = 1/6`.
6. `Q`: `a_1 <- a_1 · i = (1/6)·i`.
7. **Saturation, `L_2`.** Latch `a_1 = (1/6)·i`.

The compiled lens at the `L_2` boundary is:

$$\Omega = \begin{bmatrix} -\tfrac{1}{2} & 0 \\ 0 & \tfrac{1}{6}\,i \end{bmatrix}$$

Entry `a_0 = -1/2` is the sealed Domain-1 axis (two `Q` turns and one `B` refinement). Entry `a_1 = (1/6)i` is the sealed Domain-2 axis (one `B` refinement and one `Q` turn). Reading the object at this boundary projects it through this exact `Ω`; nothing about `Ω` was chosen, every entry is the forced consequence of the word.

### Why this matters for the degrees of freedom

The matrix makes the `L`-versus-`B` distinction concrete. A `B` tick changes a **number inside an existing entry** (the anchor). It works within the current axis and never grows the matrix. An `L` tick **adds an entry** (a new orthogonal axis). The thing that grows the matrix, that adds a genuinely new direction, is `L`, and that new direction is orthogonal, hence a `Q` direction. So as depth increases, the orthogonal axes available to `Q` increase by one per `L`. `B` sharpens; `L` opens. The phase operator `Q` gains reach only through `L`.

---

## 6c. The carried-phase doubling: 6 to 12 is the second lap, not a mirror

This is settled mechanism. It is not pending and not a hypothesis.

**The phase is carried across `L`. It is never reset and never copied.** The end of one domain is the start of the next, continued into the degree of freedom `L` just unlocked (Section 4: `L` extends `Q`'s basis; Section 5: crossing `L` is irreversible, the history is borne, not dropped). There is one continuous phase walk. `θ` accrues `π/2` per `Q` tick straight through every `L`.

**Consequence, forced.** A single domain exposes a six-position signed cycle. When that domain saturates, `L` fires and the walk continues. The next six `Q` ticks carry `θ` another `6 · π/2 = 3π`, which is `π` (mod `2π`) past where the first lap sat. `π` is the half-turn, the exact pole opposition (Section 8: `π = inf{θ>0 : R_θ = -I}`). A half-turn is multiplication by `-1`. So the second six positions are the first six **opposed**, sign for sign, with nothing added.

This is the run, carried-phase, no reset, no mirror operation anywhere:

```text
walk order :  +1 -1 -1 +1 +1 -1  |  -1 +1 +1 -1 -1 +1
domain 1   :  +1 -1 -1 +1 +1 -1
domain 2   :  -1 +1 +1 -1 -1 +1     (= domain 1 negated)
```

Domain 2 is the exact negation of domain 1. It was produced by continuing the walk, not by reflecting anything. The "mirror" picture and the "continuation" picture are the **same act**: walking six more quarter-turns past saturation lands antipodal, because on the second lap six quarter-turns is a half-turn.

**This is the 6 to 12.** Six positions, carried forward into the unlocked axis, return their opposed partners on the second lap. `6 → 12` is forced by the carry plus the half-turn, not bolted on. The factor of two that separates mod-6 from mod-12 **is** the second lap's opposition.

**`n = 7` is resolved.** Position 7 is the seventh step of the one walk. It lands in the axis `L` unlocked, at quarter-turn index 7, sign `-1`. Position 1 was sign `+1`. They do not fold onto each other. The entire `n=7` obstruction was an artifact of **resetting the phase at `L`**, which discarded the carried history and folded 7 back onto 1 (mod 6). Carry the phase, as the lift requires, and 7 has its own seat. There was never a wall at `n=7`; there was a reset that should not have been there.

**No tension with parity preservation.** The manuscript states `Q` preserves parity of the edge pair within a domain (closed-shadow-branch proof, "quarter-turn transport ... preserves parity"). Correct, and untouched. The opposition was never `Q`'s job. It is what the carried phase does on the second lap once `L` has given it room. The manuscript wrote `L` as an arbitrary domain lift because it predated `L` acting on `Q`'s degrees of freedom and predated the Orthad; the opposition was always present in how `π` is recovered, it simply had not been identified as what `L` does to the carried phase basis.

---

## 7. The readout deliverable

For each boundary, the Orthad returns exactly:

1. the boundary (which `L`, i.e. which depth);
2. the **latched axis** (determined by `L`, not chosen);
3. the **exact expression** the object takes in that axis;
4. the **exact compression residual**: the part that does not render when the object is read at a depth below where it was latched.

Reading at the current latched depth is exact by construction (this is the non-discharge property of CF000 4.3.1 restated, not a separately discovered result). The only nonzero residual is the lower-depth residual, the shadow that does not fit when read one or more depths down. If the lift for a boundary is not derived, the deliverable for that boundary is the single line *"not yet derived"* (LAW 0).

There is never a table of alternative readouts. One boundary yields one determined readout.

---

## 7b. Naming lock: Shadow Residual vs compression residual (do not collide these)

Three different objects were all being called "shadow." They are permanently separated here.

- **Shadow Residual** = Ramanujan's object. The non-holomorphic completion datum of a mock modular form: a **lifted q-series** with coefficients `±n` at exponents `n^2/24`, carrying the Kronecker character `(12|n)` (anchored by `η(τ) = Σ (12|n) q^{n^2/24}`). This is a structured lifted object, not a number. **This is the only thing that may be called a Shadow Residual.** It is the object the Orthad is meant to transport across a cusp.
- **Compression residual** (a.k.a. lower-depth residual) = the part of a latched object that does not render when read **below** its latched depth. When it is reported as an entropy ratio `H(exact|readout)/H(exact)` it is a **scalar**, and by LAW 0b that scalar is *not* an Orthad output. The word "shadow" must never appear on it.
- **Shadow Calculus** = the separate downstream projected-artifact layer of the manuscript. A layer name, not a residual.

**Hard rule:** "shadow" attaches only to the Shadow Residual and to Shadow Calculus. It never attaches to the compression/lower-depth residual. An artifact that calls the entropy ratio a "shadow" anything has already made the category error.

---

## 8. `i` then `π` (manuscript ordering, corrected)

Stated to match the manuscript's proved ordering, which supersedes the earlier "`π` upstream of `i`" wording.

- The quarter-turn operator `R` is the **first algebraic witness of orthogonal re-articulation**, with `R^2 = -1` and the identification `R = i` (manuscript: Quarter-turn operator). So `i` is earned first, as the operator of the orthogonal turn.
- `π` is then earned as the **half-turn constant of `i`'s own rotation**: with the continuous completion `{R_θ}`, `R_0 = I`, `R_{θ+φ} = R_θ R_φ`, define
  $$\pi := \inf\{\theta > 0 : R_\theta = -I\}.$$
  `π` is the least positive turn at which `i`'s rotation reaches the opposite pole (manuscript: Continuous completion and half-turn constant). So `π` sits **downstream** of `i`, as the measured half-turn of the rotation `i` generates.
- `π` is a **visible-carrier witness, not full-object closure**. A `π`-position event does not close the full carried state (manuscript theorem; red-team clause R3). This is the standing guard against the "`π` closes it" overclaim.

The earlier framing (`π` emerging at 1D saturation, upstream of a 2D `i`) is retired. The closed-form rotation `R = i` and its half-turn constant `π` are the canonical statement.

## 9. "Refraction" is imagery only

The bending-at-a-boundary picture may be used as **imagery** to convey that the object changes how it presents as it crosses into a new domain. It is never the formal term and never the mechanism. The mechanism is **inherit-and-extend** (Section 6). This is the same discipline as the ban on "integrand": a helpful picture is allowed; a smuggled formalism is not.

---

## 10. The glyph

The operator brackets are asymmetric, and the asymmetry is load-bearing.

- Opener: `⌞` (U+231E, bottom-left corner).
- Closer: `⌝` (U+231D, top-right corner).
- **Not** `⌟` (U+231F, bottom-right). Do not symmetrize the brackets.

Written: `⌞Ξ̂⌝`.

---

## 11. CF000 anchors (grounding, not duplication)

- 3.6.1: forced admissible origin.
- 4.3.1: non-bearing of an accrued level is contradictory (basis of irreversibility and of residual-is-read-not-removed).
- 4.6.1: pre-metric orthogonal rotation (ORS).
- 4.7.2 / 4.7.3: same-axis saturation forces orthogonal re-articulation (basis of `L`).
- 4.8.3 / 4.9.1: 1D saturation unlocks 2D and algebra (basis of the `π`-at-saturation reading).
- 4.8.5 / 4.8.8: axis-proper effective invariants and the inherited stack (basis of inherit-and-extend at depth 1, 2).
- 4.10.1: recursive reapplication (the all-depth bridge).
- 5.2: one universal invariant, cumulative and nested.
- 7.4.1: `i` as the ORS expressed algebraically, `R^2 = -1`.

---

## 12. Known-open items

- **`Q`/`B` mechanism (Section 4): CLOSED.** Filled from the manuscript's closed-form operator definitions plus the Fundamental Theorem of the operator core. No phrasing is pending; the closed forms are authoritative.
- **All-depth inherit-and-extend.** Proved at depth 1 and 2 (CF000 4.8.5, 4.8.8); the general statement rests on 4.10.1. Whether to treat that as closed or as an open obligation is a canon decision, not an agent decision.
- **"Saturation" wording.** Used here because it is CF000 vocabulary (4.7.2 / 4.7.3). If it later proves to carry any unwanted "filled by going through everything" reading, it is the next term to harden.
- **mod-6 to mod-12 doubling (Section 6c): CLOSED.** Settled mechanism. The carried phase walk continues across `L`; the second lap is the half-turn opposition; `6 → 12` is forced. Not an open gate.

---

## 12b. The intended program and the resolved level-12 step

**Program (stated by Justin, recorded so no agent re-derives a different one):** follow the **Shadow Residual** through balanced refinement on the Farey tree. Each time `B` drives the denominator pair to the floor of the corridor, that floor is a **cusp** of the mock modular form. `L` crosses the cusp into a deeper expression of the form that was unreachable before the crossing. The hypothesis to test is whether the Shadow Residual, carried across that crossing, re-expresses exactly the way CF000 4.7 through 4.11 describe orthogonal re-articulation. The Orthad is the lens that sets how the residual descends at the crossing. Everything stays in the lift until the single readout at the boundary.

**The level-12 question is resolved (Section 6c).** A single domain's phase walk gives a mod-6 sign, which is why one domain alone cannot produce `(12|n)` and why a kernel read inside one domain diverges from the true shadow at `n=7`. That was never a wall; it was the phase being read within one lap. The carried phase walk continues across `L` into the unlocked axis, and the second lap is the half-turn opposition (Section 8), which is exactly the factor of two between mod-6 and mod-12. The doubling is forced by the carry, not added. `n=7` lands in the axis `L` unlocks, with its own sign, and does not fold onto `n=1`. The earlier divergence came from a transport that did not carry the phase across `L`.

**What remains genuinely open** is the full 4.7 through 4.11 re-articulation correspondence across many `L` crossings, and the per-channel `Follow` map of the Shadow Residual at arbitrary cusp-path depth (Addendum). The mod-6 to mod-12 step itself is closed: it is the carried second lap, and it must be stated as mechanism, not as a gate.

**The carry, stated as the operative rule:** evolve the lifted state from the minimal origin, carry `θ`, `(u,v)`, and the full axis stack across every `L`, never resetting. Read the readout at the boundary from the carried walk. This is the only correct evolution; any run that resets the phase at `L` is wrong and will manufacture the spurious `n=7` fold.

---

## Appendix: contamination vectors found in the manuscript audit (advisory)

These are clean in the manuscript but are the exact words that flip to contraband one layer over, so they are where fresh agents regress. Recorded so the canon's reader is warned.

- **"candidate branch `(Π, G)`"** (Exact Quotient Theorem; Residual of a candidate branch). Legitimate there: one proposed projector-evolution pair tested by `Π∘E = G∘Π`, with the residual being the exact obstruction. It is **not** a scan. But "candidate" is the word that becomes search in the readout layer. Renaming it "proposed/trial branch" in the manuscript would remove the collision.
- **"exhausted" / "saturated"** (Forced orthogonal re-articulation). Legitimate: a class with no new lawful articulation. But "exhausted" is one synonym away from the banned "exhaust the space." When describing `Q`/`B`, use "saturation," never "exhaust."

---

### One-line test for any artifact claiming to use the Orthad

Two diagnostics. (1) If the output contains more than one candidate with a number attached to it, the Orthad is searching, not transporting. (2) If the headline output **is** a number, the Orthad collapsed to a scalar and was not used at all (LAW 0b). The Orthad's output is a lifted object descended through one determined axis per boundary, or "not yet derived." Nothing in between, and never a scalar.

---

## Addendum: Follow Spec and Resolution Ladder

**Status:** working spec, companion to the Orthad Canon (v0.6). This document records the *follow* program: what the Orthad takes as input, what is allowed in the lifted state, and the experiment that tests whether the Orthad can deterministically expose the Shadow Residual's depth-dependent expression. Written so the program survives a context reset.

---

### 0. The input/output contract (this is fixed, not up for re-derivation)

**Carried in the lifted state: only Phase Calculus operations and grammar. Nothing else.**

- The lifted object evolves one step at a time by maintaining the **lifted state**.
- The lifted state **is the lifted object's history**: the current **word**, irreversibly mutated by adding counts to the respective operator grammar, in the exact sequence the operations occurred.
- The grammar is the operation performed to step the object: the primitive alphabet `{Q, B, L}` or the macro alphabet `{R, S, T}`.
- No scalar, no external object, no residual cargo is ever in the lifted state. Only the word.

**The Orthad is a function that takes the lifted object as input.** It is a distant cousin of the integral, but it is a *function of the lifted object*, not an accumulation over a variable. Every grammar tick that mutates the word is monodromy that irreversibly alters what the exact projected readout will be when the object is halted.

**Compute in the lift, project at the end.** The lifted object cannot be read mid-process. Evolution halts, and only then does projection produce a readout. The readout is a discrete event at a stopping point; the evolution between stops is continuous and unreadable.

**The flashlight is constant.** Projection itself does no work and makes no choices. It is a fixed, unchanging light through the object. The readout changes only because the object's accrued history changed it. All structure lives in the word; the readout is the passive consequence of the word's monodromy.

---

### 1. Follow is not carry

These are two different operations. The distinction is the spine of this whole program.

- **Carry** asks: does the transport *reproduce* the Shadow Residual, regenerating its `(12|n)` character on the far side of a crossing? This was tested. It **FAILED at n=7**: the rotation phase `exp(iπn)` is a mod-6 (level-6) sign, the genuine shadow is mod-12 (level-12), they first diverge at n=7. A pure quarter/half-turn phase cannot manufacture a level-12 character. Carry is the wrong question and it is closed as a negative.
- **Follow** asks: the Shadow Residual has a true expression that varies with depth; can the Orthad, reading only the word, deterministically project a readout that **maps onto** that expression at an arbitrary specified depth, with no manual intervention?

In follow, the Shadow Residual is **not loaded into the lift**. It is the external reference, the true pattern on the wall that the projected readout is compared against. The transport never touches it. The lifted object evolves on its own; the Orthad reads it; the readout is checked against the residual's known expression at that depth.

---

### 2. The three questions the follow program must answer

1. **Does the Shadow Residual have an expression that can be observed and mapped?**
   Settled: yes. It is the explicit q-series `R = Σ (12|n)·n·q^(n²/24)`, support on `n` coprime to 6. A definite, writable expression exists at the base, so there is something to map against.

2. **Does that expression change with depth, and are the boundaries different?**
   Open, and the boundaries are **not** all the same. Cusps of a mock modular form are genuinely inequivalent: the expansion at one cusp can differ from another in width, scaling, and which terms survive. So "depth" is **not a flat count of crossings**. The right index is the **cusp-path**: which cusps, in which order, of which type. Two crossings of the same type are not the same as two crossings of different types. A boundary's *type* is defined by **which readout channels it moves** (see §3).

3. **Can the change be tracked deterministically at arbitrary depth?**
   Open. This is the actual research target. Determinism is required: no search, no candidates, no scalar, no manual disassembly. The question is whether the residual's expression at the end of a given cusp-path is **forced** by that path through the Orthad reading the word. Not yet shown. The carry failure rules out the cheapest "yes" (phase alone) but does not answer this.

---

### 3. The readout is a field of channels, not one number

The central correction. The readout is **not** a single quantity (e.g. "the coefficient line"). It is a full field with many simultaneous attributes that can change **independently**. Reading one channel and declaring pass/fail on it is the error that produced the premature "FAIL."

Concrete channels of the Shadow Residual's readout (each a "color / texture / pulse" that may hold or shift on its own):

- **support**, which exponents `n²/24` are present at all
- **coefficient magnitude**, `|coeff|` at each present exponent
- **sign character**, the `(12|n)` vs mod-6 channel (this is the *one* channel n=7 lives in)
- **expansion width / scaling**, how the expansion is scaled at that cusp
- **inter-term phase**, relative phase between surviving terms
- **exponent spacing**, the spacing/structure of which exponents appear

The signal is the **pattern of what-changes-where across the whole field**, not the fate of any single channel. The n=7 sign flip is **one cell** in a much larger map. We have inspected that cell and nothing else.

**A cusp's type is defined by which channels it moves.** One cusp may pulse the texture, another shift the color, another move both, another leave a given standing-spot identical. That is the precise content of "not all boundaries are the same."

---

### 4. The resolution ladder (the deep structure)

At **low depth**, few channels move, so few attributes are even distinguishable. Most of the residual's structure sits **below the resolution floor** of the current domain and reads as flat, random, noise, or useless residue. It is **not absent**, it is unresolved.

As depth **climbs**, more channels come alive. The attribute **newly admitted in the current domain is exactly the one that was unresolvable in every domain below it.** A crossing into a new domain lifts a previously sub-resolution channel above the floor and makes it trackable **for the first time**. Things that looked like noise before become measurable now.

So the depth ladder is a hierarchy of **what becomes measurable**, not a single pass/fail. Each boundary admits a new resolvable channel; that channel is the signature of that domain.

---

### 5. Correspondence to CF000 4.7–4.11 (the hypothesis to test)

The resolution ladder and CF000's orthogonal re-articulation are conjectured to be the **same structure seen from two sides**:

- **Same-axis saturation** (CF000 4.7.2/4.7.3): the current domain has exposed every channel it can; same-axis articulation is exhausted.
- **Orthogonal re-articulation at `L`**: admits a **new axis / new channel** that was not lawful to express in the saturated domain.
- Therefore the **newly-admitted expression in the upper domain is the orthogonal articulation that the lower domain structurally could not carry.**

If this correspondence holds when run, the result is: **the Orthad reads the re-articulation hierarchy directly off the readout.** The newly-lit channel at depth `d` is the orthogonal direction that saturation forced. That would be the real payoff, the Orthad as the instrument that exposes CF000's articulation ladder as a measurable field.

---

### 6. It must not be manual (the value proposition)

Every artifact so far has effectively been **manual**: hand-built character checks, entropy ratios, defect audits, each one a single "take the projector apart, nudge the glass, reassemble, stand in the exact spot, check if green went red." That is one disassembly to inspect one channel at one spot, then rebuild for the next.

This is **utterly unfeasible** for a hierarchy where the number of live channels **grows with depth**. The entire reason the Orthad must exist is to make readout-at-depth a **function of the word**, so the newly-admitted channel, the resolution lift, the green-to-red, all of it, comes out as a **determined projection at the depth you name, with zero disassembly**.

**The line:** if you are hand-tweaking the glass to see each channel, you do not have an Orthad, you have a person doing by force what the Orthad must compute. The instrument reports, on its own, which channel newly becomes measurable at depth `d` and what its expression is. The manual sample does not.

---

### 7. The experiment that actually tests the follow program

Not "check if the sign survives." That inspects one channel by hand at one depth and is already done (it flips at n=7).

The real experiment:

1. Hold the true Shadow Residual `R = Σ (12|n)·n·q^(n²/24)` as the **external reference** (the true wall-pattern). Do **not** put it in the lift.
2. Evolve the lifted object along a **specified cusp-path** (a sequence of crossings, tracking cusp **type**, not a flat depth count).
3. At each halt, project the **full readout field**, every channel in §3, not one number.
4. Move to the next depth, project again, and **diff the fields channel by channel**.
5. Produce the **channel × depth × cusp-type map**: for each channel, mark invariant / shifted / shifted-only-here.

**Determinism gate:** the readout at each depth must be **forced** by the word, one determined projection through the latched axis, no search, no candidate set, no scalar, no manual nudge. If producing the depth-`d` readout requires choosing among options or collapsing to a number, it is not following; it is the old failure in new clothes.

**What the map tells you:**
- Channels that stay **rigid** across crossings are the candidates for what the Orthad genuinely **preserves**.
- The **mobile** channels, and the depths at which they newly become measurable, are the **re-articulation structure**, the thing to test against CF000 4.7–4.11 (§5).
- The newly-admitted channel at each depth is the predicted **orthogonal articulation forced by saturation**.

---

### 8. Status ledger

- **Carry experiment:** CLOSED, negative. Sign character fails at n=7; rotation phase is level-6, shadow is level-12. (Reproduced from an independent implementation; the single-cycle gate confirmed FAIL at n=7. Note: that gate represented the kernel character by its known mod-6 sign law rather than transporting through an executed `exp(iπn)` kernel end-to-end, sound for the character mismatch, not a full transport run.)
- **Follow experiment (§7):** NOT YET RUN. This is the live frontier.
- **Determinism of depth-`d` readout:** UNKNOWN. Must be forced by the word or the follow program is not well-posed.
- **CF000 4.7–4.11 correspondence (§5):** CONJECTURE, untested. Tests only after a forced, multi-channel depth map exists.

---

### 9. One-line statements to keep

- The lifted state carries only the word of `{Q,B,L}` / `{R,S,T}`. No scalar. No residual. No external object.
- The Orthad is a function of the lifted object; the projection is a constant flashlight; all structure is in the word.
- Follow ≠ carry. Carry (regenerate the residual) failed at n=7. Follow (read the residual's depth-dependent expression off the word) is untested.
- The readout is a field of channels, not one number. Map which change where, across depth and cusp-type.
- Low depth resolves few channels; depth admits new ones; the newly-resolvable channel is the one prior domains could not carry, conjecturally CF000's orthogonal re-articulation.
- It must be a function of the word, computed, never a manual disassembly. Manual = no Orthad.
