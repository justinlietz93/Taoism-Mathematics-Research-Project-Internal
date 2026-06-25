# 52. TDAHE retained-branch quotient gate pass

## Scope

This pass adds a physical retained-branch / quotient-residual gate to the active bridge program by auditing the `Loop_Generated_Projection_in_TDAHE` Phase research package.

This is not treated as an external proof of Phase Calculus. It is used as an internal test surface for the same rule now governing the Yi, Wilhelm, Orthad, and MFE/Liu bridges:

```text
projection/readout/scalar/endpoint data is not the carried object
unless it is state-complete for the next admissible transition.
```

## New artifacts

- `tdahe_retained_branch_metrics_v46.csv`
- `tdahe_projection_state_completeness_gate_v46.csv`
- `tdahe_cross_corpus_projection_bridge_v46.csv`
- `tdahe_experimental_gate_matrix_v46.csv`
- `modular_b_operator_family_extended_v46.csv`
- `scripts/tdahe_projection_loss_sympy_attack_v46.py`
- `tdahe_projection_loss_sympy_attack_v46_output.txt`
- `proofs/TDAHEProjectionLossV46.lean`
- `notebooks/tdahe_projection_loss_attack_v46.ipynb`

## Main finding

TDAHE supplies a concrete physical bridge for retained orthogonal branch structure beyond a lower-dimensional quotient.

The working stack is:

```text
retained through-thickness loop + branch-history registers
-> field-training operations U_y, U_z
-> noncommuting register update
-> quotient residual under ordinary 2D Hall projection
-> scalar Hall output only as terminal readout
```

This directly reinforces the current project spine:

```text
retained carrier/state
-> admissible operation
-> carrier-specific refinement/update arithmetic
-> completion / blockage / threshold
-> carry / lift / re-chart
-> boundary readout
-> scalar only as terminal projection
-> invariant/custody preservation
-> state-completeness negative control
```

## Exact algebraic gates recovered

### Planar projection collision

The retained-loop identity gives:

```text
P0(gamma_+) = P0(gamma_-)
mu_y(gamma_+) != mu_y(gamma_-)
```

The SymPy audit records:

```text
loop_moment_residual_zero = True
planar_projection_residual_zero = True
```

Meaning:

```text
same planar projection does not imply same retained loop state.
```

### Ordinary 2D quotient residual

The retained branch residual is:

```text
R_TD - R_2D = chi*a_y*h_y
```

The audit records:

```text
td_residual_zero_after_subtraction = True
```

This is the physical analogue of the bridge rule already active in Yi/Wilhelm:

```text
scalar readout is downstream of retained carrier and projection convention.
```

### Field-order commutator

The branch-memory update matrices satisfy:

```text
[U_y, U_z] = alpha*beta*diag(1,-1)
```

The exact order signal is:

```text
Delta R_order = alpha*beta*(-a_y*h_y + a_z*h_z)
```

The audit records:

```text
order_signal_residual = 0
```

Controls vanish when `alpha=0`, `beta=0`, or memory is absent.

### Scalar projection obstruction

The scalar projection `p_z=h_z` collides before `U_y` and separates after `U_y`:

```text
same_initial_pz_residual = 0
after_Uy_pz_difference = -beta
after_Uz_pz_difference = 0
```

Interpretation:

```text
A single scalar h_z memory coordinate is not state-complete when the retained h_y register affects the next transition.
```

## Deterministic model outputs extracted

```text
in-plane amplitude: 0.3247768947619229 kOhm
out-of-plane amplitude: 0.08365465471140439 kOhm
coercive ratio B_parallel/B_perp: 56.49072843397721
peak density n: 1.4 1e12 cm^-2
peak displacement D: 0.9 V/nm
density branch reversal n: 1.73 1e12 cm^-2
temperature collapse: 1.56 K
deltaRxy map peak: -0.6495376791482502 kOhm at B_parallel=-0.167027027027027 T, n=1.4026200873362444
branch weight peak: 0.325150557115194 at D=0.8966480446927374 V/nm, n=1.3979452054794521
```

## Cross-corpus update

| Corpus | Projection-loss lesson from v46 |
|---|---|
| Corrected Orthad | Orthad cannot read before the emitted retained walk exists. |
| Ancient Yi | Decimal/octal/binary labels are projections from a retained place-symbol carrier. |
| Wilhelm | King Wen ordinals and names are projections over a six-line carrier with operations. |
| MFE/Liu | Diagnostics/images are not the dynamical state; field custody and boundary completion come first. |
| TDAHE | Planar Hall/scalar memory can collide while retained branch state differs. |

## Modular-B impact

v46 keeps the modular-B path open but state-completeness-gated.

The extended operator-family table now separates:

```text
Phase-origin B: carried-pair balanced/Farey-Fibonacci refinement
Ancient Yi: base-8 place-carry refinement
Wilhelm: carrier involutions and line-flip operations
TDAHE: noncommuting retained branch-register updates
```

This does not identify all of them as the same B. It preserves the stronger research hypothesis:

```text
B-like refinement may be a carrier/domain-selected operator schema.
```

## Bridge status movement

```text
TDAHE retained branch / quotient residual:
  PASS_INTERNAL_PHYSICAL_GATE

Projection-loss negative-control framework:
  STRENGTHENED

Modular-B research path:
  OPEN_AND_NOW_PHYSICAL_BRANCH_REGISTER_GATED

Yi/Wilhelm/MFE/Orthad bridge matrix:
  STRENGTHENED_BY_TDAHE_PROJECTION_COLLISION
```

## Progress estimate

```text
paper/resource first-pass coverage: ~95%
code/data bridge coverage: ~93%
overall project research pass: ~89.7%
```

## Next blockers

```text
1. Full Ancient Yi table translation and line-order proof.
2. Latest active Phase selector/floor source from HDD.
3. Dongyuan/Ceyuan diagram-to-formula state graph.
4. Liu2022 QSL/current/connectivity time series.
5. Run/compile Lean surfaces where the environment supports Lean.
```
