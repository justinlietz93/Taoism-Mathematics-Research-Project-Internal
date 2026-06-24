# 23 — Luo 2025 Yin-Yang MFE squeeze-dry pass

Source: `Tao-Research/out/Luo_2025_ApJS_280_48.pdf`  
Title: *The Yin-Yang Magnetic Flux Eruption (Yin-Yang MFE) Code: A Global Corona Magnetohydrodynamic Code with the Yin-Yang Grid*  
Status after this pass: `COMPLETE_FIRST_PASS` for research/prospecting use.

## 0. Reunified correction before reading

Phase Calculus is still an active framework. The Phase PDFs/code in the package are snapshots. They are not the total canon and must not be used as a full closure target.

Correct comparison layer for this pass:

```text
modern computational L/re-chart engineering
not ancient-symbolic Taoism
not literal QBL identity
not proof of Phase Calculus
```

## 1. What this paper actually contributes

This is a 2025 technical description of a global corona MHD code that incorporates a Yin-Yang overset grid into the Magnetic Flux Eruption code. The paper is valuable because it is not philosophical. It is a working numerical method with:

- two overlapping partial spherical-shell domains,
- orthogonal polar axes,
- local MHD evolution in each chart,
- ghost-zone boundary exchange between charts,
- interpolation coefficients computed and stored ahead of repeated updates,
- MPI message grouping for boundary processors,
- divergence-free magnetic-field machinery,
- full-sphere test cases crossing Yin-Yang boundaries.

This gives a hard computational analogue for **L as re-chart/lift**.

## 2. Core mechanism extracted

```text
single spherical coordinate chart
  → pole/axis singularity and timestep pathology
  → split into two orthogonal overlapping partial spherical-shell domains
  → evolve each domain locally in its own coordinates
  → update ghost zones from adjacent-domain interior state
  → compute edge fields / CT updates in the receiving chart
  → preserve global solution coherence across chart crossing
  → only then project / visualize / measure global physical solution
```

This is a much stronger match than “Yin-Yang looks like two halves.” The relevant structure is **legal continuation by overlapping chart custody**.

## 3. L-class interpretation

The paper strengthens the L-side of the project:

```text
L analogue:
  when one coordinate chart is pathological or insufficient,
  do not force continuation in the singular chart;
  introduce a second legal domain with different axis orientation;
  communicate only through overlap/interpolation;
  preserve retained global field coherence.
```

This maps cleanly to:

```text
Phase/QBL:
  blocked or saturated local continuation
  → re-chart / host lift
  → retained state survives across domain change
  → projection is downstream
```

Important: this paper does not provide B floor-anchor arithmetic. Its value is L/re-chart engineering.

## 4. Key algorithmic pieces

### 4.1 Governing system

The code solves single-fluid semirelativistic MHD with nonadiabatic corona terms:

- continuity,
- momentum,
- induction,
- divergence constraint,
- internal energy,
- ideal gas law,
- electric field relation,
- Boris/semirelativistic correction,
- nonadiabatic energy terms.

The nonadiabatic terms include:

- field-aligned electron heat conduction,
- optically thin radiative cooling,
- empirical coronal heating,
- numerical viscous/Ohmic heating.

### 4.2 Staggered retained placement

The code uses a staggered grid:

- scalar quantities at finite-volume cell centers,
- velocity and magnetic field components on cell faces,
- electric field and current density at cell edges.

Mechanism read:

```text
state placement matters.
projection from one location cannot substitute for retained staggered custody.
```

This resonates with the project rule that the channel field/state must exist before scalar readout.

### 4.3 Reconstruction and admissible local update

The code implements monotonic reconstruction:

- PLM: piecewise linear method,
- PDM: partial donor cell / fourth-order method,
- limiters to prevent nonphysical oscillations.

Mechanism read:

```text
local update is not arbitrary interpolation;
it is constrained by admissibility/monotonicity.
```

This is not B, but it belongs to the broader “admitted local operation” pattern.

### 4.4 Lorentz-force formulation and divergence warning

The paper explicitly avoids a Maxwell-stress divergence form for the Lorentz force because divergence error can introduce unphysical field-aligned forces. It formulates the Lorentz force directly as j × B to minimize field-aligned error.

Mechanism read:

```text
wrong projection/formulation injects spurious force along a forbidden channel.
```

This is a strong caution for Phase/Shadow comparisons:

```text
compare retained channel mechanics first;
do not force a scalar/projection form that injects false structure.
```

### 4.5 Constrained transport

The code uses constrained transport to maintain ∇·B to round-off/machine precision.

Mechanism read:

```text
closure constraint is maintained by update geometry,
not repaired afterward by scalar cleanup.
```

This is directly analogous to the rule:

```text
state coherence before projection.
```

### 4.6 Hyperbolic heat conduction

The code replaces the restrictive parabolic conduction timestep with a hyperbolic heat-conduction treatment, with a smooth transition from collisional Spitzer-like heat flux to collisionless heat flux at larger radius.

Mechanism read:

```text
stiff process is lifted into an evolution law that remains compatible with the dynamic timestep.
```

This is not a direct Q/B/L match, but it is an important modern example of **changing representation to preserve lawful continuation**.

### 4.7 Ghost-zone update and MPI communication

This is the key L evidence.

The implementation computes and stores interpolation coefficients at the beginning. It groups ghost zones into MPI messages by:

- sender,
- receiver,
- size,
- data-buffer location.

At each timestep, ghost-zone primitive variables are updated by bilinear interpolation from overlapping interior zones in the adjacent Yin or Yang domain.

Mechanism read:

```text
chart transition is not selected ad hoc at runtime;
the overlap routes/coefficient structure is compiled;
then each time step executes deterministic boundary custody.
```

This matches the corrected Orthad/QBL split:

```text
QBL custody selects/adjudicates primitive motion.
Orthad lens compiles the accrued word.
Projection reads afterward.
```

For Yin-Yang MFE:

```text
retained field state evolves locally;
boundary/ghost update keeps cross-chart state coherent;
visual/global output comes afterward.
```

## 5. Verification tests and what they establish

The paper validates the code with multiple tests:

### 5.1 Nonlinear circularly polarized Alfvén waves

Purpose:

```text
smooth nonlinear MHD wave propagation;
multidirectional flux behavior;
convergence.
```

Research value:

```text
checks that local update does not corrupt a coherent propagating structure.
```

### 5.2 Brio-Wu shock tube

Purpose:

```text
nonlinear MHD shock handling.
```

Research value:

```text
distinguishes reconstruction choices under discontinuity.
PDM behaves more robustly than PLM in the reported comparison.
```

### 5.3 Orszag-Tang vortex

Purpose:

```text
shock formation and interaction;
magnetic island / current-sheet structure;
low numerical diffusion.
```

Research value:

```text
fine structure is preserved if the admissible local update is strong enough.
```

### 5.4 3D magnetic field-loop advection across Yin-Yang boundaries

Purpose:

```text
directly test whether a magnetic structure survives chart crossing.
```

The test is especially important because the field loop crosses Yin-Yang boundaries marked in the figures.

Research value:

```text
this is the hard L-boundary test:
if chart crossing corrupts retained structure, the method fails.
reported result: loop is preserved after crossing Yin-Yang boundaries.
```

This is the strongest single test for the project’s L/re-chart prospecting.

### 5.5 Global solar wind with dipole magnetic field

Purpose:

```text
full global corona / solar-wind simulation under simple solar-minimum-like magnetic conditions.
```

Research value:

```text
demonstrates that the re-chart system can carry a large physical state into a quasi-steady global solution.
```

## 6. Strongest Phase-relevant extraction

```text
Single-chart failure is not solved by forcing the singular chart.
It is solved by adding a second lawful chart with overlap.
The overlap is not decorative; it is the actual custody interface.
Ghost cells are the boundary memory through which each chart keeps coherence with the other.
Projection/global visualization is downstream of the retained two-chart state.
```

This is one of the best external computational analogues for:

```text
L = lawful continuation into a new host/chart when current continuation saturates or becomes pathological.
```

## 7. What this paper does not establish

```text
No B floor-anchor formula.
No Q six-position carrier.
No Yijing mapping.
No Shadow η/θ/χ12 mapping.
No direct Phase Calculus proof.
```

It should not be overused. It is an L/re-chart and retained-state-coherence paper.

## 8. Mechanism ledger update

```text
Yin-Yang MFE / Luo 2025:
  Category: L-class hard computational analogue
  Strength: high
  Mechanism:
    single chart blocked by singularity/timestep pathology
    two overlapping orthogonal charts introduced
    local evolution inside each chart
    ghost-zone interpolation from adjacent chart
    CT preserves divergence-free state
    global projection after retained coherence
  Use:
    strong external evidence for re-chart/lift mechanics
  Do not use for:
    B anchor arithmetic or exact Q carrier mapping
```

## 9. Follow-on work order

1. Compare Luo 2025 against the earlier Kageyama/Yoshida Yin-Yang papers as a lineage:

```text
Kageyama 2004: grid principle
Yoshida 2014: visualization/projection caution
2508.08210v2: Yin-Yang-MFE implementation concept
Luo 2025: full algorithmic MHD code reference
```

2. Inspect whether the included source package has any implementation of the Luo 2025 ghost-zone compile/update machinery. Current status says no: included `MFE_pub-main` appears to be base MFE lineage, not full Yin-Yang-MFE.

3. Continue with `mwre-mwr-d-12-00108.1.pdf`, because it likely gives another operational Yin-Yang grid example in weather/atmospheric computation.
