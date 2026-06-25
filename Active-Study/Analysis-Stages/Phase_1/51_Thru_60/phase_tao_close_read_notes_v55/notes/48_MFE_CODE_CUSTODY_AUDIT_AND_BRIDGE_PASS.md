# 48. MFE code custody audit and retained-state bridge pass

## Scope

This pass continued the available-material research by auditing the base `MFE_pub-main` codebase and the `probs/Liu2022` setup as executable evidence for retained-state custody, boundary continuation, nonideal/dissipative channels, and projection-after-evolution discipline.

This does **not** claim that the base MFE code is the full 2025 Yin-Yang-MFE source. It is treated as the available code lineage and Liu 2022 problem setup.

## New artifacts

- `mfe_fortran_module_inventory.csv`
- `mfe_fortran_subroutine_inventory.csv`
- `mfe_fortran_call_inventory.csv`
- `mfe_orthad_custody_flow.csv`
- `mfe_boundary_callback_bridge.csv`
- `mfe_liu2022_inparam_bridge.csv`

## Main finding

The MFE code supports a strong **retained-state / custody / projection** bridge:

```text
MPI/grid initialization
-> retained full 3D field arrays
-> boundary and ghost-zone completion
-> RHS + nonideal RHS evolution
-> RK update with floors/guards
-> global energy monitoring
-> restart/output/projection after state evolution
```

Operational bridge:

```text
Corrected Phase / Orthad:
  retained Xi_hat + word
  -> admissible Q/B/L custody
  -> carried update
  -> boundary readout after emitted walk exists

MFE / Liu2022 code:
  retained 3D grid field state
  -> admissible timestep and boundary-completed RHS
  -> RK evolution + nonideal update
  -> output/restart/projection after state update
```

## Revealing code-level details

### 1. State is carried before projection

`main.F` initializes MPI/domain decomposition, calls `initialize`, computes global energies, writes restart/data products, then iterates `nudt -> rk3step -> userstep`. The simulation output is not the state itself; it is a terminal product of the retained state.

### 2. Boundary continuation is not cosmetic

`ModBval.F` and problem callbacks in `probs/Liu2022/ModUserSetup.F` provide ghost-zone and EMF boundary values. This is a concrete custody mechanism: the next update is only meaningful after boundary/edge channels are completed.

Relevant families include:

```text
bvald / bvalei / bvalv / bvaleta
bvalemf1 / bvalemf2 / bvalemf3
bvaldiffemf1 / bvaldiffemf2 / bvaldiffemf3
Liu2022 getemf* / getdiffemf* / getv* / getd* / geteint*
```

### 3. J+M bridge becomes more concrete

`ModRHS.F` supplies the core ideal-MHD RHS and EMF evolution. `probs/Liu2022/ModNonIdealRHS.F` adds field-aligned thermal conduction with flux limiting and relaxation timescale `tau_hc`.

This supports the bridge:

```text
ideal transport / EMF evolution
+ nonideal conduction / flux-limited relaxation
```

as an equation-level candidate for reversible/dissipative channel splitting. It remains a bridge, not a proof, until energy/helicity/divergence accounting is extracted.

### 4. Liu 2022 problem setup is data-constrained retained-state loading

`field_init` reads restart data, computes temperature field from retained internal energy and density, stores physical constants, sets floors, and initializes lower-boundary base arrays. The active MHD state is therefore loaded and evolved before any synthetic or observational projection is compared.

## What this strengthens

```text
Retained carrier before readout:
  STRONGER

Boundary/custody completion before update:
  STRONGER

J+M / ideal+nonideal bridge:
  STRONGER, still equation-level open

L/re-chart bridge:
  INDIRECT here; stronger in Yin-Yang grid papers than in base MFE code

B/floor-anchor bridge:
  NOT CLOSED by MFE code; current code contributes threshold/guard examples, not Phase B arithmetic
```

## What this does not close

```text
1. It does not supply the full 2025 Yin-Yang-MFE source if that implementation differs from base MFE_pub-main.
2. It does not compute Liu 2022 QSL squashing-factor maps.
3. It does not reconstruct P1->P3 connectivity from data.
4. It does not extract helicity/energy/divergence residuals.
5. It does not close B refinement arithmetic.
```

## Current progress update

```text
paper/resource first-pass coverage: ~94%
code/data bridge coverage: ~84%
overall project research pass: ~82.4%
```

## Reunified understanding after this pass

The external evidence increasingly supports this normalized project frame:

```text
A meaningful Phase bridge is not established by matching names.
It is established when an external system requires:
  retained state before projection,
  admissible transition/custody,
  completion/guard/threshold before continuation,
  lift/re-chart/carry when same-domain continuation fails,
  terminal readout only after retained-state coherence.
```

The MFE/Liu code line is strongest for retained-state custody, boundary completion, J+M-style channel splitting, and projection-after-evolution. Ancient Yi/Wilhelm remains strongest for retained carrier, finite domain completion, carry/lift, and multiple readout projections. These are complementary bridges, not duplicate claims.
