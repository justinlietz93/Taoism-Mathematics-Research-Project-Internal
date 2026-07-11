# p5-b3-v4 Audit Package

This package audits `p5-b3-v4_primary-pairing-type-boundary_20260711T145605.zip`.

It verifies artifact integrity and separates the accepted authority boundary from claims that still require a complete model-theoretic witness.

## Verdict

```text
REVISE_SCOPE
p5-b3 BRANCH STATUS: OPEN
NEXT INTERACTION: p5-b3-v5
```

## Reproduce

```bash
python scripts/p5-b3-v4_verify_agent_package.py \
  /path/to/p5-b3-v4_primary-pairing-type-boundary_20260711T145605.zip

python scripts/p5-b3-v4_scope_audit.py \
  /path/to/extracted/docs/QBL_PRIMARY_PAIRING_TYPE_BOUNDARY_v2.md
```
