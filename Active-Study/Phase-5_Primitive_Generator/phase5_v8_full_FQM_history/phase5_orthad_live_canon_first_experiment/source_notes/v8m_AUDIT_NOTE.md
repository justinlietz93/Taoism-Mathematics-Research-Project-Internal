# Phase 5 v8m External Audit

Date: 2026-07-10
Auditor: external (Claude), independent of the v8m generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md (merged: user's canon
revision of 07-10 + audit entries); findings recorded there.
Artifact of record: phase5_v8m_the_229_data_gated_decomposition_package.zip
SHA256 9e5b3b4e8fc58bf8e2097d4cde2334df97287843416a7996a88abbf28e462107
(matches the agent's quoted hash; internal MANIFEST verifies, 0 failures.)

## Verdict: ADOPTED — with one target restored and one major structural
## finding that redefines the rank>=5 path

## Verified (all PASS, all independent)

1. ALL 229 CERTIFICATES. Every basis-matrix certificate re-verified by the
   auditor's own section-V engine: SNF span, per-vector order = block D,
   cross-block b = 0, generator-level q/b agreement; R blocks pass the
   ambient radical test with b(v,v)=0 and q in {0, M/2}; the package's GRAM
   block type verified as honest recorded data (recorded q_xM vector and
   b_xM matrix match actual values on the basis vectors). 0 failures.
   Per-row radical sizes and M re-verified by enumeration: 0 mismatches.
2. THE 65 SPLIT ROWS ARE COMPLETE SPLITS. For every row booked
   RADICAL_DIRECT_SUMMAND_DECOMPOSED: the R-block vectors generate the FULL
   ambient radical (subgroup span = radical size), and every GRAM remainder
   is independently confirmed nondegenerate. No partial split was booked as
   a full one. Purity spot-checks on split rows consistent (pure, as they
   must be).
3. THE 26 UNSPLIT ROWS ARE A REAL WALL — NON-SUMMAND PROVEN. For each of the
   26, the auditor ran an exact purity test (for finite abelian groups, a
   subgroup is a direct summand iff it is pure; the radical is orthogonally
   complemented iff it is a group-theoretic summand, since any complement of
   the radical is automatically orthogonal). All 26 radicals are NON-PURE,
   each with an explicit machine-checkable witness: a radical vector r and
   integer n with r in (R meet nA) \ nR. 22 witnesses at n=2; 4 at n=3 (the
   [18,18] rows fail purity in the 3-part). Zero pure cases: the agent's
   BLOCKING_OPEN was not an implementation bug (no P6). Failure vectors
   confirmed radical; failure-rows CSV consistent with the main CSV.
4. F1 PROVENANCE DIFF: emitted, internally consistent (six edges + diag
   units match the values the v8l audit verified). Upstream values are
   agent-attested; future provenance diffs must carry upstream file path +
   SHA columns.
5. F2 STABLE CLASS KEYS: all 14 canonical representatives (lexmin members)
   and (order,q)-multiset fingerprints match the auditor's independent
   recomputation from the verified v8l class table. The v8k "class 6" /
   v8l "class 5" discrepancy is reconciled as the same invariant class under
   run-order-dependent integer labels. The archival retro-check row is now
   FULLY CLOSED.
6. F3: global_pass is now the AND of declared gates and correctly reads
   false. Scope gate 229/229, sources 193 v8e + 22 v8g + 14 v8h.

## Major finding (audit extension): THE FIVE CORES SHARE THE DISEASE

The same purity test, run on the five residual cores (specs verified in the
v8l audit), proves ALL FIVE core radicals are NON-SUMMAND:

  rank5  witness (0,2,2,0,8)              n=2   |Rad|=4     q|Rad in {0,1/2}
  rank6  witness (0,0,0,0,4,4)            n=2   |Rad|=8     q|Rad in {0,1/2}
  rank8  witness (0,0,0,0,0,4,0,4)        n=2   |Rad|=64    q|Rad = 0
  rank10 witness (0,0,0,0,0,4,0,4,0,0)    n=2   |Rad|=256   q|Rad = 0
  rank12 witness (0,0,0,0,0,0,0,4,0,0,4,0) n=2  |Rad|=2048  q|Rad in {0,1/2}

Consequences, stated exactly:
- The radical-first strip-then-Wall plan is IMPOSSIBLE as stated for every
  actual blocking target. The standing assumption "all family-F radicals
  are direct summands" is REFUTED.
- AUDITOR RETRACTION: the v8l audit's line "all five complements are
  nondegenerate pure {2,4,16}-shapes, so Wall guarantees pure A/UV
  decompositions exist with no new mathematics" was unsound. The verified
  quotient shapes stand as GROUP data (A/Rad), but no orthogonal complement
  subgroup realizes them, and the quadratic form even descends to the
  quotient only for rank8/rank10 (where q|Rad = 0). The auditor's inference
  was the loose joint; recorded in the ledger's guardrail lessons.
- The path forward is the DEGENERATE-BLOCK ALPHABET: decompositions into
  indecomposables that allow degenerate letters (explicit Gram+q data),
  per-letter indecomposability certificates, and a catalog of the distinct
  degenerate indecomposable letters occurring across the 26 (predicted
  small). Kawauchi-Kojima filtration invariants are the fallback route.
  The 26 proven non-summand rows are the natural calibration set before
  touching the cores.

## One restoration (P3 guard)

v8m's claim CSV carries "certificate gate" and "radical direct-summand
split" rows but NO disposition row for the full block-alphabet
decomposition of the 229 (the original v8l-commission item 2 object). The
target did not fail; it vanished between scope labels. RESTORED in the
ledger as the v8n definition above. Additionally, the audit upgrades the
"radical direct-summand split 229/229" disposition from BLOCKING_OPEN to
CLOSED_NEGATIVE_PROVEN (witnesses in this package) — an open row whose
impossibility is proven must not remain "open."

## Conduct note

Correct post-commission behavior on the hard target this time: the agent
attempted the split everywhere, split everything splittable (65/65 complete,
verified), and booked the genuinely impossible 26 with failure vectors and
exhausted search lists instead of relabeling. The wall it hit is real and is
now a theorem with witnesses. This is the mirror image of v8i, resolved in
one pass instead of two.
