# Phase 4 v4 — Ancient Yi Symbol Mapping

## Claim

Ancient Yi symbol rows are a terminal symbol layer over a retained LSD-first carrier. The transition-complete object is not the Unicode glyph, King Wen number, traditional name, or conventional octal string. The transition-complete object is:

```text
X = (six-line carrier, top-to-bottom line convention, LSD-first bit weights, active octal place domain)
```

## Closed mapping

```text
top displayed line        -> bit 0 -> weight 2^0
second displayed line     -> bit 1 -> weight 2^1
third displayed line      -> bit 2 -> weight 2^2
fourth displayed line     -> bit 3 -> weight 2^3
fifth displayed line      -> bit 4 -> weight 2^4
bottom displayed line     -> bit 5 -> weight 2^5
```

The top three displayed lines form the low octal digit. The lower three displayed lines form the high octal digit. The Yi octal display writes the low digit first.

## Table reconstruction result

All 64 rows pass:

```text
binary source order = decimal written as six LSD-first bits
octal source order  = decimal written as two LSD-first octal digits
successor           = decimal + 1 within domain
63 / 77 completion  = 64 / 001 higher-place lift
Unicode codepoint index = King Wen number
```

## Source-to-carrier interpretation

The symbol layer is now positioned correctly:

```text
Unicode hexagram       -> King Wen cross-reference symbol
traditional name       -> semantic name readout
pinyin                 -> pronunciation readout
English gloss          -> translation readout
source binary display  -> retained carrier display
source Yi octal        -> retained place-domain readout
successor             -> retained carrier transition
```

## Projection-loss result

A terminal symbol projection is not transition custody. Carrier state and active domain width are required.

Examples:

```text
7 and 77 share low digit 7, but 7 -> 01 and 77 -> 001.
0 and 00 share scalar value 0, but 0 -> 1 and 00 -> 10.
King Wen symbols classify hexagrams but do not supply Yi carry order.
```

## Theorem position

The Ancient Yi row is now fully integrated into Phase 4:

```text
Phase 3 v4: carry/lift closure
Phase 4 v4: symbol-to-carrier mapping closure
```

## Falsification gates

The package includes direct tests for line order, Unicode/King-Wen cross-reference, octal display, carry/lift, terminal-symbol custody, and trigram grouping.
