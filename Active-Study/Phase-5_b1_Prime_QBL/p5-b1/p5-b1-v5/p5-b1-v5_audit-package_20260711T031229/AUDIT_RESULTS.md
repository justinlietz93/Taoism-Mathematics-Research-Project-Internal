# Audit Results

## Verdict

```text
REVISE

ADOPT_AFFINE_CEILING_AND_J_CORE
ADOPT_FORBIDDEN_989
ADOPT_LENGTH3_COUNT_15
ADOPT_COMPLEXITY_AND_ENTROPY_RESULT_AFTER_PROOF_EXPANSION
ADOPT_FINITE_BOUNDARY_CERTIFICATE

WITHHOLD_EXACT_MARKOV_WITNESS_STATUS
WITHHOLD_COMPLETE_LEAN_CERTIFICATE_STATUS
```

## Verified package facts

- The uploaded archive SHA-256 matches the agent report.
- The internal corrected document SHA-256 matches the agent report.
- `MANIFEST.json` covers all 50 non-manifest files.
- Every recorded byte count and SHA-256 matches.
- A clean extraction and rebuild completes successfully.
- The rebuilt manifest verifies.
- The source and executed notebooks are separate.
- The executed notebook has 13 code cells with execution counts `1..13`.
- Every code cell prints `PASS`, prints no `FAIL`, and emits exactly one PNG figure.
- Lean is correctly reported as unavailable and compilation is not claimed.

## Mathematical findings

### Adopted

1. The affine ceiling bridge and half-open partition remain correct.
2. The one-step matrices `J` and `P` remain correct.
3. The interval proof that `989` is forbidden is correct.
4. At the current parameter, `787` is also forbidden and the length-three language has 15 words.
5. The conjugacy

   ```text
   z = E + 1 mod 1
   y = z + 2a mod 1
   y_next = 2y mod 1
   ```

   is correct.
6. The cut point `p=2a` is irrational by the stated power-identity contradiction.
7. The resulting complexity formula

   ```text
   p(n) = 2^(n+1) - 1, n >= 1
   ```

   and affine coding entropy `log(2)` are correct once the missing refinement lemma is written explicitly.
8. `M` and `K` are correctly restricted to the pairwise edge-shift envelope.
9. The finite empirical metrics reproduce.
10. The outward interval run reproduces its finite boundary certificate.

## Defects requiring revision

### 1. Boundary count is not yet a complete word-count proof on the page

Section 8 counts the distinct points

```text
{p} union D^(-1)(p) union ... union D^(-n)(p).
```

It then jumps directly to the word-complexity formula. The missing bridge is load-bearing.

The document must prove all four statements:

1. The transformed carry partition has boundary set `{p} union D^(-1)(p)`.
2. The length-`n` refinement boundary is exactly `{p} union ... union D^(-n)(p)`.
3. Every connected component of the complement is a nonempty length-`n` cylinder.
4. Adjacent components have different length-`n` words, so no counted cut is inactive.

The theorem appears correct, and direct enumeration agrees through length 12, but the current prose compresses the decisive bijection.

### 2. The Markov-order witnesses are not exact certificates

The package labels its finite cylinder witnesses “exact.” The implementation uses `Decimal` and a 95-digit decimal truncation of `gamma`:

```python
gamma_dec = Decimal(mp.nstr(c["gamma"], 95))
```

This is high-precision numerical classification, not exact affine arithmetic and not outward-rounded interval certification.

The witnesses for orders 1 through 10 reproduce and have large numerical margins, but their correct status is:

```text
HIGH-PRECISION FINITE WITNESSES
```

until they are rebuilt from symbolic endpoints `q*a+r` with rational coefficients or from outward-rounded parameter intervals.

### 3. The open hold is named too broadly

The package says:

```text
ACTUAL CARRY LANGUAGE PRESENTATION: NOT YET DERIVED
```

But the affine interval coding and its doubling-map conjugacy are already a presentation of the language. The unresolved object is narrower:

```text
FINITE-STATE/SOFIC PRESENTATION: NOT YET DERIVED
```

The current wording contradicts the package’s own construction.

### 4. The Lean `989` file formalizes only the last inequality

The Lean theorem assumes

```text
x <= -1 + 2*a
```

and proves the next image misses `I9`. It does not define the three carry intervals, define the branch maps, derive the `98` cylinder, or prove that a point with prefix `98` satisfies the hypothesis.

This is a useful local theorem surface, not a formal proof of the complete forbidden word.

Correct status:

```text
LEAN LOCAL INEQUALITY SURFACE PRESENT
FULL FORBIDDEN-WORD FORMALIZATION NOT VERIFIED
```

### 5. Rebuilds are semantically reproducible but not byte-identical

A clean rebuild succeeds and all substantive generated files reproduce. The source and executed notebook hashes change because `nbformat` assigns new random cell IDs. The rebuilt archive therefore has a different SHA-256.

This is not a mathematical defect. Fixing deterministic cell IDs would make the package fully byte-reproducible.

## Correct disposition

```text
AFFINE CEILING MAP: PROVED
HALF-OPEN PARTITION: PROVED
ONE-STEP J AND P: PROVED
FORBIDDEN 989: PROVED IN MARKDOWN; PARTIAL LEAN SURFACE
LENGTH-THREE LANGUAGE COUNT 15: PROVED
AFFINE COMPLEXITY 2^(n+1)-1: RESULT ADOPTED; PROOF BRIDGE MUST BE EXPANDED
AFFINE ENTROPY log(2): ADOPTED
MARKOV ORDERS 1..10: HIGH-PRECISION FINITE COUNTEREXAMPLES
FINITE BOUNDARY NONHIT: OUTWARD-INTERVAL CERTIFIED
FINITE-STATE/SOFIC PRESENTATION: OPEN
ACTUAL LANGUAGE MIXING: OPEN
SPECIFIC-ORBIT EQUIDISTRIBUTION: OPEN
GLOBAL THRESHOLD BRIDGE: OPEN
GAUGE/FQM MAP: OPEN
```
