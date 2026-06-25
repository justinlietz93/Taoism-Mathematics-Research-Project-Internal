# 24 - Hall & Nair 2013 DG Yin-Yang transport squeeze-dry pass

Source: `Tao-Research/out/mwre-mwr-d-12-00108.1.pdf`  
Title: *Discontinuous Galerkin Transport on the Spherical Yin-Yang Overset Mesh*  
Status after this pass: `COMPLETE_FIRST_PASS` for research/prospecting use.

Rendered review: `renders/mwre_mwr_d_12_00108_1/` generated at 110 DPI for visual/figure sanity check.

## 0. Reunified frame before reading

This paper continues the hard computational Yin-Yang grid branch. It should be read as modern numerical-method evidence for **L / re-chart / overlap custody**, not as direct evidence for B anchor arithmetic or Yijing Q carrier mapping.

Correct comparison layer:

```text
single coordinate continuation failure
  -> overlapping complementary charts
  -> cached chart-to-chart boundary map
  -> local high-order continuation inside each chart
  -> ghost-surface boundary values from adjacent chart interior
  -> global scalar projection / conservation checked afterward
```

This paper adds a distinct layer not fully covered by Luo 2025:

```text
Luo 2025:
  MHD code, ghost zones, constrained transport, global corona simulation.

Hall & Nair 2013:
  discontinuous Galerkin scalar transport,
  overset boundary flux construction,
  high-order local polynomial interpolation,
  explicit analysis of mass-conservation leakage at chart handoff.
```

## 1. What the paper contributes

The paper implements a discontinuous Galerkin transport scheme on a spherical Yin-Yang overset mesh. The Yin-Yang grid is two notched longitude-latitude meshes placed at right angles with small overlap. The DG method supplies local polynomial representation and high-order interpolation, letting overset boundary values be obtained from the interior of a single complementary-grid element instead of constructing a wide finite-volume halo.

Core contribution for this project:

```text
boundary legality is not imposed by global projection;
it is supplied by a cached local map from the adjacent chart's retained interior state.
```

That makes this a cleaner L/re-chart paper than a symbolic Yin-Yang paper.

## 2. Grid mechanics

### 2.1 YY mesh

The sphere is covered by two overlapping regions:

```text
S = Y union Y'
```

- `Y` is a notched longitude-latitude low-latitude region.
- `Y'` is identical but rotated at right angles.
- the two grids overlap at the edges.
- minimum overlap parameter `delta` must be nonzero.
- Yang Cartesian axes satisfy:

```text
(x', y', z') = (-x, z, y)
```

This is the same coordinate transform already found in `yinyang_transform.py`.

Project interpretation:

```text
L-class re-chart:
  same sphere / same physical field,
  different legal coordinate host,
  carried state crosses only through overlap.
```

### 2.2 YY-P mesh

The paper also tests a Yin-Yang polar variant:

```text
Yin equatorial region extended over all longitude;
Yang split into north and south polar caps.
```

This is useful because it shows that the re-chart architecture is not one fixed aesthetic diagram. It is a family of coverage decompositions tuned to flow geometry.

Project implication:

```text
L is not “the one picture.”
L is the admissible host change that preserves continuation when the previous chart is insufficient.
```

## 3. Transport and DG method

The PDE is conservative scalar transport on the sphere:

```text
dc/dt + div(F) = 0
F = c * velocity
```

The paper writes the divergence in longitude-latitude coordinates and then discretizes with nodal DG on elements using Gauss-Lobatto-Legendre nodes.

Relevant mechanics:

```text
state is retained locally inside each element;
solution may be discontinuous at element boundaries;
boundary coupling happens through numerical flux;
flux is selected by a Riemann/upwind rule.
```

This is useful because it gives a computational analogue for **local custody with explicit boundary law**.

Do not over-map this to B. The admissibility here is numerical-flux admissibility, not the Phase B floor-anchor.

## 4. Overset boundary implementation - key extraction

This is the most important part of the paper.

For a boundary node on Yin:

1. transform the Yin boundary point into Yang coordinates;
2. find the Yang element containing that point;
3. map that point into the Yang reference element;
4. cache that element/reference-node association once at startup;
5. at every timestep interpolate scalar values from Yang interior using DG Lagrange polynomials;
6. transform velocity components into the receiving coordinate system;
7. store these values in a **ghost surface** representing the missing neighbor element;
8. apply the usual Riemann solver to compute boundary flux.

Compressed grammar:

```text
boundary node in chart A
  -> transform into chart B
  -> locate containing retained element in chart B
  -> cache reference coordinates
  -> interpolate from chart B interior state
  -> transform vector components back to chart A
  -> populate ghost surface
  -> compute local flux in chart A
```

This is a precise L/re-chart mechanism:

```text
not global remeshing;
not scalar projection;
not symbolic complement;
not candidate search.

It is deterministic chart-to-chart custody through a cached overlap map.
```

## 5. The ghost-surface distinction

Luo 2025 emphasized ghost **zones** for MHD primitive variables. Hall & Nair 2013 uses a ghost **surface** for boundary flux in DG transport.

That distinction matters:

```text
finite-volume/MHD version:
  ghost cells/zones preserve neighboring state values.

DG transport version:
  ghost surface supplies boundary flux values for a missing neighbor.
```

Both are L-class, but they are not identical implementations. The common mechanism is:

```text
chart A cannot compute boundary law from itself alone;
chart B's retained interior supplies the missing boundary information.
```

## 6. Conservation warning - critical constraint

The paper is explicit that the straightforward overset implementation is **not strictly mass conserving** without additional constraints.

Why:

```text
on conforming mesh:
  flux leaving one element equals flux entering neighbor.

on overset boundary:
  flux leaving Yin and flux entering Yang are spatially separated by overlap distance;
  they need not exactly cancel.
```

The observed mass errors in the Gaussian test were small, but nonzero. The paper points to Peng et al. 2006 as evidence that local constraints can restore exact conservation in finite-volume Yin-Yang grids, and suggests a similar elementwise constraint should be possible for DG.

Project implication:

```text
L/re-chart alone is not enough.
A conservation/closure law must be attached at the boundary if the carried quantity is conserved.
```

This is an important red-team addition for Phase/Orthad comparisons:

```text
retained-state coherence before projection is necessary,
but not automatically sufficient;
boundary handoff must preserve the relevant invariant.
```

## 7. Performance tests and what they establish

### 7.1 Gaussian solid-body rotation

Purpose:

```text
smooth scalar field crosses Yin-Yang overset boundaries.
```

Findings:

- errors remain small;
- no significant error increase is visible at boundary crossings;
- p-refinement gives spectral/exponential convergence for smooth data;
- high polynomial order strongly outperforms merely increasing element count for smooth data.

Mechanism read:

```text
high-order local retained representation makes chart crossing nearly invisible for smooth fields.
```

### 7.2 Mass conservation diagnostic

Purpose:

```text
check whether conservative transport stays globally conservative across overset boundary.
```

Finding:

```text
small but nonzero mass error remains without extra local constraint.
```

Mechanism read:

```text
projection-level success can hide invariant leakage.
```

This is relevant to the Phase project: an apparent structural match is not enough unless the conserved/latched channel is checked.

### 7.3 Cosine bell

Purpose:

```text
less smooth C1 field; standard global advection benchmark.
```

Findings:

- convergence becomes geometric rather than spectral;
- higher-order elements still help, but with diminishing return.

Mechanism read:

```text
the legal refinement benefit depends on regularity of the retained field.
```

This is a useful caution against assuming every Phase projection will show the same convergence or smooth transformation behavior.

### 7.4 Moving vortices

Purpose:

```text
harder deformational atmospheric flow / idealized cyclone test.
```

Findings:

- numerical solution remains close to analytic solution;
- Yin-Yang boundaries do not create obvious visible artifacts;
- performance is competitive with DG cubed-sphere;
- Yin-Yang behaves well at 45 degrees, where cubed-sphere DG can show increased error.

Mechanism read:

```text
proper chart handoff can preserve coherent evolving structure through complex deformation.
```

## 8. Strong contribution to the dossier

This paper should be classified as:

```text
Q: weak/neutral
B: weak/neutral
L: very strong
Projection/invariant warning: very strong
```

The paper strengthens the L-side in a way that complements Luo 2025:

```text
Luo 2025 tells us the full MHD chart-custody architecture works.
Hall & Nair 2013 tells us exactly how DG boundary custody is compiled and where invariant leakage can occur.
```

## 9. Unified Phase/Tao reading after this paper

The strongest emerging computational pattern is now:

```text
one chart/domain is locally lawful but globally pathological;
introduce a complementary legal chart/domain;
precompute the transform/overlap relation;
continue locally inside each chart;
read boundary values from retained adjacent-chart interior;
only project globally after boundary coherence checks;
if the transported object has an invariant, add a local conservation constraint.
```

This is not merely a Taoist resemblance. It is modern numerical evidence that the Yin-Yang architecture is a practical solution to legal continuation across a domain singularity.

## 10. Research delta from this paper

New material added by this pass:

```text
1. DG-specific L boundary mechanism:
   ghost surface instead of only ghost zone.

2. Cached chart-map law:
   containing element/reference coordinate computed once,
   then reused deterministically.

3. Interpolation from adjacent retained interior state:
   not a projection from chart A alone.

4. Conservation red-team constraint:
   overset handoff can preserve visible smoothness while leaking mass.

5. Regularity dependence:
   smooth fields get spectral convergence;
   C1 cosine-bell fields get geometric convergence.
```

## 11. What this paper does not solve

```text
Does not solve B floor-anchor formula.
Does not map Jiurong/Ceyuan contact-state formulas.
Does not close Yijing Q/B/L frozen rules.
Does not establish Shadow modular transformation behavior.
Does not prove Phase Calculus.
```

## 12. New work orders

```text
YYDG-1:
  Add “boundary invariant preservation” to L/re-chart checklist.

YYDG-2:
  Distinguish ghost surface, ghost zone, and projection layer in the mechanism ledger.

YYDG-3:
  Use Hall & Nair as a control against naive L claims:
  chart re-entry must specify how boundary values are obtained and how invariants are protected.

YYDG-4:
  Continue next target: Liu_2022_ApJ_940_62.pdf or Physics_of_Buddhism control paper, depending on whether the next priority is Yin-Yang computational lineage or false-duality filtering.
```
