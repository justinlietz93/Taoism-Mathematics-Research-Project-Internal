# 22 — Phase Snapshot Rule + Yin-Yang MFE Squeeze-Dry Pass

## Pass objective

Continue the in-progress research without treating available Phase Calculus documents as the whole system.
This pass deliberately separates:

```text
Phase Calculus available documents = versioned evidence / current visible snapshot
Phase Calculus itself              = actively developing framework / larger evolving object
```

This matters because contradictions against stale or partial Phase documents are not verdicts against the framework.
They are version-bound deltas to carry until the newer HDD source is available.

---

## Locked methodological correction

```text
PHASE_DOCS_ARE_SNAPSHOTS_NOT_TOTALITY
```

Use internal Phase PDFs/code as:

```text
available state evidence
implementation witnesses
older formal surfaces
partial theorem trail
```

Do not use them as:

```text
final frozen canon
complete latest Phase Calculus
basis for kicking unresolved/stale layers
```

Updated contradiction label:

```text
STALE_OR_PARTIAL_PHASE_SOURCE_DELTA
```

instead of:

```text
Phase Calculus failure
```

---

# Resource squeezed: `Tao-Research/out/2508.08210v2.pdf`

## Bibliographic identity

Title:

```text
The Yin-Yang Magnetic Flux Eruption (Yin-Yang-MFE) Code:
A Global Corona Magnetohydrodynamic Code with the Yin-Yang grid
```

Authors:

```text
Hongyang Luo and Yuhong Fan
```

Draft date in text:

```text
September 22, 2025
```

arXiv line in text:

```text
arXiv:2508.08210v2 [astro-ph.SR] 5 Sep 2025
```

Coverage status:

```text
COMPLETE_FIRST_PASS
```

---

## What the paper actually contributes

This paper is not a Taoist-symbolic paper. It is a modern numerical-methods paper.
Its importance is that it gives a cutting-edge computational implementation of the same **L-class problem**:

```text
single coordinate chart becomes numerically pathological
→ full-domain continuation cannot remain lawful in that chart
→ introduce paired orthogonal overlapping domains
→ update ghost-zone boundary values by interpolation from the neighboring chart
→ keep the global physical field coherent through chart handoff
```

This is a hard engineering analogue for re-chart / lift / retained-state coherence.

---

## Direct technical core extracted

### 1. Full-sphere single-chart failure

Conventional spherical meshes suffer from:

```text
grid anisotropy near the axis
coordinate singularity near the poles
severe time-step restriction near the poles
```

This is not cosmetic. It is an admissibility failure: the local chart becomes a bad host for global continuation.

### 2. Two-domain orthogonal patch solution

The Yin-Yang grid is described as:

```text
two identical overlapping partial spherical shell domains
with r-theta-phi grids
with orthogonal polar axes
covering the whole sphere
```

Each component solves the MHD equations in its own spherical coordinate system.
The global field is retained across the pair rather than forced through one singular chart.

### 3. Overlap width as legal continuation margin

The paper sets each patch domain approximately as:

```text
π/4 - δ ≤ θ ≤ 3π/4 + δ
-3π/4 - δ ≤ φ ≤ 3π/4 + δ
```

with δ slightly greater than half the larger cell size.

Mechanism read:

```text
The overlap is not decoration.
It is the legal handoff margin where the adjacent chart can supply boundary state.
```

### 4. Ghost-zone update = retained-state boundary transfer

Primitive variables in ghost zones are updated by:

```text
bilinear interpolation into overlapping interior zones
of the adjacent Yin/Yang domain
```

Electric fields in ghost zones are then computed from those interpolated primitive variables.

Mechanism read:

```text
projection/local computation continues inside each chart,
but boundary legality is supplied by retained state in the paired chart.
```

### 5. Communication schedule is precompiled

At initialization the code:

```text
computes interpolation coefficients once
stores them
pre-groups ghost zones into message records
records senders, receivers, sizes, buffer locations
```

At runtime each time step performs the required MPI communication.

Mechanism read:

```text
The chart-handoff law is compiled before runtime, then executed repeatedly.
This is very close to “lens compiled from word” at the architecture level,
but here applied to numerical boundary routing rather than Orthad readout.
```

### 6. Validation of chart-crossing coherence

The 3D magnetic field loop advection test is important because the field loop crosses Yin-Yang boundaries.
The paper reports that the loop remains well preserved after crossing those boundaries.

Mechanism read:

```text
The test directly checks whether retained physical structure survives chart transition.
This is a hard numerical analogue of L preserving carried structure through a host change.
```

### 7. Active-development status

The paper explicitly states Yin-Yang MFE remains under active development, with new physics capabilities and algorithmic improvements being integrated.

This reinforces the project-method correction:

```text
Do not treat one visible formal document/code snapshot as the whole living framework.
```

---

# Codebase inspection: `code/MFE_pub-main/`

## Important correction

The provided `MFE_pub-main` source tree appears to be the older/base MFE code, not the full Yin-Yang-MFE implementation described in `2508.08210v2.pdf`.

Evidence from the local source tree:

```text
README.txt describes the Magnetic Flux Eruption MHD code generally.
It references Fan (2017), Mac/openmpi test setup, Orszag-Tang tests, output readers.
A full recursive grep for Yin/Yang/Yin-Yang/overlap/Kageyama/bilinear coefficients found no Yin-Yang implementation markers.
```

So the code tree is still useful, but not as direct proof of the 2025 Yin-Yang implementation.

Correct status:

```text
MFE_pub-main = base MFE source witness
2508.08210v2 = paper-level witness for Yin-Yang-MFE extension
full Yin-Yang-MFE source = not present in provided tree, unless hidden elsewhere
```

## Module inventory inspected

```text
ModGrid.F             grid arrays, ghost-zone indexing constants, metric coefficients
ModBoundary.F         boundary storage arrays for variables and EMF components
ModInterp.F           interpolation and MPI boundary exchange utilities
ModBval.F             major boundary-value exchange/apply machinery
main.F                MPI setup, time loop, output, performance counters
python/pyMFE.py       output/grid/physical-parameter reader; data includes ghost zones
README.txt            base-code purpose and run instructions
```

## Code mechanics relevant to research

### A. Ghost zones are physically real in the data layout

`ModGrid.F` sets interior index starts at 3 and creates `ism2`, `ism1`, `iep1`, `iep2`, `iep3`, etc.
This confirms a two-or-more layer ghost-zone architecture.

Mechanism read:

```text
The state domain includes non-interior support layers.
A computation is not just visible interior cells;
it includes boundary support required for lawful continuation.
```

### B. Boundary exchange uses paired send/receive buffers

`ModInterp.F` and `ModBval.F` use send/receive buffers and MPI nonblocking calls:

```text
MPI_IRECV
MPI_ISEND
MPI_WAITALL
reshape(sendtop/sendbot)
reshape(recvtop/recvbot)
```

Mechanism read:

```text
boundary state is not recalculated from nowhere.
it is transferred through an explicit paired boundary protocol.
```

### C. `pyMFE.py` preserves the warning that output data contain ghost zones

The Python reader says the `.dat` files contain ghost zones, and its `getdata` layer later strips to physical units inside domain.

Mechanism read:

```text
projection/readout can hide ghost-zone support,
but the retained computational state included it.
```

This is useful for the Orthad/projection doctrine:

```text
terminal visible readout is smaller than retained state.
```

---

# Reunified interpretation after this pass

The current strongest live mechanism becomes:

```text
single visible coordinate representation fails at a boundary/singularity/floor;
retained state must include extra structure beyond the visible interior;
a paired/orthogonal host supplies legal continuation;
transition values are transferred through a compiled boundary law;
only after retained coherence is preserved may the system project useful visible fields.
```

This is a major L-side reinforcement and also clarifies the Q/B side by contrast:

```text
QBL custody decides admissible primitive movement.
Orthad lens compiles the already-accrued word.
Yin-Yang-MFE is an external computational analogue for L-style host re-chart,
not a direct analogue for the Orthad lens selector.
```

---

# Updated confidence impact

```text
L / re-chart support: increased strongly
Projection-after-retention doctrine: increased
Modern cutting-edge research support: increased
B-floor support: neutral in this pass
Yijing six-line support: neutral in this pass
Shadow eta/theta support: neutral in this pass
```

---

# New work orders

```text
YY-MFE-1:
  Determine whether the actual 2025 Yin-Yang-MFE source is present elsewhere in the package.

YY-MFE-2:
  If not present, treat MFE_pub-main as base-code lineage only.

YY-MFE-3:
  Continue with Luo_2025_ApJS_280_48.pdf next because it likely connects the Yin-Yang-MFE code to boundary-data-driven solar eruption modeling.

YY-MFE-4:
  Inspect ModBval.F more deeply for how boundary-value updates preserve staggered vector/scalar placement.

YY-MFE-5:
  Cross-map ghost-zone retention to Orthad “channel field before terminal projection.”
```
