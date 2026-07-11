# Canon First Experiment - corrected dual-chart rerun

Status: `CANON_FIRST_DUAL_CHART_ONE_CROSSING_CHARACTER_MATCH_OBSERVED`

This package implements one `B -> FLOOR -> L` crossing with two word-built chart matrices, explicit cross-chart transfer, carried-state addressing, an evidence-recomputing verifier, and all required load-bearing ablations.

It does not claim final Canon completion.

## Baseline evidence

- QBL word: `BL`
- Pair: `(34,55) -> (55,89)`
- Frozen axis: `i/4895`
- `OmegaPlus`: emitted as data
- `OmegaMinus`: emitted as data
- cross-chart transfer: emitted as data
- far-side character/reference match: `12/12`
- required ablations failing the survival gate: `7/7`

The live path contains no Shadow Residual lookup. The external law `((12|n), n, n^2/24)` exists only under `src/orthad_canon/meta/` and the meta output tables.

## Run

```bash
python -m pip install -e .
python scripts/run_experiment.py
python scripts/verify_evidence.py .
pytest
```

Negative-control checks:

```bash
python scripts/verify_evidence.py . --mutate-character
python scripts/verify_evidence.py . --inject-lexeme
```

Both commands must exit nonzero.

## Claim boundary

Observed only for one finite first-period carrier and one cusp crossing. Arbitrary paths, multi-crossing stability, analytic q-series completion, mock-theta closure, field-valued MHD transport, and final Canon completion remain open.
