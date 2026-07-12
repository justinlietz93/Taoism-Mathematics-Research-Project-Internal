# Phase 5 v7z: Mock-Theta FQM Matching and Shadow Residual Channel Comparison

## Objective

Recover the old mock-theta target without violating the Follow discipline.

The retained state must not carry the scalar Shadow Residual. It may only expose terminal channel fields from retained cursor, post-L seat, parity latch, lap orientation, and FQM residue data.

## Finite module

```text
A = Z/12Z
q(r) = r^2/24 mod 1
b(r,s) = rs/12 mod 1
```

This is well-defined because

```text
q(r+12)-q(r) = r+6
```

is integral.

## Character vector

```text
v_chi = [0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1]
```

The nonzero support is exactly:

```text
r in {1,5,7,11} mod 12
```

This is the finite channel skeleton of the Shadow Residual support/sign law.

## Exact structural facts tested

```text
K_12 v_chi = v_chi
```

and, for every supported residue:

```text
r^2 ≡ 1 mod 24
```

so the fractional exponent channel is locked to `1/24` and the T phase is constant on support.

## Channel comparison

For depths 3, 4, 5, and 6, the terminal comparison records:

```text
support channel
coefficient magnitude channel
sign character channel
fractional exponent channel
terminal exponent channel
inter-term spacing channel
lap orientation channel
```

The retained state does not store:

```text
q-series scalar
mock-theta coefficient cargo
Shadow Residual object
```

## Closure interpretation

The finite FQM skeleton is not a loose analogy. It is a direct carrier-level match for the support, sign, fractional exponent, Fourier stability, and T-phase behavior of the Shadow Residual channel field.

The analytic infinite-series completion remains outside this pass.
