# Phase 4 v1 — General Shadow Correspondence II

## Status

```text
EXTENDED_CLASS_CLAIM_SUPPORTED_BY_SWEEP
GLOBAL_PASS: True
```

## Claim

For unary false-theta / mock-shadow channels carried by the finite residue-orientation module

```text
A_m = Z/(2m)Z
```

with even retained orientation vector `a(-r)=a(r)`, the shadow correspondence is the Phase Calculus projection-loss gate in the modular setting.

The retained object is the finite residue/orientation carrier. The positive-orientation readout gives the nonzero false-theta channel. The symmetric scalar n-weighted bilateral projection cancels. The coefficient-stripped channel is the lower-weight shadow.

## Primitive multiplier derivation

The carrier supplies two primitive generator actions:

```text
T_r = exp(pi i r^2/(2m))
S_rs = (2m)^(-1/2) exp(-pi i r s/m)
```

`T` is Q square seating on residue `r`. `S` is B/L dual residue seating with the unitary Gauss normalization. The derivative channel raises the weight by one:

```text
theta weight:      1/2
n-weight channel:  3/2
```

## Cases tested

| Case | m | N | kind | status |
| --- | ---: | ---: | --- | --- |
| chi12_level12_closed_instance | 6 | 12 | primitive_even_character | PASS |
| chi8_level8_second_case | 4 | 8 | primitive_even_character | PASS |
| legendre5_level10 | 5 | 10 | primitive_even_character | PASS |
| legendre13_level26 | 13 | 26 | primitive_even_character | PASS |
| nonprimitive_chi8_lift_level16 | 8 | 16 | nonprimitive_lifted_character | PASS |
| multi_orbit_m10 | 10 | 20 | vector_orbit_mixing | PASS |
| dense_even_m11 | 11 | 22 | generated_even_carrier | PASS |
| three_orbit_m15 | 15 | 30 | vector_orbit_mixing | PASS |


## Hard numeric gates

```text
max S unitarity error:          3.127e-15
max S^2 reversal error:         6.845e-15
max theta transform error:      7.579e-15
max derivative transform error: 1.370e-14
```

## Boundary discovered

Scalar quotient closure is special. Full retained vector custody is general.

```text
scalar quotient cases:       1
full vector required cases:  7
```

This is the correct strengthening: the general mechanism is not the search for more scalar chi12-like collapses. The general mechanism is retained vector-valued residue/orientation custody.

## Negative controls

The package includes negative controls for:

```text
1. odd orientation vectors,
2. non-even single-residue vectors,
3. bad S normalization,
4. wrong T denominator.
```

Each negative control fails exactly where the theorem says it must fail.

## Falsification target

The active falsifier is a finite-module unary false-theta/mock-shadow pair with an even retained orientation vector whose known shadow is not the coefficient-stripped projection of the same retained carrier, or whose known S/T action cannot be derived from the finite residue module.
