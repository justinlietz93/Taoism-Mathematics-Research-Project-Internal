# FINDINGS — p5_v8u

## Proved abstractly

1. On `Z/12Z`, `T_a(x)=x+a` is a single cycle iff `gcd(a,12)=1`; four increments `1,5,7,11` qualify.
2. Every abstract 12-cycle is conjugate to `x -> x+1`, so `+1` is a coordinate normal form rather than a clean QBL derivation.
3. The eigencharacter identity for the chosen fixed shift is exact.

## Certified finitely

- Accepted primitive trace and first-L carry reproduced from an independent oracle.
- Domain-0 local doubled surface `Z/12Z` and structural axis-block change `1 -> 2` retained.
- Newborn Domain-1 `Z/24Z` retained only as a local doubled surface.
- Four translation generators on `Z/12Z` enumerated exactly.
- Every pre-L prefix emitted with the clean successor fields open.
- v7e zero-depth legality and first-birth input mismatch checked against its source definition and executable cases.

## Open

- Clean carrier address seed `alpha_empty`.
- Native successor seed `S_empty`.
- First-`B` and all later pre-L B/Q covariance.
- First-L successor extension and retained carrier integration.
- Primary pairing, chart restrictions, directed transfers, projection, gauge, FQM, and Weil descent.

## Status lines

```text
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
FIRST_NEXT_DOMAIN_B: PASS
ACTIVE_AXIS_LOCAL_SHORTHAND: PASS
DOMAIN0_DOUBLED_CYCLIC_SURFACE: SUPPORTED
FIRST_L_AXIS_BLOCK_COUNT: 1_TO_2
NEWBORN_DOMAIN1_LOCAL_DOUBLED_SURFACE: SUPPORTED_AS_LOCAL_SURFACE_ONLY
FIRST_L_RETAINED_PRODUCT_CARRIER: NOT_YET_DERIVED
RETAINED_DOUBLED_PREFIX_ADDRESS: NOT_YET_DERIVED
FIXED_CYCLIC_SHIFT_DESCENDANT: VERIFIED_D12
NATIVE_SUCCESSOR_SEED: NOT_YET_DERIVED
PRE_L_BQ_SUCCESSOR_RECURRENCE: NOT_YET_DERIVED
FIRST_L_SUCCESSOR_EXTENSION: BLOCKED
AMBIENT_SPECTRAL_MODULE_ROLE: REQUIRED_FOR_EIGENBASIS_AND_PAIRING_FORMALIZATION
PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED
CHART_RESTRICTIONS: NOT_YET_DERIVED
MIXED_TRANSFER_RECURRENCE: NOT_YET_DERIVED
FIRST_L_ORTHAD_EXTENSION: STRUCTURAL_AXIS_BLOCK_ONLY
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```
