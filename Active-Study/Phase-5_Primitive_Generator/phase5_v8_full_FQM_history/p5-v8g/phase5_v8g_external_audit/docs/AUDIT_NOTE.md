# Phase 5 v8g External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8g generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## What was verified (all PASS)

1. FULL D=4 replication. The entire equal-D rank-3 parameter space at D=4
   (all 64 forms, chains AND triangles) was independently classified with a
   from-scratch general-shape decider. Partition matches the package
   class-by-class, and all 27 D=4 triangle dispositions match when derived
   independently (disposition = min edge count over the isometry class).
2. D=8 sampled dispositions. Stratified sample across all four labels:
   every claimed split target verified by direct isometry search (a False is
   a certificate: the search is exhaustive); core samples verified by
   same-class isometric / cross-class non-isometric spot checks. 8/8.
3. FULL mixed [2,4,2] replication. All 8 representative-invariant forms on
   Z/2 x Z/4 x Z/2 independently classified (bijectivity by image
   cardinality, valid for mixed shapes where det-parity is not). Six classes,
   exact match with the package after decoding its edge-list form encoding.
4. Scope recount. 64 + 512 = 576 rows, zero missing dispositions. The v8f
   triangle hole is closed and the scope-completeness gate is real.

## Assessment of the cross-shape rigidity resolution

The package resolves rigidity for PURE 2-primary shapes by uniqueness of the
cyclic-order multiset in a finite abelian p-group (fundamental theorem of
finite abelian groups). Correct: pure 2-group shapes admit no same-group
aliases, so cross-shape aliasing questions vanish after p-primary splitting.
The mixed-original-shape case remains only empirically gated (v8e audit) —
the package says so and does not overreach. Compliant.

## Documented caveat (carried, not new): family-split semantics

Family-F presentations pin generator q-values at 1/(2*D_i). "No same-shape
family split found" therefore does NOT prove indecomposability: a genuine
orthogonal split with non-family diagonal values would be invisible to a
same-shape search. This does not affect equality decisions (the orbit table
is the classifier) and v8g's rank-4 booking (BLOCKING_OPEN, no
indecomposability claim) is compliant. But any future claim of the form
"component X is indecomposable" requires either an extended split-target
space (arbitrary unit diagonals) or a genus/Jordan-theoretic argument.

## Obligations created for v8h

1. Rank-4 mixed core [4,4,2,16]: exact closure by pruned generator-image
   orbit search with certificates, or a reduction argument; the same-shape
   split certificate alone does not settle it.
2. If indecomposability is ever claimed, extend the split-target space
   beyond pinned family diagonals (see caveat above).
3. Rank>=5 cores: reduction-first (p-primary + Jordan blocks + splitter),
   exact orbits only on bounded irreducible cores; name any surviving
   residue precisely.

## How to run

    python3 scripts/v8g_external_audit.py [path-to-v8g-package-root]

Exit 0 = all four checks pass. Without the package path, checks 1 and 3
still run the independent mathematics; comparisons are skipped. Pure
Python, stdlib only, exact integer arithmetic in every decision path.
Runtime ~10-20 min, dominated by the D=8 sampled searches (exhaustive
non-isometry certificates are the expensive part).
