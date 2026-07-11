# Primary Pairing Type Closure

The abstract type closes at

```text
P_t : H_t -> D(H_t).
```

The concrete scalar variance does not close. Two realizations survive:

1. ordinary duality, producing a bilinear form;
2. conjugate duality over a star-object, producing a sesquilinear form.

Hermitianity is an additional self-adjointness law inside the second branch. The downstream `H=M+iJ` construction shows that branch is viable, but does not force it for the clean primary pairing.

The first separating axiom is:

```text
SCALAR_VARIANCE_AXIOM: specify whether D(lambda*id_H)=lambda*id_DH or D(lambda*id_H)=lambda^**id_DH; equivalently whether P(lambda*x,y)=lambda*P(x,y) or lambda^**P(x,y).
```

```text
EXACT_PRIMARY_PAIRING_TYPE: NOT_YET_DERIVED
SURVIVING_TYPES: ordinary-dual bilinear; conjugate-dual sesquilinear
EARLIEST_MISSING_AXIOM: SCALAR_VARIANCE_AXIOM
```
