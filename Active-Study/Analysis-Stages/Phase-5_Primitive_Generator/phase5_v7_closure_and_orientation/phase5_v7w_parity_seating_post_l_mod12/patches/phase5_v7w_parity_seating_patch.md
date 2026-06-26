# Phase 5 v7w Patch

Replace the old unresolved parity-latch note with:

```text
Post-L retained parity latch doubles the mod-6 seat to mod-12:
s12 = (n mod 6) + 6*floor((n mod 12)/6)

This separates n=7 from n=1 and recovers χ12 on support residues without scalar cargo.
```
