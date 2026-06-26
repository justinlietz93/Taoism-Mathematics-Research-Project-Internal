# Protocol Definitions

## Support

`support(n) := gcd(n,6)=1`.

## Post-L seat

```text
pre_L_seat(n) = n mod 6
parity_latch(n) = floor((n mod 12)/6)
post_L_seat(n) = pre_L_seat(n) + 6*parity_latch(n)
```

## Character readout

```text
chi12(n) = +1 for n mod 12 in {1,11}
chi12(n) = -1 for n mod 12 in {5,7}
chi12(n) = 0 otherwise
```

## Lap orientation

```text
FollowSign(lap,n) = chi12(n)       if lap is odd
FollowSign(lap,n) = -chi12(n)      if lap is even
```

## Depth width

```text
N_max(depth) = 2^(depth+2)-1
```

This width is a test aperture, not a scalar cargo field.
