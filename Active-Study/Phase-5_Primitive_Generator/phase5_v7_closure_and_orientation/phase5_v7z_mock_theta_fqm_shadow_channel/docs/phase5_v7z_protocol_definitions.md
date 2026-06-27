# Protocol Definitions

## FQM carrier

`A = Z/12Z`.

## Quadratic form

`q(r) = r^2/24 mod 1`.

## Bilinear form

`b(r,s) = rs/12 mod 1`.

## Character vector

`v_chi[r] = chi12(r)` where the table is:

```text
0:0 1:+1 2:0 3:0 4:0 5:-1 6:0 7:-1 8:0 9:0 10:0 11:+1
```

## Terminal channel rule

For cursor `n`:

```text
residue = n mod 12
support = 1 iff gcd(n,6)=1
sign = chi12(residue)
fractional exponent = (n^2 mod 24)/24
coefficient magnitude = n
terminal exponent = n^2/24
```

## Retention rule

The retained state may carry the cursor and finite channel state. It may not carry the scalar q-series or Shadow Residual object.
