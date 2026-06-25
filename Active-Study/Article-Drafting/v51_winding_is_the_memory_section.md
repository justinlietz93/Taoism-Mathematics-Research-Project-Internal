# Section: The Winding Is the Memory (v51)

*Role in the larger piece.* This section sits between the hidden-order section and the reflexive
hinge, despite arriving later in the work, because it deepens the carried-state content one more turn
before the gate is turned inward. The hidden-order section showed that a single swapped pair hides a
charge the projection cannot see. This section shows something larger is hidden: the number of times
a path has wound around, and the entire history of the loop, are carried state too. It is internal,
the framework verifying its own core, not an outside witness, and that line must survive the merge.
It assumes the shared rule and the running cross-corpus table from the outside-witness section, and
its contribution is to enlarge what counts as the retained state: not just instantaneous coordinates,
but winding, sheet, and the loop's own history.

---

## From a hidden charge to a hidden history

The previous section left the retained state as a hidden number, the swept area of one swap. This
section adds three more things to the register that the visible projection also throws away:

```
sheet            which copy of the space you are on
kappa / winding  how many times you have gone around
history          the actual word of the loop you walked
```

Plus the generator and action table that says what each move does. The claim v51 proves executably is
blunt:

> The same stripped visible projection does not imply the same full lifted-register transition.

Two processes can look identical at the readout and be in genuinely different states, because one of
them went around more times, or walked a different path to get there.

---

## Result one: the double cover, where winding is the memory

The cleanest witness is the squaring map, `z -> z^2`, taken over the nonzero complex numbers. This is
a genuine two-to-one cover: the target is wrapped twice by the source. Track a loop by three things,
the visible sheet it ends on, the winding count `kappa`, and the history word:

```
empty loop:     sheet 0,  kappa 0,  history []
one turn (g):   sheet 1,  kappa 1,  history [g]
two turns (gg): sheet 0,  kappa 2,  history [g, g]
```

Read the first and last lines. The two-turn loop ends on the same visible sheet as the empty loop,
sheet 0. By the visible projection alone, nothing happened, same as doing nothing at all. But the
two-turn loop has winding 2 and history `[g, g]`. Same shadow, different retained state. The package
flags the lost coordinates exactly: `kappa`, `sheet`, `history`.

The teaching image, and one deliberately different from the spiral staircase used earlier so the two
sections do not blur: Dirac's belt trick. Hold a belt fixed at one end and rotate the buckle a full
turn. The buckle looks exactly as it did, but the belt now carries a twist. Rotate a second full turn
and, surprisingly, the belt can be untwisted without turning the buckle back. The buckle's visible
orientation cannot tell zero turns from one turn. The belt can. The twist is the winding, and it is
real, physical, retained state that the buckle's face does not show. This is not a loose analogy. The
double cover here is the same two-to-one structure that makes the belt trick work and that
distinguishes a 360-degree turn from rest in the physics of spin.

Note one detail worth keeping for the foundational section: the state being lifted in these witnesses
carries the canonical anchor, `q = (55, 89)`, `c = (..., 4895)`. The monodromy register is stacked on
top of the same Farey anchor the rest of the essay tracks, so this is not a separate gadget. It is the
same carried object gaining a winding coordinate.

Status: proven. Double-cover CLI certificate passes, SymPy audit passes, seven tests pass. The Lean
surface is indexed but not compiled in this environment. Report it that way.

---

## Result two: the quintic commutator, where order is the memory

The second witness uses a five-sheet branch presentation with two generators, `a` and `b`. Take the
commutator, the round trip "do a, do b, undo a, undo b":

```
[a, b] = a b a^-1 b^-1
permutation = [0, 2, 4, 3, 1]
cycle = (1 2 4)
is_identity = false
```

If `a` and `b` commuted, that round trip would cancel to nothing and return you home. It does not. It
leaves a three-cycle. The order in which the moves happened is still legible in the end state even
though every move was apparently undone. Order is retained state, not display metadata.

The teaching image: a round trip that does not bring you home. Walk a, then b, then a backward, then b
backward. On a flat commuting world you are back at the door. Here you are three doors over, and which
three tells you the order you walked. The displacement is the memory.

Now the resonance, marked carefully because it is the reason this particular witness was chosen, and
because it must not be overstated. The proven fact is local: this commutator is non-identity and
leaves the cycle (1 2 4). The larger structure it gestures at is the classical theorem that the
general quintic cannot be solved by radicals. That theorem is, at its core, a statement about exactly
this: the monodromy group of the five roots around the branch points is non-abelian and non-solvable,
so no finite tower of radical readouts can reconstruct the roots. "Solvable by radicals" means the
answer reduces to a sequence of simple readouts. "Unsolvable" means it does not, because the
path-history carries irreducible non-commutative structure that no flat readout sequence can replace.
Read through this essay's lens, the unsolvability of the quintic is a projection-loss theorem two
centuries old: the visible roots are not state-complete, and the retained monodromy is what they drop.

The boundary to hold in the merge: the package proves the small fact, a non-identity commutator on a
five-sheet presentation. The connection to Abel and Ruffini and Galois is the meaningful resonance
that explains why the witness matters, not a claim the package re-proves the unsolvability theorem. State
the small fact as proved and the large connection as the reason it was chosen, and the section stays
honest.

Status: proven for the local commutator fact. The Galois connection is named as resonance, not as a
re-derivation.

---

## Why this sharpens the whole essay

The contribution to the running rule is to enlarge the retained register. After this section, "the
state" provably includes sheet, winding, loop history, and the generator and action table, alongside
the coordinates earlier sections established. None of these are optional proof decoration. They are
what the next admissible transition depends on.

It also supplies the sharpest internal negative control for the Orthad ordering rule that the
reflexive section will lean on. Orthad insists that the lifted state and the emitted walk come first,
the readout second, the external scalar comparison last. Monodromy as memory proves why the readout
cannot be promoted to author the state:

```
the quotient or readout may be lawful;
the quotient or readout may even commute;
the quotient or readout still need not be injective;
therefore the readout cannot author custody.
```

A readout can be perfectly well-behaved and still collapse distinct histories onto the same value.
That is the whole reason it is a readout and not the state.

---

## What this section contributes, and what stays open

Contributes to the merged draft: the enlargement of the retained register to include winding and
history; the belt-trick image, which carries "the endpoint looks identical but the winding is real"
in one picture; and the quintic witness, which connects the essay's central rule to one of the
oldest deep results in algebra, giving the whole argument a long historical root.

Stays open: compiling the Lean surface, the Ancient Yi translation and line-order proof, the active
selector and floor source still on local storage, and the Liu 2022 plasma data.

Two guards to preserve through the merge. First, this is internal verification, not outside
corroboration; it proves the framework's own gate at full strength and must not be dressed as an
independent system agreeing. Second, the quintic connection is exact only at the level of the proven
commutator. The unsolvability of the quintic is the resonance that makes the witness worth choosing,
not something these artifacts establish on their own. Keep that line bright.

*Hands off to.* With the retained register now grown to its full size, including winding and history,
and with the internal proof that a lawful readout still cannot author the state, the essay is ready
for the reflexive hinge, where this same gate is turned on Phase Calculus's own foundational text and
cuts one of its own older operators.
