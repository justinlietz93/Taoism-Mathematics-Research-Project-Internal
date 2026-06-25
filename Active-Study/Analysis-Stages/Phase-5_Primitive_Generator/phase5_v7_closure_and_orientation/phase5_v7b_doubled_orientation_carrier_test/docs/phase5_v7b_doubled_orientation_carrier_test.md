# Phase 5 v7b: Doubled Orientation Carrier Test

## Claim

The odd-N failure in Phase 5 v7 is a folded-carrier artifact. The quadratic self-twist must be carried on the doubled orientation carrier

```text
D_n = Z/(2n)Z
```

not forced onto `Z/nZ`.

## Corrected law

For base modulus `n`, set `D = 2n`.

```text
K_D(a,b) = D^(-1/2) exp(-2π i a b / D)
G_D(a)   = exp(π i a^2 / D)
         = exp(π i a^2 / (2n))
```

This is the same overset Orthad transfer and quadratic self-twist, but on the carrier where the denominator says it belongs.

## Result

The doubled carrier passes for every swept base modulus, including odd base moduli.

```text
base_moduli_swept: 65
min: 1
max: 180
max_unitarity_residual: 4.51673279695716e-14
max_reversal_residual: 1.1589991119609344e-13
max_polarization_residual: 9.641409168821612e-13
max_postseal_G_residual: 0.0
```

## Reclassification

The phrase "even-carrier law" should be replaced by:

```text
orientation-doubled carrier law
```

Odd carrier sizes fail only when one folds the two orientation hands into `Z/nZ` before the quadratic is read. That is projection loss at the carrier-definition layer.

## Old even cases

The previous even examples are preserved by renaming the base modulus. Carrier size `D=8` is base `n=4`; carrier size `D=12` is base `n=6`; carrier size `D=26` is base `n=13`.

## Falsifier

Find a base modulus `n` for which the doubled carrier `Z/(2n)Z` fails unitarity, reversal, fourth-power identity, representative invariance, or quadratic polarization under the sealed construction.
