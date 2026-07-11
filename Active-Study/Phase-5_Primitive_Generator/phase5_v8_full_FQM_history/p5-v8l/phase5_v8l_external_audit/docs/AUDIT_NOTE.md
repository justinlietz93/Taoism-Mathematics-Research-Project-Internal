# Phase 5 v8l External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8l generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.
Artifact of record: phase5_v8l_full_decomposition_under_data_gates.zip
SHA256 3c8e0bd24d9aec500a994182ca2f44ae6fb9553e4a0720ab0d9929249fd50f32
(agent-quoted 45b3275b... does not match the uploaded artifact; the internal
MANIFEST_SHA256SUMS verifies with 0 failures, so package content integrity is
intact — the outer hash discrepancy is a transport/serialization question, not
a content defect. The hash above is the one that binds this audit.)

## Verdict: PARTIALLY ADOPTED

The owed table is real, complete, and verified to the same standard as the
pinned v8h table. The two commissioned decomposition targets were not
attempted. Nothing published overclaims; one provenance gap and one
identifier-stability defect were found.

## Verified (all PASS, all independent)

1. TRUE-DIAGONAL RANK-4 TABLE — FULL INDEPENDENT RE-CLASSIFICATION. The audit
   enumerated all 512 admissible forms on [4,4,2,16] with diag units [1,3,3,5]
   and classified them from scratch (own fingerprint invariant, own exhaustive
   isometry decider with SNF span test): 14 classes, partition IDENTICAL to
   the published table (bijective class match, identical member sets;
   512/512 unique disposition rows consistent with the class table).
2. ALL 530 DECISION ROWS. 498 positives: every witness basis verified as data
   (image orders divide block orders, generator q-values match, all pairwise
   b-values match, SNF span certificate). 32 negatives: every one confirmed by
   the audit's independent partition. Coverage complete: every non-representative
   member has a verified positive decision to its class representative. Zero
   prose in any certificate column.
3. FINGERPRINT DISCIPLINE. (order,q)-multiset constant within every published
   class (0 violations). 13 fingerprint groups; exactly one cross-class
   collision (published ids 11/12), separated by the audit's own exhaustive
   search — the same collision structure the pinned table had.
4. ARCHIVAL MEMBERSHIP. The archival form (c01=3,c02=2,c03=4,c12=2,c13=12,
   c23=0) lands in published class 5 under the audit's own classification.
   The published claim is correct for the published table.
5. GROUND-TRUTH CSV. 229 rows exactly (193 v8e + 22 v8g + 14 v8h). Per-row
   radical size, q-values on radical, and radical witnesses re-verified by
   enumeration: 0 mismatches. The single certified row ([2,2] c01=1 =
   A_2(1) PERP R_2(q=0), basis [[1,0],[1,1]]) passes the full section-V
   standard (span, orders, cross-block b=0, A-block q, ambient radical test,
   b(v,v)=0, q(v)=0).
6. FIVE CORES. SNF radical sizes re-confirmed: 4/8/64/256/2048 (method
   re-validated against full enumeration at rank5 and rank6). Every published
   radical generator verified ambient-radical against all standard generators;
   generator spans enumerated and equal to the full radicals; q-values on the
   radicals match. QUOTIENT SHAPES verified by SNF and match the published
   nondegenerate complement shapes:
     rank5  -> [2,2,4,16]
     rank6  -> [2,4,4,4,16]
     rank8  -> [2,2,2,2,4,4,4,16]
     rank10 -> [2,2,2,2,2,4,4,4,16]
     rank12 -> [2,2,2,4,4,4,4,4,16]
   Consequence worth naming: all five complements are nondegenerate pure
   {2,4,16}-shapes — Wall's theorem guarantees pure A/UV decompositions exist.
   No new mathematics is needed to close the cores; only honest construction.

## Findings

F1. ARCHIVAL EDGE PROVENANCE (P4 pattern). The archival form's six edge values
    are HARDCODED in the agent's script (line 322) even though the script
    extracts the v8h/v8k upstream packages it could have loaded them from. No
    provenance diff CSV exists for these values. This is exactly the retyping
    pattern that lost the rank10/12 edge lists in v8h. The table itself is
    verified regardless; the RETRO-CHECK ROW stays one notch below full
    closure until a programmatic diff of (six edges + diag units) against the
    upstream artifact is emitted.
F2. CLASS-ID INSTABILITY (new standing rule). v8k cited "archival in class 6";
    the published table says class 5; the audit confirms 5 is correct for the
    published table. The agent's class ids depend on Python set-iteration
    order — not stable identifiers. STANDING RULE 5 (STABLE_CLASS_KEYS)
    adopted in the ledger: every published class carries an invariant key
    (lexicographically minimal member as canonical representative + the
    (order,q)-multiset fingerprint); cross-package citations use the key,
    never the integer id.
F3. WORDING: result card publishes global_pass=true while two of its own
    declared gates fail (GROUNDTRUTH_CERTIFICATE_DATA 228 failures,
    RANKGE5_CERTIFICATE_DATA 5 failures). The status string is honest; the
    boolean is not. global_pass must be the AND of declared gates or be
    renamed.
F4. THE HARD DELIVERABLES WERE NOT ATTEMPTED (P7 watch). Commission items 2
    and 3 returned 1/229 and 0/5 with status "not_constructed" — no failure
    vectors, no attempted splits, no named obstruction. Honest bookkeeping,
    but this is the second consecutive package in which the decomposition
    target produced nothing, and at rank<=4 (group order <=512 per row) no
    computational excuse exists. The v8m commission is scoped to make partial
    delivery impossible: the 229 are the sole deliverable.

## Obligations created for v8m

1. 229/229 radical-first decomposition, per-row explicit basis-matrix
   certificates passing section V. Sole closing target.
2. Provenance diff CSV for the archival form spec (F1).
3. Stable-class-key patch columns for the v8l table (F2); state whether the
   v8k "class 6" was the same class under a different run ordering.
4. global_pass semantics fix (F3).
Cores are v8n, alone, after the 229 machinery is proven at scale.
