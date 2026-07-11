# p5-b1-v6 Audit Results

## Verdict

```text
REVISE

AFFINE CEILING MAP: ADOPT
HALF-OPEN PARTITION: ADOPT
ONE-STEP J AND P: ADOPT
FORBIDDEN 989: ADOPT
LENGTH-THREE COUNT 15: ADOPT
AFFINE COMPLEXITY p(n)=2^(n+1)-1: ADOPT
AFFINE ENTROPY log(2): ADOPT
ACTUAL AFFINE LANGUAGE MIXING: ADOPT
FINITE BOUNDARY CERTIFICATE A=0..10000: ADOPT

FINITE-STATE/SOFIC STATUS: WITHHOLD PENDING ONE MISSING BRIDGE
FINITE MARKOV ORDER NONE: WITHHOLD AS DEPENDENT CLAIM
FINITE MARKOV ORDERS 1..10: CERTIFIED COUNTEREXAMPLES
```

## Integrity and reproducibility

The submitted package passes every mechanical check performed.

```text
Submitted package SHA-256:
2b21db666b26273b0ba945b0f9a855bf074596ac6a67237f2e571ad7e29fb3af

Document SHA-256:
b3b75959831fd868b98672eb17eacabc0c4d59432107e371dffe9b9fad4c814b

Manifest entries:                  57
Manifest coverage:                 complete
Manifest byte counts:              PASS
Manifest SHA-256 values:           PASS
Executed notebook code cells:      15
Cells printing PASS:               15
PNG figures in executed notebook:  15
Clean semantic rebuild:            PASS
Byte-identical archive rebuild:    PASS
Lean compilation:                  not run; correctly unclaimed
```

The deterministic archive rebuild reproduces the submitted package hash only when the extracted root keeps the package's original directory name. That is consistent with the included builder because the root directory name is part of every archive member path.

## Adopted mathematical results

### 1. Complexity and entropy

The refinement proof now supplies the bridge missing in `p5-b1-v5`:

1. the length-`n` refinement boundary is
   \[
   \bigcup_{k=0}^{n}D^{-k}(p);
   \]
2. irrationality of `p` makes all levels disjoint;
3. every complementary arc carries one nonempty word;
4. every refinement cut separates adjacent arcs with different words.

Therefore

\[
p(n)=2^{n+1}-1
\]

and

\[
h_{\mathrm{affine}}=\log 2.
\]

The direct rational-affine cylinder engine reproduces the counts

```text
3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191
```

through depth 12.

### 2. Mixing

The mixing argument is valid. For any realizable word `u`,

\[
U=D^{|u|}(\operatorname{int}C(u))
\]

is a nonempty open arc or the full circle. Doubling is topologically exact, so some iterate maps `U` onto the circle, and every later iterate remains the circle. Hence every target cylinder can be reached with every sufficiently large bridge length.

This proves mixing for the actual interval language. It does not import mixing from the pairwise envelope `M`.

### 3. Finite certifications

The package independently validates:

- one trace row for every `A=0..10000`;
- 9999 adjacent transitions;
- exact agreement with the included transition-count table;
- outward-rounded affine-cylinder comparisons through depth 12;
- rational-affine finite-memory counterexamples for orders `1..10`;
- outward-rounded nonintersection with all carry boundaries through `A=10000`.

The minimum certified finite boundary gap is approximately

\[
9.72886578265059\times 10^{-5}
\]

at `A=1416`.

## Load-bearing proof gap

The non-soficity section proves a separation result for **open arcs**:

\[
\mathcal F(U)=\{v:\operatorname{int}C(v)\cap U\ne\varnothing\}.
\]

It then states:

> The follower set of the word carried by `C_n^±` is exactly `F(U_n^±)`.

That statement is the missing bridge.

The standard follower set of a finite word is formed from the actual half-open cylinder `C(w)`, not only its interior. Its follower region is

\[
H_w=D^{|w|}(C(w)),
\]

which can include endpoints. The document does not prove that endpoint-only continuations cannot occur, nor does it reformulate the separation argument directly for the half-open regions `H_w`.

Without this lemma, repetition of standard follower sets in a finite labeled graph does not yet imply repetition of the open arcs `U_n^±`. Therefore the step

\[
\text{finite sofic follower sets}
\Longrightarrow
U_n^\pm=U_m^\pm
\]

is not established on the page.

This is a missing bridge, not a discovered counterexample. The theorem appears repairable in either of two ways:

1. prove that every continuation realized at an included endpoint is also realized from the same-side interior, so the standard follower set equals `F(int H_w)`; or
2. avoid open-arc follower languages and prove directly that equality of standard follower sets forces equality of the interiors of the selected half-open follower regions.

The proof should also expand the compressed injectivity claim for the two cylinders adjacent to `p`: their lengths are strictly below `2^{-n}` because `p` lies strictly between two points of `D^{-n}(p)`, so `D^n` is injective on each.

## Consequence for Markov order

The explicit order `1..10` counterexamples survive.

The global statement

```text
FINITE MARKOV ORDER: NONE
```

is derived from non-soficity. It remains withheld until the follower-set bridge is closed.

## Lean boundary

The package correctly states:

```text
LEAN SOURCE PRESENT; COMPILATION NOT VERIFIED
```

The Lean files formalize the elementary geometric sum, the `J` identities, and a complete `989` interval theorem. They do not formalize the non-soficity or mixing arguments, and the document does not claim otherwise.

## Branch status

```text
p5-b1: NOT YET CLOSED
```

The affine-language branch has one remaining theorem-grade bridge. If `p5-b1-v7` closes it without changing the accepted results, Branch 1 can be marked closed and the following interaction may advance to Branch 2.

## Holds retained

```text
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GLOBAL T_A=ceil(y_A) BRIDGE: NOT YET PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```
