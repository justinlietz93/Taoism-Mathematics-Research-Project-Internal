# 25 - Liu 2022 ApJ 940:62 squeeze-dry pass

Source:

`Prospect-Leads/Liu_2022_ApJ_940_62.pdf`

Related code/resource:

`source/code/MFE_pub-main/probs/Liu2022/`

Status:

`COMPLETE_FIRST_PASS`

## One-line conclusion

Liu 2022 is not another Yin-Yang grid/re-chart paper. Its value is different: it is a data-constrained MHD/topological-custody paper where a retained 3D magnetic state evolves through reconnection, separates an upper erupting channel from a lower stable filament, then produces scalar/visual observational projections only afterward.

## What the paper actually does

The paper models the 2012 July 12 X1.4 flare/CME in solar active region 11520. Observations show a low-lying filament and high-lying sigmoid/hot channel. The authors build a data-constrained MHD simulation using:

- observed solar active-region constraints,
- flux rope insertion,
- magnetofrictional relaxation,
- the magnetic flux eruption code,
- spherical geometry,
- synthetic AIA 94 Å and 304 Å image projections.

The resulting model contains:

- a magnetic flux rope (MFR),
- a hyperbolic flux tube (HFT),
- a null-point structure,
- overlying confining magnetic fields,
- a low-lying stable filament/sheared arcade below the HFT,
- a higher erupting sigmoid/hot channel above the HFT.

## Core mechanism extracted

The key sequence is:

```text
observed boundary/state constraints
-> inserted MFR path
-> magnetofrictional relaxation
-> nearly force-free but unstable retained magnetic state
-> MHD evolution
-> null-point reconnection changes high-channel footpoint P1 -> P3
-> tether-cutting reconnection at HFT cuts upper/lower connection
-> high-lying sigmoid/MFR erupts
-> low-lying filament remains stable
-> synthetic AIA projection reproduces ribbons/hot channel signatures
```

## Quantitative/model details worth preserving

- Initial model time: 2012-07-12 15:00 UT.
- Initial axial flux: `4 x 10^21 Mx`.
- Initial poloidal flux: `6 x 10^10 Mx cm^-1`.
- Force-free quality check: current-weighted average `sigma_J = 0.046`, interpreted as about `3 degrees` average current-field angle.
- Spherical wedge domain:
  - `r in [1.008 R_sun, 2.225 R_sun]`
  - `theta in [93.4 deg, 125.3 deg]`
  - `phi in [-15.2 deg, 30.6 deg]`
- Grid: `396 x 300 x 400`.
- Radial spacing: about `1.5 Mm` at bottom to `3.1 Mm` at top.
- Lower boundary: line-tied, zero velocity and electric field.
- Side/top boundaries: outward extrapolation allowing flow through.
- Thermodynamics: field-aligned heat conduction, numerical heating, no empirical coronal heating, no optically thin radiative cooling, gamma `1.1`.
- Synthetic observation channels: AIA 94 Å and 304 Å.
- Eruption tracking: 20 mass elements, 12 erupt with the cavity, 8 side elements are squeezed to flanks and do not erupt.
- Final uniform MFR speed in model: about `370 km/s` near height `1.7 R_sun` at `t ≈ 0.2 hr`.

## Figure-level extraction

### Figure 1 - observed filament/sigmoid system

Shows the observed active-region setup: polarity labels P1/P2/P3/P4/N1, filament, low-lying sigmoid, high-lying sigmoid, brightenings, flare ribbons, semicircular ribbon.

Mechanism value:

```text
observation gives terminal projection constraints;
it is not the retained 3D magnetic state itself.
```

### Figure 2 - initial 3D field structure

Shows two perspectives of the simulation domain and the initial magnetic field: MFR, null point, overlying confining fields, and HFT/MFR structure.

Mechanism value:

```text
retained state contains topology not visible from any one projection.
```

### Figure 3 - current density and decay index

Current density and decay-index contour indicate the unstable region and torus-instability susceptibility.

Mechanism value:

```text
transition condition is not arbitrary;
it is tied to retained state geometry/topology and decay-index threshold.
```

### Figure 4 - model/observation comparison

Compares AIA observations, squashing-factor Q, and field-line structure. High-Q ribbons correspond to observed flare ribbons and semicircular ribbon.

Important warning:

```text
Q here = squashing factor, not Phase primitive Q.
Do not conflate them.
```

Mechanism value:

```text
a topology diagnostic field maps retained magnetic connectivity to observable ribbon support.
This is projection/readout-like, not primitive selection.
```

### Figures 5-6 - eruption viewed from two perspectives

Field lines are colored by temperature; simulation shows separation of high-lying hot channel field lines from low-lying filament field lines.

Mechanism value:

```text
active upper structure lifts/erupts;
lower structure remains stable.
This is a real topological active/retained split.
```

### Figures 7-9 - temperature, density, squashing factor

Temperature/density slices show ribbons, shock front, filament, and hot channel. Squashing-factor Q shows double-J ribbons, semicircular ribbon, and HFT.

Mechanism value:

```text
separate physical fields provide different projections of the same retained evolution.
```

### Figures 10-11 - synthetic AIA 94 Å and 304 Å

Synthetic AIA images are line-of-sight integrations. The loop-like hot channel appears in 94 Å but not 304 Å.

Mechanism value:

```text
projection depends on observation channel and line of sight;
the retained 3D state must be primary.
```

### Figure 12 - height and velocity

Only 12 of 20 tracked mass elements erupt. Others are squeezed to flanks and do not erupt.

Mechanism value:

```text
not all local state is promoted/lifted;
there is state-selective separation.
```

## Code/resource pass: `probs/Liu2022`

The included source files are not a whole paper reproduction package, but they are highly useful because they show the problem-specific MFE setup.

### `ModPar.F`

Key facts:

```text
inmax = 401
jnmax = 305
knmax = 405
nproc1 = 12
nproc2 = 12
nproc3 = 16
nproc = 2304
```

This matches the high-resolution parallel simulation regime. It is not a small demonstration toy.

### `ModUserSetup.F`

Important mechanics:

- Reads `grid_in.dat` and broadcasts grid arrays through MPI.
- Builds spherical geometry metric factors.
- Sets line-tied lower boundary with zero inward velocity behavior.
- Reads restart/initial state data through `readrst_mpi`.
- Computes `tfield` from internal energy and density.
- Stores baseline lower-boundary ghostzone arrays for energy and density.
- Updates lower boundary energy/density from base arrays using transition time `tau_tr`.
- Uses `userstep` to cap temperature at `2 x 10^8 K` and refresh ghostzone base arrays.
- Includes coordinate/vector transforms, plus MPI message-passing utilities.

Most important boundary-custody details:

```text
lower boundary:
  v1/v2/v3 inward ghost velocities set or clipped to enforce line-tied/controlled base behavior

outer boundary:
  values copied/extrapolated outward; v1 uses sign clipping to permit outward flow while suppressing inflow

energy/density lower ghostzones:
  not simply overwritten by arbitrary constants;
  they transition from retained base arrays toward temperature-linked values
```

### `ModNonIdealRHS.F`

Important mechanics:

- Implements field-aligned heat conduction under `THCONDUCT`.
- Computes `b dot grad T`.
- Uses Spitzer-like `T^(5/2)` conductivity with a temperature floor/modifier.
- Limits conductive flux using saturation terms.
- Adds heat flux divergence into the internal-energy update.
- Calls boundary updates for heat flux/limiter fields.

Mechanism value:

```text
this is another example of admitted local transport:
field direction B determines allowed heat-flow channel.
```

But this is not QBL-B. It is a local anisotropic transport law.

### `inparam`

Important settings:

```text
itmax = 8000000
itout = 1000
tout = 0.05
tend = 5.0
wtlimit = 43000
gamma = 1.1
unit_rho = 0.8365e-15
unit_len = 0.696e11
unit_b = 20
unit_temp = 1e6
```

### `data_initial_state_link`

The actual initial data is external, provided through a Globus shared point. So this code folder is not fully reproducible by itself.

## Reunified read against Phase/QBL/Orthad research

### Strong useful analogy

Liu 2022 strongly supports this general rule:

```text
retained high-dimensional state first;
terminal observation/projection afterward.
```

Observed ribbons and synthetic AIA channels are not the state. They are projections/readouts of retained topology and plasma evolution.

### Strong topological-custody lead

The HFT and null point form a topological transition architecture:

```text
retained field topology
-> null-point reconnection changes one footpoint connection
-> HFT tether-cutting cuts upper/lower coupling
-> upper structure erupts
-> lower structure remains stable
```

This is not identical to Orthad L, but it is a good external example of:

```text
state-selective topological separation.
```

### Possible L/latching analogue, but not exact

There is a tempting L-like read:

```text
upper hot channel = active promoted structure
lower filament = retained/stabilized structure
HFT reconnection = boundary event
postflare loops cover lower filament = stabilizing latch-like aftermath
```

Do not overclaim this.

Correct status:

```text
L-adjacent topological split, not full L equivalence.
```

Reason:

```text
Orthad L preserves q and latches an axis while appending a new active axis.
Liu 2022 reconnection physically changes magnetic connectivity.
It is not pure coordinate re-chart or exact inherit-and-extend.
```

### Strong projection warning

The synthetic AIA result is a clean projection warning:

```text
same retained evolution
-> 94 Å sees hot channel
-> 304 Å does not
-> line-of-sight choice changes visible morphology
```

So scalar/visual match must always be downstream of retained-state comparison.

### Q-name warning

The paper uses `Q` for the squashing factor, a magnetic-topology diagnostic. This must never be confused with primitive Phase `Q`.

Correct classification:

```text
squashing-factor Q = diagnostic/readout field
primitive Q = custody/phase operation
```

## Updated classification

```text
Q-side:
  Not direct. The paper's Q is squashing factor, not primitive Q.

B-side:
  Weak direct support. Some local laws are state-admitted, but no B floor-anchor analogue.

L-side:
  Medium support through topological separation/reconnection, but not clean re-chart/latching.

Projection-side:
  Strong. Synthetic AIA and observed ribbons are downstream projections of retained 3D state.

Code-side:
  Medium-high. Liu2022 problem setup shows boundary custody, base-state retention, controlled ghostzone updates, and anisotropic admitted heat transport.
```

## What to keep

```text
1. Retained topology before projection.
2. HFT/null-point boundary structure as a topological transition mechanism.
3. Upper/lower state-selective separation.
4. Projection-channel dependence: 94 Å vs 304 Å and line-of-sight integration.
5. Squashing-factor Q as topology diagnostic, not Phase Q.
6. Code-level boundary custody and ghostzone base-state retention.
```

## What not to claim

```text
Do not claim Liu 2022 is a QBL match.
Do not claim it validates B floor-anchor logic.
Do not claim reconnection is the same as Orthad L.
Do not conflate squashing-factor Q with primitive Q.
Do not use synthetic AIA visual similarity as primary evidence before topology/state comparison.
```

## New research pressure added

For future L/re-chart/latching candidates, split three cases:

```text
1. Pure re-chart:
   same object, new coordinates, invariants preserved.

2. Topological reconnection:
   connectivity changes, but conserved physical laws may hold.

3. Orthad-style latch/lift:
   active axis freezes, carried q remains, new active axis opens.
```

Liu 2022 belongs primarily to case 2, with projection-side relevance and partial case-3 visual resemblance.

