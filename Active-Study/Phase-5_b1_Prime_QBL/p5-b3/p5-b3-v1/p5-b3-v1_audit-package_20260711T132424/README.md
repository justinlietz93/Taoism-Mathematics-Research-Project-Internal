# p5-b3-v1 Audit Package

This audit verifies the `p5-b3-v1` delivery and tests the scope of its hierarchical grammar-lift claims.

## Verdict

```text
REVISE

CANONICAL BOUNDARY-ORBIT SEMICONJUGACY: PROVED
FULL AFFINE GRAMMAR FACTOR: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
p5-b3 BRANCH STATUS: NOT YET CLOSED
NEXT INTERACTION: p5-b3-v2
```

## Contents

- `AUDIT_RESULTS.md`: complete audit findings.
- `OUTGOING_INSTRUCTIONS.md`: `p5-b3-v2` task.
- `DIAGRAM_REVIEW.md`: review of the supplied Orthad architecture diagram.
- `SOURCE_MAP.md`: authority and source roles.
- `scripts/`: independent integrity and factor-scope checks.
- `outputs/`: machine-readable and logged audit results.
- `inputs/`: the audited document, current custody law, and diagram.

## Run the audit scripts

```bash
python scripts/p5-b3-v1_verify_agent_package.py \
  /path/to/p5-b3-v1_hierarchical-grammar-lift_20260711T120831.zip \
  --output outputs/package-verification.json

python scripts/p5-b3-v1_factor_scope_audit.py \
  --output outputs/factor-scope-audit.json
```
