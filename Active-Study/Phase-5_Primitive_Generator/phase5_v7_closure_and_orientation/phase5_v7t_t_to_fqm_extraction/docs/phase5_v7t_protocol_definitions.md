# Protocol Definitions

## Native transition record

A row emitted by the v7q transition assignment with:

```text
event, kind, src, dst, pair, scale_num, scale_den, phase_mod4, c_projection, contact_dz
```

## Axis carrier

For each retained axis `a`, the carrier is:

```text
D_a = even doubled carrier derived from denominators and phase support touching a.
```

In this bounded pass the implemented policy is:

```text
D_a = max(8, 4*lcm(scale_den touching a)) when odd phase support occurs,
D_a = 4*lcm(scale_den touching a) otherwise,
then force evenness.
```

## Pair contribution

For pair `a:b`, each transition contributes a native increment reduced modulo:

```text
L_ab = lcm(D_a,D_b)
```

The aggregate pair entry becomes:

```text
C_ab = sum(delta_ab) mod L_ab.
```

## FQM presentation

The extracted presentation is:

```text
D = Π_i Z/D_i Z
B(e_i,e_j) = C_ij / lcm(D_i,D_j) mod 1
q(x) = 1/2 B(x,x), routed through 2-primary policy.
```

## Canonical comparison

The raw matrix is not compared directly. The classifier emits a canonical gauge key from the module presentation and the 2-primary Jordan-symbol policy.
