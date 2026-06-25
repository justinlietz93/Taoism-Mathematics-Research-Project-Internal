# Section: The Shadow of a Change (v49)

*Role in the larger piece.* This section pushes the essay's central rule to its extreme form, where
the shadow of a real change becomes identical to the shadow of no change at all, and it does so with
machine-checked algebra. It is internal, not external: the framework verifying its own core, not an
outside system corroborating it. That distinction is load-bearing and must survive the merge. Place
this section after the outside-witness section, which states the shared rule and owns the running
cross-corpus table, and before the reflexive hinge.

This section assumes the rule and the table from the outside-witness section. It adds the
non-commutative geometry row, sharpens what "not state-complete" can mean, and continues the polarity
thread the Pencil section opened.

---

## From a self-inverse flip to a hidden score

The Pencil section showed a polarity that was a self-inverse half-turn: Yin-to-Yang and back were the
same operation, so order did not matter. This section is the next turn of the same screw. Here the
two sides do not commute. Doing one operation then another differs from the reverse order, and the
difference is real but invisible. The progression, self-inverse polarity to non-commuting polarity,
is deliberate, and the two sections should be read in that order.

---

## Result one: order leaves a hidden charge the projection cannot see

Take two basic operations as vectors, `a = (1,0,0)` and `b = (0,1,0)`. The difference between doing
them in one order versus the other is the commutator `[a,b]`, and the package verifies

```
[a, b] = (0, 0, 1)
```

The order difference does not vanish. It lands entirely in the third, hidden coordinate. Now apply
the visible projection, which keeps the first two coordinates and drops the third:

```
visible([a, b]) = (0, 0)
visible(origin)  = (0, 0)
```

These are equal. The visible shadow of "I did a then b instead of b then a" is identical to the
shadow of "I did nothing." The projection collapses exactly the coordinate that recorded the order.

The symbolic form makes the meaning exact. For general operations `(m,n)` and `(m',n')` the hidden
charge is `m*n' - m'*n`, the signed area of the parallelogram the two operations span. So the hidden
coordinate is not arbitrary bookkeeping. It is the area swept by doing the operations in a given
order, and its sign flips when you reverse them.

The teaching image, the one to carry into the merged draft: a spiral staircase, or a parking-garage
ramp. Walk one full loop and look at your shadow on the ground, where the ground is the projection
that throws away height. The shadow traces a closed loop back to where it started. By the shadow
alone you came back. But you are one floor up, and the height you gained equals the area your loop
enclosed. The ground cannot tell you which floor you are on, and that floor is the order state the
projection erased.

This is the same algebra as quantum phase and the Aharonov-Bohm effect, a path that returns to the
same visible point while carrying a hidden accumulated phase set by the enclosed area. The package is
not borrowing that as a metaphor; it is the same commutator structure.

Status: proved. SymPy audit, CLI report, and Python tests pass. The Lean surface is written but not
compiled, since no Lean toolchain was available in the run environment. Report it that way.

---

## Result two: a whole family of hidden states casts the same blank shadow

One example could be a fluke, so v49 swept many. Sampling operation pairs with components from minus
two to two:

```
commutator cases sampled:        496
distinct hidden charges found:   14   (from -8 to +8)
visible projection, every case:  (0, 0)
```

Every case projects to the same visible origin. Behind that one blank shadow sit at least fourteen
genuinely different hidden states. The fiber, the set of hidden states living above one visible
point, is richly populated. Stated as a control:

```
visible projection only            ->  FAIL, not state-complete
visible projection + order charge  ->  PASS, retained order state recovered
```

If all you keep is what you can see, you cannot tell these states apart, and you cannot predict the
next step, because the next step depends on the order the projection threw away. The package checks
the same effect in a finite, discrete setting with permutations, where swapping two transpositions
leaves a hidden three-cycle, `[(12),(23)] = (132)`. Same lesson on different hardware.

Status: proved and found in shipped artifacts.

---

## Result three: the (55,89) anchor, kept honest

This package also carries the balanced-refinement operator `B(u,v) = sort(v,u+v)`, and it handles its
most quotable number exactly the right way, which is worth flagging because it is where an earlier
overstatement got corrected. Starting from the canonical seed `(1,1)` and applying `B` nine times
reaches `q = (55,89)`, `uv = 4895`. The correct framing, now locked:

> (55,89) is the canonical origin-path witness. It is not a rigid definition of all B refinement.

To make that concrete, v49 ran `B` from several different starting pairs. The finding is clean and is
the heart of the modular-B direction: different starts produce different valid corridors and
different anchor values, yet every corridor's ratio converges to the same number, the golden ratio,
roughly 1.618, by about depth nine.

The teaching image: a river system. Wherever you put the boat in, the current carries you to the same
sea. The particular town you drift past depends on your put-in point, but the direction of flow is
universal. The golden ratio is the sea; (55,89) is the town the canonical put-in passes at mile nine.
Reporting that one town as if it were the whole river was the overstatement. Reporting the universal
flow with the canonical town as one labeled landmark is the honest version, and it is what the data
shows.

This keeps the larger question open in its strong form: a B-like refinement may be a carrier-selected
arithmetic, with the golden corridor as one verified instance and the Ancient Yi base-eight carry as
a separate candidate on the same skeleton.

Status: proved and tabulated. Convergence to the golden ratio is visible directly in the data.

---

## The kill-test discipline

Worth its own mention for the merged draft, because it is what separates this from loose
pattern-matching: the package ships deliberate kill tests, each a way the claim could fail with the
exact lost state named. Visible projection only fails. Visible commutator residual only fails. The
canonical corridor treated as the general definition of B fails. An operator word without its action
registry fails. The one passing case is a readout used only as a final report, with the standing rule
that a readout must never be fed back in as if it were the state. A claim that lists the ways it could
break, and shows them breaking on cue, is a different kind of object than a resemblance.

---

## What this section contributes, and what stays open

Contributes to the merged draft: the extreme form of the central rule, where the shadow of a change
equals the shadow of no change, which is the strongest possible statement of why the readout is not
the state; the spiral-staircase image with its exact backing, the hidden charge as swept area; and
the honest handling of (55,89), which converts a tempting number into a correct claim about a
universal attractor.

Stays open: compiling the Lean surface, the full close-read sweep of the foundational papers, the
Ancient Yi translation and line-order proof, and the Liu 2022 data.

Two guards to preserve through the merge. First, this section is internal verification, not outside
corroboration, and must not be dressed as the latter; it is the framework proving its own gate at
full strength, and that proved gate is the instrument the external sections are measured with.
Second, the connection to quantum phase is exact at the level of commutator algebra and must stop
there. The section may say the same algebra appears in quantum phase. It must not reach toward "this
is why quantum phase works," a far heavier claim these artifacts do not establish.

*Hands off to.* The hidden charge of a single swap is only the first layer of retained state. The
next section enlarges it, showing that the number of times a path has wound around, and the entire
history of the loop, are carried state the projection drops as well, before the reflexive hinge turns
the gate inward.
