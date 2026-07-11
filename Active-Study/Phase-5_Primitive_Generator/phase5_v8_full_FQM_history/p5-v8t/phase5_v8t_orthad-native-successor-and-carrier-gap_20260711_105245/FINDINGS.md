# Findings

## Status

```text
PRIMITIVE_FIRST_CROSSING: PASS
FIRST_L_CARRY: PASS
FIRST_NEXT_DOMAIN_B: PASS
ACTIVE_AXIS_LOCAL_SHORTHAND: PASS
SPECIFIED_PHASE5_ARTIFACT_LINEAGE: PASS
EXTERNAL_OVERSET_SOURCE_CORPUS: INCOMPLETE
CONCRETE_RETAINED_CARRIER: DERIVED_AS_FINITE_AXIS_PRODUCT_CARRIER
NATIVE_SUCCESSOR_RECURRENCE: NOT_YET_DERIVED
AMBIENT_MODULE_FUNCTOR_ROLE: OPTIONAL_FORMAL_PRESENTATION
PRIMARY_PAIRING_RECURRENCE: NOT_YET_DERIVED
CHART_RESTRICTIONS: NOT_YET_DERIVED
MIXED_TRANSFER_RECURRENCE: NOT_YET_DERIVED
FIRST_L_ORTHAD_EXTENSION: STRUCTURAL_AXIS_BLOCK_EXTENSION_ONLY
ORTHAD_CAUSAL_PROJECTION: NOT_RUN
GAUGE_FQM_WEIL_DESCENT: NOT_RUN
```

## Main result

The supplied and inventoried source set supports **case 2**. The clean state plus the doubled-carrier and independent-axis results fixes a concrete finite product carrier:

- before the first L: `Z/12Z`;
- immediately after L: inherited `Z/12Z` times newborn `Z/24Z`;
- structural axis-block count: `1 -> 2`.

The historical cyclic successor `s_D(r)=r+1 mod D` is rederived exactly on the fixed factors `D=12` and `D=24`. What is not derived is the clean word-dependent successor recurrence, especially the first-L extension map and its intertwining law. The sources do not decide whether the retained product has one global successor cycle or a commuting family of factor successors.

The earliest exact gap is therefore `Phi_L^S`, not an ambient-module functor and not a scalar mixed term.

## Why interesting

This moves the hard stop one layer earlier and makes it concrete. The carrier and point basis no longer need to be invented. The missing object is the successor action on that carrier under the clean B/Q/L history. That gap blocks the claimed successor-to-pairing generative direction before chart modules or transfers are introduced.

The additional v7 sources sharpen two historical formulas without promoting them:

- v7q ratios survive as an exact local scalar cochain;
- v7e shared-L coupling is a reconstruction clue for two preexisting axes, but its input type is not satisfied at the first axis birth.

## Scope

No primary pairing, chart restriction, directed transfer, terminal projection, gauge quotient, FQM object, or Weil descent is emitted. The exact accepted baseline SHA and five reused evidence paths are emitted in `outputs/20260711T105245_baseline_reuse_inventory.csv`. The unavailable `phase5_v5_orthad_primitive_origin_audit_package.zip` and `orthad_overset_grids.zip` prevent a complete historical-corpus claim.


Verification is evidence-bound to the baseline ZIP, source snapshot, full carrier prefix table, fixed cyclic-successor witnesses, local v7q ratio table, and the nondegenerate bilinear witness. Fourteen current tests pass, and twenty-one temporary-copy corruption controls make their named gates fail. The clean rebuild matches all seventeen deterministic scientific artifacts byte-for-byte under the documented normalized-semantic contract.
