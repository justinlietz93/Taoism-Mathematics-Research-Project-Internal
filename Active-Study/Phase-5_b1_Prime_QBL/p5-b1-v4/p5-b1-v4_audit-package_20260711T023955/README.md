# p5-b1-v4 Audit Package

This is the auditor-side package for the agent response delivered at `p5-b1-v4`.
It audits `experiment_package_20260711_064604.zip`; it is not an experiment package and does not replace that source artifact.

## Verdict

```text
REVISE

AFFINE_CEILING_BRIDGE: ADOPT
ENDPOINT_PARTITION: ADOPT
ONE_STEP_J_LAW: ADOPT
FINITE_EDGE_METRICS: ADOPT

FULL_SYMBOLIC_SYSTEM_M: REJECT AS STATED
TOPOLOGICAL_ENTROPY_LOG_1_PLUS_SQRT2: REJECT AS ACTUAL-CODING CLAIM
PARRY_MEASURE_K: RELABEL AS EDGE-SHIFT ENVELOPE
FULL_PACKAGE_CLOSURE: WITHHOLD
```

## Run the audit scripts

From this package root:

```bash
python scripts/p5-b1-v4_symbolic_language_audit.py --out outputs
python scripts/p5-b1-v4_verify_agent_package.py /path/to/experiment_package_20260711_064604.zip --out outputs
```

The first command uses only Python's standard library. The second verifies the source archive, its internal manifest, the corrected document hash, and notebook structure. Add `--rebuild` to rerun the source package builder when its pinned dependencies are installed.

## Start here

- `AUDIT_RESULTS.md`
- `OUTGOING_INSTRUCTIONS.md`
- `outputs/p5-b1-v4_audit-summary.json`
- `outputs/p5-b1-v4_word-complexity.csv`
- `MANIFEST.json`
