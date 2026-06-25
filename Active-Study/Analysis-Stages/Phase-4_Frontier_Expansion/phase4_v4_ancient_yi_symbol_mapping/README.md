# Phase 4 v4 — Ancient Yi Symbol Mapping

Status: `SYMBOL_TO_RETAINED_CARRIER_MAPPING_CLOSED`

This package maps Ancient Yi symbols, names, King Wen numbers, Unicode hexagrams, binary source order, and Yi octal display into the retained LSD-first six-line/octal carrier closed in Phase 3 v4.

## Result

The source table rows map cleanly:

```text
six-line source display: top-to-bottom
bit assignment: top line = 2^0, ..., bottom line = 2^5
octal display: least-significant digit first
low octal digit: top three displayed lines
high octal digit: lower three displayed lines
unicode / King Wen / names: terminal symbol cross-reference layer
Yi decimal order: retained carrier value order
```

## Hard numbers

```json
{
  "rows_reconstructed": 64,
  "unique_unicode_hexagrams": 64,
  "unique_king_wen_numbers": 64,
  "binary_failures": 0,
  "octal_failures": 0,
  "successor_failures": 0,
  "unicode_kingwen_failures": 0,
  "line_column_failures": 0,
  "projection_loss_witnesses": 4
}
```

## Main files

- `docs/phase4_v4_ancient_yi_symbol_mapping.md`
- `outputs/phase4_v4_symbol_to_carrier_mapping_table.csv`
- `outputs/phase4_v4_line_position_mapping.csv`
- `outputs/phase4_v4_gate_matrix.csv`
- `outputs/phase4_v4_verification_summary.json`
- `scripts/phase4_v4_ancient_yi_symbol_mapping.py`
- `notebooks/phase4_v4_ancient_yi_symbol_mapping.ipynb`
- `proofs/Phase4V4AncientYiSymbolMapping.lean`
