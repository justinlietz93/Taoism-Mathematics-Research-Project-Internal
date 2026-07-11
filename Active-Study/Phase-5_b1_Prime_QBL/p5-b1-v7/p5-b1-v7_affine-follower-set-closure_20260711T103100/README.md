# p5-b1-v7 Affine Follower-Set Closure

This package closes the standard-follower-set bridge withheld by the p5-b1-v6 audit.

## Main results

```text
AFFINE COMPLEXITY: p(n)=2^(n+1)-1
AFFINE ENTROPY: log(2)
STANDARD HALF-OPEN FOLLOWER BRIDGE: PROVED
FINITE-STATE/SOFIC STATUS: PROVED NON-SOFIC
ACTUAL AFFINE LANGUAGE MIXING: PROVED INDEPENDENTLY
FINITE MARKOV ORDER: NONE
p5-b1 BRANCH STATUS: CLOSED
```

The load-bearing repair is the exact half-open identity

```text
Fol(w) = {v : D^|w|(C(w)) intersects C(v)}.
```

Equality of standard follower sets therefore forces equality of follower-region interiors. For the two cylinders adjacent to the cut, the ordered interiors retain the oriented minus-to-plus handoff `D^n(p)`. Repetition of an ordered follower-set pair would force repetition of the irrational cut orbit.

The proof does not require an unsafe claim that follower data determines isolated endpoint membership. It also does not require the two follower-region closures to have only one common endpoint: when the image arcs are complementary, their ordered orientation still distinguishes the handoff at `D^n(p)`.

## Boundaries retained

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

`QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` is the Orthad authority. The older canonical ledger is provenance only.

## Rebuild

From the package root:

```bash
python scripts/20260711T103100_build_package.py --root . --zip
```

The builder reruns the derivation, validates the imported trace, rebuilds and executes the no-I/O notebook, extracts figures, attempts Lean compilation when available, regenerates the manifest, and writes a deterministic zip archive.
