
# 65. Ancient Yi Full Table Reconstruction and Line-Order Proof v58

## Status

`AVAILABLE-SOURCE TABLE BLOCKER RESOLVED FOR BRIDGE RESEARCH`

This pass converts the Ancient Yi 64-row table from a partially inspected image table into a machine-readable reconstruction with row locators, binary/octal/decimal fields, successor events, and line-order proof rows.

## Output files

- `ancient_yi_full_64_table_reconstruction_v58.csv`
- `ancient_yi_line_order_proof_rows_v58.csv`

## Key result

The source table is not using ordinary left-to-right most-significant octal order. It displays the least-significant place first.

```text
source row 0: 坤, binary 000000, octal 00, decimal 0
source row 1: 剥/剝, binary 100000, octal 10, decimal 1
source row 2: 比, binary 010000, octal 20, decimal 2
source row 3: 观/觀, binary 110000, octal 30, decimal 3
```

The decisive line-order inference is:

```text
six-line carrier is displayed top-to-bottom,
but the top line is the 2^0 place.
```

That is why `100000` is decimal `1` in the source table and names 剥/剝, the hexagram with the single yang line at the top.

## Full 64-row state-machine interpretation

For every decimal state `d` from `0` to `63`:

```text
binary_display = six-bit expansion of d written least-significant bit first
source_octal_display = two octal digits written least-significant digit first
successor(d) = d + 1 for d < 63
successor(63) = 64 = 001 in the source's three-place octal display
```

The bridge statement is now stronger:

```text
retained six-line carrier
-> fixed top-to-bottom line-order convention
-> LSD-first binary/octal readout
-> successor within finite two-place octal domain
-> 77 completion
-> 001 higher-place carry/lift
```

## Remaining philological limit

This table reconstruction resolves the operational bridge blocker. A philological edition would still require a human Chinese edition check of every printed name glyph against the source scan, but that is no longer a bridge-level blocker because the row order, line-order convention, and successor/carry law are mechanically determined by the source formulas and confirmed by the first-page source rows.
