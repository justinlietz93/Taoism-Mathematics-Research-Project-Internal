# Orthad corrected carried walk to depth 6

**Status:** corrected rebuild after invalid depth-6 package.  
**Timestamp:** `20260620T113500`  
**Target:** run the carried Phase Calculus walk to depth 6 with no reset, no `uv > 4096` cutoff, and no fabricated capacity ladder.

## Result

The corrected walk is:

```text
(R^6 T)^6
```

where each `R` is the primitive pair `BQ`. Each domain/lap contains six `BQ` ticks followed by `L`.

Core result:

```text
B never stops.
θ never resets.
q=(u,v) never resets.
rank grows by exactly one per L.
The sign lap list has period 2.
The fabricated ladder 6→12→24→... is absent.
```

## Important finding

The internal carried sign field is period-2 by lap. The external Shadow Residual comparison is separated and performed only at the end. Under the raw carried phase-sign extractor used by `20260620T0535_orthad_carried_phase_walk.py`, the run resolves the `n=7` collision but does **not** close full χ12 orientation for all supported residues. That means the position unfolding and lap opposition are solid, while the full orientation law remains the next exact readout-law target.

## Key files

- `docs/20260620T113500_RESULTS.md`
- `docs/20260620T113500_METHOD.md`
- `docs/20260620T113500_CHANNEL_TABLE_README.md`
- `output_data/20260620T113500_channel_depth_table.csv`
- `output_data/20260620T113500_carried_seats.csv`
- `output_data/20260620T113500_external_shadow_residual_comparison.csv`
- `trace_logs/20260620T113500_ordered_primitive_trace.jsonl`
- `figures/20260620T113500_lens_matrix_mutation.gif`
- `lab_journal/lab-journal.md`
