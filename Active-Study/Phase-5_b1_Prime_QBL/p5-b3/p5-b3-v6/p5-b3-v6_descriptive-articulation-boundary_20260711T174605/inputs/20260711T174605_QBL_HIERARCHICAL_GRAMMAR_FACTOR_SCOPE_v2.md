# QBL Hierarchical Grammar Factor Scope

**Step:** `p5-b3-v2`  
**Status:** corrected dynamical-scope and higher-order-`L` boundary analysis  
**Primary authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Accepted theorem inputs:** closed Branch 1 affine-language results and closed Branch 2 global threshold bridge  
**Older canonical ledgers:** provenance only

## 1. Disposition

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
FULL AFFINE INTERVAL FACTOR: IMPOSSIBLE FOR THE STATED DOMAIN
ENLARGED LAWFUL QBL-TO-FULL-INTERVAL FACTOR: NOT YET DERIVED
CANONICAL ORBIT LANGUAGE = FULL AFFINE LANGUAGE: NOT YET PROVED

A. CARRY APPENDED AT INSTANTANEOUS PRIMITIVE L: FAIL
B. EXACT BOUNDARY-RETURN COCYCLE: PASS
C. HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED

HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
p5-b3 BRANCH STATUS: OPEN
```

The accepted arithmetic theorem is exact but narrower than a factor onto the full affine interval system. It gives a state-internal semiconjugacy between one canonical QBL boundary orbit and its corresponding affine orbit. It does not prove that this single itinerary realizes the complete non-sofic affine language.

The stronger invariant remains the boundary renormalization cocycle

\[
(j_A,b_A,E_A)\longmapsto
(2j_A+6,\,2b_A+c_{A+1},\,2E_A+\gamma-c_{A+1}),
\]

with `b_A=nu(q_A)=T_A`. This proves an exact arithmetic recurrence across completed domain returns. It does not decide whether the complete retained Orthad extension realizes the user's proposed higher-order descriptive `L`.

## 2. Source map

| Classification | Source | Role |
|---|---|---|
| **Primary** | `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` | Exact custody state, strict `B>Q>L`, boundary construction, coupled Orthad architecture, and open all-depth recurrences. |
| **Accepted** | `QBL_CARRY_AFFINE_FOLLOWER_STRUCTURE_v5.md` | Full affine interval coding: complexity, entropy, non-soficity, mixing, and no finite Markov order. |
| **Accepted** | `QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md` | Global theorem `T_A=ceil(y_A)` and exact threshold indexing. |
| **Conjectural** | `STRONG-EXPLICIT-NOTES` extract | The higher-order self-recurrence question only; not a premise. |
| **Contextual** | `CF03` active-depth extract | Active depth is new retained structure by scale, not raw multiplicity. |
| **Contextual architecture** | supplied Orthad diagram | Visualizes pairing-first rank extension; the written law controls any ambiguity. |
| **Provenance only** | `p5-b3-v1` document and audit | Records the corrected scope boundary and branch lineage. |

## 3. Canonical pre-`L` boundary states

Let the complete coupled state be

\[
\widehat X=(X,P,\Omega^+,\Omega^-,T^{+\to-},T^{-\to+}),
\qquad
X=(A,q,\theta,k,j,W).
\]

For Domain `A`, define

\[
N_A=6\,2^A,
\qquad
J_A=\sum_{r=0}^{A}N_r=6(2^{A+1}-1).
\]

The canonical state immediately before the `L` closing Domain `A` is

\[
S_A^-=
\bigl(
A,q_A,\theta_A,N_A-1,J_A,W_A^-,b_A;
P_A^-,\Omega_A^{+,-},\Omega_A^{-,-},
T_A^{+\to-,-},T_A^{-\to+,-}
\bigr),
\]

where

\[
b_A=\#_B(W_A^-)=\nu(q_A).
\]

The accepted threshold theorem and Fibonacci corridor give

\[
q_A=(F_{T_A+1},F_{T_A+2}),
\qquad
b_A=T_A.
\]

No Orthad coordinate is replaced by a count. The pairing, chart restrictions, and transfers are retained but remain without an all-depth closed recurrence.

## 4. The two canonical orbit systems

### 4.1 QBL boundary orbit

Define

\[
\mathcal O_{\mathrm{QBL}}:=\{S_A^-:A\ge0\}
\]

and the boundary-return map

\[
\mathcal R(S_A^-):=S_{A+1}^-.
\]

`R` here is a calligraphic boundary-return map, not an `R/S/T` macro. It includes the closing primitive `L` and the complete self-selected `B/Q` evolution of the next domain.

For topology, use the subspace topology inherited from the product retained-state arena in which the integer and finite-word custody coordinates are discrete. Because the domain counter `A` is discrete and unique on this orbit, every `S_A^-` is isolated; `O_QBL` is countable and discrete. Its measurable structure is the power-set sigma algebra.

### 4.2 Restricted affine orbit

Set

\[
\lambda=\frac{\log2}{\log\varphi},
\qquad
\beta=\frac{\log5}{2\log\varphi}-\frac32,
\]

\[
y_A=\lambda J_A+\beta,
\qquad
E_A=y_A-T_A\in(-1,0).
\]

Define

\[
\mathcal O_E:=\{E_A:A\ge0\}\subset(-1,0)
\]

with the subspace topology and Borel sigma algebra. Let

\[
c_{A+1}=T_{A+1}-2T_A\in\{7,8,9\}
\]

and define the restricted map

\[
F(E_A):=E_{A+1}=2E_A+\gamma-c_{A+1},
\qquad
\gamma=6\lambda-\beta.
\]

The global threshold theorem supplies nonintegrality of every `y_A`; equivalently the canonical orbit does not land on a carry boundary. Thus `F` is unambiguous on `O_E`. The maps `R` and `pi` are continuous because `O_QBL` is discrete. The restricted map `F|_{O_E}` is continuous at every orbit point because each point lies in the interior of one affine branch. Hence the commuting theorem below is a topological semiconjugacy of the two countable orbit systems, as well as a measurable one.

## 5. State-internal boundary coordinate

On canonical pre-`L` states define

\[
\boxed{
\pi(S_A^-)=\lambda j_A+\beta-\nu(q_A).
}
\]

The inputs are retained custody invariants:

1. the global phase-position index `j_A`;
2. the carried Fibonacci pair `q_A`, from which its unique reachable corridor index `nu(q_A)` is recovered;
3. fixed constants of the law.

It is not the trivial map `A -> E_A`. At the canonical boundary,

\[
\pi(S_A^-)=\lambda J_A+\beta-T_A=E_A.
\]

## 6. Canonical boundary-orbit semiconjugacy

### Theorem 6.1

\[
\boxed{\pi\circ\mathcal R=F\circ\pi\quad\text{on }\mathcal O_{\mathrm{QBL}}.}
\]

**Proof.** The custody law gives

\[
j_{A+1}=2j_A+6.
\]

The exact threshold counts give

\[
\nu(q_{A+1})=2\nu(q_A)+c_{A+1}.
\]

Therefore

\[
\begin{aligned}
\pi(\mathcal R(S_A^-))
&=\lambda(2j_A+6)+\beta-
  (2\nu(q_A)+c_{A+1})\\
&=2(\lambda j_A+\beta-\nu(q_A))
 +(6\lambda-\beta)-c_{A+1}\\
&=2\pi(S_A^-)+\gamma-c_{A+1}\\
&=F(\pi(S_A^-)).
\end{aligned}
\]

This proves the commuting law. ∎

The map is surjective onto `O_E` by construction: every `E_A` equals `pi(S_A^-)`. Injectivity is not required for a semiconjugacy and is not used here.

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
```

## 7. Standard full-factor scope

A standard factor onto the full affine interval system would require a named dynamical domain `X`, the full interval codomain `(-1,0]`, and a surjective map

\[
\Pi:X\twoheadrightarrow(-1,0]
\]

that intertwines the dynamics.

For the stated domain `X=O_QBL`, this is impossible even before continuity is considered:

- `O_QBL` is countable;
- `(-1,0]` is uncountable;
- no map from a countable set can be surjective onto an uncountable interval.

Hence

```text
FULL AFFINE INTERVAL FACTOR: IMPOSSIBLE FOR THE STATED DOMAIN
```

This does not rule out a future factor from an enlarged lawful QBL boundary-state family. The current primitive authority supplies one canonical orbit from the fixed origin and does not derive an uncountable family of lawful boundary states with the required recurrence. Arbitrary pairs `(j,b)` cannot be inserted and renamed QBL states.

```text
ENLARGED LAWFUL QBL-TO-FULL-INTERVAL FACTOR: NOT YET DERIVED
```

## 8. Canonical itinerary versus full affine language

Define the canonical carry itinerary

\[
\mathbf c=c_1c_2c_3\cdots,
\qquad
c_{A+1}=T_{A+1}-2T_A.
\]

Its finite-word language is

\[
\mathcal L_{\mathrm{can}}
=
\{w:\text{$w$ occurs as a contiguous block of }\mathbf c\}.
\]

Branch 1 defines the full affine cylinder language

\[
\mathcal L_{\mathrm{aff}}
=
\{w:C(w)\ne\varnothing\},
\]

where `C(w)` is the exact half-open interval cylinder.

Because the canonical error sequence is one orbit of the affine map,

\[
\boxed{\mathcal L_{\mathrm{can}}\subseteq\mathcal L_{\mathrm{aff}}.}
\]

Equality is not established. A dense canonical orbit in `(-1,0]` would suffice, because every nonempty affine cylinder has nonempty interior and a dense orbit meets every such interior. Specific-orbit equidistribution would also suffice but is stronger than needed. Neither density nor equidistribution is proved for this logarithmic starting point.

```text
CANONICAL ORBIT LANGUAGE = FULL AFFINE LANGUAGE: NOT YET PROVED
```

## 9. Correct transfer of Branch 1 properties

The following remain theorems of the **full affine interval coding**:

\[
p(n)=2^{n+1}-1,
\qquad
h_{\mathrm{affine}}=\log2,
\]

and that language is non-sofic, mixing, and has no finite Markov order.

For the canonical QBL carry itinerary, this pass proves only:

- the globally exact `7/8/9` recurrence;
- every canonical finite block lies in the full affine language;
- all universal affine forbidden-word and cylinder constraints apply to the canonical itinerary;
- the exact state-internal boundary-orbit semiconjugacy.

It does **not** transfer full-language non-soficity, mixing, entropy, complexity, or absence of finite Markov order to the shift-orbit closure of the canonical itinerary.

## 10. Three distinct higher-order `L` claims

### A. Carry appended at the instantaneous primitive `L`

**Verdict: FAIL.**

At the primitive step

\[
S_A^-\xrightarrow{L}S_A^+,
\]

`L` increments `A`, resets the local index, appends `L` to the word, carries `q` and `theta`, and extends the retained Orthad rank. The arithmetic carry

\[
c_{A+1}=\nu(q_{A+1})-2\nu(q_A)
\]

cannot be evaluated until `S_{A+1}^-` exists after the complete next-domain return.

### B. Exact boundary-return cocycle

**Verdict: PASS.**

The complete return satisfies

\[
(j,b,E)\mapsto(2j+6,2b+c,2E+\gamma-c),
\qquad c\in\{7,8,9\}.
\]

This is an exact arithmetic cocycle derived from two successive canonical pre-`L` boundaries.

### C. Higher-order descriptive `L` on completed lower-layer dynamics

**Verdict: NOT YET DERIVED.**

A descriptive-layer `L` theorem requires a defined meta-state space, an old-description map, a retained extension coordinate or axis, and an extension map that preserves the completed old description while opening one new independent distinction and resuming the governing law. The arithmetic cocycle proves resumed boundary law, but it does not define the full descriptive extension object.

```text
A. CARRY APPENDED AT INSTANTANEOUS PRIMITIVE L: FAIL
B. EXACT BOUNDARY-RETURN COCYCLE: PASS
C. HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
```

## 11. Independence criterion

Let `Z` be a lawful comparison family of completed lower-layer states and let

\[
D:Z\to Y
\]

be the old descriptive readout. A proposed new coordinate

\[
\xi:Z\to K
\]

is independent relative to `D` when it does not factor through `D`. Equivalently, there must exist lawful states `z,z'` such that

\[
D(z)=D(z')
\qquad\text{but}\qquad
\xi(z)\ne\xi(z').
\]

Thus the extension splits at least one fiber of the old description.

The present canonical orbit supplies only one completed state at each domain index and no derived comparison family of completed Orthad boundary states sharing an old description while differing in the proposed new axis. The arithmetic carry is a function of the boundary return and does not by itself provide or refute such a fiber split.

```text
DESCRIPTIVE-LAYER INDEPENDENT AXIS TEST: NOT YET DERIVED
```

## 12. Orthad dependency that remains open

The written authority and supplied diagram agree on the architecture:

1. primitive custody chooses `B`, `Q`, or `L`;
2. the primary pairing mutates;
3. two chart restrictions are derived from that pairing;
4. two directed transfers mutate;
5. at `L`, the completed active axis is latched and one new active orthogonal axis is appended throughout the retained pairing/Orthad object.

The arithmetic map `pi` ignores these coordinates. Therefore it cannot disprove an Orthad-level higher-order recurrence.

The exact dependency still missing is the all-depth construction

\[
(P_t,\Omega_t^+,\Omega_t^-,T_t^{+\to-},T_t^{-\to+})
\xrightarrow{B,Q,L}
(P_{t+1},\Omega_{t+1}^+,\Omega_{t+1}^-,T_{t+1}^{+\to-},T_{t+1}^{-\to+}),
\]

including:

- the primary-pairing recurrence at every word prefix;
- explicit chart maps proving both restrictions at every prefix;
- exact bidirectional transfer recurrences;
- the `L` latching/extension map on those objects;
- a lawful comparison family and old-description fibers for the independence test.

Until these are derived:

```text
ORTHAD-LEVEL HIGHER-ORDER L RECURRENCE: NOT YET DERIVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

## 13. Hierarchical depth boundary

Branch 1 gives

\[
p(A)=2^{A+1}-1,
\]

while QBL custody gives

\[
J_A=6(2^{A+1}-1).
\]

Therefore

\[
\boxed{J_A=6p(A).}
\]

This is an exact multiplicity identity. It does not define the QBL retained distinctions that host affine cylinders, nor a refinement-preserving map between them.

CF03 counts active depth only when a scale exposes new boundaries after coarser boundaries have been removed. A canonical map

\[
\iota_A:\mathcal C_A\to\mathcal H_A
\]

from affine length-`A` cylinders to a defined QBL retained hierarchy, compatible with refinement and `L`, remains absent.

```text
HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY
```

## 14. Exact strength of self-recurrence

| Statement | Status |
|---|---|
| Exact internal self-recurrence of complete primitive `L` at a higher descriptive layer | **NOT YET DERIVED** |
| Exact canonical boundary-orbit arithmetic semiconjugacy | **PROVED** |
| Exact boundary-return arithmetic cocycle | **PROVED** |
| Structural resumed-law recurrence at the custody arithmetic level | **PROVED** |
| Full affine interval/language factor from the canonical QBL orbit | **IMPOSSIBLE / NOT YET DERIVED at enlarged scope** |
| Raw cardinality resemblance | **Exact count identity but non-load-bearing for depth** |

The appropriate current theorem label is **canonical boundary-orbit arithmetic semiconjugacy**, not “fractal `L`” or “higher-dimensional `L`.” The descriptive-layer conjecture remains live and depends on the open retained Orthad recurrence.

## 15. Formal and computational boundary

The package regenerates:

- an exact finite custody simulation and boundary-state table;
- symbolic factor algebra and recurrence checks;
- canonical-language finite comparisons without promoting them to language equality;
- a premise-derived three-claim `L` status table;
- source and executed no-I/O notebooks;
- figures, outputs, traces, manifest, and deterministic archive.

The Lean file is a theorem surface. It contains only parameterized statements and elementary proof sketches; no compiled certificate is claimed.

```text
LEAN THEOREM SURFACE PRESENT; PROOF AND COMPILATION NOT VERIFIED
```

## 16. Final status

```text
CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: PROVED
FULL AFFINE INTERVAL FACTOR: IMPOSSIBLE FOR THE STATED DOMAIN
ENLARGED LAWFUL QBL-TO-FULL-INTERVAL FACTOR: NOT YET DERIVED
CANONICAL ORBIT LANGUAGE = FULL AFFINE LANGUAGE: NOT YET PROVED

A. CARRY APPENDED AT INSTANTANEOUS PRIMITIVE L: FAIL
B. EXACT BOUNDARY-RETURN COCYCLE: PASS
C. HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
DESCRIPTIVE-LAYER INDEPENDENT AXIS TEST: NOT YET DERIVED
ORTHAD-LEVEL HIGHER-ORDER L RECURRENCE: NOT YET DERIVED

HIERARCHICAL DEPTH RECURRENCE: COUNT ALIGNMENT ONLY
SPECIFIC-ORBIT EQUIDISTRIBUTION: NOT PROVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
LEAN THEOREM SURFACE PRESENT; PROOF AND COMPILATION NOT VERIFIED
p5-b3 BRANCH STATUS: OPEN
```
