# Clean successor seed derivation attempt

## Strategic result

The sources support case 2 and a constrained form of case 3:

- `T_1(x)=x+1 mod 12` is a correct historical cyclic normal form and its eigencharacter identity is exact.
- It is not the clean `S_empty` because the clean doubled-carrier address/orientation map is absent.
- The strongest source-supported interpretation is a word-covariant successor system `(C_t,S_t,alpha_t)` feeding the pairing-first spectral layer.

## Earliest exact gap

The first missing object is

```text
alpha_empty : clean retained seed state -> C_0 = Z/12Z
```

and the first chronological covariance equation is

```text
alpha_B(F_B(X_empty)) = S_B(alpha_empty(X_empty)).
```

The old fixed shift gives a coordinate normal form only after `alpha_empty` and the carrier orientation are chosen. The available v7c executable constructs Fourier, Gauss, and reversal matrices but does not implement a successor or a QBL-to-successor recurrence.

## Finite nonuniqueness witness

There are four translation generators of `Z/12Z`: increments `1,5,7,11`. All are single cycles. Thus even the stronger historical statement “the successor is a cyclic translation” does not select `+1` without a clean coordinate convention.
