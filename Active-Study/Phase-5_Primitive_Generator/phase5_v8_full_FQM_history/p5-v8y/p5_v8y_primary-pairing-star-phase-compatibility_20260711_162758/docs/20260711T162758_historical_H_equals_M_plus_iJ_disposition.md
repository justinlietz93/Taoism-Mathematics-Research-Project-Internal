# Historical H=M+iJ disposition

The included v7n source defines, on bounded admissible trace-cocycle histories:

- `J_ij=c_ij/lcm(D_i,D_j)` with `J_ji=-J_ij`;
- `M` as a real symmetric graph-Laplacian gluing metric from shared-boundary/latch incidence;
- `H=M+iJ`.

These assumptions make `H` Hermitian because `M^T=M` and `J^T=-J`. The executable source verifies the residual numerically on its finite cases and treats `C` as a coordinate projection from `J`.

Dependencies assumed by that construction:

1. a historical retained event/trace-cocycle representation;
2. extracted `c_native` coupling values;
3. shared-boundary/latch incidence weights;
4. a real matrix presentation and complexification;
5. bounded admissible history families;
6. post-construction gauge/permutation checks.

It is therefore a rederived downstream Hermitian overlap reconstruction. It is not a clean `P_0`, not a per-tick `B/Q/L` recurrence, and not evidence that the primary star must be conjugate transpose.

```text
HISTORICAL H=M+iJ:
DERIVED_HERMITIAN_OVERLAP_RECONSTRUCTION_ON_HISTORICAL_ADMISSIBLE_TRACE_COCYCLE_TESTS; NOT_PRIMARY_SEED_OR_RECURRENCE
```
