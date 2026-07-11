# QBL Carry-J Experiment Package

This package closes the short interval-dynamics track for the QBL carry word on the affine ceiling model. It derives the exact endpoint law, the Lebesgue joint edge matrix `J`, the conditional matrix `P`, the topological matrix `M`, the Parry joint edge law `K`, and direct finite comparisons using the prior `A=0..10000` trace. It keeps specific-orbit equidistribution, the global exact Fibonacci-threshold bridge, and any gauge/FQM prime map open.

## Rebuild

From the package root, with Python 3.13 and the pinned dependencies installed:

```bash
python scripts/20260711T064604_build_package.py --package-root .
```

To rebuild and also write a sibling zip:

```bash
python scripts/20260711T064604_build_package.py --package-root . --zip
```

The builder regenerates `outputs/`, `figures/`, `trace/`, the source and executed notebooks, the Lean compiler log, and `MANIFEST.json` from the included inputs.

## Start here

- `FINDINGS.md`
- `docs/QBL_CARRY_J_DERIVATION_AND_RESEARCH_BOUNDARY_v2.md`
- `docs/20260711T064604_RESULTS.md`
- `outputs/20260711T064604_numerical_results.json`
- `notebooks/20260711T064604_J_Derivation_executed.ipynb`
