# QBL Primitive Custody Law

**Status:** clean working lock of the primitive evolution understood in this session  
**Scope:** determines the ordered `Q/B/L` word and the carried state. It deliberately stops before Orthad lens mechanics or terminal readout.  
**Primitive authority:** `{B, Q, L}` only.  

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

## 11. Boundary of this document

This document fixes only:

- how the next primitive letter is determined;
- how `B`, `Q`, and `L` update custody state;
- how the first domain reaches `(55,89)`;
- why the first `L` is forced;
- how the state enters the next domain.

It intentionally does **not** yet specify:

- the Orthad pairing;
- the two overset chart matrices;
- cross-chart transfer;
- per-tick Orthad matrix mutation;
- the carried channel field;
- terminal projection or readout.

Those structures must be attached to this primitive custody law without changing it.
