# 38 — Liu 2022 mechanism table + code bridge pass

## Purpose

Continue the Liu 2022 bridge without downgrading the comparison because names do not match.  This pass treats Liu 2022 as a possible **continuous physics bridge** and asks whether the paper/code expose an operational chain comparable to Phase Calculus after normalization:

```text
retained state
-> admissibility / instability condition
-> coupled twist + stress refinement
-> topology-changing event
-> separated promoted/stable structures
-> terminal projection/readout
```

This is not a claim that Liu 2022 is literally Phase Calculus. It is a functional bridge analysis.

---

## Source status

```text
paper: Prospect-Leads/Liu_2022_ApJ_940_62.pdf
status: COMPLETE_FIRST_PASS retained
new status: MECHANISM_TABLE_PASS_COMPLETE

code: source/code/MFE_pub-main/probs/Liu2022
previous: 75%
new: 90%
```

The paper remains complete first-pass. This pass deepens it by extracting the mechanism sequence and code-level custody surfaces.

---

## Corrected bridge classification

Previous weak-label language is retired.

```text
Retained-state / projection discipline:
  STRONG_CONFIRMED

Primitive Q bridge:
  TWIST_ORIENTED_TRANSFER_BRIDGE_OPEN

Primitive B bridge:
  STRESS_CONCENTRATION_THRESHOLD_BRIDGE_OPEN

Primitive L bridge:
  TOPOLOGICAL_REARTICULATION_PROMOTION_BRIDGE_OPEN

Orthad readout / support-channel bridge:
  HIGH_VALUE_DIAGNOSTIC_BRIDGE_OPEN

J+M dynamics bridge:
  HIGH_VALUE_EQUATION_LEVEL_BRIDGE_OPEN

Exact Phase selector/floor law:
  NOT_TESTABLE_FROM_THIS PAPER ALONE
```

No bridge is closed negative here. The paper gives enough structure for a serious normalized mapping.

---

## Liu mechanism table

| Liu object / event | Paper-side function | Phase-normalized read |
|---|---|---|
| AIA 94 Å / 304 Å observations | visible projected data | terminal projection / incomplete witness |
| 3D MHD state | evolved retained physical state | retained lifted state analogue |
| inserted MFR + HFT + null point + overlying field | initial constrained topology | retained topological carrier |
| nearly force-free state, `σ_J ≈ 0.046`, average angle ≈ 3° | equilibrium-like retained state but unstable | retained state is coherent but admissibility conditions are already near/over threshold |
| decay-index contour near `-1.5` sign convention | torus-instability admissibility condition | possible Q/B floor-capacity or instability-bound bridge |
| current sheet at HFT | stress localization / topological compression | B-like refinement / narrowing / burden concentration bridge |
| overlying null-point reconnection | topology change that moves sigmoid footpoint P1 → P3 | re-articulation / domain routing bridge |
| tether-cutting reconnection at HFT | separates low filament from high sigmoid | L-like separation / promoted branch vs retained stable branch |
| upper hot channel eruption / CME | promoted structure enters higher energetic domain | lift / new host-domain bridge candidate |
| low-lying filament remains stable | unpromoted retained branch persists | branch split / non-discharge remainder bridge |
| synthetic AIA 94/304 images | projected readout from 3D simulation | Orthad/projection discipline: compute in retained state, read out afterward |

---

## Timing and event sequence extracted

```text
Initial condition:
  data-constrained MHD state starts already unstable.

Torus-instability marker:
  significant current/twisted field lies in region where decay-index contour indicates torus onset.

Current-sheet / HFT response:
  HFT and null point make current sheets readily form as twisted field rises.

Overlying/null-point reconnection:
  inferred to occur before tether-cutting because brightenings around P3 appear shortly before eruption.

Footpoint rerouting:
  right footpoint of rising MFR starts moving from P1 to P3.

Tether-cutting reconnection:
  cuts off connection between low-lying filament and high-lying sigmoid.

Thermal/observable signals:
  remote heating evident around 0.025–0.05 hr.
  erupting MFR heated to tens of MK around 0.1 hr.
  semicircular ribbon enhances from about 0.10–0.19 hr.

Macroscopic output:
  high-lying sigmoid becomes loop-like and erupts as CME.
  low-lying filament remains stable.
  MFR speed stabilizes near 370 km/s at height about 1.7 R_sun around 0.2 hr.
```

This is a useful bridge because it gives more than labels. It gives a state sequence with thresholds, constrained topology, separation, promotion, and terminal projection.

---

## Q/B/L normalized comparison

### Q-side: oriented transfer / accumulated twist

The paper does not contain primitive Phase `Q`. The possible bridge is functional:

```text
field-line twist / shear / footpoint migration
-> phase-like oriented transfer in retained magnetic topology
-> visible ribbons/sigmoid morphology as projection
```

Useful comparison question:

```text
Can field-line twist/shear accumulation be treated as the continuous-shadow analogue of Q-like oriented phase transport?
```

Missing piece for stronger status:

```text
Need a measurable twist/writhe/shear parameter over time and a rule connecting it to reconnection onset or route selection.
```

### B-side: stress concentration / thresholded refinement

The best B bridge is not the squashing-factor name. It is:

```text
HFT/current-sheet formation
-> concentration of gradients/current density
-> narrowing of topological transition layer
-> reconnection when local structure can no longer continue in old connectivity
```

This is functionally closer to B as state-dependent refinement under a floor/capacity than a literal denominator pair.

Missing piece for stronger status:

```text
Need exact evolution of current density, QSL width, squashing factor, and reconnection onset timing.
Need decide whether the threshold is current-density, numerical diffusion/resistive trigger, decay-index crossing, or combined topology/instability state.
```

### L-side: topological re-articulation / branch promotion

The L bridge is strong operationally if L is read as:

```text
cycle/continuation failure
-> old connectivity cannot carry the next state
-> branch separates
-> one structure remains in old domain
-> another enters a new host/energetic domain
```

Liu provides this structure:

```text
low filament remains stable
high sigmoid erupts into CME
P1 -> P3 footpoint rerouting
HFT tether-cutting separates structures
```

Missing piece for stronger status:

```text
Need exact topological graph before/after reconnection:
  nodes/polarities
  field-line connectivity classes
  which connection is cut
  which connection is newly opened
  which branch is retained vs promoted
```

### Orthad / readout side

This is one of the strongest bridges:

```text
Liu does not infer the 3D magnetic field from images alone.
They evolve the retained 3D MHD state first.
Only afterward do they compute synthetic AIA images by line-of-sight integration.
```

Phase-normalized read:

```text
retained magnetic topology and plasma fields
-> evolved custody state
-> terminal synthetic projection
```

This directly supports the project rule:

```text
compute in the retained/lifted state;
project only at the boundary/readout layer.
```

---

## J+M bridge from equations

The paper solves MHD equations with:

```text
mass continuity
momentum with pressure, gravity, Lorentz force, semi-relativistic correction
induction equation
∇·B = 0
internal energy with advection, pressure work, field-aligned heat conduction, numerical heating
ideal-gas equation of state
```

Bridge read:

```text
ideal transport / Lorentz evolution / induction:
  J-like conservative or structure-preserving channel candidate

reconnection heating / numerical diffusion / heat conduction:
  M-like dissipative entropy/thermal channel candidate
```

This needs an equation-level pass before any stronger claim. The bridge is high-value because Liu explicitly couples ideal instability with reconnection/thermal dissipation, but the paper does not present a metriplectic decomposition.

Missing piece:

```text
Need derive or identify conserved quantities and dissipative terms:
  magnetic energy
  helicity if available
  entropy/thermal production
  divergence constraint
  numerical diffusion contribution Hnum
```

---

## Code/source pass: Liu2022 problem setup in MFE_pub-main

Inspected files:

```text
probs/Liu2022/ModNonIdealRHS.F
probs/Liu2022/ModPar.F
probs/Liu2022/ModUserSetup.F
probs/Liu2022/makefile
probs/Liu2022/rundir/inparam
probs/Liu2022/rundir/data_initial_state_link
```

### Code facts

The Liu2022 code surface includes:

```text
THCONDUCT conditional module
field-aligned thermal conduction
flux limiting ratio qlim
saturated heat flux fsat
lower-boundary e/d ghost-zone custody
spherical coordinate/vector transforms
run parameters for MFE-style simulation
external initial state link
```

### Name-collision warning

`q` in `ModNonIdealRHS.F` is a heat-conduction flux/state variable, not Phase `q=(u,v)` and not solar squashing-factor `Q`.

```text
Do not compare names.
Compare roles.
```

### Operational bridge from code

The code strengthens the **custody / boundary / dissipation** bridge:

```text
ghost-zone e/d values are explicitly retained and updated
thermal flux is limited by local saturation ratios
energy is bounded by a temperature ceiling
external initial state is required
```

The code does **not** provide enough by itself to prove the Q/B/L mapping because:

```text
initial data are external
squashing-factor computation is not visible in this problem folder
connectivity tracing/reconnection analysis is not fully contained here
```

But it does confirm that the numerical implementation has real retained boundary state and dissipative/thermal channel machinery.

---

## Objective missing pieces to resolve current bridge weakness

### For Q bridge

```text
time series of twist / shear / writhe / field-line rotation
mapping from footpoint migration to retained topology state
rule for when twist can continue vs must reconnect
```

### For B bridge

```text
definition/evolution of squashing factor Q in this workflow
HFT thickness or current-sheet width over time
current-density threshold or numerical trigger condition
relationship between QSL/HFT concentration and reconnection onset
```

### For L bridge

```text
connectivity graph before/after null-point reconnection and tether cutting
P1/P3 field-line mapping table
separation proof: which magnetic structure remains old-domain, which is promoted
```

### For J+M bridge

```text
energy/helicity/invariant accounting
numerical-diffusion heating Hnum extraction
thermal conduction entropy role
explicit ideal-vs-dissipative split
```

### For Orthad readout

```text
mapping between retained field/topology channels and projected AIA features:
  high-Q ribbons
  double-J ribbons
  semicircular ribbon
  loop-like 94 Å hot channel
  absence in 304 Å
```

---

## Reunified project-level conclusion from this pass

Liu 2022 should remain a high-value physics bridge, not because its symbols match Phase symbols, but because its successful simulation strategy depends on the same operational hierarchy being tested across the external corpus:

```text
visible projection is incomplete;
retain the full state;
let the state evolve under admissibility and instability constraints;
allow topology-changing events when the old continuation cannot carry the next state;
then project/read out terminal observable channels.
```

The current analysis has not reached an endpoint. The next best Liu-specific work is a **connectivity/time table** using figures/animations if available, plus a squashing-factor/QSL extraction from the paper or companion code.
