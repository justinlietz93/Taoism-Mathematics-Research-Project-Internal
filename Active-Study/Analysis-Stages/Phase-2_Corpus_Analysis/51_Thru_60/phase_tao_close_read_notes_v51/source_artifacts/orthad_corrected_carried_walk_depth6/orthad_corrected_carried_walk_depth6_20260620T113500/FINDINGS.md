# Findings

## Validated corrections

```text
no uv cutoff: PASS
B after every L: PASS
theta carry: PASS
q carry: PASS
rank +1 per L: PASS
no capacity ladder: PASS
sign lap period: 2
```

## Carried word

```text
primitive: BQBQBQBQBQBQLBQBQBQBQBQBQLBQBQBQBQBQBQLBQBQBQBQBQBQLBQBQBQBQBQBQLBQBQBQBQBQBQL
macro:     RRRRRRTRRRRRRTRRRRRRTRRRRRRTRRRRRRTRRRRRRT
```

## Lap signed position lists

```text
lap 0 / depth after L 1: + - - + + -
```
```text
lap 1 / depth after L 2: - + + - - +
```
```text
lap 2 / depth after L 3: + - - + + -
```
```text
lap 3 / depth after L 4: - + + - - +
```
```text
lap 4 / depth after L 5: + - - + + -
```
```text
lap 5 / depth after L 6: - + + - - +
```

## Period map

```json
{
  "sign_lap_period": 2,
  "phase_factor_lap_period": 2,
  "anchor_lap_period_observed": null,
  "lap_negation_checks": [
    {
      "lap": 0,
      "next_lap": 1,
      "next_is_negation": true
    },
    {
      "lap": 1,
      "next_lap": 2,
      "next_is_negation": true
    },
    {
      "lap": 2,
      "next_lap": 3,
      "next_is_negation": true
    },
    {
      "lap": 3,
      "next_lap": 4,
      "next_is_negation": true
    },
    {
      "lap": 4,
      "next_lap": 5,
      "next_is_negation": true
    }
  ],
  "note": "sign and absolute phase factor lists have period 2 by lap; anchors do not repeat through depth 6 because B continues refining."
}
```

## External comparison status

The external q-series used only at the final check is:

```text
R(q) = Σ_(gcd(n,6)=1) (12|n) · n · q^(n²/24)
```

Here `n` is the external q-series term index. It is not a Phase Calculus step, not a Q tick, and not depth.

The internal carried sign field resolves the n=7 collision but does not match full χ12 orientation for every supported residue under the raw sign extractor. See `output_data/20260620T113500_external_shadow_residual_comparison.csv`.
