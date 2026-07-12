# Canonical Research Trunk

**Revision:** v6 comprehensive lock  
**Status:** current working semantic and research intake  
**Primary written authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Supersedes:** trunk revisions v3, v4, and v5  
**Purpose:** Give a zero-context researcher one complete statement of the current primitive engine, lifted object, Orthad, same-tick dual-matrix law, pairing-first dependency, transfer timing, projection boundary, historical lineage, salvage boundary, and unresolved mathematical obligations.

---

## 0. Authority, evidence classes, and conflict handling

### 0.1 Authority order

Use this order when sources differ:

1. The user's direct ratification of intended behavior.
2. `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`.
3. This comprehensive trunk, which resolves later clarifications against that authority.
4. Results exactly reproduced under the current `B > Q > L` law.
5. Older Phase Calculus and Orthad archives.
6. External inspiration papers and analogies.

A later summary does not override an earlier primary authority merely because it is newer.

A historical result may remain useful even when its original interpretation is obsolete. Separate internal mathematical validity from current Orthad provenance.

### 0.2 Evidence classes

Every claim belongs to one of these classes.

```text
USER-RATIFIED INTENT
    The user's direct statement of what the system is supposed to do.

CURRENT-CANON RESULT
    A result derived or exactly reproduced under the current primitive law.

RECOVERED LEGACY KERNEL
    An older exact construction whose local mathematics survives after obsolete
    grammar and interpretation are removed.

PROVISIONAL FORMALIZATION
    A mathematical form that may realize the intent but is not yet fully typed
    or derived.

CONDITIONAL DOWNSTREAM RESULT
    Correct mathematics on supplied downstream objects, without a complete
    provenance bridge from the clean Orthad.

INSPIRATION OR CALIBRATION
    External mathematics or older Phase Calculus work that supplies geometry,
    tests, constraints, or tools without defining the Orthad.

SUPERSEDED OR FALSE
    A claim contradicted by later evidence or incompatible with current canon.
```

### 0.3 Conflict rule

When formal terminology conflicts with the ratified behavior, preserve the behavior and reopen the formalization.

Do not reopen a ratified behavior merely because its current mathematical realization remains incomplete.

---

## 1. Cold-start semantic lock

The following block is the shortest complete semantic lock. Future agents should quote it rather than paraphrase it.

```text
The primitive state X_t is autonomous.

X_t alone self-selects exactly one primitive U_t in {B,Q,L} through its own
current predicates and the strict priority B > Q > L.

The Orthad does not select, permit, block, veto, schedule, or alter U_t.
Removing the Orthad leaves the primitive evolution unchanged.

Every primitive step is immediately also an Orthad step.

The same selected primitive U_t mutates both opposed Orthad chart matrices
simultaneously. There are not separate U_t+ and U_t- primitive operators.

The two chart results may differ because the chart states are already
counter-oriented. The difference comes from the states and frames on which
the same operator acts, not from replacing, splitting, reversing, or
independently choosing the primitive.

After the simultaneous chart-local mutation, any required bidirectional
cross-chart transfer or reconciliation occurs within that same atomic tick.

The complete updated primitive state, primary relation, two chart matrices,
and two directed transfers are retained before X_{t+1} self-selects the next
primitive.

Pairing-first is a generative dependency inside the tick. It is not a delayed
pipeline in which a pairing changes now and the matrices catch up later.

No projection, terminal readout, candidate comparison, or external-reference
matching occurs during retained evolution.
```

This block is settled. It is not an experimental question.

---

## 2. Layer and vocabulary boundaries

### 2.1 Primitive state

\[
X_t=(A_t,q_t,\theta_t,k_t,j_t,W_t),
\qquad q_t=(u_t,v_t),\quad 1\le u_t\le v_t.
\]

`X_t` contains the state needed for autonomous primitive evolution.

The word **custody** means that this state carries and preserves the exact evolution. It does not name a separate controller.

### 2.2 Fully retained lifted state

The coupled retained state is represented schematically as

\[
\widehat X_t=
\left(
X_t,
P_t,
\Omega_t^+,
\Omega_t^-,
T_t^{+\to-},
T_t^{-\to+}
\right).
\]

The notation is schematic until all carriers and maps are typed.

### 2.3 Orthad

The Orthad is the deterministic, word-built, dual-chart reader and geometry wrapping the lifted object.

It is not:

```text
the primitive state
the lifted object itself
a primitive selector
a scheduler
a single diagonal matrix
a post-L attachment
a scalar
a bank of terminal projectors
a terminal classifier
```

It is:

```text
two opposed, overset chart matrices;
two directed cross-chart transfer blocks;
one common primary relation represented through those blocks;
an evolving geometry present at every exact B/Q/L prefix;
the structure that constrains lawful terminal descent.
```

Removing the Orthad does not stop `X_t`. It removes the intrinsic dual-chart descent geometry and forces applications to rebuild filters, projectors, branch registers, and recovery rules manually.

### 2.4 Primary relation or pairing

`P_t` is the common generative relation underlying the two chart-local blocks and both cross-chart blocks.

Pairing-first means:

```text
the four visible blocks are not independently invented;
their agreement must come from one common retained relation;
the common relation is generatively prior as structure;
all components still mutate within one atomic primitive tick.
```

`P_t` is not a third lens beside the two matrices. The full block operator is a dual-chart presentation of the common relation:

\[
\mathcal O_t=
\begin{pmatrix}
\Omega_t^+ & T_t^{-\to+}\\
T_t^{+\to-} & \Omega_t^-
\end{pmatrix}.
\]

The intended restriction form is

\[
\Omega_t^+=\iota_{+,t}^{*}P_t\iota_{+,t},
\qquad
\Omega_t^-=\iota_{-,t}^{*}P_t\iota_{-,t},
\]

\[
T_t^{+\to-}=\iota_{-,t}^{*}P_t\iota_{+,t},
\qquad
T_t^{-\to+}=\iota_{+,t}^{*}P_t\iota_{-,t}.
\]

These equations state the intended dependency. They do not yet type the star, carrier, argument objects, chart maps, or recurrence.

### 2.5 Opposed or counter-oriented

The two chart matrices coexist and face in complementary orientations.

The settled geometric reading is:

> Apply the same world operation to two local frames that face opposite ways.

The primitive is one operation. Complementary local results arise because the two retained chart states and frames differ.

“Opposite” does not yet prove any one formula such as

```text
Omega- = -Omega+
Omega- = inverse(Omega+)
Omega- = transpose(Omega+)
Omega- = adjoint(Omega+)
Omega- = conjugate(Omega+)
Omega- = a fixed rotation of Omega+
Omega- = a dual object
```

Any of these may be tested only as a proposed realization of the already settled counter-orientation.

### 2.6 Rank and axis

Before the pairing is fully typed, distinguish:

```text
architectural axis count or block size
algebraic matrix rank
nondegenerate rank
module rank
pairing rank
```

At `L`, one new active direction is appended structurally. This does not by itself prove that the algebraic rank of an eventual matrix or pairing rises by one.

When older documents say “rank extension” before typing the pairing, read it as architectural axis or block extension unless an algebraic-rank proof is supplied.

---

## 3. Exact primitive engine

### 3.1 State coordinates

- `A` is the current domain or dimensional counter.
- `q=(u,v)` is the carried balanced-refinement pair.
- `theta` is the carried phase.
- `k` is the zero-based phase-position index inside the current domain.
- `j` is the one-based global phase-position index.
- `W` is the exact ordered primitive word already executed.

The exact word is retained state. Operation counts do not replace it.

### 3.2 Available phase positions

\[
N_A=6\cdot 2^A.
\]

Thus

\[
N_0=6,\qquad N_1=12,\qquad N_2=24,\ldots
\]

The first global position in domain `A` is

\[
j_{\mathrm{start}}(A)=1+6(2^A-1),
\]

and

\[
j=j_{\mathrm{start}}(A)+k.
\]

`j` counts available phase positions. It is not the number of emitted `Q` letters.

### 3.3 Capacity law

\[
\Delta(j)=
\begin{cases}
2, & j=1,\\
4, & j=2,\\
2^{2j}, & j\ge 3.
\end{cases}
\]

Domain 0 therefore has capacities

\[
2,\ 4,\ 64,\ 256,\ 1024,\ 4096.
\]

Domain 1 begins at `j=7`, with

\[
\Delta(7)=16384.
\]

### 3.4 Primitive `B`

\[
B(u,v)=\operatorname{sort}(v,u+v).
\]

For `u<=v`:

\[
(u,v)\mapsto(v,u+v).
\]

`B` changes the pair and refinement scale. It does not change `A`, `k`, or `theta`.

At a nonterminal position, `B` is admissible when the next pair remains within capacity:

\[
(u',v')=B(u,v),
\qquad
u'v'\le\Delta(j).
\]

At the final position, the boundary-crossing `B` is admitted while the current pair remains below capacity:

\[
uv<\Delta(j).
\]

The first produced pair at or beyond the final capacity is the floor anchor. It is not selected externally.

### 3.5 Primitive `Q`

\[
\theta\mapsto\theta+\frac{\pi}{2},
\qquad
k\mapsto k+1.
\]

`Q` leaves `q` and `A` unchanged.

`Q` is admissible exactly when

\[
k<N_A-1.
\]

The initial position `k=0` counts as one available position. Domain 0 therefore emits at most five actual `Q` letters.

Visible phase repetition does not block `Q`. The exact retained state distinguishes repeated projections.

### 3.6 Primitive `L`

`L` fires only when `B` is blocked and no `Q` position remains.

Its primitive action is

\[
A\mapsto A+1.
\]

It carries:

```text
q unchanged
theta unchanged
the exact word and all retained history
all previously accumulated geometry
```

It sets the new domain-local index to `k=0`.

`L` does not add a quarter turn. It does not reset the pair or phase.

### 3.7 Strict priority and self-selection

\[
B>Q>L.
\]

After every primitive step, the current `X_t` reevaluates the predicates from `B` first.

```text
if B is admissible:
    execute one B
elif Q is admissible:
    execute one Q
else:
    execute L
```

There is no macro selector, fixed word, fixed cadence, timer, or external choice.

### 3.8 Exact first-domain trace

Initial state:

\[
A=0,\qquad q=(1,1),\qquad k=0.
\]

Exact word:

```text
B Q Q B B B Q B Q B B Q B B L
```

| Step | `k` | Capacity | Primitive and result |
|---:|---:|---:|---|
| 0 | 0 | 2 | Start `(1,1)` |
| 1 | 0 | 2 | `B: (1,1)->(1,2)` |
| 2 | 1 | 4 | `Q` |
| 3 | 2 | 64 | `Q` |
| 4 | 2 | 64 | `B: (1,2)->(2,3)` |
| 5 | 2 | 64 | `B: (2,3)->(3,5)` |
| 6 | 2 | 64 | `B: (3,5)->(5,8)` |
| 7 | 3 | 256 | `Q` |
| 8 | 3 | 256 | `B: (5,8)->(8,13)` |
| 9 | 4 | 1024 | `Q` |
| 10 | 4 | 1024 | `B: (8,13)->(13,21)` |
| 11 | 4 | 1024 | `B: (13,21)->(21,34)` |
| 12 | 5 | 4096 | `Q` |
| 13 | 5 | 4096 | `B: (21,34)->(34,55)` |
| 14 | 5 | 4096 | `B: (34,55)->(55,89)` |
| 15 | 5 | 4096 | `L` |

Therefore

\[
q_{\mathrm{floor},0}=(55,89),
\qquad
55\cdot89=4895.
\]

Five `Q` letters occur. `L` adds no phase.

After `L`:

\[
A=1,\quad q=(55,89),\quad k=0,\quad N_1=12.
\]

The first new-domain step is

\[
(55,89)\xrightarrow{B}(89,144),
\qquad
89\cdot144=12816<16384.
\]

---

## 4. One atomic primitive-and-Orthad tick

### 4.1 Selection stage

The next primitive is determined only from `X_t`:

\[
U_t=\Sigma(X_t),
\qquad U_t\in\{B,Q,L\}.
\]

`Sigma` is notation for the primitive predicates. It is not a separate selecting object.

### 4.2 Local mutation stage

The selected `U_t` immediately updates the primitive state and the common Orthad relation.

In the dual-chart presentation, that same `U_t` acts on both diagonal chart matrices simultaneously:

\[
(\widetilde\Omega_{t+1}^+,\widetilde\Omega_{t+1}^-)
=
U_t\cdot(\Omega_t^+,\Omega_t^-).
\]

The tilde marks the post-local-mutation, pre-transfer chart state.

This equation does not introduce separate chart primitives. It states one operator acting on a pair of counter-oriented states.

Pairing-first is structural here. The update of `P_t` and the two local chart mutations are one coupled event. There is no temporal interval in which the pairing is updated but the matrices remain stale.

### 4.3 Transfer and reconciliation stage

After both local chart mutations, any required bidirectional overlap transfer or reconciliation occurs:

\[
(\Omega_{t+1}^+,\Omega_{t+1}^-,
T_{t+1}^{+\to-},T_{t+1}^{-\to+})
=
\mathcal R_{U_t}
\left(
P_{t+1},
\widetilde\Omega_{t+1}^+,
\widetilde\Omega_{t+1}^-,
W_{t+1}
\right).
\]

This is a formal shell, not the derived recurrence.

The transfer stage:

```text
is inside the same atomic Orthad tick;
occurs after the simultaneous chart-local mutation;
is not another primitive;
does not alter primitive selection;
may be nontrivial or identity on a given tick;
must remain bidirectional and orientation-aware.
```

Whether every tick requires a nontrivial handoff remains open.

### 4.4 Retention stage

The complete updated state is retained:

\[
\widehat X_{t+1}=
\left(
X_{t+1},
P_{t+1},
\Omega_{t+1}^+,
\Omega_{t+1}^-,
T_{t+1}^{+\to-},
T_{t+1}^{-\to+}
\right).
\]

Only then does `X_{t+1}` self-select the next primitive.

### 4.5 Forbidden tick interpretations

The tick is not:

```text
primitive steps first, matrix updates later
one primitive for the + chart and another for the - chart
U on one chart and inverse(U) on the other
one chart undoing the other
a J/M split of the primitive into two independent actions
a terminal comparison followed by repair
a transfer stage that selects or vetoes the next primitive
```

A chart-coordinate transformation may be needed to express transferred components in the receiving frame. That bookkeeping does not change which primitive acted.

---

## 5. Pairing-first and the active dual-matrix realization

The following are both settled and must be held together:

```text
PAIRING-FIRST
    One common retained relation non-vacuously generates or constrains the two
    chart-local blocks and both cross-chart blocks.

SAME-OPERATOR DUAL-MATRIX MUTATION
    One selected B, Q, or L acts on both counter-oriented chart matrices
    simultaneously during the local mutation stage.
```

Neither statement cancels the other.

Pairing-first does not license a delay.

Same-operator mutation does not license independent chart fitting.

The complete block presentation

\[
\mathcal O_t=
\begin{pmatrix}
\Omega_t^+ & T_t^{-\to+}\\
T_t^{+\to-} & \Omega_t^-
\end{pmatrix}
\]

is the visible dual-chart presentation of the common relation. The off-diagonal blocks are the directed transfers across the charts.

The primary relation is not selected from a bank. It must be forced by the retained state and exact word.

---

## 6. Per-primitive Orthad behavior

### 6.1 Recovered active-axis kernel

An older exact local kernel survives the obsolete macro grammar:

\[
a_t=\frac{i^{\#Q(W_t)}}{u_tv_t}
\]

on the first-domain active axis.

Its exact local updates are

\[
B:a\mapsto a\frac{u}{u+v},
\qquad
Q:a\mapsto ia.
\]

At `L`, the completed value is latched and a new active slot opens at the identity value in the historical shorthand.

This is a recovered local mutation kernel. It is not the complete modern Orthad.

### 6.2 `B`: active arithmetic refinement

Primitive action:

\[
(u,v)\mapsto(v,u+v).
\]

Required Orthad behavior in the same tick:

```text
preserve all previously latched directions;
update the active common relation from the new pair;
apply the same B to both counter-oriented chart matrices simultaneously;
preserve accumulated Q phase;
update or reconcile both directed transfers after the local mutations;
perform no projection.
```

The local active-axis witness changes by

\[
a\mapsto a\frac{u}{u+v}.
\]

The exact full-matrix `B` recurrence remains to be recovered or derived.

### 6.3 `Q`: active phase and orientation advance

Primitive action:

\[
\theta\mapsto\theta+\frac{\pi}{2},
\qquad
k\mapsto k+1.
\]

Required Orthad behavior:

```text
preserve the pair and every latched direction;
rotate the active common relation by the quarter-turn content;
apply the same Q to both counter-oriented chart matrices simultaneously;
allow complementary local results to arise from their opposite frames;
update or reconcile both directed transfers after the local mutations;
perform no projection.
```

The local witness changes by

\[
a\mapsto ia.
\]

The second chart does not receive a different primitive such as `Q^{-1}`. Any opposite-looking coordinate response arises from the chart state and orientation.

### 6.4 `L`: inherit, latch, and extend

`L` is forced only when `B` and `Q` are both blocked.

Primitive action:

```text
A increases by one;
q carries unchanged;
theta carries unchanged;
k restarts at zero in the new domain;
the exact word and all history carry.
```

Required Orthad behavior:

```text
freeze the completed active direction;
preserve the complete old common-relation block;
apply the same L to both chart matrices simultaneously;
append exactly one new active structural direction to both charts;
extend both directed transfer blocks to the new direction;
preserve the counter-orientation relation;
open the newborn local active slot unmutated;
perform no projection.
```

The settled claim is structural extension by one active direction.

The exact new-new and mixed values, and the exact algebraic rank consequence, remain open until the pairing is typed.

---

## 7. Exact first-domain active-axis witness

Along the exact first word:

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
L             latch completed direction; open a new active direction
```

Thus

\[
a_{\mathrm{completed},0}=\frac{i}{4895}.
\]

The historical single-lens shorthand after the first `L` is

\[
\operatorname{diag}\left(\frac{i}{4895},1_{\mathrm{active}}\right).
\]

This shorthand is not the complete modern Orthad.

It must not be promoted without proof to:

```text
the complete primary relation
a Hermitian diagonal self-pairing
both dual-chart diagonal blocks
a transfer value
a global all-domain formula
the complete retained object
```

---

## 8. Overlap and directed transfer

Neither chart is globally sufficient by itself.

The transfer blocks are active state components. They are not:

```text
terminal comparison functions
repairs after the evolution
a third chart
a second primitive
a selector
independently fitted target values
```

A lawful transfer must:

```text
use the post-local-mutation chart states;
re-express transferred data in the receiving orientation;
remain bidirectional;
depend on the exact retained word and state;
remain non-vacuously tied to the common primary relation;
preserve the relevant whole-object content or invariant;
complete before the next primitive is selected;
avoid projection.
```

The exact transfer recurrence is open.

The exact invariant preserved across transfer is also open.

A transfer may be the identity when no nontrivial overlap handoff is required. That possibility does not remove the transfer blocks from retained state.

---

## 9. What the inspiration papers license

### 9.1 Yin-Yang and Chimera overset grids

They support:

```text
two complementary local grids covering one global field;
the same physical evolution law on both grids;
opposed local coordinate frames;
transformed, not merely copied, cross-grid components;
bidirectional overlap handoff;
possible involutive or reversible chart change;
the need for global conservation beyond local interpolation agreement.
```

This is the strongest external analogue for:

```text
the same B/Q/L acting on both charts;
counter-oriented local results;
cross transfer after local updates;
one chart-independent retained object.
```

They do not prove the exact QBL opposition map, transfer recurrence, or pairing type.

### 9.2 MHD and polarity

MHD is useful because vector and tensor components, flux orientation, and divergence constraints make cross-grid handoff nontrivial.

Keep these distinct:

```text
chart orientation:
    how the same field or mutation is expressed in a local frame

physical polarity:
    intrinsic signed or opposed content carried by the field

inverse primitive:
    a different claim that is not licensed by chart opposition
```

MHD polarity does not by itself prove that one Orthad chart receives the inverse primitive.

### 9.3 Metriplectic `J/M` analogy

The `J/M` split is licensed only as an analogy for complementarity without cancellation.

It does not license:

```text
splitting one B/Q/L into two primitive operators;
assigning B to one chart and another action to the other;
one chart undoing the other;
replacing the same-operator law.
```

### 9.4 Cech, sheaf, and cocycle language

These provide provisional languages for:

```text
local data on overlapping regions;
restriction or placement maps;
compatibility on overlaps;
global content assembled from coherent local data;
cocycle failure as an obstruction.
```

They do not determine the primitive update law.

### 9.5 Homotopy lifting

This supports the distinction between a visible return and a distinct retained lifted path. It does not define the matrices.

### 9.6 Asynchronous automata and trace monoids

These support one shared action updating multiple local states and the load-bearing role of exact word order. They do not define the Orthad geometry.

### 9.7 Inspiration-source disposition

| Source family | Salvaged role | Boundary |
|---|---|---|
| Axis-free Yin-Yang overset grids | Counter-oriented dual-grid geometry, reversible coordinate change, vector transfer | Numerical analogue, not QBL law |
| Conservative overlap schemes | Global invariant constraints across handoff | Preserved Orthad invariant not yet identified |
| MHD Yin-Yang simulations | Field-valued transfer, polarity, flux and divergence pressure | Physical analogue, not proof of inverse primitive action |
| Sheaves and Cech cohomology | Overlap consistency and obstruction language | No primitive dynamics |
| Homotopy lifting | Retained path versus projected return | No matrix recurrence |
| Asynchronous automata | One shared action updating local states | No geometry |
| Trace monoids | Exact word and partial-commutation tools | Supplemental only |
| FQM and lattice papers | Downstream finite algebra and Gram-matrix targets | Require Orthad provenance bridge |
| Weil representation papers | Downstream finite representation machinery | Cannot be imported as the Orthad |
| Solar magnetic topology | Robust global topology and reconnection inspiration | External physical tooling |
| Heterogeneous transmission and domain-decomposition papers | Interface-control analogies | Supplemental only |

---

## 10. Pre-Orthad lineage

The earlier Phase Calculus papers did not contain the Orthad.

They repeatedly solved the missing descent-geometry problem manually through:

```text
filters and projectors
sheet and history registers
completion coordinates
branch guards
recovery maps
commuting descent tests
monodromy records
negative controls
domain-specific certification surfaces
```

The filter systems in *Operational Utility and Multiscale Invariance* and the operation/quotient descent papers are direct precursors.

They established recurring requirements:

```text
one retained object can admit multiple lawful views;
projection is not the state;
lost branch, sheet, phase, or path information must remain retained;
a visible branch law must commute with retained evolution;
recovery and negative controls are required;
same visible output does not imply same retained state.
```

The Orthad is the attempt to internalize the common geometry behind those repeated manual constructions.

The old filters and registers are calibration targets, not the Orthad itself.

---

## 11. Projection boundary

No projection occurs during retained evolution.

The retained trajectory is

\[
\widehat X_0
\xrightarrow{U_0}
\widehat X_1
\xrightarrow{U_1}
\cdots
\xrightarrow{U_{n-1}}
\widehat X_n.
\]

Only after halt may a terminal projection act:

\[
\widehat X_n\xrightarrow{\Pi_{\mathrm{terminal}}}Y.
\]

The terminal projection is passive. It may not:

```text
choose a chart;
search a projector bank;
repair missing structure;
infer lost state;
select a primitive;
compare candidates during the evolution;
feed back into the retained dynamics.
```

Two distinct retained histories may share a projected signature.

For Follow experiments, the true Shadow Residual remains outside the lift and is used only in the meta-layer for terminal comparison.

---

## 12. Gauge, holonomy, FQM, and Weil boundary

### 12.1 Raw matrices are presentations

A raw chart matrix is not retained truth by itself.

The intended invariant spine is:

```text
word-built dual-chart matrices
-> directed overlap transitions
-> confluence and cocycle consistency
-> retained loop or holonomy content
-> gauge-equivalence class
-> finite quadratic presentation when lawfully available
-> FQM isometry class
-> terminal Weil or shadow descent
```

### 12.2 Doubled carrier and lap relation

The current authority records the finite carrier

\[
\mathbb Z/(2N)\mathbb Z
\]

and the retained relation

\[
\mathrm{lap}_2=-\mathrm{lap}_1.
\]

These are active downstream structural anchors. They do not replace the all-prefix Orthad recurrence.

### 12.3 Finite quadratic modules

An FQM is a finite abelian group `A` with

\[
q:A\to\mathbb Q/\mathbb Z
\]

whose polarization

\[
b(x,y)=q(x+y)-q(x)-q(y)
\]

is bilinear.

The intended bridge is:

```text
retained QBL history
-> clean word-built Orthad
-> transfer, cocycle, and holonomy data
-> FQM presentation
-> gauge/isometry class
```

The bridge is not complete until the clean all-prefix pairing, chart, and transfer recurrences are established.

### 12.4 Salvaged FQM corpus

The v8m corpus remains valuable as conditional mathematics and calibration:

```text
229 independently reverified basis-matrix certificates;
138 nondegenerate rows;
65 complete radical direct-summand splits;
26 proved non-summand radicals;
five higher-rank residual cores with the same obstruction.
```

These results constrain future Orthad outputs. They do not prove that the clean Orthad already generates those presentations.

### 12.5 Weil structure

Finite Weil machinery is retained downstream.

The level-12 skeleton

\[
A=\mathbb Z/12\mathbb Z,
\qquad
q(r)=\frac{r^2}{24}\pmod 1
\]

is a finite calibration object. It is not the analytic completion of a full mock-theta function and is not proof of the missing upstream recurrence.

---

## 13. Exact supplemental arithmetic

### 13.1 Arbitrary-start `B` ladder

The v7y continuant matrices, inverse recovery, and unimodular wedge identities remain compatible with the exact `B` mutation.

They are primitive arithmetic results. Their projection conclusions remain calibration results.

### 13.2 Global threshold bridge

The global exact-threshold identity

\[
T_A=\lceil y_A\rceil
\]

for all `A>=0` is retained as exact arithmetic connecting the Fibonacci threshold sequence to the affine ceiling law.

It does not determine the primary pairing, chart maps, or transfer recurrence.

### 13.3 Separation rule

Arithmetic, symbolic-dynamics, and finite-module results may constrain the Orthad. They may not be promoted into the Orthad recurrence without an explicit provenance map.

---

## 14. Guardrails and contamination lock

### 14.1 Primitive-law guardrails

- `X_t` alone self-selects `B`, `Q`, or `L`.
- There is no separate custody controller.
- There is no Orthad selector.
- There is no `R/S/T` authority.
- There is no fixed window, 64-tick schedule, clock, cadence, or externally supplied word.
- `Q` does not automatically alternate with `B`.
- `L` adds no quarter turn.
- Pair and phase carry through `L`.
- Exact word order is retained state.

### 14.2 Orthad guardrails

- Every primitive tick immediately mutates the Orthad.
- The same primitive acts on both chart matrices simultaneously.
- There are not separate chart primitives.
- One chart does not receive the inverse primitive.
- The primitive is not split into a metriplectic pair.
- Complementary chart results arise from counter-oriented states.
- Pairing-first is generative, not temporally delayed.
- The four block descendants may not be independently fitted.
- The off-diagonal blocks are directed transfers, not a third lens.
- Transfer follows the local chart mutations within the same atomic tick.
- The transfer stage is not another primitive.
- No projection occurs during evolution.

### 14.3 Formalization guardrails

- A bare formula `D=R(P)` is vacuous if `R` can encode the desired target.
- The star notation is not yet typed.
- A nonzero imaginary local witness cannot be a Hermitian diagonal self-pairing.
- One-sided orthogonality does not force both mixed blocks to vanish.
- Architectural axis growth does not automatically prove algebraic rank growth.
- A represented form `P:H->D(H)` requires a representability or duality law.
- Four local restriction obligations do not prove a global bifunctor.
- A finite carrier cannot retain an unbounded exact word injectively.
- A local scalar descendant is not the complete retained state.
- A downstream FQM certificate is not proof of upstream Orthad provenance.

### 14.4 Forbidden substitutions

```text
R/S/T selector              for the autonomous B > Q > L law
fixed W=64 window           for domain-local phase capacity
fixed Delta=4096 regime     for the derived position capacity
BL                          for the complete first crossing word
post-L matrix construction  for tick-by-tick matrix existence
single diagonal Omega       for the dual-chart Orthad
separate U+ and U-          for one primitive on two charts
inverse primitive on chart- for counter-oriented response
chart-local raw matrix      for retained invariant content
terminal character label    for retained address or parity
Bloch sphere                for the full lifted object
imported Weil matrices      for generated Weil structure
MHD intake                  for a completed field-valued Orthad
```

---

## 15. Status ledger

### 15.1 Settled semantic architecture

```text
X_t is autonomous.
X_t alone self-selects B, Q, or L.
The Orthad has no selection authority.
The Orthad exists before the first L.
Every primitive immediately mutates the Orthad.
The same primitive acts on both chart matrices simultaneously.
The chart matrices are counter-oriented.
The off-diagonal blocks are directed transfers.
Transfer follows local mutation within the same atomic tick.
Pairing-first is the intended generative dependency.
No projection occurs during retained evolution.
Removing the Orthad leaves primitive evolution unchanged.
```

These statements must not be presented as hypotheses to test.

### 15.2 Exact current-canon results

```text
state tuple X=(A,q,theta,k,j,W)
strict priority B > Q > L
capacity and admissibility laws
exact first word BQQBBBQBQBBQBBL
first floor pair (55,89)
floor product 4895
five Q steps before first L
pair and phase carry through L
first next-domain B gives (89,144)
Domain-0 active-axis witness ending at i/4895
```

### 15.3 Recovered legacy mathematics

```text
B active-axis update a -> a*u/(u+v)
Q active-axis update a -> i*a
L historical shorthand: latch completed entry and open identity active slot
```

This kernel is current-compatible locally but is not the complete dual-chart recurrence.

### 15.4 Intended but not fully typed

```text
P_t as the common generative relation
both chart matrices as restrictions or local presentations of P_t
both transfer blocks as cross-chart descendants of P_t
L as one-direction structural extension
counter-orientation as a precise relation between chart frames
```

### 15.5 Not yet recovered or derived in the clean chain

```text
the exact carrier and argument type of P_t
the exact initial seed P_0
the exact chart maps iota_+ and iota_-
the typed meaning of star
the exact algebraic encoding of counter-orientation
the complete B recurrence on P and all four blocks
the complete Q recurrence on P and all four blocks
the complete L mixed and new-new values
the exact bidirectional transfer recurrence
the invariant preserved by transfer
whether transfer is nontrivial on every tick
the all-depth provenance bridge to generated FQMs
```

The phrase **not yet recovered or derived** is deliberate. It does not assert that the project never discussed or encoded the item somewhere in the archives.

### 15.6 Conditional downstream mathematics

```text
FQM classifiers and isometry tools
SNF radical, purity, and non-summand tests
229 v8m certificates
finite Z/12 shadow skeleton
finite Weil representation tooling
legacy transition-to-FQM and lens-compiler pipelines
confluence and cocycle instrumentation
```

These remain useful as calibration, obstruction, and external instrumentation until their clean Orthad provenance is rebuilt.

### 15.7 Superseded claims

```text
Phase 5 was fully closed
successor-first generation as the governing causal route
fixed cyclic carrier as the complete retained state
BL-only first crossing
synthetic FLOOR event
hard-coded i/4895 or lap opposition
Hermitian promotion of the local witness
automatic zero mixed blocks
architectural axis +1 automatically proves algebraic rank +1
legacy FQM objects are canonical outputs without provenance
```

---

## 16. Active constructive target

The next derivation must not test whether the charts are coupled, whether the Orthad mutates every tick, whether the same primitive acts on both, or whether pairing-first is intended. Those are settled.

The smallest faithful target is one complete first `B` tick:

\[
\left(
X_0,P_0,\Omega_0^+,\Omega_0^-,
T_0^{+\to-},T_0^{-\to+}
\right)
\xrightarrow{B}
\left(
X_1,P_1,\Omega_1^+,\Omega_1^-,
T_1^{+\to-},T_1^{-\to+}
\right).
\]

The work must determine or isolate exactly:

```text
P_0;
the chart-state encoding of counter-orientation;
the intrinsic B action on P;
the simultaneous effect of the same B on both chart matrices;
the post-local-mutation transfer or reconciliation;
the exact relation from P_1 to all four blocks;
the preserved whole-object invariant, if one is required.
```

The first pass should recover these from the archives before inventing a new algebraic category.

A new name for the missing law is not progress.

If derivation stops, report the first exact blocked equation and one smallest missing datum. Do not replace the missing datum with an umbrella term.

---

## 17. Zero-context agent protocol

Before doing any Orthad work, an agent must:

1. Read Sections 1 through 8 of this trunk.
2. Read `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`.
3. Copy the cold-start semantic lock into its working notes.
4. State which evidence class supports every load-bearing claim.
5. Separate what is settled, exactly derived, recovered from legacy work, provisional, and open.
6. Preserve the same-operator and same-tick laws verbatim.
7. Treat the old archives as provenance and recovery sources, not automatic authority.
8. Stop when an exact datum is missing. Do not fill it with a familiar category or a guessed matrix.

Every research report must include:

```text
SETTLED INPUTS
EXACT DERIVATIONS
RECOVERED LEGACY COMPONENTS
PROVISIONAL FORMALIZATION
OPEN EQUATIONS
CONTAMINATION CHECK
```

Any report that asks whether the two matrices are coupled, whether the Orthad selects the primitive, or whether matrix mutation happens every step has failed intake.

---

## 18. Revision audit

### v3

Retained:

```text
evidence classes
broad inspiration-paper audit
pre-Orthad lineage
projection boundary
arithmetic salvage
counterexample guardrails
```

Corrected:

```text
v3 demoted pairing-first from ratified architecture to a candidate.
That demotion conflicted with the primary authority and is withdrawn.
```

### v4

Retained:

```text
pairing-first restoration
fully retained state
per-primitive behavior
downstream FQM/gauge/Weil boundary
first-B constructive target
```

Corrected:

```text
v4 used chart-specific Phi_U+ and Phi_U- notation.
That notation could be read as two primitive operators.
The current trunk uses one U_t acting on a pair of counter-oriented states.
```

### v5

Retained:

```text
one-operator lock
simultaneous chart-local mutation
post-local transfer stage
same-tick retention
J/M analogy boundary
```

Expanded:

```text
v5 was narrower than v3 and omitted evidence classes, the complete inspiration
disposition, exact capacity law, full first trace, arithmetic salvage, the
recovered local kernel, and the cold-start protocol.
All are restored here.
```

No material from v3, v4, or v5 is silently discarded. Each item is preserved, corrected, or explicitly quarantined.

---

## 19. Compact whole-system specification

```text
Primitive engine:
    X_t autonomously reevaluates B > Q > L after every step.
    B refines while admissible.
    Q advances only when B is blocked and another position remains.
    L fires only when B and Q are both blocked.
    Exact word order is retained.

Atomic Orthad tick:
    X_t self-selects one U_t in {B,Q,L}.
    U_t updates X_t and the common primary relation.
    The same U_t mutates both counter-oriented chart matrices simultaneously.
    Any required bidirectional cross transfer follows those local mutations.
    The complete coupled state is retained.
    Only then does X_{t+1} select the next primitive.

Pairing-first:
    The two diagonal chart blocks and two off-diagonal transfer blocks are
    non-vacuous descendants or presentations of one common retained relation.
    Pairing-first is structural, not a delayed pipeline.

At B:
    update refinement content;
    preserve phase and latched directions;
    apply the same B to both charts;
    reconcile transfers;
    do not project.

At Q:
    advance phase by pi/2;
    preserve pair and latched directions;
    apply the same Q to both charts;
    reconcile transfers;
    do not project.

At L:
    increment the domain;
    carry pair, phase, word, and old geometry;
    latch the completed direction;
    append one new active structural direction to both charts and transfers;
    do not project.

After halt:
    apply one passive terminal projection.
    Compare to an external reference only in the meta-layer.
```

The retained truth is the complete word-built, counter-oriented, dual-chart, cross-coupled history and its lawful equivalence class, not a raw matrix, a local scalar, or a terminal channel.
