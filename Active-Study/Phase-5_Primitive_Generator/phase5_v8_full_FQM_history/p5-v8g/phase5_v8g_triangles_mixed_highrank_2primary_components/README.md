# Phase 5 v8g: Triangles + Mixed/High-Rank 2-Primary Components

STATUS: `V8G_TRIANGLES_AND_MIXED_RANK3_CLASSIFIER_CLOSED_MIXED_HIGH_RANK_COMPONENTS_BLOCKING_OPEN`

GLOBAL_PASS: true  
PHASE5_CLOSED: false  
v8c: SUSPENDED_REMAINS_SUSPENDED

## Main result

v8g closes the v8f audit hole: equal-D triangles now have disposition rows. The pass enumerates the full D=4 and D=8 rank-3 equal-D Family-F parameter spaces, runs splitting before classification, and verifies that zero forms are missing from the disposition table.

## Triangle counts

```text
{
  "TRIANGLE_CORE_CLASSIFIED_BY_EXACT_ORBIT_TABLE": 126,
  "TRIANGLE_SPLITS_TO_CHAIN": 204,
  "TRIANGLE_SPLITS_TO_SIZE2": 27,
  "TRIANGLE_SPLITS_ENTIRELY": 13
}
```

## Mixed/high-rank result

The v7u rank-3 mixed 2-primary core `[2,4,2]` is classified exactly on its full representative-residue range. The v7u rank-4 and higher mixed/high-rank cores remain BLOCKING_OPEN.

## Scope-completeness gate

Every D=4 and D=8 equal-D rank-3 form has one disposition row. Missing rows: `0`.
