# 40. Ancient Yi Carry/Lift and ICPR Automata Completion Pass

## Scope

Continued the external-corpus research under the active project framing:

- Phase Calculus/QBL is a primitive discrete mathematical framework under development.
- External Taoist/Chinese mathematical, logical, numerical, and physics sources are comparison corpora.
- The comparison target is operational/functionality overlap after normalization, not identity of names or religious/philosophical labels.

This pass focused on:

1. `Tao-Research/out/Unearthing-the-Ancient-Yi_Chinese.pdf`, rendered pages 49–64.
2. `Prospect-Leads/icpr2011_Logic-and-Philosophy-Today.pdf`, final targeted bridge synthesis.

---

## A. Ancient Yi: the successor/carry/lift law is now visible in the rendered tables

Earlier Ancient Yi notes had already established:

- 3-line trigram carrier -> binary 3-place / octal 1-place readout.
- 6-line hexagram carrier -> binary 6-place / octal 2-place readout.
- Same retained symbol field -> multiple readout conventions.

This pass adds the missing carry/lift bridge from the later tables.

### A1. Two-octal-place hexagram table: 0–63

Rendered page 53 explicitly presents:

```text
64 hexagram symbolic numerals, octal two-place symbolic numerals, counting table
natural numbers 0–63
```

The examples show the readout law:

```text
(00) -> 0*8^0 + 0*8^1 = 0
(10) -> 1*8^0 + 0*8^1 = 1
(67) -> 6*8^0 + 7*8^1 = 6 + 56 = 62
(77) -> 7*8^0 + 7*8^1 = 7 + 56 = 63
```

### A2. Three-octal-place extension: 64–511

Rendered page 55 explicitly presents:

```text
Yijing octal three-place symbolic numeral counting table
natural numbers 64–511 = 8^3 - 1
```

The examples show:

```text
(001) -> 0*8^0 + 0*8^1 + 1*8^2 = 64
(101) -> 1*8^0 + 0*8^1 + 1*8^2 = 65
(677) -> 6*8^0 + 7*8^1 + 7*8^2 = 510
(777) -> 7*8^0 + 7*8^1 + 7*8^2 = 511
```

### A3. Four-octal-place extension: 512–4095

Rendered page 63 explicitly presents:

```text
Yijing octal four-place symbolic numeral counting table
natural numbers 512–4095 = 8^4 - 1
```

The examples show:

```text
(0001) -> 0*8^0 + 0*8^1 + 0*8^2 + 1*8^3 = 512
(1001) -> 1*8^0 + 0*8^1 + 0*8^2 + 1*8^3 = 513
(6777) -> 6*8^0 + 7*8^1 + 7*8^2 + 7*8^3 = 4094
(7777) -> 7*8^0 + 7*8^1 + 7*8^2 + 7*8^3 = 4095
```

### A4. The important operational discovery

This is no longer only a retained-carrier/readout bridge.

It also supplies an explicit cycle-completion/lift pattern:

```text
2-place domain: 00 ... 77 = 0 ... 63 = 8^2 - 1
cycle completes at 77
next admissible continuation is not another 2-place state
next domain opens as 001 = 64

3-place domain: 001 ... 777 = 64 ... 511 = 8^3 - 1
cycle completes at 777
next admissible continuation is not another 3-place state
next domain opens as 0001 = 512

4-place domain: 0001 ... 7777 = 512 ... 4095 = 8^4 - 1
```

This is directly relevant to the user's correction:

```text
L happens when a cycle completion event occurs and no next step can be taken without repeating, so a new domain is created or lifted to.
```

### A5. Operational classification update

```text
Q/support-channel:
  STRONG_OPERATIONAL_BRIDGE
  finite 3-line / 6-line / multi-hexagram retained carrier;
  each octal digit is an 8-state finite position system.

B/refinement / successor:
  STRONG_OPERATIONAL_CANDIDATE
  in-domain successor/carry refinement is explicit;
  digit-place capacity governs legal continuation;
  exact Phase floor-anchor law is not expected here and should not be used to discard the bridge.

L/re-chart/lift:
  STRONG_OPERATIONAL_BRIDGE
  after all states in a fixed-place domain are exhausted,
  continuation opens a higher-place domain.

Orthad custody / readout:
  STRONG_OPERATIONAL_BRIDGE
  retained line-symbol carrier is read through binary, octal, decimal, and computer-counting conventions;
  scalar number is a terminal readout, not the retained object itself.
```

### A6. Normalized Phase comparison

The normalized comparison is:

```text
Ancient Yi:
  retained line-symbol carrier
  -> finite place-value domain
  -> successor/carry within domain
  -> terminal state 77/777/7777
  -> no next same-domain state without repetition
  -> lifted place domain 001/0001/...
  -> scalar decimal readout afterward

Phase Calculus/QBL:
  retained Ξ̂ state
  -> Q/B admitted continuation in current domain
  -> finite/capacity-governed cycle completion
  -> no next same-domain move without repetition/excess
  -> L opens lifted domain
  -> Orthad/readout projection afterward
```

This is an operational bridge, not a claim that Ancient Yi is literally Phase Calculus.

---

## B. ICPR logic volume: targeted pass can now be marked complete for bridge purposes

The full volume is large, but the relevant targeted sections have now been covered enough for the current comparative purpose:

1. Chinese logic / Mingbianxue.
2. Moism and School of Names.
3. `ming`, `shi`, `bian`, `gu`, `lei`, `fa` comparison layer.
4. Temporal/dynamic logic.
5. Category theory.
6. Memory and automata.
7. Belief change / history-sensitive revision.

### B1. Chinese logic bridge

The Chinese logic section gives these operational components:

```text
ming  = name/classification layer
shi   = object/referent layer
bian  = argumentation / disputation / distinguishing
xue   = study/systematic inquiry
fa    = standard/model/rule of admissibility
lei   = kind/class/sameness-difference carrier
gu    = reason/cause/ground
```

Important comparison content:

- Moists emphasize defining notions according to the actual situation, not fixed names.
- School of Names explicitly separates names from objects and treats name changes as required when object states change.
- Liang Qichao maps Chinese `ci / gu / lei` to proposition / reason / kind in comparative logic.
- Hu Shi uses `gu / lei / fa` to understand inference in ancient Chinese logic.

Operational implication:

```text
Do not map by labels.
Map by how a retained object-state is classified,
which standard/rule admits the next operation,
and how reasons/kinds support inference.
```

### B2. Automata bridge

The automata section gives a direct computational normalization template:

```text
finite alphabet
finite states
transition relation
input word
run
accepting state / accepting condition
```

For tree automata:

```text
node labels with arity
child states
transition relation computes parent state
root accepting state
```

For infinite words:

```text
finite state set
infinite run
states visited infinitely often
accepting condition over recurrence
```

Operational Phase mapping:

```text
finite state/configuration
-> enabled transition
-> accrued run word
-> accepting/saturation boundary
```

### B3. Category-theory bridge

The category section gives the normalization grammar:

```text
object       -> retained carrier/state
morphism     -> transition / operation / projection
composition  -> accrued word / operation history
identity     -> no-op / preserved state
functor      -> cross-domain normalization preserving structure
forgetful map-> projection/readout losing structure
```

This is now a central meta-tool for the whole comparison program.

### B4. Belief-change/history bridge

The belief-change section explicitly flags a problem where a method disregards revision history. This is useful because Phase Calculus treats accrued history/word as part of the retained state, not as disposable metadata.

Operational implication:

```text
If external systems require history-sensitive revision,
then Phase-style retained word / monodromy / custody may be applicable.
```

---

## C. Reunified project conclusion after this pass

The external corpus increasingly supports the following research hypothesis:

```text
Phase Calculus may serve as a primitive discrete normalization grammar for systems where:

1. a retained carrier/state precedes scalar readout;
2. admissible operations depend on current retained state;
3. continuation has finite/capacity/cycle constraints;
4. completion or blockage forces carry/re-chart/lift;
5. multiple projections can be read from the same retained object;
6. continuous physics/numerical methods appear as downstream smooth projections of retained-state custody.
```

Ancient Yi now becomes one of the strongest non-physics external corpora because it supplies:

```text
finite symbol carrier
multiple readout bases
explicit place-value expansion
explicit cycle completion at 8^k - 1
explicit lifted place domain after cycle completion
```

That is exactly the kind of operational bridge this project is seeking.

---

## D. Remaining missing pieces

### D1. Ancient Yi

Still needed for full closure:

```text
1. Exact line-order convention for each digit.
2. Full 64-row machine-readable extraction.
3. Whether the tables give only counting succession or also rule-governed transformation/situation change.
4. Relationship between Ancient Yi counting order and Shao Yong / Fu Xi / King Wen ordering.
```

### D2. Phase Calculus

Still needed:

```text
1. Latest selector/floor source from HDD.
2. Exact current Q/B/L floor-anchor law.
3. Current version of macro calculus if selector-complete macro is stale.
```

### D3. Physics bridge

Still needed:

```text
1. Liu 2022 simulation data or author response.
2. QSL/Q-factor time series.
3. HFT current-density sequence.
4. P1->P3 connectivity graph.
5. AIA projection table from retained topology channels.
```
