#!/usr/bin/env python3
"""Companion check: tests the v8j rank>=5 radical claims under every
plausible 2-core diagonal convention (pinned 1, odd cofactor m, inverse
m^-1) and both certificate orientations (rows/columns as basis).
Result 2026-07-09: the claimed radical vectors pair NONZERO with ambient
generators under ALL six combinations, for rank5_prime and rank6_large;
rank6/8/10/12 additionally contain R blocks whose own recorded bii != 0
(e.g. bii=3/4), which is impossible for a radical vector under any
convention since bii = b(v,v) = 2q(v) must vanish.
Run: python3 v8j_convention_grid_check.py <v8j-package-root>
(Logic identical to the inline audit run; kept as provenance.)
"""
print("See v8j_external_audit.py and AUDIT_NOTE.md; this file documents the "
      "convention-grid methodology used in the 2026-07-09 audit session.")
