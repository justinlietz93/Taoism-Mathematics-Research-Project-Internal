# p5-b3-v2 Audit Package

This package audits `p5-b3-v2_hierarchical-grammar-factor-scope_20260711T134500.zip`.

It contains the audit verdict, reproduced integrity checks, an independent scope check, and the outgoing `p5-b3-v3` instruction package.

Run the package verifier:

```bash
python scripts/p5-b3-v2_verify_agent_package.py \
  /path/to/p5-b3-v2_hierarchical-grammar-factor-scope_20260711T134500.zip \
  --expected-zip-sha256 aaf8690e8a64ac531dce4be785b37139a0551be59bebf8279142a10953b311ec \
  --expected-document-sha256 63a522df4882409f7147ea96db128554b9a87530d880780cb8ffbda8025f31fd
```

Run the independent scope audit against an extracted agent package root:

```bash
python scripts/p5-b3-v2_verify_factor_scope.py /path/to/extracted/package/root
```
