# Source-Forced Two-Slot Pairing Interface

**Step:** `p5-b3-v7`  
**Authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Scope:** architectural interface only; no scalar-valued, linear, represented-dual, or operator-valued realization is selected.

## 1. Interface object

For every primitive prefix `W_t`, the authority requires one generative primary-pairing object

\[
P_t\in\operatorname{Pair}_2(\mathsf H_t^{(1)},\mathsf H_t^{(2)}),
\]

where `Pair_2` denotes only a two-slot pairing interface. It does **not** assert that `P_t` is a function, a scalar-valued form, a matrix, or a morphism to a dual.

The two argument architectures may be two named copies of one ambient architecture. The source does not decide whether they are equal, dual, conjugate, opposite-orientation, or related by another operation.

## 2. Required restriction mechanism

The same primary object must generate four chart-side descendants:

\[
\operatorname{Res}_{+,+}(P_t),\quad
\operatorname{Res}_{-,-}(P_t),\quad
\operatorname{Res}_{+,-}(P_t),\quad
\operatorname{Res}_{-,+}(P_t).
\]

The current law writes the intended algebraic shape as

\[
\iota_a^*P_t\iota_b.
\]

This fixes the placement of one chart map in each slot and the direction of construction from `P_t`. It does not type the star as a linear adjoint, conjugate transpose, categorical dual, or any other specific operation. The law itself says the exact chart-map recurrence remains an obligation.

## 3. Architectural rank

There is one active axis before the first `L`. `B` and `Q` preserve architectural rank. Every `L` appends exactly one new active axis and increases architectural rank by one. Therefore

\[
r_t^{\mathrm{arch}}=A_t+1.
\]

This is an architectural axis count. It is not an algebraic matrix rank, module rank, or rank of a scalar form until a realization axiom defines those notions.

## 4. Exact-word dependence

`P_t` is generated from the advanced retained state and the exact word prefix. Therefore two prefixes with equal operation counts are not identified unless an independent theorem proves equality of the generated pairing objects.

## 5. Forced operation signatures

### `B`

`B` keeps the two argument architectures and architectural rank fixed, preserves every latched sector, preserves phase, updates the retained pair, and requires active pairing data to mutate. No slot pullback or value law is forced.

### `Q`

`Q` keeps the two argument architectures and architectural rank fixed, preserves every latched sector and the retained pair, advances active orientation by the quarter-turn witness, and requires active pairing data to mutate. The source does not choose whether this acts in the first slot, second slot, both slots, the value object, or orientation metadata.

### `L`

`L` extends each argument architecture into old and new sectors while retaining two-slot arity. The old-old component is the embedded previous pairing. The old-new, new-old, and new-new components are not fixed by the current authority. The word “orthogonal” is architectural here because pairing-orthogonality has not been typed.

## 6. First missing laws

```text
B: active-sector transport/value law under (u,v)->(v,u+v)
Q: typed quarter-turn action on the pairing interface
L: typed extension-component and orthogonality law
```

Until these are supplied by an earlier canonical source or ratified as a realization axiom, the exact primary-pairing recurrence remains open.
