# Findings

## Proved abstractly

- The affine ceiling map and half-open carry partition remain accepted.
- The exact standard follower identity is
  `Fol(w)={v:H_w intersect C(v) is nonempty}`, where `H_w=D^|w|(C(w))`.
- The identity is set-theoretic and preserves every included and excluded endpoint case.
- Equality of standard follower sets forces equality of the interiors of their half-open follower regions.
- The boundary-adjacent cylinders lie in one `D^-n(p)` fundamental gap, so `D^n` preserves their order.
- Their exact follower regions are `(alpha_n,q_n]` and `(q_n,beta_n]`, with oriented handoff `q_n=D^n(p)`.
- The ordered standard follower-set pairs are all distinct because the cut orbit is nonrepeating.
- The affine carry language is non-sofic.
- No finite Markov order presents the language.
- `p(n)=2^(n+1)-1`, entropy `log(2)`, and actual-language mixing remain adopted. Mixing is independent of the non-soficity proof.

## Certified finitely

- Exact rational-affine cylinder endpoints were regenerated through length 12.
- Finite half-open follower-region geometry was generated for lengths 1 through 12.
- Explicit finite-memory counterexamples remain certified for orders 1 through 10.
- The imported `A=0..10000` trace and all 9999 transitions validate.
- Outward-rounded interval propagation certifies no affine-orbit boundary hit on `A=0..10000`.

## Observed

- The finite edge table remains closer to the Lebesgue one-step matrix `J` than to the Parry edge measure `K` of the pairwise envelope.
- State and defect frequencies remain finite evidence only.

## Open

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## Branch disposition

```text
p5-b1 BRANCH STATUS: CLOSED
```

The interval presentation is exact; a finite-state/sofic presentation is proved not to exist.
