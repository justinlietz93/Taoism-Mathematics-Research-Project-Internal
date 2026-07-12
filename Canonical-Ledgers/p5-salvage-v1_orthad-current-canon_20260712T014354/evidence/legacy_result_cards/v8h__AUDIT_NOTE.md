# Phase 5 v8h External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8h generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## Rank-4 [4,4,2,16] classifier: VERIFIED

1. Loop soundness. The v8h classifier pre-groups the 512 forms by q-value
   histogram and runs a leader algorithm within groups. Sound: the q-value
   multiset is a true isometry invariant (an isometry is a q-preserving
   bijection), and the leader algorithm is complete because isometry is an
   equivalence relation. The 530-decision count (rather than ~512 x 14) is
   explained by this pre-grouping and is legitimate.
2. Every positive certificate re-verified: 498/498 witness bases pass
   independent pointwise q-pullback over all 512 group elements (exact
   integers, bijectivity by image cardinality).
3. Independent fingerprint — the multiset of (element order, q value) pairs,
   computed from scratch for all 512 forms — is constant within every one of
   the 14 claimed classes (0 violations). Exactly one fingerprint collides
   across classes; the colliding cross-class pair was separated by an
   independent exhaustive generator-image search (non-isometry certificate).
   Every other class separation follows from the fingerprints alone.
   Net: the 14-class partition is confirmed sound (no false merges: witnesses
   verify) and complete (no false splits: fingerprints + exhaustive sample).

## Finding: rank10/rank12 residual-core edge data LOST in transcription

The v8h script hardcodes its archival table "from v8g known rows" — but the
rank10_large and rank12_large entries were hardcoded with EMPTY edge lists,
while the upstream v8g routing rows carry 41 and 62 2-core edges
respectively. v8h then published surviving cores claiming "edges": [] for
those two cases. Consequences:
- The BLOCKING_OPEN dispositions remain correct (no classifier was claimed).
- But the named surviving cores — the pass's deliverable for these cases —
  are wrong for 2 of 5. An edgeless core would falsely suggest those cases
  are trivially classifiable as uncoupled carrier products.
- rank4/rank5/rank6/rank8 edges match upstream exactly (verified), so the
  loss is isolated to the two largest cases.
This is the "forgotten critical detail" failure mode appearing as silent
data loss rather than a conceptual slip. Correction: restore the edge lists
from v8g (this audit's outputs/audit_rankge5_edge_provenance.csv contains
the full v8g edge lists for both cases) and republish the routing rows.

## Obligations created for v8i

1. PATCH: restore rank10/rank12 edges_2core from v8g and republish the
   named surviving cores. Add a standing provenance gate: archival data
   carried across packages must be diffed against the upstream artifact,
   never retyped.
2. Attack rank>=5 by constructive block decomposition (extended-diagonal
   splitting), not orbit enumeration — see commission.

## How to run

    python3 scripts/v8h_external_audit.py <v8h-package-root> [v8g-package-root]

Exit 0 = rank-4 checks pass. Check 4 (provenance) reports findings in
audit_rankge5_edge_provenance.csv. Pure Python, stdlib only, exact integer
arithmetic in every decision path. Runtime ~15-30 min, dominated by
re-verifying 498 witnesses over 512 elements each and the exhaustive
non-isometry sample.
