# Minimal Pairing Interface

## Result

The weakest interface forced by the pairing-first formulas is a **duality morphism**, not yet a bilinear or Hermitian matrix.

Let `C` be an additive category with finite biproducts and a contravariant duality `D`. The retained argument object is `H_t`, and

```text
P_t : H_t -> D(H_t).
```

For chart embeddings `iota_a:C_a->H_t`, every chart or mixed block is the same composite:

```text
P_ab = D(iota_a) o P_t o iota_b : C_b -> D(C_a).
```

This gives both diagonal restrictions and both directed mixed blocks. A gauge automorphism acts by

```text
P_t -> D(U) o P_t o U.
```

The quarter-turn requires an active automorphism `J` with `J^2=-id`, or a concrete coefficient realization containing `i`.

At `L`, the architectural law supplies `H_(t+1)=H_t direct_sum A_new`. Old-block retention and two-sided orthogonality imply

```text
P_(t+1) = block_diag(P_t,p_new).
```

The new diagonal `p_new`, the coefficient realization, the scalar variance, and any self-adjointness law remain open.

## Forced interface versus chosen realization

Forced: `H_t`, `D`, `P_t`, two embeddings, four induced blocks, congruence gauge action, quarter-turn-capable realization, orthogonal direct-sum extension.

Chosen later: coefficient ring/field, ordinary or conjugate dual, dimension/basis, symmetry law, normalization, seed gauge group.

```text
MINIMAL_PAIRING_INTERFACE: DERIVED
```
