# QBL Primitive Custody and Orthad Law

**Revision:** v3 clarity lock  
**Status:** primary semantic authority for the current primitive law and Orthad architecture  
**Scope:** fixes the ordered `Q/B/L` word, carried state, same-tick dual-chart Orthad evolution, pairing-first dependency, transfer timing, downstream bridge boundaries, and terminal projection boundary.  
**Primitive authority:** `X_t` alone self-selects one operator in `{B,Q,L}`. The Orthad never selects that operator. The same selected operator mutates both opposed chart matrices during the same atomic tick.  
**Interpretation rule:** settled behavior must not be reopened merely because its complete algebraic realization is not yet typed or has not yet been recovered into the clean chain.  

---

## 0A. Clarity and status protocol

This document distinguishes six different states of knowledge.

```text
SETTLED BEHAVIOR
    The system's intended causal or operational law is fixed.
    An agent may not present it as a hypothesis to test.

EXACT CURRENT-CANON RESULT
    The statement has been derived or exactly reproduced under the current
    autonomous B > Q > L primitive law.

RECOVERED LEGACY KERNEL
    Exact local mathematics survives from older work after obsolete grammar
    and interpretation are removed.

SETTLED BUT NOT FULLY TYPED
    The behavior is fixed, but the exact carrier, map type, basis, or algebraic
    realization remains to be specified.

NOT YET RECOVERED OR DERIVED IN THE CLEAN CHAIN
    No exact formula has yet been validated in the active canonical chain.
    This does not mean the idea was never discussed or encoded in the archives.

CONDITIONAL DOWNSTREAM RESULT
    The mathematics is exact on supplied downstream objects, but its complete
    provenance from the clean Orthad remains open.
```

The phrase `NOT YET DERIVED` may be used only for an exact equation, map, carrier,
or proof obligation. It must not be used to reopen any settled behavior below.

### Cold-start semantic lock

```text
The primitive state X_t is autonomous.

X_t alone self-selects exactly one primitive U_t in {B,Q,L} through its own
current predicates and strict priority B > Q > L.

The Orthad does not select, permit, block, veto, schedule, or alter U_t.
Removing the Orthad leaves the primitive evolution unchanged.

Every primitive step is immediately also an Orthad step.

The same selected primitive U_t mutates both opposed Orthad chart matrices
simultaneously. There are not separate U_t+ and U_t- primitive operators.

The chart results may differ because the chart states and local frames are
already counter-oriented. The difference comes from the states on which the
same operator acts, not from splitting, reversing, conjugating, or independently
choosing the primitive.

After the simultaneous chart-local mutation, any required bidirectional
cross-chart transfer or reconciliation occurs within that same atomic tick.

The complete updated primitive state, primary relation, two chart matrices,
and two directed transfers are retained before X_{t+1} self-selects the next
primitive.

Pairing-first is a structural dependency inside the tick. It is not a delayed
pipeline in which the pairing changes now and the matrices catch up later.

No projection, terminal readout, candidate comparison, or external-reference
matching occurs during retained evolution.
```

This block is settled. It is not an experimental question.

---

## 0. Hard exclusions

This law does **not** use:

- `R/S/T`;
- a macro selector;
- a fixed window;
- a 64-tick schedule;
- a clock or cadence;
- an externally supplied operator word;
- a choice among candidate next steps;
- projection or readout during evolution.

The next primitive letter is determined by the current primitive state `X_t` alone. Orthad data is not an input to primitive selection.

---

## 1. State carried by the primitive evolution

At a minimum, the custody state contains

$$
X=(A,q,\theta,k,j,W),
\qquad q=(u,v),\quad 1\le u\le v.
$$

Where:

- `A` is the current dimensional/domain counter;
- `q=(u,v)` is the carried balanced-refinement pair;
- `θ` is the carried phase;
- `k` is the zero-based phase-position index **inside the current domain**;
- `j` is the one-based global phase-position index across all domains;
- `W` is the exact ordered primitive word already executed.

The local number of available phase positions in domain `A` is

$$
N_A=6\cdot 2^A.
$$

Thus

$$
N_0=6,\qquad N_1=12,\qquad N_2=24,\ldots
$$

The first global position in domain `A` is

$$
j_{\mathrm{start}}(A)
=1+\sum_{r=0}^{A-1}N_r
=1+6(2^A-1),
$$

and within that domain

$$
j=j_{\mathrm{start}}(A)+k.
$$

`j` counts available phase positions. It is **not** the number of emitted `Q` letters.

`j` is retained for explicit global addressing, but it is constrained by

$$
j=j_{\mathrm{start}}(A)+k.
$$

It is not an independent selector coordinate. A lawful implementation may derive
`j` from `(A,k)` or carry it redundantly while enforcing this invariant.

For the exact first trace, the initial state is

$$
A=0,\qquad q=(1,1),\qquad \theta=0,\qquad k=0,\qquad j=1,\qquad W=\varepsilon.
$$

---

## 2. Primitive operations

### 2.1 `B`: highest-priority refinement

`B` performs one exact balanced refinement:

$$
B(u,v)=\operatorname{sort}(v,u+v).
$$

For an ordered pair `u≤v`, this is

$$
(u,v)\mapsto(v,u+v).
$$

`B` changes the carried pair and the associated refinement scale. It does not change `A`, `k`, or `θ`.

### 2.2 `Q`: phase-position advance

`Q` performs one quarter turn:

$$
\theta\mapsto\theta+\frac{\pi}{2}.
$$

It advances the local phase-position index:

$$
k\mapsto k+1.
$$

`Q` leaves `q` and `A` unchanged. Its effect is to expose the next available phase position, which expands the refinement capacity available to `B`.

### 2.3 `L`: forced dimensional extension

`L` fires only when neither `B` nor `Q` can continue in the current domain.

Its primitive custody action is:

$$
A\mapsto A+1.
$$

Then the state is carried into the new domain:

- `q` is carried unchanged;
- `θ` is carried unchanged;
- the exact ordered word/history is carried unchanged except for appending `L`;
- all previously accrued state is retained;
- the new domain begins at local phase-position index `k=0`;
- the available position count expands from `N_A` to `N_{A+1}=2N_A`.

**`L` does not perform a quarter turn.** It does not add `π/2` to `θ`. It increments the dimensional counter and carries the state into the enlarged domain.

Only the domain-local occupancy index restarts at zero. The carried phase and refinement history do not reset.

---

## 3. Capacity attached to a phase position

Each phase position carries a refinement capacity `Δ`.

Using the global phase-position index `j`:

$$
\Delta(j)=
\begin{cases}
2, & j=1,\\
4, & j=2,\\
2^{2j}, & j\ge 3.
\end{cases}
$$

Therefore Domain 0 has the exact capacities

$$
2,\ 4,\ 64,\ 256,\ 1024,\ 4096.
$$

After the first `L`, Domain 1 starts at global position `j=7`, so its first capacity is

$$
\Delta(7)=2^{14}=16384.
$$

A `Q` step does not arbitrarily alternate with `B`. It is used only after `B` is blocked, and its new phase position provides a larger `Δ` against which `B` is tested again.

---

## 4. Strict primitive priority

The priority order is

$$
B>Q>L.
$$

It is reevaluated after **every primitive step**.

### Deterministic next-step law

```text
loop:
    test B at the current state

    if B is admissible:
        execute exactly one B
        append B to the ordered word
        return to the top of the loop

    if B is blocked and another Q position exists:
        execute exactly one Q
        append Q to the ordered word
        return to the top of the loop

    if B is blocked and no Q position remains:
        execute L
        append L to the ordered word
        carry the state into A+1
        return to the top of the loop
```

This means:

- `B` continues for as many consecutive steps as the current phase position permits;
- `Q` occurs only when `B` is blocked;
- after every `Q`, priority returns immediately to `B`;
- consecutive `Q` steps occur only when `B` remains blocked after the preceding `Q`;
- `L` occurs only when `B` is blocked **and** all phase positions in the domain have been used.

There is no separate selector object. The state predicates make the next letter self-selecting.

---

## 5. When `Q` can no longer step

The initial phase position counts as position `k=0`. Therefore a domain with `N_A` available positions emits at most `N_A-1` actual `Q` letters.

`Q` is admissible exactly when

$$
k<N_A-1.
$$

`Q` is blocked exactly when

$$
k=N_A-1.
$$

Examples:

- Domain 0: `N_0=6`, so `k=0,1,2,3,4,5` are available and only five actual `Q` steps can occur.
- Domain 1: `N_1=12`, so eleven actual `Q` steps can occur.

Visible phase repetition does not block `Q`. The carried state distinguishes repeated visible phases. `Q` blocks only when the current domain has no unused lawful phase position left.

---

## 6. `B` admission and the floor anchor

At a nonterminal phase position, `B` may continue only while the next refined pair remains within the current capacity:

$$
(u',v')=B(u,v),
\qquad
u'v'\le\Delta(j).
$$

At the final phase position of a domain, the boundary-crossing `B` is admitted from a current anchor still below the capacity:

$$
uv<\Delta(j).
$$

That last `B` may carry the pair across the capacity. Its result is the floor anchor. Once the current product is at or above the final capacity, `B` is blocked.

Thus the floor anchor is not selected externally. It is the first carried pair produced by the final allowed refinement whose product lies beyond the final phase-position capacity.

The domain is saturated exactly when

$$
\text{`B` blocked}
\quad\land\quad
k=N_A-1.
$$

At that state, `L` is forced.

---

## 7. Exact first-domain trace from `(1,1)` to the first `L`

Initial state:

$$
A=0,\qquad q=(1,1),\qquad k=0,\qquad N_0=6.
$$

The exact ordered primitive word is

```text
B Q Q B B B Q B Q B B Q B B L
```

The order is load-bearing.

| Primitive step | Current phase position | Capacity | Operation and carried result | Why the next priority changes |
|---:|---:|---:|---|---|
| 0 | `k=0` | `2` | Start at `(1,1)` | `B` has priority |
| 1 | `k=0` | `2` | `B: (1,1)→(1,2)`, product `2` | Next child `(2,3)` has product `6>2`; `B` blocks |
| 2 | `k=1` | `4` | `Q` | `B` is retried |
| 3 | `k=2` | `64` | `Q` | At `k=1`, next child still had product `6>4`; the second `Q` opens capacity `64` |
| 4 | `k=2` | `64` | `B: (1,2)→(2,3)`, product `6` | `B` remains admissible |
| 5 | `k=2` | `64` | `B: (2,3)→(3,5)`, product `15` | `B` remains admissible |
| 6 | `k=2` | `64` | `B: (3,5)→(5,8)`, product `40` | Next child product `104>64`; `B` blocks |
| 7 | `k=3` | `256` | `Q` | `B` is retried |
| 8 | `k=3` | `256` | `B: (5,8)→(8,13)`, product `104` | Next child product `273>256`; `B` blocks |
| 9 | `k=4` | `1024` | `Q` | `B` is retried |
| 10 | `k=4` | `1024` | `B: (8,13)→(13,21)`, product `273` | `B` remains admissible |
| 11 | `k=4` | `1024` | `B: (13,21)→(21,34)`, product `714` | Next child product `1870>1024`; `B` blocks |
| 12 | `k=5` | `4096` | `Q` | This is the final phase position; `B` is retried |
| 13 | `k=5` | `4096` | `B: (21,34)→(34,55)`, product `1870` | Current product remains below `4096`; boundary refinement continues |
| 14 | `k=5` | `4096` | `B: (34,55)→(55,89)`, product `4895` | The floor has been crossed; `B` blocks |
| 15 | `k=5` | `4096` | `L` | `B` is blocked and no seventh phase position exists |

Therefore the first floor anchor is

$$
q_{\mathrm{floor},0}=(55,89),
\qquad
55\cdot89=4895.
$$

Five actual `Q` letters occurred, so the carried phase advanced by

$$
5\cdot\frac{\pi}{2}.
$$

`L` itself adds no phase.

---

## 8. State immediately after the first `L`

The first `L` changes only the dimensional/domain counter and opens the enlarged domain:

$$
A:0\mapsto1.
$$

The carried state entering Domain 1 is

$$
q=(55,89),
\qquad
\theta=\theta_{\mathrm{before}\ L},
\qquad
k=0,
\qquad
N_1=12.
$$

The ordered history remains

```text
B Q Q B B B Q B Q B B Q B B L
```

with all prior state retained.

The first global phase position of Domain 1 is `j=7`, with

$$
\Delta(7)=16384.
$$

Priority begins again with `B`.

The next refinement is

$$
(55,89)\xrightarrow{B}(89,144),
\qquad
89\cdot144=12816<16384.
$$

Therefore the first primitive step in the new domain is deterministically `B`.

No macro rule, timer, or external word chooses it.

---

## 9. Compact executable specification

```text
state:
    A                  dimensional/domain counter
    q=(u,v)            carried balanced pair
    theta              carried phase
    k                  local phase-position index
    j                  global phase-position index
    W                  exact ordered primitive history

N(A):
    6 * 2^A

JStart(A):
    1 + 6 * (2^A - 1)

Capacity(A,k):
    Delta(JStart(A) + k)

Delta(j):
    2            if j == 1
    4            if j == 2
    2^(2*j)      if j >= 3

CanQ(state):
    k < N(A) - 1

NextPair(q):
    (v, u+v)

CanB(state):
    if k < N(A)-1:
        product(NextPair(q)) <= Capacity(A,k)
    else:
        product(q) < Capacity(A,k)

Step(state):
    if CanB(state):
        q = NextPair(q)
        W += B
        # A, theta, k, and j do not change
    elif CanQ(state):
        theta += pi/2
        k += 1
        j += 1
        W += Q
    else:
        A += 1
        k = 0
        j = JStart(A)
        W += L
        # q and theta carry unchanged

invariant:
    j == JStart(A) + k
```

After every step, `Step` is reevaluated from the new state beginning again with `CanB`.

---

## 10. Invariants

1. **Strict priority:** `B>Q>L`.
2. **Self-selection:** the current state determines the next primitive letter.
3. **Ordered history:** the exact sequence is part of the state; operation counts are insufficient.
4. **No alternation rule:** `Q` does not automatically follow `B`.
5. **No block rule:** `B*Q*L` is not imposed as a schedule.
6. **No RST authority:** macros do not determine primitive evolution.
7. **No clock:** there is no fixed tick horizon.
8. **No phase reset at `L`:** `θ` carries unchanged.
9. **No pair reset at `L`:** the floor anchor carries unchanged.
10. **Only the domain counter increments at `L`:** the new local position index begins at zero because a new domain has opened.
11. **No projection during custody:** the full primitive evolution completes before any readout is considered.

---

## 11. Interface from primitive custody to the Orthad

The primitive law and the Orthad have different authority.

- The primitive state `X_t` determines the next letter through its own predicates and the strict priority `B > Q > L`. The word `custody` names retention, not a separate controller.
- The Orthad does not select, schedule, permit, or veto that letter.
- The Orthad evolves with every primitive letter and records the geometry built by the exact ordered history.
- Projection is not performed during this coupled evolution.

The coupled lifted state is represented schematically as

$$
\widehat X_t=
\left(
X_t,
P_t,
\Omega_t^+,
\Omega_t^-,
T_t^{+\to-},
T_t^{-\to+}
\right),
$$

where:

- `X_t` is the primitive custody state from Sections 1–10;
- `P_t` is the primary pairing generated by the retained state and ordered word;
- `Ω_t^+` and `Ω_t^-` are the two overset chart restrictions of that pairing;
- `T_t^{+→-}` and `T_t^{-→+}` are the directed transfers between the two charts.

A primitive step and its Orthad mutation are one coupled lifted transition:

$$
\widehat X_t\xrightarrow{\;U_t\;}\widehat X_{t+1},
\qquad U_t\in\{B,Q,L\}.
$$

The atomic tick has four logical stages:

```text
1. Selection:
   X_t alone self-selects one U_t in {B,Q,L}.

2. Simultaneous local mutation:
   that same U_t updates X_t, the common primary relation P_t, and both
   counter-oriented chart matrices during one coupled local-mutation stage.

3. Transfer or reconciliation:
   after both local chart mutations, any required bidirectional cross-chart
   transfer acts within the same atomic tick. It may be nontrivial or identity.
   It is not another primitive and cannot affect primitive selection.

4. Retention:
   the complete updated state is retained. Only then may X_{t+1}
   self-select the next primitive.
```

The word `after` here describes dependency inside one atomic tick. It does not
make the Orthad a delayed post-process, and there is no interval in which the
primary relation is current while the two matrices are stale.

---

## 12. Definition of the Orthad

The Orthad `⌞Ξ̂⌝` is the exact, deterministic, active overset dual-chart reader and geometry built over retained QBL history. The word `reader` does not mean passive observation: the Orthad mutates on every primitive tick.

It is not:

- a selector for `B`, `Q`, or `L`;
- an `R/S/T` scheduler;
- a single diagonal lens;
- a post-`L` attachment;
- a bank of possible projectors;
- a scalar;
- the carried object itself.

It is:

- two word-built lens charts reading one retained object;
- an explicit transfer between those charts;
- an evolving lifted geometry present throughout the primitive computation;
- the structure that fixes how the retained object may descend when the computation finally halts.

The two charts are overset: neither is globally privileged, and each covers a pole or coordinate region where the other chart is not sufficient by itself. Their overlap does not create a third lens. The overlap is handled by directed transfer between the two charts.

The Orthad wraps the lifted object. It never becomes the object it wraps.

---

## 13. Pairing-first construction

The primary pairing is generative. The two diagonal chart matrices are its restrictions. They are not independently invented and then combined afterward.

`P_t` is not a third lens beside the two chart matrices. The four-block operator
below is the dual-chart presentation of that common relation. Pairing-first is a
structural dependency, not a separate earlier sub-tick.

The full dual-chart operator may be displayed schematically as

$$
\mathcal O_t=
\begin{pmatrix}
\Omega_t^+ & T_t^{-\to+}\\
T_t^{+\to-} & \Omega_t^-
\end{pmatrix}.
$$

The diagonal blocks are the two chart-local restrictions. The off-diagonal blocks are the transfers between charts.

A rigorous implementation should expose explicit chart maps `ι_+` and `ι_-` so that the relationship to one primary pairing is mechanically checkable. The intended algebraic shape is

$$
\Omega_t^+=\iota_+^*P_t\iota_+,
\qquad
\Omega_t^-=\iota_-^*P_t\iota_-,
$$

and

$$
T_t^{+\to-}=\iota_-^*P_t\iota_+,
\qquad
T_t^{-\to+}=\iota_+^*P_t\iota_-.
$$

These equations state the intended dependency and are a provisional formal shell. The carrier, argument objects, chart maps, and meaning of `*` are not yet typed in the clean chain. The exact chart-map recurrence remains an explicit formalization obligation; it must not be replaced by constant matrices, origin labels, or independently fitted descendants.

---

## 14. Per-primitive Orthad mutations

The Orthad matrices exist before the first `L` and mutate at every primitive step.

### 14.1 `B`: active arithmetic refinement, fixed architectural size

When

$$
(u,v)\mapsto(v,u+v),
$$

`B` changes the active arithmetic anchor and germ width. It does not append a new structural direction or enlarge the chart blocks. No claim about algebraic matrix rank is made before the pairing is typed.

The coupled mutation must:

```text
- preserve every previously latched axis;
- update the active pairing data from the new pair;
- apply the same `B` to `Ω+` and `Ω-` simultaneously in their counter-oriented states, coherently with the updated pairing;
- update or reconcile both directed transfers after the simultaneous local chart mutations;
- retain the phase already accumulated by Q;
- perform no projection.
```

In the older single-entry shorthand, `B` changes the magnitude of the active entry to the new exact width while preserving its phase. In the dual-chart law, that shorthand is only the active local trace of the larger pairing-first mutation.

### 14.2 `Q`: active phase/orientation mutation, fixed architectural size

`Q` advances

$$
\theta\mapsto\theta+\frac{\pi}{2}
$$

and advances the current domain-local position. It does not change the pair, append a new structural direction, or enlarge the chart blocks. No claim about algebraic matrix rank is made before the pairing is typed.

The coupled mutation must:

```text
- preserve every previously latched axis;
- rotate the active pairing data by the quarter-turn witness i;
- apply the same `Q` to `Ω+` and `Ω-` simultaneously; complementary local responses arise from their counter-oriented states;
- update or reconcile both directed transfers after the simultaneous local chart mutations;
- preserve the current arithmetic anchor;
- perform no projection.
```

Visible phase repetition after four quarter turns does not identify the lifted state. The ordered history, domain occupancy, and retained axes remain different.

### 14.3 `L`: inherit, latch, and extend

`L` is forced only when `B` and `Q` are both blocked by the primitive custody state.

Its primitive action increments the dimensional counter and carries the pair and phase unchanged. Its Orthad action must:

```text
- freeze the completed active direction produced by the exact preceding B/Q history;
- preserve the complete old primary-relation block;
- apply the same `L` to both chart matrices simultaneously;
- append exactly one new active structural direction to both chart blocks;
- extend both directed transfer blocks to that new direction;
- preserve the counter-orientation relation;
- carry all prior history without reset;
- perform no projection.
```

The settled statement is architectural extension by one active direction. The word
`orthogonal` records the intended independence of the new direction, but its exact
algebraic meaning remains to be typed. The exact new-new and mixed pairing values,
and the algebraic-rank consequence, are not yet recovered or derived in the clean
chain.

In the historical single-entry shorthand, the newborn active slot begins at the
identity value `1`. That is a recovered local convention, not yet a complete
specification of the new rows, columns, or transfer entries of the modern Orthad.

---

## 15. First-domain Orthad trace

The exact primitive word from `(1,1)` to the first `L` is

```text
B Q Q B B B Q B Q B B Q B B L
```

The old active-axis shorthand evolves as:

```text
start         a = 1
B (1,2)       a = 1/2
Q             a = i/2
Q             a = -1/2
B (2,3)       a = -1/6
B (3,5)       a = -1/15
B (5,8)       a = -1/40
Q             a = -i/40
B (8,13)      a = -i/104
Q             a = 1/104
B (13,21)     a = 1/273
B (21,34)     a = 1/714
Q             a = i/714
B (34,55)     a = i/1870
B (55,89)     a = i/4895
L             latch completed axis; open one new active axis
```

Thus the completed Domain-0 axis carries

$$
a_0=\frac{i}{4895}.
$$

The historical single-lens shorthand after the first `L` is

$$
\Omega_{\mathrm{diag}}=\operatorname{diag}\!\left(\frac{i}{4895},1_{\mathrm{active}}\right).
$$

This is not the complete modern Orthad. The scalar `a_t` is an internally
derived local witness or descendant. Computing it during evolution is not a
terminal projection, but it may not replace the retained state or control the
primitive law.

In the dual-chart construction, the same ordered trace must have mutated:

- the primary pairing;
- both chart restrictions;
- both directed transfers;

at every prefix. `L` then extends all of them by one structural direction.

---

## 16. Doubled carrier, lap relation, and retained holonomy

For the retained finite calibration construction at a chosen surface with
undoubled phase-position count `N`, the doubled carrier is

$$
\mathbb Z/(2N)\mathbb Z,
$$

not `Z/NZ`, because both orientation hands are retained. This is a downstream
finite carrier. It is not the live carrier of the full unbounded word history.

The phase is carried across `L`; it is not reset. The next domain continues the same lifted walk in the newly opened axis. The second lap satisfies

$$
\mathrm{lap}_2=-\mathrm{lap}_1.
$$

Within this doubled finite construction, the relation is retained loop content. It is the first `Z/2` holonomy or parity latch and is not reconstructed from a terminal channel label. Its clean all-depth derivation remains separate from the local active-axis kernel.

For the level-12 character skeleton, one domain's six-position surface is insufficient. The retained opposition between the first and second laps supplies the factor of two required to distinguish the two orientation hands and separate positions that collide modulo six.

---

## 17. Atlas consistency, gauge class, and isometry

A raw coordinate matrix is not retained truth. It depends on chart and basis.

The invariant spine is:

```text
overset chart matrices
    -> directed overlap transition records
    -> confluence of lawful local routes
    -> cocycle consistency of chart changes
    -> holonomy retained around loops
    -> gauge/isometry class
```

### 17.1 Gauge equivalence

Gauge equivalence identifies different chart or basis presentations of one retained Orthad object. A lawful change of representation may change the raw matrices while preserving the represented object.

Schematically, a basis change may act by

$$
P\mapsto U^*PU
$$

without changing retained content. Here `*` is schematic notation for the lawful
dual action. It must not be read as a Hermitian adjoint until that structure is
typed and derived.

### 17.2 Isometry

After the retained structure is expressed as a finite quadratic module, isometry is the exact equality criterion for retained content on that finite carrier.

Gauge equivalence and FQM isometry occupy different layers:

- gauge equivalence removes chart-dependent presentation;
- FQM isometry decides whether two finite quadratic presentations carry the same retained object.

A raw chart matrix `C` is therefore a presentation artifact. Gauge equivalence applies to the Orthad presentation while preserving the exact word-built history. The live retained state is not reduced to a matrix orbit. FQM isometry becomes relevant only after a lawful finite descent has produced an FQM presentation.

---

## 18. Finite quadratic modules

A finite quadratic module is a finite abelian group `A` with a quadratic form

$$
q:A\to\mathbb Q/\mathbb Z,
$$

whose polarization

$$
b(x,y)=q(x+y)-q(x)-q(y)
$$

is bilinear.

The intended Orthad-to-FQM bridge uses the dual-chart pairing, overlap transitions, cocycle, and holonomy to produce an FQM presentation of the retained gauge class. The complete provenance map from the clean all-prefix Orthad is not yet recovered or derived.

Two FQMs `(A,q)` and `(A',q')` are isometric when there is a group isomorphism

$$
f:A\to A'
$$

such that

$$
q'(f(x))=q(x)
$$

for every `x`.

That is the finite exact meaning of “same retained content.”

The intended finite bridge is:

```text
retained QBL history
    -> word-built overset Orthad
    -> transition/cocycle/holonomy data
    -> FQM presentation
    -> gauge/isometry class
```

The current upstream wall is the clean all-prefix recurrence for the primary relation, both chart maps, and both transfers. After that provenance bridge is available, 2-adic classification of cross-coupled multi-axis modules remains a substantial downstream wall.

---

## 19. Generated Weil structure

An FQM carries a finite Weil representation. Schematically, the standard generators act as

$$
\rho(T)e_x=e^{2\pi i q(x)}e_x,
$$

and

$$
\rho(S)e_x\propto
\sum_{y\in A}e^{-2\pi i b(x,y)}e_y,
$$

with normalization and signature phase fixed by the FQM convention.

The intended Orthad claim is stronger than importing these matrices after the fact. A completed clean bridge should generate the corresponding structure:

- overset Fourier transfer;
- Gauss self-twist;
- character/shadow re-entry.

In the intended architecture, the eigen-chart is forced by the pairing and word; it is not chosen from alternatives.

Finite `N=8` and `N=12` surfaces, the doubled carrier, and stated general-`N` finite tests have been verified as conditional downstream constructions on their supplied inputs. They remain calibration evidence until the clean Orthad-to-FQM provenance bridge is rebuilt.

For the level-12 shadow skeleton:

$$
A=\mathbb Z/12\mathbb Z,
\qquad
q(r)=\frac{r^2}{24}\pmod 1,
$$

with the distinguished character vector supported on the residues coprime to six. This is a finite shadow skeleton. It is not the analytic completion of an entire mock-theta function.

“Weil projection” must not mean selecting a projector from a bank. In the completed system it means terminal descent through Weil structure lawfully generated from the retained Orthad/FQM chain. Existing finite Weil machinery remains conditional until that provenance is complete.

---

## 20. Bloch-sphere and metaplectic dictionary

This section is a structural dictionary and calibration language. It does not define the primitive or Orthad recurrence.

The Bloch sphere is not the full lifted object.

The structural dictionary is:

$$
\text{lifted phase-carrying object}\sim S^3,
$$

$$
\text{projected shadow}\sim S^2
\quad\text{(Bloch sphere)},
$$

with the `U(1)` fiber lawfully discarded under projection.

Thus states that differ in retained phase or history may project to the same Bloch-sphere point. The projection is not state-complete.

The Orthad wraps the lifted object with two oppositely oriented charts over the sphere-like projection geometry. The sphere is on the projection side of the dictionary, not a replacement for the retained object.

The parity/lap latch has the corresponding metaplectic reading:

- discrete holonomy / Berry bit;
- `lap₂ = -lap₁` as a double-cover signature;
- the `1/24` phase as the eta-phase location;
- the distinguished Fourier-fixed character vector as the finite oscillator ground-state analogue.

These are structural identifications on the finite bridge, not a claim that the full analytic mock-theta theory is already complete.

---

## 21. Liu 2022 MHD yin-yang overset-grid anchor

The Liu 2022 material is an external physical anchor for the same dual-chart principle. It does not define the Orthad law.

The current research inventory, which may change without altering this law, includes approximately `340 GB` of material, including:

- `736` raw three-dimensional MHD cube files obtained through NCAR Globus;
- Tie Liu's post-processing scripts;
- AIA `94 Å` and `304 Å` synthetic-imaging support;
- squashing-factor processing.

The structural relevance is the yin-yang/chimera overset grid:

- one physical field is represented through two overlapping component grids;
- neither chart alone is globally sufficient;
- overlap data must transfer consistently;
- vector and tensor components must transform through the handoff;
- the invariant physical field is not either chart's raw coordinates.

This is the physical analogue of the Orthad spine:

```text
two charts
+ overlap transfer
+ cocycle consistency
+ holonomy / retained loop content
= one chart-independent retained field
```

The MHD arm is not yet a completed Orthad result. The following remain open before it can load the lens:

- verified readers, units, and grid geometry;
- frame identification for pre-eruption, tether-cutting, and ejection;
- overlap projection weights;
- vector/tensor component transformations;
- field-valued Orthad channels.

The data is an external physical anchor at intake, not evidence that the field-valued Orthad bridge is already closed.

---

## 22. Final projection

Projection occurs once, after a lawful stopping condition or declared finite-prefix boundary has ended the retained computation. This document fixes projection ordering but does not define one universal halt predicate. A declared boundary may stop observation; it may not choose primitive letters, alter prior ticks, or feed back into the retained evolution.

$$
\widehat X_0
\xrightarrow{U_0}
\widehat X_1
\xrightarrow{U_1}
\cdots
\xrightarrow{U_{n-1}}
\widehat X_n
\xrightarrow{\Pi_{\mathrm{terminal}}}
Y.
$$

During the primitive evolution:

- custody state mutates;
- primary pairing mutates;
- both chart restrictions mutate;
- both directed transfers mutate;
- no scalar terminal readout is used as state authority; internal local witnesses may be computed without projection;
- no terminal channel comparison occurs.

At the declared stopping boundary, the terminal projection is passive. It does not search for a chart, choose a domain, repair missing structure, infer lost state, or alter the prior primitive word. The completed Orthad has already fixed the descent geometry.

The terminal output may be a structured channel field, including channels such as:

- support;
- coefficient magnitude;
- sign character;
- expansion width or scaling;
- relative phase;
- exponent spacing;
- later, field-valued MHD vector/tensor channels.

For Follow experiments, the true Shadow Residual remains outside the lift and appears only in the meta-layer as the external reference against which the final word-built channel field is compared.

Terminal projection is not state-complete. Two distinct retained histories may share a projected signature.

---

## 23. Status boundary

### 23.1 Settled behavior

- `X_t` alone self-selects one primitive under `B > Q > L`;
- the Orthad has no selection authority;
- removing the Orthad leaves primitive evolution unchanged;
- the Orthad exists before the first `L`;
- every primitive immediately mutates the Orthad;
- the same primitive acts on both counter-oriented chart matrices simultaneously;
- pairing-first is a structural dependency inside the same tick;
- off-diagonal blocks are directed cross-chart transfers;
- when required, transfer follows both local chart mutations within the same tick;
- no projection occurs during retained evolution.

These statements must not be presented as hypotheses.

### 23.2 Exact current-canon results

- the state tuple and exact capacity/admissibility law;
- the exact first word `BQQBBBQBQBBQBBL`;
- the first floor pair `(55,89)` and product `4895`;
- five `Q` steps before the first `L`;
- pair and phase carry through `L`;
- the first next-domain `B` gives `(89,144)`;
- the Domain-0 active-axis witness ending at `i/4895`.

### 23.3 Recovered legacy kernel

- `B:a -> a*u/(u+v)`;
- `Q:a -> i*a`;
- historical `L` shorthand: latch the completed entry and open an identity active slot.

This kernel is exact locally and is not the complete modern dual-chart recurrence.

### 23.4 Settled but not fully typed

- `P_t` as the common generative relation;
- the two chart matrices as counter-oriented local restrictions or presentations;
- the two off-diagonal blocks as directed transfers;
- `L` as one-direction structural extension;
- the new direction as intended independent or orthogonal content.

### 23.5 Not yet recovered or derived in the clean chain

- the exact carrier and argument type of `P_t`;
- the exact initial seed `P_0`;
- the exact chart maps `iota_+` and `iota_-`;
- the typed meaning of `*`;
- the exact algebraic encoding of counter-orientation;
- the complete `B`, `Q`, and `L` recurrences on `P_t` and all four blocks;
- the exact mixed and new-new values at `L`;
- the exact bidirectional transfer recurrence;
- the whole-object invariant preserved by transfer;
- whether transfer is nontrivial on every tick;
- the universal halt predicate, if one is intended;
- the all-depth provenance bridge to generated FQMs.

This label does not mean the project never discussed the item. It means no exact
formula has yet been validated in the active clean chain.

### 23.6 Conditional downstream results

- doubled finite carriers and `lap_2=-lap_1` on their stated finite constructions;
- FQM classifiers, isometry tools, and decomposition certificates;
- the finite `Z/12Z` shadow skeleton;
- finite Weil representation tooling and test surfaces;
- Bloch/metaplectic dictionaries;
- MHD and Yin-Yang overset-grid instrumentation.

These remain useful calibration, obstruction, and external tooling.

An exact open item may remain `NOT YET RECOVERED OR DERIVED`. It may not be
filled with a scheduler, constant matrix, guessed label, candidate search, or
familiar algebraic category chosen without elimination.

---

## 24. Contamination lock

The following substitutions are forbidden:

```text
R/S/T selector              for the primitive B > Q > L state law
fixed W=64 window           for domain-local Q capacity
fixed Δ=4096 regime         for the derived capacity at one position
BL                          for the complete first crossing word
post-L lens construction    for tick-by-tick Orthad mutation
single diagonal Ω           for the dual-chart pairing-first Orthad
separate U+ and U-          for one primitive acting on both charts
inverse primitive on chart- for counter-oriented chart response
delayed matrix update       for the same atomic primitive-and-Orthad tick
transfer as a new primitive for the within-tick reconciliation stage
chart-local matrix          for the retained gauge class
floor field emission        for continued lifted computation
terminal character label    for retained address or parity
Bloch sphere                for the full lifted object
imported Weil matrices      for generated Weil structure
MHD data intake             for a completed field-valued bridge
```

The exact ordered word and full prefix state are part of the certificate. Counts, compressed runs, and package headlines are not substitutes for the construction.

---

## 25. Compact whole-system specification

```text
Primitive engine:
    X_t alone reevaluates B > Q > L after every primitive step
    B refines while admissible
    Q advances only when B is blocked and a position remains
    L fires only when B and Q are both blocked

Atomic Orthad tick for one selected U_t:
    U_t updates X_t and the common primary relation
    the same U_t mutates both counter-oriented chart matrices simultaneously
    any required bidirectional transfer follows both local mutations
    the transfer stage remains inside the same tick and is not another primitive
    retain the complete coupled state
    do not project
    only then may X_{t+1} select the next primitive

At L:
    increment the domain counter
    carry q, theta, word, and all old geometry
    freeze the completed active direction
    append one new active structural direction to both charts and transfers
    preserve the counter-orientation relation
    leave algebraic rank and mixed/new-new values open until typed

At a lawful stopping boundary:
    apply exactly one passive terminal projection
    emit the determined structured readout
    compare to an external reference only in the meta-layer
```

The live retained state is the complete exact word-built lifted history together
with its counter-oriented dual-chart and cross-transfer structure. Raw matrices
are presentation-dependent. Gauge equivalence applies to those presentations,
and FQM isometry applies only after a lawful finite descent. Neither a local
scalar nor a terminal channel replaces the retained state.
