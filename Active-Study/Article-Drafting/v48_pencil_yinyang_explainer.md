# v48: The Pencil Code Yin-Yang Bridge, Explained

A plain-language teaching translation of pass 54. Written to be saved and used as raw
material for a later article. Every claim is marked as either proved, found-in-code, or open.

---

## 0. The one-paragraph version

A widely used astrophysics simulation program called Pencil Code contains a feature its own
authors named the "Yin-Yang grid." It exists for a purely practical reason: to cover a sphere
with two overlapping patches so neither patch has the crowding-and-singularity problem that a
single grid hits at the poles. v48 audited that feature and found that, with no knowledge of
Phase Calculus and no connection to Taoist thought beyond the borrowed name, the code is forced
to implement the exact functional stack the project has been tracking across every other corpus:
keep the state, transform charts by a self-inverse map, complete the boundary, split vector from
scalar channels, transfer, then read out. The headline finding is narrow and hard: across a chart
boundary, the bare component numbers of a vector field are not enough information to continue the
simulation correctly. You must also retain the chart basis those numbers were written in. That is
the same projection-loss rule the project has been proving everywhere else, now demonstrated by an
independent piece of working scientific software.

---

## 1. What Pencil Code is, and why it is a good witness

Pencil Code is a real, high-performance, open-source code used for magnetohydrodynamics and
astrophysical fluid simulation. It was not written to illustrate any of this. That is exactly why
it counts as evidence. When you are testing whether a structure is real rather than imagined, the
strongest witness is a system built by people solving an unrelated problem who were forced into the
structure anyway.

The "Yin-Yang grid" name is not decoration the project added. The grid's own designers named it
after the Taijitu because the solution is two identical complementary patches, each covering the
region the other handles poorly, the way the two halves of the Taijitu each carry the seed of the
other. A modern physicist independently built a complementary-covering structure and recognized it
as yin-yang. That is convergence by independent engineering, not a borrowing or a translation.

Files inspected in this pass:

- `src/yinyang.f90` : the active interpolation and chart-transfer module
- `src/yinyang_mpi.f90` : the distributed gap and cap completion module
- `idl/lib/yin2yang_coors.pro` : the explicit coordinate transform
- `idl/lib/merge_yin_yang.pro` : the merged readout after transform
- `src/noyinyang.f90` and `src/noyinyang_mpi.f90` : dummy stand-ins used as a negative control

---

## 2. Result one: the chart transform is a clean half-turn

The coordinate transform that maps one patch onto the other is, in Cartesian coordinates:

```
T(x, y, z) = (-x, -z, -y)
```

As a matrix:

```
A = [ -1   0   0 ]
    [  0   0  -1 ]
    [  0  -1   0 ]
```

The SymPy audit and the Lean proof both confirm four properties:

| Property | Meaning in plain terms |
|---|---|
| `A^2 = I` | The transform is its own undo. Apply it twice and you are back where you started. |
| `A^T A = I` | It is rigid. No stretching, no distortion. Lengths and angles survive. |
| `det(A) = +1` | It is a proper rotation, not a mirror flip. Orientation is preserved. |
| norm residual = 0 | The length of every vector is exactly preserved. Verified symbolically, not numerically. |

Putting those together, the transform is a 180-degree rotation, a half-turn, about a fixed axis.

This is the point worth slowing down on for the article. A half-turn is the unique kind of
rotation that is its own inverse. Going from the Yin patch to the Yang patch and going from the
Yang patch back to the Yin patch are the **same operation**, not two different ones. The code
comment says it directly: there is no Yin-versus-Yang distinction in the transform, because the
matrix is self-inverse.

So the polarity here is not two separate maps glued together. It is one self-inverse map whose two
"sides" are identical. Yin and Yang are the two readings of a single involution. That matches the
deeper Phase Calculus pattern in which polarity is not two pre-existing things but the two faces of
one primitive operation.

Status: **proved** (SymPy attack `pencil_yinyang_transform_attack_v48.py`, Lean surface
`PencilYinYangTransformV48.lean`, certificate `pencil_yinyang_transform_certificate_v48.json`).

---

## 3. Result two: the vector/scalar split (this is the headline)

Inside the active interpolation code, fields are handled along two different paths depending on
what kind of field they are.

```
scalar field:  interpolate directly -> buffer
vector field:  transform to shared basis FIRST -> then interpolate -> buffer
```

A scalar field is a field of plain numbers with no direction. Temperature is the standard example.
The number 300 kelvin means the same thing in either patch. You can copy it across the boundary and
interpolate it as is.

A vector field is a field of arrows, things with direction. Velocity and magnetic field are the
examples that matter here. The catch is that a vector's three component numbers are written in the
local chart's coordinate frame. The numbers only mean something relative to that frame. Move to the
other patch, whose frame is rotated by the half-turn above, and the same three numbers now describe
a different arrow. To carry the vector across correctly you must first re-express it in the shared
basis using the transform, and only then interpolate.

The teaching analogy: a compass bearing. "Thirty degrees" is not a complete description of a
direction. It is only complete once you also know which north it was measured from. Hand someone
the number 30 with no reference north and you have handed them an incomplete state. They cannot act
on it correctly. They will point the wrong way.

This is what "not state-complete" means, stated precisely:

> The component tuple of a vector field is not state-complete across a chart boundary.
> The chart basis must be retained and transported with it.

The bare readout, the three numbers, is a **terminal projection**. It looks like the whole answer.
It is not. The information needed for the next correct step lives partly in the chart relation that
the readout dropped.

Status: **found in active code** (the branch in `yinyang.f90` that transforms vector fields before
interpolation while passing scalar fields through directly). The exact component-transform bodies
(`transform_spher_cart_yy`, `transform_thph_yy_other`) are listed as the next thing to audit, so the
mechanism is confirmed and its lowest-level Fortran detail is the open follow-up.

---

## 4. Result three: the boundary must be completed before readout

Before any field can be read out coherently, the overlap regions, gaps, and polar caps between the
two patches have to be filled in. The code does real work here. `prep_interp` retains a registry of
interpolation metadata (indices, coefficients, point coordinates, gap markers) and expands a
processor's range when the interpolation order needs neighbor support. `yinyang_mpi.f90` then
gathers the gap and cap contributions across processors and accumulates them with weights before
any summed readout is produced.

The lesson is the same one in a different costume: the readout is downstream of a completed boundary
state. You cannot read first and complete later. The retained registry of indices, weights, and gap
markers is part of the state, not part of the output.

Status: **found in active code**. Exact MPI send/receive ownership graph is open follow-up.

---

## 5. The negative control

Pencil Code ships dummy modules, `noyinyang.f90` and `noyinyang_mpi.f90`, that deliberately halt if
active Yin-Yang interpolation is requested without the real machinery. This matters for rigor. It
proves the Yin-Yang re-chart is not an optional cosmetic overlay on top of an otherwise complete
simulation. A run that genuinely needs the re-chart cannot quietly fall back to a no-op. The
chart-transfer custody is load-bearing, and the code itself draws the line between a run that needs
it and a run that does not.

Status: **found in code**. Confirming the build actually selects active-versus-dummy by config is
the open follow-up.

---

## 6. Why this connects to everything else in the project

There is one rule the whole project has been circling, and v48 is another independent instance of it:

> A readout is a terminal projection. It is valid as the carried object only if it retains enough
> state to determine the next admissible transition. Otherwise it is a lossy shadow of the real
> state, and continuing from the shadow alone produces the wrong next step.

Read across the corpora, the same rule keeps reappearing on different hardware:

| System | The tempting readout | The state it secretly drops |
|---|---|---|
| Ancient Yi | the decimal/octal/binary label | the line carrier plus digit-order convention |
| Wilhelm I Ching | the hexagram name or King Wen number | the six-line carrier plus the changing-line operation |
| MFE / Liu MHD | the diagnostic image | the full field plus boundary completion plus update law |
| Pencil Yin-Yang | the vector component numbers | the chart basis and interpolation registry |
| Orthad | the boundary channel value | the emitted walk plus q, theta, rank, and latches |

In every row the readout looks complete and is not. The missing piece is always the part needed to
take the next correct step. That recurrence, across an ancient divination system, a modern plasma
code, and the framework's own internal machinery, is the actual subject of the project. It is the
fingerprint that the projection-loss principle is a real feature of how branching, state-carrying
systems work, not a habit of one tradition.

---

## 7. What v48 proves, and what it does not

Proved, with machine-checkable artifacts:

- The Yin-Yang chart transform is a self-inverse, length-preserving, orientation-preserving
  half-turn. `A^2 = I`, `A^T A = I`, `det(A) = +1`, norm residual zero.

Found in the active source, not yet executed:

- The active interpolation path transforms vector fields to a shared basis before interpolating and
  passes scalar fields through directly. This is the state-completeness result.
- Boundary, gap, and cap state is completed and held in a retained registry before coherent readout.
- A real negative control exists that refuses to silently no-op an active re-chart run.

Open, named as next gates:

- Run or build a Pencil Yin-Yang sample if a compiler stack is available.
- Audit the exact Fortran bodies of the component transforms.
- Extract the exact interpolation ownership graph for the gap and cap MPI routes.
- Compare the Pencil boundary-completion table against the MFE boundary callback table.
- Add the chart-basis rule to the universal bridge-validation matrix.

What this is **not**: it is not a claim that Pencil Code is Phase Calculus, and it is not a claim
that Pencil Code was influenced by Taoism beyond the borrowed name. The claim is narrower and
stronger. An independent, working scientific code, written to solve a sphere-gridding problem, was
forced into the same retain-transform-complete-split-transfer-readout stack, and it independently
hit the same state-completeness wall the project has been documenting elsewhere. That is the value
of the witness: it did not know about any of this, and it did it anyway.

---

## 8. One sentence to anchor the article

A general-purpose astrophysics code, with no knowledge of Phase Calculus, proves on its own that the
visible numbers coming out of a system are not the system: to take the next correct step across a
boundary you must keep the frame those numbers were written in, and that retained frame, not the
readout, is the real state.
