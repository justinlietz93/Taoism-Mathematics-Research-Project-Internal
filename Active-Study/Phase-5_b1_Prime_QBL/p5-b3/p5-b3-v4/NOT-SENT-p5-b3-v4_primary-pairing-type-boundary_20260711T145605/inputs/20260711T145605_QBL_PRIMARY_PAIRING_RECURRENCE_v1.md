# QBL Primary Pairing Recurrence

**Step:** `p5-b3-v3`  
**Status:** hard-stop derivation of the earliest pairing-first dependency  
**Primary authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Contextual architecture:** supplied Orthad diagram; written law controls notation  
**Branch status:** open

## 1. Disposition

```text
JUST-COMPLETED CARRY c_A RECOVERABLE AT S_A^-: PASS
FUTURE CARRY c_{A+1} APPENDED BY THE INSTANTANEOUS L STEP: FAIL

MINIMAL PRIMARY-PAIRING INTERFACE: DERIVED
EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED
EARLIEST MISSING TYPE LAW: SCALAR_VARIANCE_AXIOM
SEED NOT UNIQUE UNDER CURRENT AUTHORITY: RAW PRESENTATION LEVEL
RETAINED GAUGE-CLASS SEED UNIQUENESS: NOT YET DERIVED

B PAIRING TYPE SIGNATURE: DERIVED
B PAIRING VALUE RECURRENCE: NOT YET DERIVED
Q PAIRING TYPE SIGNATURE: DERIVED
Q PAIRING VALUE RECURRENCE: NOT YET DERIVED
L PAIRING TYPE SIGNATURE: DERIVED
L PAIRING VALUE RECURRENCE: NOT YET DERIVED

PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
p5-b3 BRANCH STATUS: OPEN
```

The present authority uniquely fixes primitive custody, the local active-axis shorthand, the architectural rank behavior, and the direction `primary pairing -> chart restrictions/transfers`. It does not uniquely fix the algebraic variance, seed, or value-level `B/Q/L` recurrence of the primary pairing.

The smallest missing law is not a convenient matrix entry. It is the pairing datum and its scalar-variance rule:

\[
\mathcal D_P=(K,H_0,D,\text{variance},\text{symmetry/adjoint law},\text{normalization}),
\]

followed by a seed map and three word-sensitive mutations.

## 2. Source map

| Class | Source | Use in this pass |
|---|---|---|
| **Primary** | `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md` | Custody state, strict `B>Q>L`, local active-axis trace, pairing-first architecture, rank behavior, open-status boundary. |
| **Accepted** | `QBL_HIERARCHICAL_GRAMMAR_FACTOR_SCOPE_v2.md` and its audit | Canonical boundary semiconjugacy, corrected carry indexing, Branch 3 scope. |
| **Accepted** | `QBL_GLOBAL_EXACT_THRESHOLD_BRIDGE_v2.md` | Exact cumulative `B` threshold count. |
| **Contextual** | supplied Orthad diagram | Causal order and intended rank-extension picture only. |
| **Contextual prior result** | pairing-first type extract | Minimal duality-morphism interface and scalar-variance fork. |
| **Provenance only** | older ledgers and downstream FQM/Weil material | May not seed the primary pairing. |

## 3. Correct carry indexing

Let

\[
S_A^-=(A,q_A,\theta_A,k_A,j_A,W_A^-;\text{Orthad coordinates})
\]

be the complete retained state immediately before the `L` closing Domain `A`. Define

\[
T_A=\nu(q_A)=\#_B(W_A^-).
\]

For `A>=1`, the exact carry of the just-completed boundary return is

\[
\boxed{c_A=T_A-2T_{A-1}=\nu(q_A)-2\nu(q_{A-1}).}
\]

`T_A` is recovered from the current pair on the Fibonacci corridor. `T_{A-1}` is recoverable from the retained exact word history because the preceding domain boundary and its cumulative `B` count are already inside `W_A^-`. Hence `c_A` is a lawful derived boundary label once `S_A^-` exists with its preceding retained boundary history.

It is not a primitive-custody coordinate. The custody tuple remains

\[
X_t=(A_t,q_t,\theta_t,k_t,j_t,W_t).
\]

The instantaneous closing step

\[
S_A^-\xrightarrow{L}S_A^+
\]

carries `q`, `theta`, `W`, and the cumulative `B` count unchanged while opening Domain `A+1`. Therefore it cannot contain

\[
c_{A+1}=T_{A+1}-2T_A,
\]

because `T_{A+1}` is not determined until the complete next-domain `B/Q` evolution reaches `S_{A+1}^-`.

```text
JUST-COMPLETED CARRY c_A RECOVERABLE AT S_A^-: PASS
FUTURE CARRY c_{A+1} APPENDED BY THE INSTANTANEOUS L STEP: FAIL
```

For `A=0`, there is no preceding canonical boundary unless a separate initialization convention is declared; the difference formula begins at `A=1`.

## 4. What the current law forces about `P_t`

The fully retained state is schematically

\[
\widehat X_t=(X_t,P_t,\Omega_t^+,\Omega_t^-,T_t^{+\to-},T_t^{-\to+}).
\]

The authority forces the following facts.

1. `P_t` is generative and retained from the first primitive tick.
2. The two chart restrictions and two directed transfers must all be induced from `P_t`.
3. `B` and `Q` preserve architectural pairing rank.
4. `L` retains the complete old pairing block, latches the completed active axis, appends one new orthogonal active axis, and raises architectural rank by one.
5. The exact word prefix is retained and may be used by the mutation law.
6. No projection occurs during the coupled transition.

These facts determine an interface, not a unique scalar-valued form.

## 5. Minimal algebraic type

The least structure that simultaneously expresses same-chart restrictions, mixed directed blocks, and gauge-style pullback is an abstract duality morphism

\[
\boxed{P_t:H_t\longrightarrow D(H_t),}
\]

where `D` is a contravariant duality on an additive carrier category with the finite biproduct required by `L`.

For chart embeddings

\[
\iota_{+,t}:H_t^+\to H_t,
\qquad
\iota_{-,t}:H_t^-\to H_t,
\]

the four blocks have the common type

\[
D(\iota_{a,t})\,P_t\,\iota_{b,t}.
\]

This supports the intended formulas without deciding in advance whether the scalar realization is bilinear or sesquilinear.

### 5.1 Carrier and coefficient data

The current law does **not** uniquely force a concrete coefficient ring or a free module `K^r`. A scalar realization must at least support:

- an element representing the quarter turn, with `i^2=-1`;
- the rational width factors `1/(uv)`;
- the carried initial phase normalization.

On the canonical quarter-turn orbit, `Q(i)` is sufficient for the local scalar shorthand and `C` is an admissible ambient field. Neither is uniquely selected as the primary coefficient ring by custody alone.

The law forces an **architectural rank count**

\[
r_t=A_t+1,
\]

because the first domain begins with one active axis and each `L` appends exactly one axis. It does not, without an additional carrier axiom, identify this count with the dimension of a specific free module.

### 5.2 Surviving type fork

Two scalar realizations remain admissible:

- ordinary-dual bilinear variance;
- conjugate-dual sesquilinear variance.

The first missing type axiom must decide whether

\[
D(\lambda\,\mathrm{id})=\lambda\,\mathrm{id}
\]

or

\[
D(\lambda\,\mathrm{id})=\lambda^*\,\mathrm{id}.
\]

Equivalently, it must decide whether the first argument obeys ordinary or conjugate scalar variance. Hermitian/self-adjoint symmetry is a further law and is not forced merely by the symbol `*` in a pullback.

A quadratic refinement cannot be used directly as `P_t` without first supplying a polarization map. Operator-valued and polarized-quadratic realizations remain possible only after their additional maps are declared.

```text
MINIMAL PRIMARY-PAIRING INTERFACE: DERIVED
EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED
EARLIEST MISSING TYPE LAW: SCALAR_VARIANCE_AXIOM
```

## 6. Seed boundary

At the pre-word state

\[
A=0,\quad q=(1,1),\quad \theta=\theta_0,\quad k=0,\quad W=\varnothing,
\]

the accepted local shorthand is normalized to

\[
a_0=1
\]

for `theta_0=0`. This fixes only one designated local descendant of the seed, not the complete `P_0`.

For example, on a one-dimensional complex carrier with basis vector `e`, both

\[
P_{\mathrm{bil}}(x,y)=xy,
\qquad
P_{\mathrm{sesq}}(x,y)=\overline{x}y
\]

satisfy

\[
P_{\mathrm{bil}}(e,e)=P_{\mathrm{sesq}}(e,e)=1,
\]

but they differ, for example, at `(x,y)=(i,1)`. The custody seed and local normalization do not choose between them.

The unresolved freedom includes:

- coefficient ring and duality;
- ordinary versus conjugate scalar variance;
- symmetry or adjoint law;
- seed admissibility and normalization beyond the local active witness;
- basis/gauge presentation;
- any extra operator-valued or polarized structure.

Thus raw seed presentations are not unique under the current authority. Whether all such presentations collapse to one retained gauge class cannot be decided before the gauge relation and seed-admissibility law are supplied.

```text
SEED NOT UNIQUE UNDER CURRENT AUTHORITY: RAW PRESENTATION LEVEL
RETAINED GAUGE-CLASS SEED UNIQUENESS: NOT YET DERIVED
EXACT PRIMARY PAIRING SEED: NOT YET DERIVED
```

The missing seed map is

\[
\eta_P:(X_0,W_0,\mathcal D_P)\longmapsto P_0.
\]

## 7. Exact local active-axis descendant

The current law does force the local scalar shorthand

\[
\boxed{a_t=\frac{i^{\#_Q(W_t)}}{u_tv_t}}
\]

on the canonical quarter-turn normalization. This is a component read from the intended active pairing data. It is not the complete primary pairing.

### 7.1 `B` local update

For

\[
(u,v)\mapsto(v,u+v),
\]

phase is preserved, so

\[
\boxed{a_{t+1}=a_t\frac{u}{u+v}
      =\frac{i^{\#_Q(W_t)}}{v(u+v)}.}
\]

### 7.2 `Q` local update

For

\[
\theta\mapsto\theta+\frac\pi2,
\]

the pair is preserved, so

\[
\boxed{a_{t+1}=i\,a_t.}
\]

### 7.3 `L` local update

At `L`, the completed local witness is latched and the new unmutated active slot begins with local witness `1`. This yields the historical local shorthand

\[
\operatorname{diag}(a_{\mathrm{completed}},1_{\mathrm{active}}),
\]

but the authority explicitly forbids identifying that shorthand with the complete modern Orthad or complete primary pairing.

## 8. `B` pairing signature and missing value law

A lawful full mutation must have the type

\[
\Phi_B:(P_t,X_t,X_{t+1},W_{t+1})\longmapsto P_{t+1}
\]

and must satisfy:

1. architectural rank is unchanged;
2. every latched axis and the complete latched old block are preserved;
3. carried phase is preserved;
4. the designated active local descendant changes by `u/(u+v)`;
5. chart restrictions and transfers are later derived from the resulting `P_{t+1}`;
6. no projection occurs.

These conditions do not determine how mixed old/active entries, orientation coupling, or operator-valued components change. Therefore they are a type signature, not a closed recurrence.

```text
B PAIRING TYPE SIGNATURE: DERIVED
B PAIRING VALUE RECURRENCE: NOT YET DERIVED
```

## 9. `Q` pairing signature and missing value law

A lawful full mutation must have the type

\[
\Phi_Q:(P_t,X_t,X_{t+1},W_{t+1})\longmapsto P_{t+1}
\]

and must satisfy:

1. architectural rank is unchanged;
2. every latched axis and the complete latched old block are preserved;
3. the carried pair is preserved;
4. the designated active local descendant is multiplied by `i`;
5. both orientation hands remain retained;
6. no projection occurs.

Without the scalar-variance axiom, even the exact action of the quarter-turn on the first versus second pairing argument is not fixed. The local multiplier `i` does not close the full recurrence.

```text
Q PAIRING TYPE SIGNATURE: DERIVED
Q PAIRING VALUE RECURRENCE: NOT YET DERIVED
```

## 10. `L` pairing signature

The strongest type-level statement licensed by the authority is an orthogonal biproduct extension

\[
H_{t+1}\cong H_t\oplus A_{\mathrm{new}}.
\]

After choosing a duality realization, the block form must have the shape

\[
\boxed{
P_{t+1}=
\begin{pmatrix}
P_t&0\\
0&\sigma_{\mathrm{new}}
\end{pmatrix}.}
\]

The zero mixed birth blocks are forced by the statement that the appended axis is orthogonal at birth. The old block embeds unchanged:

\[
D(\iota_{\mathrm{old}})P_{t+1}\iota_{\mathrm{old}}=P_t.
\]

The local active descendant of `sigma_new` is normalized to `1`, but `sigma_new` itself is not determined until the pairing type, seed normalization, and rank-one carrier are declared. Consequently the block **signature** and old-block embedding are derived, while the exact value-level extension is not.

```text
L PAIRING TYPE SIGNATURE: DERIVED
OLD PAIRING BLOCK EMBEDDING AT L: DERIVED
MIXED OLD/NEW BIRTH BLOCKS: ZERO BY ORTHOGONALITY
L PAIRING VALUE RECURRENCE: NOT YET DERIVED
```

This axis decomposition is distinct from the later plus/minus chart decomposition. Zero old/new axis blocks do not independently determine the two directed chart-transfer blocks.

## 11. First-domain prefix trace

The exact primitive word is

```text
B Q Q B B B Q B Q B B Q B B L
```

The complete custody and local active-axis trace is:

| Prefix | Primitive | Pair | Q count | Local witness | Primary pairing status |
|---:|:---:|:---:|---:|:---:|:---|
| 0 | start | `(1,1)` | 0 | `1` | not instantiated |
| 1 | B | `(1,2)` | 0 | `1/2` | not instantiated |
| 2 | Q | `(1,2)` | 1 | `i/2` | not instantiated |
| 3 | Q | `(1,2)` | 2 | `-1/2` | not instantiated |
| 4 | B | `(2,3)` | 2 | `-1/6` | not instantiated |
| 5 | B | `(3,5)` | 2 | `-1/15` | not instantiated |
| 6 | B | `(5,8)` | 2 | `-1/40` | not instantiated |
| 7 | Q | `(5,8)` | 3 | `-i/40` | not instantiated |
| 8 | B | `(8,13)` | 3 | `-i/104` | not instantiated |
| 9 | Q | `(8,13)` | 4 | `1/104` | not instantiated |
| 10 | B | `(13,21)` | 4 | `1/273` | not instantiated |
| 11 | B | `(21,34)` | 4 | `1/714` | not instantiated |
| 12 | Q | `(21,34)` | 5 | `i/714` | not instantiated |
| 13 | B | `(34,55)` | 5 | `i/1870` | not instantiated |
| 14 | B | `(55,89)` | 5 | `i/4895` | not instantiated |
| 15 | L | `(55,89)` carried | 5 | latch `i/4895`; new local active `1` | type-level extension only |

Thus

\[
\boxed{a_{\mathrm{completed},0}=\frac{i}{4895}}
\]

is recovered exactly as a local consequence of the custody trace. No row claims a complete `P_t` value.

## 12. Uniqueness and order dependence

The local shorthand depends on current `q` and carried quarter phase. On the balanced corridor, its value can therefore be reconstructed from the counts of `B` and `Q`. This does not imply that the full primary pairing is count-determined.

After the first `L`, two candidate bilinear presentations can share:

- the same retained old block;
- the same active local diagonal descendant;
- the same architectural rank;
- the same zero mixed blocks at axis birth;

and then differ in a mixed old/active block after a later `B` or `Q`. The current law provides no equation choosing that mixed update.

Likewise, one candidate mutation may depend only on counts while another may depend on an order statistic of `W`, with both reproducing the same local active shorthand. These are underdetermination witnesses, not promoted models.

The canonical custody path is deterministic, so this pass does not contain two canonical lawful prefixes from the same seed with equal counts and different order. Therefore actual order sensitivity of `P_t` cannot be tested from such a comparison family.

```text
LOCAL ACTIVE SHORTHAND DETERMINED BY q AND PHASE: PROVED
ORDERED WORD W RETAINED AS REQUIRED INPUT/CERTIFICATE: PROVED BY AUTHORITY
COUNTS DETERMINE FULL P_t: NOT DERIVED
FULL P_t ORDER SENSITIVITY: NOT YET DERIVED
```

## 13. Future chart interface

Once `P_t` is closed, the next dependency must provide chart carriers and embeddings

\[
\iota_{+,t}:H_t^+\to H_t,
\qquad
\iota_{-,t}:H_t^-\to H_t.
\]

The required outputs are

\[
\Omega_t^+=D(\iota_{+,t})P_t\iota_{+,t}:H_t^+\to D(H_t^+),
\]

\[
\Omega_t^-=D(\iota_{-,t})P_t\iota_{-,t}:H_t^-\to D(H_t^-),
\]

\[
T_t^{+\to-}=D(\iota_{-,t})P_t\iota_{+,t}:H_t^+\to D(H_t^-),
\]

\[
T_t^{-\to+}=D(\iota_{+,t})P_t\iota_{-,t}:H_t^-\to D(H_t^+).
\]

The chart interface must additionally specify:

- the overlap domain and cover condition;
- how both embeddings coevolve with every primitive prefix;
- compatibility with the old-axis embedding and new-axis extension at `L`;
- route/cocycle consistency on the overlap;
- no independent chart or transfer seed.

```text
EXACT CHART MAPS: NOT YET DERIVED
EXACT DIRECTED TRANSFERS: NOT YET DERIVED
```

## 14. Descriptive-layer `L` test

A descriptive independence theorem requires a lawful comparison family `Z`, an old-description map

\[
D_{\mathrm{old}}:Z\to Y,
\]

and a proposed new-axis coordinate

\[
\xi:Z\to K
\]

such that some lawful pair satisfies

\[
D_{\mathrm{old}}(z)=D_{\mathrm{old}}(z'),
\qquad
\xi(z)\ne\xi(z').
\]

The current pass derives only the pairing interface and the type-level `L` extension signature. It does not derive pairing values or a lawful comparison family of fully retained states. Therefore neither `D_old` nor `xi` can yet be instantiated at the required level.

The scalar boundary cocycle does not settle this Orthad-level fiber question.

```text
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
DESCRIPTIVE-LAYER INDEPENDENT AXIS TEST: NOT YET DERIVED
```

## 15. Smallest missing law

The primary pairing is underdetermined at the earliest type fork. The next theorem must supply, in order:

1. **Scalar variance axiom:** ordinary or conjugate duality.
2. **Symmetry/adjoint axiom:** if any.
3. **Seed law:** `eta_P(X_0,W_0,D_P)=P_0`, including normalization and admissibility.
4. **Value recurrences:** exact `Phi_B`, `Phi_Q`, and `Phi_L` on the primary pairing.
5. **Word dependence law:** how `W` affects mixed and active blocks.

A narrower mixed-pairing formulation may equivalently give the initial mixed datum and recurrence

\[
\tau_0,
\qquad
\tau_{t+1}=\Phi_{U_t}(X_{t+1},W_{t+1},\tau_t),
\]

but this is sufficient only after the carrier, duality, and relation of `tau` to the complete `P_t` are fixed.

No convenient matrix is selected in this document.

## 16. Formal and computational boundary

The companion Lean file formalizes the architectural rank laws, a conditional block-embedding interface, the local first-domain result, and an explicit raw type/seed nonuniqueness witness. It does not instantiate the missing primary pairing recurrence.

```text
LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
```

The notebook and derivation script verify the custody trace, local scalar recurrences, carry indexing, type fork witnesses, conditional `L` embedding algebra, and rejection of a nonorthogonal `L` negative control. Numerical or symbolic checks are not labeled as proofs of the missing pairing law.

## 17. Final status

```text
PRIMARY PAIRING TYPE DATUM: PARTIALLY CLOSED AS ABSTRACT DUALITY INTERFACE
EXACT PRIMARY PAIRING TYPE: NOT YET DERIVED
EXACT PRIMARY PAIRING SEED: NOT YET DERIVED
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
EXACT CHART MAPS: NOT YET DERIVED
EXACT DIRECTED TRANSFERS: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
p5-b3 BRANCH STATUS: OPEN
```
