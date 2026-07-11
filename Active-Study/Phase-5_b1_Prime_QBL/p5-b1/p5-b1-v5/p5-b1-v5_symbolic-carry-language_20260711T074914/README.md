# p5-b1-v5 Symbolic Carry Language Experiment Package

This package corrects the prior `J` track by separating the exact affine interval coding from its pairwise edge-shift envelope.

## Primary results

- The accepted affine ceiling bridge, endpoint partition, `J`, `P`, defect masses, and finite edge metrics are retained.
- `989` is proved impossible although both adjacent pairs are allowed by the pairwise matrix `M`.
- At the current constant, 15 length-three words are realizable; `M` admits 17.
- The affine carry language has exact complexity `2^(n+1)-1` and entropy `log(2)`.
- `log(1+sqrt(2))` and `K` are relabeled as properties of the pairwise edge-shift envelope only.
- No finite-state/sofic presentation of the full affine carry language is claimed.

## Rebuild

From the package root:

```bash
python scripts/20260711T074914_build_package.py --package-root . --zip
```

The builder regenerates outputs, traces, source and executed notebooks, figures, Lean compiler log, manifest, and archive. It fails on malformed input coverage, invalid carries, transition-count disagreement, symbolic normalization failure, notebook mismatch, or manifest mismatch.

## Evidence boundary

The exact Fibonacci-threshold agreement through `A=10000` is imported prior finite evidence. This package does not independently rerun that threshold verifier.

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
