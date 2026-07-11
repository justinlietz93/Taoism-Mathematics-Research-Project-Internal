# Phase 5 v8k External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8k generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## Verified (all PASS)

1. WORKED CERTIFICATE IS DATA AND CORRECT. basis [[1,0],[1,1]] on the
   [2,2] c01=1 form verifies exactly: q(v0)=1/4 (A_2(1)), v1 pairs to zero
   with every ambient generator (true radical, ambient test — the v8j bug
   is fixed), q(v1)=0, cross-orthogonal, spans. CERTIFICATE_IS_DATA and
   RADICAL_BII_ZERO genuinely enforced, not just named.
2. RADICAL SIZES FOR ALL FIVE CORES independently confirmed by SNF kernel
   counting (radical = kernel of the Gram system; |Rad| computed exactly
   from Smith invariant factors, no enumeration), validated against full
   enumeration on rank5 (1024 elems) and rank6 (16384 elems):
   4 / 8 / 64 / 256 / 2048 — all five match the package.
3. FORM SPEC MATH CORRECT: diag_units [1,3,3,5] reproduce exactly from the
   odd cofactors mod 2D ([1,3,15,5] -> [1,3,3,5]).
4. RETRO-CHECK PREMISE SUBSTANTIATED: pinned vs true-diagonal archival
   forms have different q-value histograms — genuinely non-isometric
   objects. v8h had classified the wrong object; the retro-check was
   necessary, not cosmetic.
5. HONEST SCOPE: 229/229 and all five core decompositions booked
   BLOCKING_OPEN; no v8j certificate reused; dispositions carry scope and
   evidence. Correct post-reject behavior: claim less, verify all.

## One publication gap (obligation, not a reject)

The retro-check books CLOSED_POSITIVE_AFTER_RETROCHECK citing a NEW
true-diagonal orbit table (512 forms, 14 classes, archival in class 6)
that is NOT in the package — no class table, no representatives, no
decision certificates. The premise is verified (above); the conclusion
rests on unpublished ground truth. Under CERTIFICATE_IS_DATA, the table
and its decision certificates must be published in v8l before the
retro-check row is fully closed.

## Obligations created for v8l

1. Publish the true-diagonal rank-4 orbit table with decision certificates
   (same standard as v8h's pinned table, which was externally verified).
2. Ground-truth decomposition 229/229 with per-row data certificates
   (basis matrices), radical-first, ambient radical test.
3. Rank>=5 cores: radical-first decomposition with data certificates using
   the completed form specs. Radical sizes are large (up to 2048 at rank
   12) — stripping the radical first shrinks the nondegenerate part
   substantially; report each core's nondegenerate complement shape.
