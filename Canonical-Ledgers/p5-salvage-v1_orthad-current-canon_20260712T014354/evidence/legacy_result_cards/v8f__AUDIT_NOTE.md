# Phase 5 v8f External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8f generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## What was verified

1. Flagship splitter control. The connected D=8 chain (c01,c02,c12)=(1,0,4)
   is isometric to the split form (0,0,1). Verified from scratch: explicit
   witness basis found by independent generator-image search, then confirmed
   by POINTWISE q equality over all 512 group elements. Exact integers,
   no floats.

2. Full independent re-classification at D=4. All 16 chain forms (c02=0)
   classified with an independent decider; result is 5 classes matching the
   package's orbit table class-by-class, member-by-member. The audit run
   independently rediscovered the secret split (2,0,2) ~ (0,0,0) without
   being pointed at it.

## Finding: equal-D triangle scope hole (five-disposition-law violation)

v8f classifies CHAINS only (c02 = 0). Forms with all three edges nonzero
(triangles) are reachable in family F via three O_ij events, are equal-D
and rank 3 — so they fall in neither the closed chain scope nor the
mixed/high-rank BLOCKING_OPEN scope — and carry NO disposition row anywhere
in the package (zero mentions across docs and CSVs). A target did not get
mislabeled; it silently ceased to exist between two adjacent scope labels.
Booked in the ledger as BLOCKING_OPEN (audit-added). This is the third
distinct leak class in the arc: v7z = name over-reach, v8c = hidden
deferral premise, v8f = gap between scopes. None is catchable by gates that
only check whether listed targets pass; hence the v8g scope-completeness
gate (enumerate the full parameter space of the stated range and prove the
scoped subsets cover it).

## Obligations created for v8g

1. Classify equal-D triangles (D=4, D=8 complete), splitter-first; every
   triangle gets a disposition row.
2. Adopt the scope-completeness gate as a standing control.

## How to run

    python3 scripts/v8f_external_audit.py [path-to-v8f-package-root]

Exit 0 = checks 1 and 2 pass. Check 3 is informational (writes the scope-
hole evidence CSV). Without the package path, the cross-comparison in
check 2 and the mention-scan in check 3 are skipped; the independent
mathematics still runs. Pure Python, stdlib only. Runtime ~1 min,
dominated by the D=8 flagship search.
