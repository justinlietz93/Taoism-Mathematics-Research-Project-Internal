# Source-forced pairing interface

## Derived interface

The four ratified expressions require one primary **two-slot pairing object** and contravariant restriction in each argument. The weakest interface used here is:

```text
objects A,B in a retained-argument class C
Pair(A,B)                         pairing objects with two slots
(f,g)^*: Pair(A,B) -> Pair(A',B')
    for f:A'->A and g:B'->B
P_t in Pair(H_t,H_t)
```

The pullback obeys identity and composition in both slots. Then every chart block has the common form

```text
Omega_plus  = (iota_plus,iota_plus)^* P_t
Omega_minus = (iota_minus,iota_minus)^* P_t
T_plus_minus  = (iota_minus,iota_plus)^* P_t
T_minus_plus  = (iota_plus,iota_minus)^* P_t
```

At this layer `*` names first-slot pullback. It is not yet an adjoint, conjugate transpose, scalar involution, or duality functor.

A scalar-valued form, a represented morphism `H_t -> D(H_t)`, and a kernel/profunctor realization are models of this interface. None is forced by the source text.

```text
SOURCE_FORCED_PAIRING_INTERFACE: DERIVED
```
