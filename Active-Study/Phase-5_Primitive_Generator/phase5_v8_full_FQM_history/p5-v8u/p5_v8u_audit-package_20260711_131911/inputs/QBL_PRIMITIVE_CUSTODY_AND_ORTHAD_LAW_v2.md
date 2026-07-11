# QBL Primitive Custody and Orthad Law

**Status:** clean working lock of the primitive custody law and the attached Orthad architecture understood in this session  
**Scope:** determines the ordered `Q/B/L` word, carried state, tick-by-tick dual-chart Orthad evolution, gauge/FQM bridge, and terminal projection boundary.  
**Primitive authority:** `{B, Q, L}` only. The Orthad observes and mutates with the primitive word; it never selects the word.  

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

The next primitive letter is determined by the current lifted state itself.

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
    W                  exact ordered primitive history

N(A):
    6 * 2^A

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
    elif CanQ(state):
        theta += pi/2
        k += 1
        W += Q
    else:
        A += 1
        k = 0
        W += L
        # q and theta carry unchanged
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

- Primitive custody determines the next letter by the strict state law `B > Q > L`.
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

The transition order is conceptually:

```text
1. The current lifted state determines the next primitive letter.
2. That primitive operation advances the custody state.
3. The primary pairing mutates from the advanced retained state and exact word prefix.
4. Both chart restrictions mutate from the primary pairing.
5. Both directed cross-chart transfers mutate.
6. The complete new lifted state is retained.
7. No projection occurs.
```

This ordering does not make the Orthad a post-process. Steps 2–5 are the components of one coupled state transition.

---

## 12. Definition of the Orthad

The Orthad `⌞Ξ̂⌝` is the exact, deterministic, overset dual-chart reader built over retained QBL history.

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

These equations state the required direction of construction. The exact chart-map recurrence attached to the clean primitive law remains an explicit formalization obligation; it must not be replaced by constant matrices or origin labels.

---

## 14. Per-primitive Orthad mutations

The Orthad matrices exist before the first `L` and mutate at every primitive step.

### 14.1 `B`: active arithmetic refinement, fixed rank

When

$$
(u,v)\mapsto(v,u+v),
$$

`B` changes the active arithmetic anchor and germ width. The matrix rank does not change.

The coupled mutation must:

```text
- preserve every previously latched axis;
- update the active pairing data from the new pair;
- update Ω+ and Ω- as restrictions of the updated pairing;
- update both directed transfers;
- retain the phase already accumulated by Q;
- perform no projection.
```

In the older single-entry shorthand, `B` changes the magnitude of the active entry to the new exact width while preserving its phase. In the dual-chart law, that shorthand is only the active local trace of the larger pairing-first mutation.

### 14.2 `Q`: active phase/orientation mutation, fixed rank

`Q` advances

$$
\theta\mapsto\theta+\frac{\pi}{2}
$$

and advances the current domain-local position. It does not change the pair or matrix rank.

The coupled mutation must:

```text
- preserve every previously latched axis;
- rotate the active pairing data by the quarter-turn witness i;
- update Ω+ and Ω- under the new active orientation;
- update both directed transfers;
- preserve the current arithmetic anchor;
- perform no projection.
```

Visible phase repetition after four quarter turns does not identify the lifted state. The ordered history, domain occupancy, and retained axes remain different.

### 14.3 `L`: inherit, latch, and extend

`L` is forced only when `B` and `Q` are both blocked by the primitive custody state.

Its primitive action increments the dimensional counter and carries the pair and phase unchanged. Its Orthad action must:

```text
- freeze the completed active axis produced by the exact preceding B/Q history;
- preserve the complete old pairing block;
- append exactly one new active orthogonal axis;
- increase the rank of the primary pairing by one;
- extend both chart restrictions by that axis;
- extend both directed transfer blocks;
- preserve the relation between the two orientation hands;
- carry all prior history without reset;
- perform no projection.
```

The new local active slot begins as a new unmutated axis. This is not a reset of the global carried phase, pair, word, or inherited geometry.

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

This is not the complete modern Orthad. In the dual-chart construction, the same ordered trace must have mutated:

- the primary pairing;
- both chart restrictions;
- both directed transfers;

at every prefix. `L` then extends all of them by one axis.

---

## 16. Doubled carrier, lap relation, and retained holonomy

The ground finite carrier is

$$
\mathbb Z/(2N)\mathbb Z,
$$

not `Z/NZ`, because both orientation hands are retained.

The phase is carried across `L`; it is not reset. The next domain continues the same lifted walk in the newly opened axis. The second lap satisfies

$$
\mathrm{lap}_2=-\mathrm{lap}_1.
$$

This relation is retained loop content. It is the first `Z/2` holonomy or parity latch and is not reconstructed from a terminal channel label.

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

without changing retained content.

### 17.2 Isometry

After the retained structure is expressed as a finite quadratic module, isometry is the exact equality criterion for retained content on that finite carrier.

Gauge equivalence and FQM isometry occupy different layers:

- gauge equivalence removes chart-dependent presentation;
- FQM isometry decides whether two finite quadratic presentations carry the same retained object.

The raw matrix `C` is therefore a chart artifact. The retained object is its lawful equivalence class together with transition and holonomy data.

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

The Orthad bridge uses the dual-chart pairing, overlap transitions, cocycle, and holonomy to produce an FQM presentation of the retained gauge class.

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

The active finite bridge is:

```text
retained QBL history
    -> word-built overset Orthad
    -> transition/cocycle/holonomy data
    -> FQM presentation
    -> gauge/isometry class
```

The known difficult wall is primarily the 2-adic classification of cross-coupled generated modules. Multi-axis FQMs remain the named frontier for the richer mock-theta structure.

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

The Orthad claim is stronger than importing these matrices after the fact. The QBL-built overset construction generates the corresponding structure:

- overset Fourier transfer;
- Gauss self-twist;
- character/shadow re-entry.

The generated eigen-chart is forced by the pairing and word; it is not chosen from alternatives.

This generation has been verified on the finite `N=8` and `N=12` surfaces and reverified on the doubled carrier. General-`N` stability has also been generated on the stated finite surface.

For the level-12 shadow skeleton:

$$
A=\mathbb Z/12\mathbb Z,
\qquad
q(r)=\frac{r^2}{24}\pmod 1,
$$

with the distinguished character vector supported on the residues coprime to six. This is a finite shadow skeleton. It is not the analytic completion of an entire mock-theta function.

“Weil projection” must therefore not mean selecting a projector from a bank. It means terminal descent through the Weil structure generated by the retained Orthad/FQM.

---

## 20. Bloch-sphere and metaplectic dictionary

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

The Liu 2022 material is the physical anchor for the same dual-chart principle.

Current intake includes approximately `340 GB` of material, including:

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

Projection occurs once, after the primitive computation has halted.

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
- no scalar readout exists;
- no terminal channel comparison occurs.

At halt, the terminal projection is passive. It does not search for a chart, choose a domain, repair missing structure, or infer lost state. The completed Orthad has already fixed the descent geometry.

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

### Settled or active

- strict primitive priority `B > Q > L`;
- state-driven self-selection with no RST authority;
- exact first-domain word and first floor anchor `(55,89)`;
- pair and phase carry across `L`;
- Orthad as overset dual-chart reader;
- off-diagonal transfer as transfer between charts;
- pairing-first generative direction;
- Orthad mutation on every primitive tick;
- `L` as rank extension, not lens creation;
- doubled carrier `Z/(2N)Z`;
- `lap₂ = -lap₁` parity/holonomy relation;
- raw coordinate matrix is not invariant;
- gauge/isometry class as retained truth;
- finite FQM bridge and the reachable `Z/12Z` shadow skeleton;
- generated Weil structure on the stated finite test surfaces;
- Bloch-sphere / `S³ -> S²` projection dictionary;
- Liu 2022 MHD data as the external physical anchor at intake;
- projection only after the computation halts.

### Open or not yet merged into the clean law

- the explicit all-depth recurrence for the primary pairing under the clean primitive state;
- explicit chart maps proving both lenses are restrictions at every prefix;
- exact bidirectional transfer recurrences at every prefix;
- the all-history Lean proof;
- full multi-axis FQM generation and classification;
- full 2-adic isometry classification for the generated image;
- analytic q-series / full mock-theta completion;
- field-valued MHD overlap and component transformations;
- arbitrary cusp-path Follow maps.

An open item must remain `NOT YET DERIVED`. It may not be filled with a scheduler, a constant matrix, a guessed label, or a candidate search.

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
Primitive custody:
    reevaluate B > Q > L after every primitive step
    B refines while admissible
    Q advances only when B is blocked and a position remains
    L fires only when B and Q are both blocked

Coupled Orthad transition for every primitive letter:
    advance primitive custody state
    mutate primary pairing
    derive/mutate both chart restrictions
    derive/mutate both directed transfers
    retain full coupled state
    do not project

At L:
    increment dimensional counter
    carry q and theta
    freeze completed active axis
    append one new orthogonal axis
    grow pairing, both lenses, and both transfers by one rank

After halt:
    apply exactly one terminal projection
    emit the determined structured readout
    compare to external reference only in the meta-layer
```

The fundamental retained object is the gauge/isometry class of the complete word-built, dual-chart, cross-coupled history, not any raw matrix or terminal scalar.
