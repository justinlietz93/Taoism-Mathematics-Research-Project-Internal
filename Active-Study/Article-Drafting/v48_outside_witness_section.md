# Section: An Outside Witness, Pencil Code (v48)

*Role in the larger piece.* This is the essay's first deep corpus section and its most accessible
one, so it doubles as the reader's entry into the central pattern. It carries the strongest kind of
evidence the essay offers, a system built by people who never heard of any of this and were forced
into the same structure anyway, and it introduces the two things every later section leans on: the
shared rule, stated once here, and the running cross-corpus table, which later sections deepen one
row at a time. Merge it early, ahead of the internal and reflexive sections.

---

## The rule the whole essay runs on

State it once, here, so the rest of the piece can refer back rather than repeat:

> A readout is a terminal projection. It is the real carried state only if it retains enough to
> determine the next admissible transition. Otherwise it is a lossy shadow, and continuing from the
> shadow produces the wrong next step.

Every corpus the essay examines is a place where this rule holds on unfamiliar hardware. The pattern,
as a roadmap for what follows:

| System | The shadow that looks complete | The retained state it drops |
|---|---|---|
| Ancient Yi | the octal or decimal label | the line carrier plus digit-order convention |
| Wilhelm I Ching | the hexagram name or number | the six-line carrier plus the changing-line operation |
| MFE / Liu MHD | the diagnostic image | the full field, boundary callbacks, nonideal channels |
| Pencil Yin-Yang | the vector component numbers | the chart basis and interpolation registry |
| Non-Commutative Phase Geometry | the visible projection | the hidden order charge, the swept area |
| Corrected Orthad | the boundary readout | q, theta, rank, axis, latches, and the emitted word |

This section takes the Pencil row. Later sections take the others. The table is not restated in full
again; sections add or sharpen a single row.

---

## Why Pencil Code is the witness that counts

Pencil Code is a real, high-performance, open-source code used for magnetohydrodynamics and
astrophysical fluid simulation. It was not written to illustrate any of this, and that is exactly
why it is the strongest witness in the essay. When you are testing whether a structure is real
rather than imagined, the best evidence is a system built by people solving an unrelated problem who
were forced into the structure anyway.

The feature in question is one the code's own authors named the Yin-Yang grid. It exists for a
practical reason: to cover a sphere with two overlapping patches so neither has the crowding and
singularity a single grid hits at the poles. The name is not something this project added. The
grid's designers named it after the Taijitu because the solution is two identical complementary
patches, each covering the region the other handles poorly. A modern physicist independently built a
complementary-covering structure and recognized it as yin-yang. That is convergence by independent
engineering, not borrowing or translation, and it is the note to carry into the merged draft: the
witness did not know about any of this and did it anyway.

---

## Result one: the chart transform is a clean half-turn

The transform mapping one patch onto the other is, in Cartesian coordinates, `T(x,y,z) = (-x,-z,-y)`,
the matrix

```
A = [ -1   0   0 ]
    [  0   0  -1 ]
    [  0  -1   0 ]
```

The SymPy attack and the Lean surface confirm four properties:

| Property | Meaning in plain terms |
|---|---|
| `A^2 = I` | the transform is its own undo; apply it twice and you are back to start |
| `A^T A = I` | it is rigid; no stretching, lengths and angles survive |
| `det(A) = +1` | it is a proper rotation, not a mirror flip |
| norm residual = 0 | every vector's length is exactly preserved, verified symbolically |

Together these say the transform is a 180-degree rotation, a half-turn, about a fixed axis. The point
worth slowing down on is that a half-turn is the unique rotation that is its own inverse. Going from
the Yin patch to the Yang patch and going back are the same operation, not two different ones. The
code comment says it directly: there is no Yin-versus-Yang distinction in the transform, because the
matrix is self-inverse. The polarity here is one self-inverse map whose two sides are identical, the
same polarity-as-one-operation shape the foundational reading finds in CF000. The later section on
non-commutative geometry sharpens this from a self-inverse half-turn, where order does not matter,
into genuine non-commutation, where it does; the two sections are a deliberate progression and should
be merged in that order.

Status: proved. SymPy attack, Lean surface, and JSON certificate all pass.

---

## Result two: the vector/scalar split, the row's core

Inside the active interpolation code, fields take two different paths depending on what kind of field
they are:

```
scalar field:  interpolate directly -> buffer
vector field:  transform to shared basis FIRST -> then interpolate -> buffer
```

A scalar field is a field of plain numbers with no direction, temperature being the standard example.
The number means the same thing in either patch, so it can be copied across and interpolated as is.

A vector field is a field of arrows, things with direction, like velocity or magnetic field. Its
three component numbers are written in the local chart's frame, and the numbers only mean something
relative to that frame. Move to the other patch, whose frame is rotated by the half-turn above, and
the same numbers describe a different arrow. To carry the vector across correctly you must first
re-express it in the shared basis, then interpolate.

The teaching image, and the one to keep for the merged draft because it carries the whole idea: a
compass bearing. "Thirty degrees" is not a complete description of a direction. It is complete only
once you also know which north it was measured from. Hand someone the number with no reference north
and you have handed them an incomplete state. They cannot act on it. They will point the wrong way.

That is what "not state-complete" means, stated precisely: the component tuple of a vector field is
not state-complete across a chart boundary; the chart basis must be retained and transported with it.
The bare numbers look like the whole answer and are not.

Status: found in the active source. The branch that transforms vectors before interpolating while
passing scalars through directly is confirmed; the exact Fortran transform bodies are the named
follow-up, so the mechanism is established and only its lowest-level detail is open.

---

## Boundary completion and the negative control

Two smaller findings reinforce the same row. Before any field is read out, the overlap regions, gaps,
and polar caps between the patches must be filled. The code retains a registry of interpolation
metadata, indices, coefficients, gap markers, and gathers the gap and cap contributions across
processors with weights before any summed readout. The readout is downstream of a completed boundary
state; the retained registry is part of the state, not part of the output.

And the code ships dummy modules that deliberately halt if active Yin-Yang interpolation is requested
without the real machinery. This proves the re-chart is not an optional cosmetic overlay. A run that
needs it cannot silently fall back to a no-op. The chart-transfer custody is load-bearing, and the
code itself draws the line.

Status: found in code. The exact MPI ownership graph and the build-config selection are named
follow-ups.

---

## What this section contributes, and what stays open

Contributes to the merged draft: the entry point and the roadmap table; the strongest evidence type
in the essay, an unrelated working code forced into the same stack; the half-turn result as the first
appearance of polarity-as-one-operation; and the compass-bearing image, which is the cleanest single
carrier of the state-completeness idea for a general reader.

Stays open: the exact component-transform Fortran bodies, the MPI gap and cap ownership graph, the
comparison of Pencil's boundary-completion table against the MFE one, and an actual build-and-run if a
compiler stack becomes available.

A correction guard to preserve through the merge: do not let this section drift into "Pencil Code
shows Taoism is physics." The witness logic is narrower and the narrowness is the strength. An
unrelated code hit the same wall on its own. State exactly that and the claim holds. Inflate it and
you hand a critic the easy dismissal.

*Hands off to.* With the rule stated, the table laid out, and the most accessible witness in hand,
the essay can move to the internal sections that sharpen the rule toward its extreme form, beginning
with the non-commutative core where the same polarity stops being a simple self-inverse and starts
keeping a hidden score.
