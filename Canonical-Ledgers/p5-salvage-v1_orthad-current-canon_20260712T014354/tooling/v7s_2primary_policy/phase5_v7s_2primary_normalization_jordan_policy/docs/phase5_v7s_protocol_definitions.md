# v7s Protocol Definitions

## Canonical comparison target

The canonical comparison target is a normalized p-primary Jordan-symbol key, not raw `C`.

## Odd cyclic 2-primary block

`A(2^k,t)` is admitted only when `t` is odd. Its policy key is:

```text
('2-primary', 'odd-cyclic', k, t mod 8, Brown(q))
```

Generator changes by odd unit `u` act by:

```text
t -> t*u^2 mod 2^(k+1)
```

The pass checks that this operation preserves the normalized key.

## Even rank-2 blocks

`U(2^k)` and `V(2^k)` are retained as separate block types. They may share order/rank/exponent, but the policy forbids collapsing them unless a stronger isometry proof is supplied.

## Direct-sum symbol

The direct-sum policy sorts block symbols and adds Brown invariants mod 8.

## Orthad handoff

The v7q transition assignment may feed this classifier only after native support, trace rewrite, cocycle, and gauge gates pass.
