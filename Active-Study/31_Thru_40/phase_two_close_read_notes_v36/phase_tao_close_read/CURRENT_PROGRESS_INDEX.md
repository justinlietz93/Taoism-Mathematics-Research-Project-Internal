# Current Progress Index

Latest pass: `42_ANCIENT_YI_SUCCESSOR_CARRY_EXTRACTION_PASS.md`

## Most recent artifacts

- `notes/42_ANCIENT_YI_SUCCESSOR_CARRY_EXTRACTION_PASS.md`
- `ancient_yi_64_lsd_first_successor_table.csv`
- `ancient_yi_place_domain_carry_model.csv`
- `ancient_yi_successor_carry_spec.json`

## Latest addition — Ancient Yi digit-order / successor-carry extraction

Main lock:

```text
The Ancient Yi octal tables display digits least-significant-place first.

Examples:
  (10)  = 1*8^0 + 0*8^1 = 1
  (67)  = 6*8^0 + 7*8^1 = 62
  (001) = 0*8^0 + 0*8^1 + 1*8^2 = 64
  (0001)= 0*8^0 + 0*8^1 + 0*8^2 + 1*8^3 = 512
```

Bridge status:

```text
retained carrier/readout: STRONG_OPERATIONAL_BRIDGE
finite place-domain completion -> lift/carry: STRONG_OPERATIONAL_BRIDGE
successor/carry as B-like refinement: STRONG_OPERATIONAL_CANDIDATE / NOT_EXHAUSTED
```

Next useful target:

```text
Extract the line-symbol-to-digit convention for all 64 Ancient Yi rows.
```
