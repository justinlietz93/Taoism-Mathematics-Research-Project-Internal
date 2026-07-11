# Findings

## Proved abstractly

- The transformed carry partition on the circle has boundary `{p} union D^(-1)(p)`.
- Its length-`n` refinement boundary is exactly `union_{k=0}^n D^(-k)(p)`.
- Every complementary arc is one nonempty cylinder and adjacent arcs carry distinct words.
- `p(n)=2^(n+1)-1` for every `n>=1`.
- The affine coding entropy is `log(2)`.
- The affine carry language is non-sofic.
- The affine carry language is topologically mixing.
- No finite Markov order can present the language.

## Certified finitely

- Exact symbolic cylinder endpoints `q*a+r` were generated through length 12.
- Rational comparisons over an outward-rounded enclosure of `a` reproduce all direct cylinder counts through length 12.
- Explicit finite memory counterexamples were certified for orders 1 through 10.
- The imported `A=0..10000` trace and all 9999 transitions validate.
- No affine-orbit boundary hit occurs on `A=0..10000` under outward-rounded interval propagation.

## Observed

- The finite edge table is closer to the Lebesgue matrix `J` than to the Parry edge measure `K` of the pairwise envelope.
- The state and defect frequencies closely track their Lebesgue benchmarks on the finite range.

## Open

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## Correct scope of M and K

`M` is the pairwise edge-envelope matrix only. `K` is the Parry joint measure of that envelope only. Neither describes the full affine language.

## Reproducibility

A clean extraction and rebuild reproduced every internal file hash and the final zip archive hash byte-for-byte. Stable notebook cell IDs, stripped volatile metadata, removed bytecode caches, and fixed zip metadata are load-bearing for this result.
