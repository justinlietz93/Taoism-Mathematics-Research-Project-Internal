# Phase 5 v7s: 2-Primary Normalization and Jordan Symbol Policy

## Objective

Remove the largest classification ambiguity left by v7r: the 2-primary sector. In finite quadratic-module comparison, the raw tensor `C=(c_ij)` is only a coordinate presentation. The 2-primary component needs its own normalization policy because even-order modules can collide under coarse order/rank/Brown checks while remaining different as Jordan-symbol data.

## Protocol

```text
input finite module presentation
  -> reject nontrivial radical
  -> split p-primary components
  -> for p=2 apply Jordan-symbol policy
  -> normalize odd cyclic A(2^k,t) by oddity t mod 8
  -> retain even U/V rank-2 block identity
  -> record Brown invariant mod 8
  -> sort direct-sum blocks by exponent/type/oddity
  -> compare normalized symbol keys, not raw matrices
```

## 2-primary blocks used in this pass

```text
Odd cyclic block:
  A(2^k,t), t odd
  q(x) = t x^2 / 2^(k+1) mod 1
  symbol: 2^k_{t mod 8}^sign

Even rank-2 blocks:
  U(2^k): q(x,y) = xy / 2^k
  V(2^k): q(x,y) = (x^2 + xy + y^2) / 2^k
```

## Results

```text
block rows: 138
cyclic odd block rows: 126
even rank-2 block rows: 12
generator-orbit checks: 126
generator-orbit passed: 126
direct-sum symbols: 1076
negative controls: 21 / 21
unique normal keys: 34
```

## Standing correction

```text
raw C matrix:
  coordinate presentation

v7r FQM class:
  gauge/isometry object

v7s Jordan policy:
  required 2-primary normalization layer before class comparison
```
