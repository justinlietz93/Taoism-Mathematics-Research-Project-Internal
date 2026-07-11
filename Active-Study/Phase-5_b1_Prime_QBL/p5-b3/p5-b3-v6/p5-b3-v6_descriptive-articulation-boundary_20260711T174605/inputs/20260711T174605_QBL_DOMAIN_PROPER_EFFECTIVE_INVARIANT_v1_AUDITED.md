# QBL Domain-Proper Effective Invariant

**Step:** `p5-b3-v5`  
**Primary structural authority:** `CF000_Primitive_Distinguishability`  
**Primary custody/Orthad authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Accepted inputs:** closed Branch 1 affine-language theorems, closed Branch 2 global threshold theorem, and the canonical QBL-to-affine boundary-orbit semiconjugacy  
**Scope:** the descriptive effective invariant induced on the canonical pre-`L` boundary-return layer  
**Excluded lane:** derivation of the Orthad primary pairing, chart restrictions, transfers, gauge class, FQM, or Weil projection

---

## 1. Disposition

### PROVED

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
EXACT BOUNDARY-RETURN COCYCLE: PROVED
CANONICAL CARRY ITINERARY: APERIODIC
CANONICAL SYMBOLIC ORBIT CLOSURE: INFINITE AND TOPOLOGICALLY TRANSITIVE
D1 EFFECTIVE INVARIANT GENUINELY NEW: PROVED
HIGHER-ORDER DESCRIPTIVE L: PROVED
```

The intrinsic D1 object is not merely the scalar error coordinate. It is the **boundary-renormalization cocycle package**

\[
\mathfrak I_{D1}
=
(\Sigma^-,\mathcal R,\pi,c,\mathbf c,X_{\mathrm{can}},\mathcal L_{\mathrm{can}}),
\]

consisting of the saturated pre-`L` boundary section, its induced return map, the state-internal affine coordinate, the exact three-valued return cocycle, the resulting canonical carry itinerary, and the itinerary's own shift-orbit closure and language.

The full Branch 1 language remains an ambient system. Its stronger properties transfer to D1 only if the canonical orbit is dense, or if language equality is otherwise proved.

### CERTIFIED FINITELY

The accepted `A=0..10000` carry trace was revalidated and reanalyzed. It contains every full-affine word through length seven. This is strong finite coverage, not a density theorem.

### OBSERVED

The finite itinerary has state and edge frequencies close to the accepted Lebesgue benchmarks. This remains evidence only.

### OPEN

```text
CANONICAL ORBIT CLOSURE: NOT YET DETERMINED
CANONICAL ORBIT CLOSURE = FULL AFFINE SYSTEM: NOT YET PROVED
CANONICAL ORBIT CLOSURE IS PROPER: NOT YET PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
CANONICAL ORBIT-CLOSURE NON-SOFICITY: NOT YET PROVED
CANONICAL ORBIT-CLOSURE MIXING: NOT YET PROVED
CANONICAL ORBIT-CLOSURE FINITE MARKOV ORDER: NOT YET DETERMINED
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
```

The exact missing density statement is that

\[
\alpha=12\frac{\log2}{\log\varphi}
\]

is **base-2 disjunctive**, equivalently that its doubling orbit is dense. This is strictly weaker than equidistribution, but it is not supplied by irrationality.

---

## 2. Source map

| Classification | Source | Load-bearing role |
|---|---|---|
| **Primary** | `CF000_Primitive_Distinguishability.pdf` | Genuinely higher determination, same-domain saturation, inherited invariant stacking, and domain-proper effective invariants. |
| **Primary** | `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` | Primitive custody state, strict `B>Q>L`, saturation at the final phase position, retained word/pair/phase, and the Orthad dependency boundary. |
| **Accepted** | `QBL_CARRY_AFFINE_FOLLOWER_STRUCTURE_v5.md` | Full affine interval language, exact complexity, entropy, non-soficity, mixing, and no finite Markov order. |
| **Accepted** | `QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md` | Global identity `T_A=ceil(y_A)` and nonintegrality of all canonical affine thresholds. |
| **Accepted** | `QBL_HIERARCHICAL_GRAMMAR_FACTOR_SCOPE_v2.md` | Canonical boundary-orbit semiconjugacy and countability boundary for a full interval factor. |
| **Contextual** | supplied Orthad diagram | Dependency-order visualization only. The written law controls notation and status. |
| **Finite accepted input** | accepted carry trace `A=0..10000` | Finite language coverage and regression statistics. It is not used to prove density. |

CF000's criterion is explicitly non-geometric: a genuinely higher determination adds an internal determination rather than renaming the lower one, and a new admitted domain inherits the prior stack while adding a domain-proper effective invariant. No metric, matrix, or pairing rank is required for that descriptive conclusion.

---

## 3. Descriptive domains

### 3.1 D0: primitive QBL custody

Let

\[
D_0=(\mathcal X_0,\operatorname{Step}),
\]

where a custody state is

\[
X_t=(A_t,q_t,\theta_t,k_t,j_t,W_t),
\qquad q_t=(u_t,v_t),
\]

and `Step` selects exactly one primitive letter by the strict priority

\[
B>Q>L.
\]

Its lawful transformations are:

- `B`: balanced refinement of the carried pair;
- `Q`: quarter-turn and local phase-position advance;
- `L`: domain increment after both `B` and `Q` are blocked.

The exact ordered prefix `W_t` is retained. Operation counts are not substitutes for the prefix.

### 3.2 D1: induced pre-`L` boundary-return layer

For each domain `A`, let `S_A^-` be the complete retained state immediately before the `L` that closes that domain. Define the canonical boundary section

\[
\Sigma^-:=\{S_A^-:A\ge0\}.
\]

The induced return map is

\[
\mathcal R(S_A^-)=S_{A+1}^-.
\]

It is not a primitive letter. It is the variable-length composition consisting of:

1. the closing `L` at `S_A^-`;
2. the complete self-selected `B/Q` evolution of Domain `A+1`;
3. arrival at the next saturated pre-`L` boundary.

For `A>=1`, the return edge

\[
e_A=(S_{A-1}^-,S_A^-)
\]

carries the exact derived label

\[
c_A=\nu(q_A)-2\nu(q_{A-1})\in\{7,8,9\}.
\]

Thus D1 is an induced dynamical layer whose primitive objects are saturated boundary states and whose lawful transformation is the first-return map `R` with its cocycle.

### 3.3 Definition table

| Layer | State objects | Lawful transformation | Native invariant-bearing data | Not native to the layer |
|---|---|---|---|---|
| `D0` primitive custody | `X_t=(A,q,theta,k,j,W)` | one self-selected letter `B`, `Q`, or `L` | exact pair, phase, local/global positions, ordered word, domain saturation predicate | affine carry as an instantaneous coordinate |
| `D1` boundary return | saturated states `S_A^-`, return edges `e_A` | induced first-return map `R` | inherited boundary state, state-internal `E_A`, return cocycle `c_A`, canonical itinerary and orbit closure | Orthad pairing/chart/transfer values |

---

## 4. Inherited structure in D1

At `S_A^-`, the current custody law supplies

\[
A,
\quad
q_A,
\quad
\theta_A,
\quad
k_A=N_A-1,
\quad
j_A=6(2^{A+1}-1),
\quad
W_A^-.
\]

The accepted threshold theorem gives

\[
q_A=(F_{T_A+1},F_{T_A+2}),
\qquad
\nu(q_A)=T_A.
\]

The count `nu(q_A)` is recoverable in either of two exact ways:

1. count the `B` letters in the retained prefix `W_A^-`;
2. recover the unique Fibonacci-corridor index of the retained pair `q_A`.

The previous boundary is also recoverable from the retained history by locating the preceding closing `L` prefix. Consequently

\[
c_A=\nu(q_A)-2\nu(q_{A-1})
\]

is recoverable once `S_A^-` exists. It is a derived edge label, not a primitive coordinate appended by the preceding instantaneous `L`.

### 4.1 Inherited-invariant map

\[
\begin{aligned}
I_{0\to1}:S_A^-\longmapsto
(&A,q_A,\theta_A,j_A,W_A^-;\\
&\nu(q_A),E_A,e_A,c_A).
\end{aligned}
\]

The semicolon separates directly retained data from derived D1 objects. The map does not discard the lower layer. D1 is defined over its retained saturated states.

### 4.2 State-internal affine coordinate

Let

\[
\lambda=\frac{\log2}{\log\varphi},
\qquad
\beta=\frac{\log5}{2\log\varphi}-\frac32.
\]

Then

\[
\pi(S_A^-)=\lambda j_A+\beta-\nu(q_A)=E_A.
\]

The exact cocycle law is

\[
E_A=2E_{A-1}+\gamma-c_A,
\qquad
\gamma=6\lambda-\beta.
\]

For `n` returns, iteration gives the exact weighted cocycle identity

\[
T_{A+n}
=
2^nT_A+
\sum_{r=1}^{n}2^{n-r}c_{A+r}.
\]

This composition law is intrinsic to the induced return layer.

---

## 5. Exact conjugacy to doubling

Represent the affine state interval as the circle

\[
I=(-1,0]\cong\mathbb T=\mathbb R/\mathbb Z.
\]

Define

\[
h(E)=[E+\gamma]\in\mathbb T.
\]

For the affine branch law

\[
F(E)=2E+\gamma-c(E),
\qquad c(E)\in\{7,8,9\},
\]

we have

\[
\begin{aligned}
h(F(E))
&=[2E+2\gamma-c(E)]\\
&=2[E+\gamma]\\
&=D(h(E)),
\end{aligned}
\]

where

\[
D(z)=2z\pmod1.
\]

Thus

\[
h\circ F=D\circ h.
\]

At the canonical boundary,

\[
E_A=\lambda j_A+\beta-T_A,
\qquad
j_A=6(2^{A+1}-1).
\]

Because `T_A` is integral and `beta+gamma=6lambda`,

\[
\begin{aligned}
h(E_A)
&=[\lambda j_A+\beta+\gamma]\\
&=[\lambda(j_A+6)]\\
&=[12\lambda\,2^A].
\end{aligned}
\]

Set

\[
\alpha=12\lambda=12\frac{\log2}{\log\varphi}.
\]

Then the canonical affine orbit is conjugate to

\[
z_A=D^A([\alpha])=[2^A\alpha].
\]

---

## 6. What can be proved about the canonical orbit closure

### 6.1 Irrationality

The number `lambda` is irrational. Suppose instead that

\[
\lambda=\frac pq
\]

with positive integers `p,q`. Then

\[
\varphi^p=2^q.
\]

Apply the nontrivial Galois conjugation of `Q(sqrt(5))`, under which

\[
\varphi\mapsto\psi=-\varphi^{-1}.
\]

The rational integer `2^q` is fixed, so

\[
\psi^p=2^q.
\]

If `p` is odd, the left side is negative. If `p` is even, its absolute value is less than one, while `2^q>1`. Both are impossible. Therefore

\[
\lambda\notin\mathbb Q,
\qquad
\alpha\notin\mathbb Q.
\]

The doubling orbit is consequently not preperiodic.

### 6.2 Density is a different theorem

For a non-dyadic point `alpha`, the following are equivalent:

1. `closure{D^A(alpha):A>=0}=T`;
2. the binary expansion of `alpha` contains every finite binary word;
3. `alpha` is base-2 disjunctive.

This follows because binary cylinders form a basis for the circle topology.

Irrationality does **not** imply disjunctivity. Proper infinite closed doubling-invariant sets can contain irrational points. No accepted source proves disjunctivity of

\[
12\frac{\log2}{\log\varphi}.
\]

Therefore

```text
CANONICAL ORBIT CLOSURE: NOT YET DETERMINED
```

The exact unresolved fork is:

```text
Case 1: alpha is base-2 disjunctive, so the closure is the full affine system.
Case 2: alpha is not base-2 disjunctive, so the closure is a proper invariant subsystem.
```

Case 3 from the task is too weak and is rejected below.

---

## 7. Intrinsic symbolic system of the canonical orbit

Let

\[
\mathbf c=c_1c_2c_3\cdots
\]

be the exact canonical carry itinerary. Its language is

\[
\mathcal L_{\mathrm{can}}
=
\{w:\text{$w$ occurs contiguously in }\mathbf c\}.
\]

Define its one-sided shift-orbit closure

\[
X_{\mathrm{can}}
=
\overline{\{\sigma^n\mathbf c:n\ge0\}}
\subseteq\{7,8,9\}^{\mathbb N}.
\]

This is an intrinsic compact symbolic dynamical system of D1 whether or not it equals the ambient full affine coding.

### 7.1 Aperiodicity

The affine partition is generating on boundary-avoiding points. On every length-`n` cylinder, `F^n` has slope `2^n`, so the cylinder diameter is at most `2^{-n}`. Hence two boundary-avoiding points with the same infinite carry code are equal.

The global threshold theorem proves that the canonical orbit never hits a partition boundary. If `c` were eventually periodic, two distinct tail points of the canonical doubling orbit would have identical infinite codes. Generating injectivity would make those orbit points equal, making `alpha` preperiodic under doubling. That would force `alpha` to be rational, contradicting Section 6.1.

Therefore

\[
\boxed{\mathbf c\text{ is not eventually periodic}.}
\]

### 7.2 Canonical complexity bounds

Let

\[
p_{\mathrm{can}}(n)=|\mathcal L_{\mathrm{can}}\cap\{7,8,9\}^n|.
\]

By the Morse-Hedlund criterion, an aperiodic one-sided word satisfies

\[
p_{\mathrm{can}}(n)\ge n+1.
\]

Every canonical word is an ambient affine word, while Branch 1 proves

\[
p_{\mathrm{aff}}(n)=2^{n+1}-1.
\]

Thus

\[
\boxed{n+1\le p_{\mathrm{can}}(n)\le2^{n+1}-1.}
\]

Consequently the canonical orbit-closure entropy satisfies

\[
\boxed{0\le h(X_{\mathrm{can}})\le\log2.}
\]

The exact value is not known.

### 7.3 Transitivity

By definition, the forward shift orbit of `c` is dense in `X_can`. Therefore

\[
\boxed{X_{\mathrm{can}}\text{ is topologically transitive}.}
\]

This does not imply mixing.

### 7.4 Case-3 rejection

The canonical layer intrinsically carries more than the scalar arithmetic cocycle:

- an exact aperiodic three-symbol itinerary;
- an infinite compact shift-orbit closure;
- an intrinsic finite-word language;
- unbounded complexity;
- a topologically transitive symbolic system;
- exact complexity and entropy bounds.

Therefore

```text
CASE 3, “ONLY THE ARITHMETIC COCYCLE IS INTRINSIC”: FALSE
```

The unresolved strategic fork is Case 1 versus Case 2.

---

## 8. Property transfer table

| Property | Canonical orbit / itinerary | Canonical orbit closure `X_can` | Full affine system | Transfer status | Proof or witness |
|---|---|---|---|---|---|
| exact `7/8/9` carry law | proved | inherited by closure | proved | exact | global threshold plus boundary cocycle |
| aperiodicity | proved | infinite | contains aperiodic points | exact | irrational doubling seed plus generating coding |
| language inclusion | `L_can subset L_aff` | same language as itinerary | ambient language | exact | every canonical point follows affine coding |
| language equality | open | open | self | not transferred | equivalent to dense symbolic coverage; density sufficient |
| complexity | finite-word function defined | `n+1 <= p_can(n) <= 2^(n+1)-1` | `2^(n+1)-1` | bounded only | Morse-Hedlund plus ambient inclusion |
| entropy | not a property of one word alone | `0 <= h <= log 2` | `log 2` | bounded only | complexity bounds |
| follower-set structure | canonical follower languages defined | intrinsic but unclassified | infinitely many; non-sofic | not transferred | density/language equality absent |
| soficity | not applicable to one orbit | open | non-sofic | not transferred | no closure equality theorem |
| finite Markov order | not applicable as ambient property | open | none | not transferred | no closure equality theorem |
| transitivity | orbit generates closure | proved | mixing, hence transitive | intrinsic proof | definition of orbit closure |
| mixing | not established | open | proved | not transferred | transitivity is weaker |
| equidistribution | open | not required for closure definition | Lebesgue invariant benchmark | not transferred | finite frequency evidence only |

---

## 9. Finite language coverage

The accepted trace contains 10,000 carry symbols, corresponding to `c_1` through `c_10000`.

The reanalysis gives:

| length `n` | observed canonical words | full affine words | finite coverage |
|---:|---:|---:|---:|
| 1 | 3 | 3 | 100% |
| 2 | 7 | 7 | 100% |
| 3 | 15 | 15 | 100% |
| 4 | 31 | 31 | 100% |
| 5 | 63 | 63 | 100% |
| 6 | 127 | 127 | 100% |
| 7 | 255 | 255 | 100% |
| 8 | 507 | 511 | 99.217% |

The four length-eight ambient words not seen in that finite prefix are

```text
78887888
79789888
87979888
88889888
```

Their absence in a finite prefix is not an exclusion theorem. Complete coverage through length seven is evidence compatible with density, but no finite prefix can prove disjunctivity.

---

## 10. The D1 domain-proper effective invariant

### 10.1 Smallest lawful nontrivial package

The smallest package that is both exact and intrinsically D1 is:

\[
\boxed{
\mathfrak C_{D1}
=(\Sigma^-,\mathcal R,c)
}
\]

with its canonically generated symbolic descendant

\[
(\mathbf c,X_{\mathrm{can}},\mathcal L_{\mathrm{can}}).
\]

The affine coordinate `pi` supplies a semiconjugate realization, but the effective invariant is not dependent on presenting it as a real number. The core is the **renormalized return relation**

\[
\nu(q_A)=2\nu(q_{A-1})+c_A,
\qquad c_A\in\{7,8,9\},
\]

and its composition across complete saturated domains.

### 10.2 Why it is not merely a rename of D0

Every closing primitive step has the same instantaneous letter `L`. Nevertheless successive complete returns carry different labels, for example

\[
c_1=9,\qquad c_2=7,\qquad c_3=8.
\]

No symbol map

\[
\{B,Q,L\}\to\{7,8,9\}
\]

can reproduce the boundary word, because the three values classify complete return edges rather than primitive ticks.

More strongly, the return map has a variable stopping time and the cocycle compares two completed boundary states after removing the universal doubling contribution. This relation does not exist as an object of the instantaneous D0 transition category. It becomes lawful only after induction on the saturated boundary section.

The cocycle is fully derived from retained D0 history, so it does not add uncaused information. CF000 does not require informational independence. It requires a new internal determination rather than renaming. The D1 branch label is exactly such a new relational determination.

Therefore

```text
D1 EFFECTIVE INVARIANT GENUINELY NEW: PROVED
```

The exact strength is:

> D1 adds a domain-proper induced return invariant, not a new primitive invariant and not an independent raw coordinate.

---

## 11. Invariant stacking

The dependency stack is

```text
CF000 primitive unresolved invariant
        |
        v  inherited, not discharged
D0 primitive QBL custody
    exact pair, phase, positions, word, saturation law
        |
        | restrict to saturated pre-L boundary section
        | retain complete boundary states and history
        v
D1 induced boundary-return domain
    inherited D0 state stack
    + return map R
    + domain-proper cocycle c in {7,8,9}
    + canonical symbolic itinerary and orbit closure
```

The realizations differ:

- the primitive invariant is origin-level unresolved opposition;
- D0 realizes it through primitive custody and saturation;
- D1 realizes a new effective invariant through return-edge renormalization and symbolic memory.

CF000 expressly permits different realization types across admitted domains. The new effective invariant need not resemble the prior one geometrically.

---

## 12. Same-layer saturation for D1

Non-soficity is not itself saturation. A native criterion must be stated independently.

Let `Y` be a lawful D1 symbolic subsystem and let

\[
\mathcal D:Y\to Z
\]

be a proposed D1 description. Define `D1` same-layer saturation by the following falsifiable conditions:

1. **Future separation.** If `D(x)=D(x')`, then `x` and `x'` have the same follower language and the same future return-cocycle values at every depth.
2. **Return-observable completeness.** Every lawful invariant-bearing observable of the boundary-return dynamics that is unchanged by replacing a D0 microstep realization with another realization of the same boundary edge factors through `D`.
3. **No internal refinement left.** There is no strictly finer lawful equivalence inside the same boundary-return domain that separates future behavior while preserving the declared lower-layer inheritance.

A direct falsifier is a pair `x,x'` with

\[
\mathcal D(x)=\mathcal D(x')
\]

but some finite continuation word admitted from one and not the other. A second falsifier is a boundary-return observable that cannot be computed from `D` but does not require leaving D1.

This criterion does not assert that the current finite descriptors saturate D1. It states exactly what must be shown before a future re-articulation out of D1 can be called saturation-forced.

---

## 13. Descriptive-level L test

The D0-to-D1 admission is tested separately from Orthad rank extension.

| Requirement | Verdict | Certificate |
|---|---|---|
| prior invariant stack retained | **PASS** | every `S_A^-` contains the full retained custody boundary state and exact history; D1 is induced over those states |
| new descriptive domain lawfully admitted | **PASS** | `R` is the exact first-return map from one saturated pre-`L` section point to the next |
| new domain-proper effective invariant present | **PASS** | exact cocycle `c_A in {7,8,9}` and its intrinsic symbolic system |
| not reducible to renaming inside D0 | **PASS** | one closing primitive letter `L` supports three distinct complete-return classes; no symbolwise map exists |
| same-layer saturation stated independently | **PASS** | Section 12 gives a follower/future-separation criterion independent of non-soficity |

The lower primitive domain is genuinely saturated at every `S_A^-`: `B` is blocked and no unused `Q` position remains. D1 retains that completed structure and admits a new return-level determination.

Therefore, at the descriptive grammar layer,

```text
HIGHER-ORDER DESCRIPTIVE L: PROVED
```

This theorem does **not** say that the future carry is appended by the instantaneous primitive `L`, and it does not say that the Orthad has acquired a proved new pairing axis.

The indexed carry boundary remains:

```text
JUST-COMPLETED CARRY c_A RECOVERABLE AT S_A^-: PASS
FUTURE CARRY c_{A+1} APPENDED BY THE INSTANTANEOUS L STEP: FAIL
```

The descriptive theorem says that the completed lower-layer dynamics, once viewed through their lawful boundary-return section, admit a new domain-proper effective invariant.

---

## 14. Orthad lane remains separate

The current Orthad dependency order is

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

The first open obligation is still the all-depth primary pairing recurrence. Without it, the following remain open:

- exact primary pairing type, seed, and value mutation;
- exact chart maps `iota_+` and `iota_-` at every prefix;
- exact bidirectional transfer recurrences;
- proof that the Orthad `L` extension embeds the old pairing and appends an independent retained axis under a uniquely licensed realization.

The grammar-level result neither proves nor negates that stronger recurrence.

```text
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
```

Counts and carry symbols still do not determine chart matrices, gauge values, holonomy, FQM classes, or Weil projections.

---

## 15. Final strategic result

The current evidence does not select Case 1 or Case 2 because density of the explicit logarithmic doubling seed is not proved. It does, however, eliminate Case 3.

The exact outcome is:

```text
CANONICAL ORBIT CLOSURE: NOT YET DETERMINED
CASE 1 VERSUS CASE 2: REDUCED TO BASE-2 DISJUNCTIVITY OF alpha
CASE 3: FALSE
```

The domain-proper invariant is already strong enough to close the descriptive-level question:

\[
\boxed{
\text{complete QBL domain returns}
\longrightarrow
\text{exact three-valued renormalization cocycle}
\longrightarrow
\text{intrinsic aperiodic symbolic boundary system}.
}
\]

What remains open is not whether D1 has an effective invariant. It is how large the canonical invariant subsystem is inside the ambient full affine coding.

---

## 16. Final status ledger

### PROVED

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
EXACT BOUNDARY-RETURN COCYCLE: PROVED
CANONICAL CARRY ITINERARY APERIODIC: PROVED
CANONICAL SYMBOLIC ORBIT CLOSURE INFINITE: PROVED
CANONICAL SYMBOLIC ORBIT CLOSURE TRANSITIVE: PROVED
D1 EFFECTIVE INVARIANT GENUINELY NEW: PROVED
HIGHER-ORDER DESCRIPTIVE L: PROVED
```

### CERTIFIED FINITELY

```text
ACCEPTED CARRY TRACE A=0..10000: REVALIDATED
ALL FULL-AFFINE WORDS OF LENGTH 1..7 OCCUR IN THE FINITE TRACE
```

### OBSERVED

```text
FINITE FREQUENCIES ARE CLOSE TO THE ACCEPTED LEBESGUE BENCHMARKS
FINITE WORD COVERAGE IS CONSISTENT WITH DENSITY
```

### OPEN

```text
CANONICAL ORBIT CLOSURE = FULL AFFINE SYSTEM: NOT YET PROVED
CANONICAL ORBIT CLOSURE IS PROPER: NOT YET PROVED
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
CANONICAL ORBIT-CLOSURE NON-SOFICITY: NOT YET PROVED
CANONICAL ORBIT-CLOSURE MIXING: NOT YET PROVED
CANONICAL ORBIT-CLOSURE FINITE MARKOV ORDER: NOT YET DETERMINED
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
ORTHAD-LEVEL HIGHER-ORDER L: NOT YET DERIVED
GAUGE/FQM MAP FROM d_A=+-1: NOT YET DERIVED
```
