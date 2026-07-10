# Phase 5 v8f: Rank>=3 Family-F Components

STATUS: `V8F_RANK3_EQUAL_2PRIMARY_CHAIN_CLASSIFIER_CLOSED_ON_TESTED_RANGE_MIXED_HIGH_RANK_COMPONENTS_BLOCKING_OPEN`

GLOBAL_PASS: true  
PHASE5_CLOSED: false

This pass follows the authoritative v8f canonical ledger and applies split-first routing before rank>=3 classification.

## Main result

Closed exactly on the stated equal 2-primary rank-3 chain range:

- D=4: all two-edge chains
- D=8: all two-edge chains, including all v7t rank3 witnesses
- D=16: even-c margin set

The exact decision procedure is pullback equality of the quadratic form, not structural keys.

## Blocking result

The seven routed v7u rank>=3 cases remain BLOCKING_OPEN because their mixed/high-rank 2-primary cores fall outside the equal-core rank3 range closed here.

## Important negative result

Connected coupling graph does not imply indecomposable. The splitter caught secretly split connected controls, including D=8 form `[1,0,4]` splitting to `[0,0,1]`.

## Acceptance

The word classifier appears only for exact orbit/pullback-form completeness on the stated range.
