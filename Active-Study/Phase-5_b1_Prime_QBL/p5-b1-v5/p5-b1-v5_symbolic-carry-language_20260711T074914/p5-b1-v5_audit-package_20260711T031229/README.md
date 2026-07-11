# p5-b1-v5 Audit Package

This package audits the agent artifact:

`p5-b1-v5_symbolic-carry-language_20260711T074914.zip`

It verifies package integrity and rebuild behavior, independently reproduces the finite symbolic-language counts, records the audit verdict, and supplies the outgoing instructions for `p5-b1-v6`.

## Run

From this audit-package root:

```bash
python scripts/p5-b1-v5_verify_agent_package.py /path/to/p5-b1-v5_symbolic-carry-language_20260711T074914.zip
python scripts/p5-b1-v5_symbolic_language_audit.py /path/to/p5-b1-v5_symbolic-carry-language_20260711T074914.zip
```

The first script uses only the Python standard library. The second also uses only the standard library.
