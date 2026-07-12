# Phase 5 v7s: 2-Primary Normalization and Jordan Symbol Policy

Status: `TWO_PRIMARY_NORMALIZATION_AND_JORDAN_SYMBOL_POLICY_SUPPORTED_ON_CYCLIC_PLUS_UV_BLOCK_SWEEP`  
Global pass: `true`  
Phase 5 closed: `false`

## Main correction

v7s upgrades v7r by adding an explicit 2-primary normalization policy. The raw matrix or `c_ij` presentation is not the invariant. The invariant comparison now goes through:

```text
T-derived finite module presentation
  -> p-primary split
  -> 2-primary Jordan block policy
  -> radical rejection
  -> Brown / oddity / U-V block tags
  -> sorted direct-sum Jordan symbol
  -> gauge/isometry comparison
```

## Result counts

```json
{
  "block_rows": 138,
  "cyclic_odd_block_rows": 126,
  "even_rank2_block_rows": 12,
  "generator_orbit_checks": 126,
  "generator_orbit_passed": 126,
  "direct_sum_symbol_rows": 1076,
  "negative_controls": 21,
  "negative_controls_passed": 21,
  "unique_normal_keys": 34
}
```

## Boundary

This pass does not claim complete global finite quadratic module classification. It establishes the policy layer needed before Orthad can compare 2-primary FQM outputs without raw-coordinate false contradictions.
