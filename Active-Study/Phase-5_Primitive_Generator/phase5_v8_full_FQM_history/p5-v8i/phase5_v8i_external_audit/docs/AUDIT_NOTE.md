# Phase 5 v8i External Audit

Date: 2026-07-09
Auditor: external (Claude), independent of the v8i generating agent.
Authority: subordinate to PHASE5_CANONICAL_LEDGER.md; findings recorded there.

## Provenance patch: VERIFIED

All seven restored edge lists match the v8g upstream artifact exactly,
including rank10_large (41 edges) and rank12_large (62 edges). Credit: the
agent's programmatic diff also caught rank3_mixed (3 edges lost in v8h),
which the prior external audit's narrower comparison missed. The provenance
gate works.

## Splitter failure: DIAGNOSED — implementation gap, not a wall

The v8i splitter failed ground-truth validation on 91/229 forms, all with
reason NO_CERTIFIED_A_OR_EQUAL_LEVEL_UV_PIVOT, and the package booked the
splitter CLOSED_NEGATIVE as a closure path. The booking was honest, but the
implicit frame ("path rejected") is wrong. This audit independently computed
the radical Rad = {x : b(x,y)=0 for all y} of every one of the 229
validation forms:

    split_success  <=>  |Rad| = 1     ...  229/229 rows, zero exceptions.

The splitter succeeds on every nondegenerate form (138/138) and fails on
every degenerate form (91/91). Cause: the pivot search demands a
unit-diagonal A pivot or an invertible equal-level UV Gram; a radical vector
can satisfy neither (it pairs to zero with everything), so the search
starves with the radical as the active residual — exactly the observed
failure signature. The block alphabet is missing a RADICAL block type.
Wall/Kawauchi-Kojima theory is untouched: it guarantees decomposition of
NONDEGENERATE forms, and on those the splitter already achieves 100%.

Worked completion: the smallest failed case, shape [2,2] c01=1, decomposes
as A_2(1) PERP R_2(q=0) — explicit orthogonal basis (1,0), (1,1); span,
orthogonality, radical membership, and pointwise q-additivity all verified
exactly. The agent's own partial output (A_2(1) + active residual [1]) was
one block short of the answer.

Family F genuinely contains degenerate forms (v8e flagged PASS_WITH_RADICAL
when it classified them), so radical handling is mandatory, not optional.
Remaining genuine subtlety for v8j: a radical need not be a direct summand
of the carrier group in general (e.g. 2Z/4 inside Z/4); whether non-summand
radicals actually occur inside family F is measurable and must be measured.

## Obligations created for v8j

1. Radical-first decomposition: compute Rad and q|Rad before any pivot;
   split radical blocks with certificates where Rad is a summand; recurse
   the existing (validated-on-nondegenerate) A/UV machinery on the rest.
2. Measure whether any family-F validation or residual case has a
   non-summand radical; if yes, those cases need filtration invariants
   (Kawauchi-Kojima) and must be named individually.
3. Re-run the full 229-row ground-truth validation; target 229/229.
4. Only then re-attempt the five rank>=5 residual cores.

## How to run

    python3 scripts/v8i_external_audit.py <v8i-package-root> <v8g-package-root>

Exit 0 = all checks pass. Outputs: audit_radical_correlation.csv (all 229
rows with radical sizes and q|radical), audit_worked_completion.csv. Pure
Python, stdlib only, exact integer arithmetic. Runtime ~5-15 min, dominated
by radical scans over the 512-element groups.
