# 39 — Ancient Yi readout table and data-request-aware continuation

## Status

Continued the external-source analysis while Liu 2022 data access is pending from repository/authors.

The strongest work in this pass was a manual figure/table pass over `Tao-Research/out/Unearthing-the-Ancient-Yi_Chinese.pdf` using rendered pages from the image-only PDF.

## Resource advanced

```text
Tao-Research/out/Unearthing-the-Ancient-Yi_Chinese.pdf
  85% -> 95%
  status: manual table/readout pass; full OCR/translation still missing
```

## Concrete extraction from Ancient Yi tables

### 1. Three-line trigram carrier

The text presents a table for the eight trigrams as a **three-position symbol carrier**.

Observed table columns include:

```text
original trigram name
original trigram sequence/name
symbol-count form
binary positional conversion
three-bit value
single octal value
```

The table explicitly computes decimal value by positional expansion:

```text
b0*2^0 + b1*2^1 + b2*2^2
```

and also treats each trigram as an octal one-place value:

```text
n * 8^0 = n
```

### 2. Six-line hexagram carrier

The later table presents the sixty-four hexagrams as a **six-position symbol carrier**.

Observed table columns include:

```text
hexagram name
hexagram symbol/index
six-bit binary count
two-place octal count
binary-to-decimal expansion
base-ten count
```

The printed examples show a six-line binary positional expansion of the form:

```text
b0*2^0 + b1*2^1 + b2*2^2 + b3*2^3 + b4*2^4 + b5*2^5
```

The octal table separately gives two octal digits and expands them by:

```text
o0*8^0 + o1*8^1
```

### 3. Key operational finding

This is not merely “hexagrams look binary.”

The text is operating on the same retained carrier through multiple readout transformations:

```text
retained line-symbol carrier
  -> binary positional readout
  -> octal positional readout
  -> decimal scalar readout
```

That is directly relevant to the Orthad custody feature of `Xi_hat`:

```text
carrier/state is retained;
readout transformations are applied at the boundary;
scalar/number outputs are terminal projections, not the carried object.
```

## Correct bridge classification

### Q/support-channel

```text
STRONG_OPERATIONAL_BRIDGE
```

Reason:

```text
finite retained line positions
fixed line-order convention
trigram/hexagram carrier states
six-position support channel
```

### Projection / Orthad readout

```text
STRONG_OPERATIONAL_BRIDGE
```

Reason:

```text
same retained symbol field supports multiple non-equivalent readouts:
  line symbol
  binary vector
  octal pair
  decimal index
```

This is one of the clearest external examples so far of **readout transformation after retained-state custody**.

### B/refinement

```text
OPERATIONAL_REFINEMENT_BRIDGE_OPEN / NOT_EXHAUSTED
```

Do not reduce this to “no exact Phase floor formula found.”

The table shows a real refinement/enumeration mechanism:

```text
line state changes
least-significant position steps
carry propagates when a lower position saturates
six positions define the closed 64-state carrier
```

Missing piece:

```text
Need extracted successor/carry law across all 64 rows.
Need determine whether cycle completion at 63 forces a new domain/readout/lift in the author's framework, or merely ends enumeration.
```

### L/re-chart/lift

```text
STRONG_CANDIDATE
```

Reason:

```text
trigram domain: 3 positions / 8 states
hexagram domain: 6 positions / 64 states
binary-six readout re-charted as octal-two readout
same carrier can move between symbolic, binary, octal, decimal, and base-64-style interpretations
```

Phase-normalized reading:

```text
L should be tested here as:
  cycle completion or domain-size completion
  -> no legal continuation inside current finite carrier
  -> new carrier dimension or new readout domain opens
```

Not as literal Phase-specific latch vocabulary.

## Reunified operational statement

Ancient Yi gives a strong external case for the following normalization stack:

```text
finite retained carrier
-> ordered support positions
-> state-specific readout convention
-> positional expansion
-> scalar projection only after retained carrier is fixed
```

This is a high-value bridge for the project goal:

```text
Can Phase Calculus provide a primitive discrete grammar that normalizes external symbolic, computational, and physical systems before mapping them into continuous readout surfaces?
```

## Data / resource status

Liu 2022 remains open pending repository/author response.

When data arrives, the target table should be:

```text
time
MFR height
MFR velocity
decay index
squashing-factor Q / QSL surface
current density near HFT
reconnection event marker
footpoint connectivity P1/P3
AIA projection channel
```

## Missing pieces that would close current weakness

```text
1. Ancient Yi machine-readable 64-row table.
2. Confirmation of line-order convention from a translated section.
3. Successor/carry rule across all 64 hexagrams.
4. Whether the author defines a post-63 continuation, base-64 lift, or domain transition.
5. Latest Phase floor-anchor/selector source from HDD for direct normalization.
6. Liu 2022 simulation data or field-line connectivity tables for physics bridge closure.
```
