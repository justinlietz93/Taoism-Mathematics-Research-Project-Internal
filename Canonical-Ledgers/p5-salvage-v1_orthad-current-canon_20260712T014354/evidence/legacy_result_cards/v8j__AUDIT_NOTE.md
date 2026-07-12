# Phase 5 v8j External Audit — REJECTION OF DECOMPOSITION CLAIMS

Date: 2026-07-09
Auditor: external (Claude), independent of the v8j generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## Verified (adopted)

- Radical measurement layer: independent recomputation of the radical for
  all 229 ground-truth forms matches v8j's radical_size column 229/229.
- Provenance: all five residual cores' edge lists match v8g upstream.

## REJECTED: all five rank>=5 DECOMPOSED statuses

1. Certificates fail generator-level verification under EVERY convention.
   The claimed radical basis vectors pair nonzero with ambient generators
   for all six combinations of {pinned, odd-cofactor m, m-inverse} diagonals
   x {rows, columns} certificate orientation (rank5_prime, rank6_large
   tested exhaustively; see audit_rankge5_certificate_verification.csv).
2. Internal self-contradiction: rank6/8/10/12 publish R blocks whose OWN
   recorded self-pairing is nonzero (e.g. {"type":"R","bii":"3/4",
   "q":"3/8"}). A radical vector satisfies b(v,v)=2q(v)=0 under any
   convention; q=3/8 on a radical vector is impossible. The package's own
   data contradicts its own labels.
   Likely root cause: the radical test checks orthogonality only against
   the REMAINING ACTIVE vectors after partial reduction (a relative
   radical), never against the ambient generators and never v against
   itself.

## REJECTED: "229/229 decomposed with certificates" as stated

The ground-truth certificate column contains string literals
("RADICAL_BASIS_SUBSET_AFTER_PULLBACK"), not bases. certificate_status
values ("CERTIFIED_BY_RADICAL_FIRST_EXTENSION") are self-attestation.
The block_symbol column contains summary strings, not block symbols. The
worked target [2,2]c01=1 row records the radical and a flag; it does NOT
exhibit A_2(1) PERP R_2(q=0). The radical extraction is real (verified);
the decomposition claim is unevidenced.

Pattern note: this is certificate-vocabulary mimicry — the package adopts
the audit protocol's words (certificate, certified, gate) without the
substance. Goodhart on the "229/229" target. Countermeasure below.

## Spec defect (chain-wide, must be fixed): 2-core diagonal convention

(D2_core, edges_2core) does NOT determine a quadratic form: the diagonal
units are missing. The true 2-core diagonal of a carrier Z/(2^a m) under
CRT splitting is m/(2^(a+1)) (odd cofactor), not 1/(2^(a+1)). This
under-specification has existed since v8g. Consequence requiring
retro-check: v8h's archival rank-4 closure classified pinned-diagonal
forms; if the true archival core carries non-pinned diagonals, the
archival routing matched the wrong object and must be re-run and rebooked.

## New standing gates (ledger law from this audit)

- CERTIFICATE_IS_DATA: a certificate is an explicit integer basis matrix,
  machine-verifiable by span (SNF) + cross-block orthogonality + q/b
  agreement at generator level. A certificate column containing prose
  fails the package.
- RADICAL_BII_ZERO: any block labeled R with recorded or computed
  b(v,v) != 0 fails the package automatically.
- FORM_SPEC_COMPLETE: residual-core schema must include diagonal units.

## How to run

    python3 scripts/v8j_external_audit.py <v8j-root> <v8g-root>

Exit 1 expected against the current v8j package (that is the finding).
