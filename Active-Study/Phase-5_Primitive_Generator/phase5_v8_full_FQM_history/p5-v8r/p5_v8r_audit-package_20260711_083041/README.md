# p5_v8r Audit Package

This package audits `p5_v8r_orthad-first-crossing-recurrence_20260711_080825.zip` and supplies the next relay instructions for `p5_v8s`.

## Verdict

```text
REVISE
```

The primitive crossing, first-L carry, and local active-axis shorthand are retained. The broad Orthad hard stop is retained. The claimed scalar `tau_t` is not yet a well-typed smallest missing equation, the historical overlap record needs a semantic audit, the Lean artifact does not prove bilinear underdetermination, and the source lineage and archive manifest remain incomplete.

## Start here

- `p5_v8r_AUDIT_REPORT_20260711T083041.md`
- `p5_v8s_AGENT_INSTRUCTIONS_20260711T083041.md`
- `p5_v8r_AUDIT_RESULTS_20260711T083041.json`

## Reproduce

```bash
python scripts/p5_v8r_reproduce_audit_20260711T083041.py \
  /path/to/p5_v8r_orthad-first-crossing-recurrence_20260711_080825.zip
```

The reproduction script verifies the exact response ZIP hash, compares the archive path set to its manifest, runs the package verifier before cache-producing tools, and runs pytest with its cache provider disabled.
