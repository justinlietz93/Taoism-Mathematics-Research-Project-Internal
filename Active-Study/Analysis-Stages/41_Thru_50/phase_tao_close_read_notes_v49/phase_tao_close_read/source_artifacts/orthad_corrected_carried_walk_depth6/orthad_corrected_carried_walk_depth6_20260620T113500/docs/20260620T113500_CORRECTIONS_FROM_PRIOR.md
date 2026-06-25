# Corrections From Invalid Depth-6 Package

The previous package is invalid as evidence.

## Removed bugs

1. `uv > 4096` cutoff stopped B after the first corridor. Removed.
2. Capacity ladder `6,12,24,48,...` was fabricated. Removed.
3. Claim that lap negation breaks at depth 3 was caused by fabricated ladder. Removed.
4. Flat germ-width anchor was caused by B cutoff. Removed.

## Corrected rule

```text
Each domain: (BQ)^6 L
Depth 6: ((BQ)^6 L)^6
```

B interleaves in every domain. L carries q and θ and increases rank by one.
