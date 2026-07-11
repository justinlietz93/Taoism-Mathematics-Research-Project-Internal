# p5-b3-v5 Audit Package

This package audits `p5-b3-v5_domain-proper-effective-invariant_20260711T162253.zip`.

It verifies artifact integrity and reproducibility, reproduces the accepted canonical-orbit calculations, and isolates the remaining CF000 bridge between an induced return description and a genuinely new descriptive domain.

## Verdict

```text
REVISE

CANONICAL RETURN SYMBOLIC PACKAGE: ADOPT
D1 INDUCED RETURN INVARIANT: ADOPT
D1 DOMAIN-PROPER EFFECTIVE INVARIANT: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
```

## Run

```bash
python scripts/p5-b3-v5_verify_agent_package.py \
  --archive /path/to/p5-b3-v5_domain-proper-effective-invariant_20260711T162253.zip

python scripts/p5-b3-v5_audit_structural_claims.py \
  --archive /path/to/p5-b3-v5_domain-proper-effective-invariant_20260711T162253.zip
```
