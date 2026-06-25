# Current progress index

## Latest package

`phase_tao_close_read_notes_v46.zip`

## Latest pass

`notes/52_TDAHE_RETAINED_BRANCH_QUOTIENT_GATE_PASS.md`

## Latest revealing finding

TDAHE now supplies an internal physical projection-loss gate for the whole bridge program:

```text
same planar projection does not imply same retained loop state;
scalar h_z memory is not state-complete when h_y affects the next update;
field-order protocols expose retained branch-history through a nonzero commutator.
```

Exact gates recovered:

```text
loop moment residual: 0
planar projection residual: 0
R_TD - R_2D = chi*a_y*h_y
[U_y,U_z] = alpha*beta*diag(1,-1)
after U_y scalar p_z collision separates by -beta
```

## Current bridge spine

```text
retained carrier/state
-> admissible operation
-> carrier-specific refinement/update arithmetic
-> completion / blockage / threshold
-> carry / lift / re-chart
-> boundary readout
-> scalar only as terminal projection
-> invariant/custody preservation
-> state-completeness negative controls
```

## Current progress estimate

```text
paper/resource first-pass coverage: ~95%
code/data bridge coverage: ~93%
overall project research pass: ~89.7%
```

## Highest-value open blockers

1. Ancient Yi full translation and line-order proof.
2. Latest active Phase selector/floor source from HDD.
3. Dongyuan/Ceyuan diagram-to-formula state graph.
4. Liu2022 QSL/current/connectivity time series.
5. Run/compile Lean surfaces where the environment supports Lean.
