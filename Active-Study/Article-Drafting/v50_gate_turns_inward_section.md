# Section: The Gate Turns Inward (v50)

*Role in the larger piece.* This section is the reflexive hinge of the essay. The preceding
sections built one rule, the projection-loss or state-completeness rule, and showed it holding
across an ancient divination system, a modern plasma code, and the framework's own non-commutative
core. A fair reader will ask the obvious question at this point: is this rule only ever pointed
outward, a one-way instrument the project uses to judge other systems while sparing itself? v50 is
the answer. Here the gate is turned on Phase Calculus's own foundational text, and it cuts. This
section also assembles the internal spine that earlier sections leaned on without deriving, so it
doubles as the backbone the rest of the piece rests against. It sits after the internal-sharpening
sections on hidden order and winding, and before the executable-replay section.

This section assumes the shared rule and the running cross-corpus table introduced earlier. It does
not restate them in full. It adds the internal, reflexive row and the provenance of the gate itself.

---

## 1. The problem v50 had to resolve

The framework's large reference text, the complete formalisation, had been treated as a single flat
canon. That was the last major internal blocker, because parts of it disagreed with the corrected
results the project had since established. Reading it as one surface meant an older passage could
silently overwrite a newer correction. v50 resolves this not by throwing the old text away but by
splitting it into three honest layers.

```
Layer 1  primitive operator core (Q, B, L)        keep, canon-compatible
Layer 2  executable selector machinery (R, S, T)  demote to historical witness
Layer 3  projector hygiene                         keep, and promote to master gate
```

The teaching point is that "stale" does not mean "wrong everywhere." It means the document mixed a
durable core, a piece of branch-local scaffolding that has since been superseded, and the very
hygiene principle that lets you tell the two apart. Separating the layers is the work.

---

## 2. The decisive conflict, in plain terms

The conflict that forced the split is exact and small, which is what makes it convincing. It is a
disagreement between two versions of the lift operator, the operation that hosts a state up into a
new domain.

The old Chapter 7 operator, called `T`, does this:

```
T : (A, (u, v), t, ...)  ->  (A+1, (1, A+1), t+1, ...)
```

Read the second slot. The carried pair `(u, v)`, which holds the accumulated refinement state, is
thrown away and reset to `(1, A+1)`. The lift arrives in the new domain having emptied its pockets.

The corrected Orthad operator, called `L`, does this instead:

```
L : carries q and theta forward;  rank grows by exactly one;  refinement continues after the lift
```

The lift arrives in the new domain still holding everything it was carrying.

The teaching image: two elevators. The old one wipes your hands clean every time it lifts you a
floor, so you reach the new floor with nothing. The corrected one carries your load with you. If
the state you were accumulating matters for what you do next, and the whole project has been about
exactly that, then the old elevator is not a stylistic alternative. It is a state-losing operation.

---

## 3. Why this is the gate turning inward

Here is the move that gives the section its title. The framework's own Chapter 8, the projector
hygiene layer, states the rule the entire essay runs on:

> A projection or readout is admissible only as a readout. It is state-complete only if it preserves
> the state needed for the next admissible transition. A branch certificate must report its retained
> coordinates, its action law, its history, and whatever it dropped.

Apply that rule to the old `T`. `T` resets `q`, so it does not preserve the state needed for the
next refinement step. By the framework's own hygiene clause, `T` is not state-complete. The text
contains, in one chapter, the exact principle that demotes the operator in an earlier chapter.

That is the sharp version of v50's finding, and it is the one to carry into the merged draft:

> The complete formalisation already contains the projector-hygiene machinery needed to demote its
> own older selector layer.

So the correct action was never rejection. It was layer separation performed by the document's own
standard. Keep the primitive operator core. Keep the hygiene gate. Keep the mechanism spine. Demote
the old executable selector schedule, `R`, `S`, `T`, and the selector law `Sigma`, to a historical
witness layer that records how an early branch once ran, with no authority to author current canon.

This is the credibility keystone of the whole piece. The instrument the project points at the
Yijing, at Pencil Code, at MHD diagnostics, is the same instrument it points at its own foundational
text, and it accepts the cut when the instrument finds one.

Status: **proved / found in shipped artifacts**. The companion attack verifies each leg locally:
corrected `L` carries `q` (PASS), old `T` fails to carry `q` on non-origin state (PASS), the visible
phase projection collides while not being state-complete for the next refinement (PASS), and the
Ancient Yi least-significant-first carry case (PASS). The Lean theorem surface is written but not
compiled, since no Lean toolchain was available in the run environment. Report it that way.

---

## 4. The internal spine the rest of the essay stands on

v50 also assembles the foundational papers into one mechanism chain, in order. Earlier sections used
this gate as if its origin were settled. This is where its provenance is laid out, and the chain is
clean enough to quote directly into the draft as the backbone.

```
CF000   same-axis saturation is not termination;
        exhausting lawful same-domain articulation forces a move to a new orthogonal axis.

Farey   the canonical refinement on that move is exact Fibonacci denominator-pair arithmetic;
        truncation at a finite floor is lawful orthogonal transfer, not deletion.

CF19    the visible witness is not state-complete;
        exact return belongs to the completed lifted object, not to the visible carrier alone.

hygiene the projector hygiene layer makes that obstruction a general gate.

Orthad  the corrected carried-walk is the canon those four assemble into.
```

Read top to bottom, this is one continuous claim. A system saturates an axis, is forced sideways
into a new one, refines there under an exact arithmetic with a finite floor, transfers lawfully at
that floor rather than discarding anything, and the true returning state lives in the completed
lifted object rather than in the visible readout. Every corpus section in the essay is a sighting of
some stretch of this spine in foreign material. This section is where the spine itself is named.

The placement of `CF000` at the head also closes a loop with the opening section. The same paper that
derives polarity as the forced content of an admissible origin is the
paper that supplies the first link of this mechanism chain. Origin and mechanism are the same
document read at two depths.

---

## 5. What this section contributes, and what stays open

Contributes to the merged draft:

- The reflexive integrity moment. The state-completeness gate is applied to Phase Calculus itself
  and demotes one of its own older operators. This pre-empts the strongest fair objection to the
  whole essay, that the rule is only ever aimed outward.
- The provenance of the gate. Earlier sections used projector hygiene as a given. This section shows
  it is Chapter 8 of the framework's own formalisation, and links it back through CF19, Farey, and
  CF000 into a single spine.
- A worked, small, exact conflict (`T` resets `q`, `L` carries it) that a reader can hold in mind as
  the concrete picture of what state-completeness means, rather than an abstraction.

Stays open, to be tracked in the closing section of the piece:

- Ancient Yi full translation and exact line-order proof.
- The latest active selector and floor source, still on local storage and not yet in hand.
- The Liu 2022 plasma time series and connectivity data.
- Line-by-line Lean compilation, blocked only by toolchain availability, not by any known defect.

---

*Hands off to.* The gate has now been built, sharpened, and turned inward, but everything so far has
been argued and close-read. The next section asks whether the framework's own claims survive
execution, rerunning the core kernels from real code and data before the essay reaches its closing
assessment. The load-bearing sentence this section gives the rest of the draft: the project's own
measuring instrument was turned on the project's own canon, and where it found a state-losing operator
hiding in an old chapter, it cut, by the standard written into a later chapter of the same book.
