# QBL Primary Pairing: State-Forced Action Boundary

**Artifact:** `QBL_PRIMARY_PAIRING_STATE_FORCED_ACTION_v1.md`  
**Research interaction:** `p5-b3-v8`  
**Primary authority:** `QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md`  
**Constraint:** State-Forced Derivation Principle  
**Parallel input:** `p5_v8y_primary-pairing-star-phase-compatibility_20260711_162758.zip`, verified SHA-256 `491ecfffd78ce5ab11e82794381e7579168027892dce7986fb9d4d3507395d27`

## Executive result

The complete retained-state discipline requires one autonomous intrinsic transition, but the current authority does not yet provide the state-to-pairing generation law needed to compute it.

The strongest exact conclusion is:

```text
SOURCE-FORCED LOCAL ORDERED TWO-SLOT INTERFACE: PROVED
AUTONOMOUS COMPLETE TRANSITION INTERFACE: PROVED
ONE PRIMARY OBJECT MUST GENERATE ALL FOUR DESCENDANTS: PROVED
STAR IS TYPED BY CURRENT AUTHORITY: FALSE
STAR SEMANTICS IS AN INDEPENDENT AXIOM: NOT PROVED
ONE EXPLICIT STATE-FORCED B/Q/L PAIRING ACTION: NOT YET DERIVED
COMPLETE-MODEL INDEPENDENCE THEOREM: NOT YET DERIVED
```

The first missing bridge is not a choice between transpose and conjugate transpose. It is the complete state-generated law

\[
\mathfrak G_p:
(\widehat X_t, X_{t+1})
\longmapsto
\bigl(P_{t+1},\,R_{++,t+1},R_{--,t+1},R_{+-,t+1},R_{-+,t+1}\bigr),
\qquad p=\Sigma_{{\rm cust}}(X_t),
\]

including its seed, its `B/Q/L` cases, and its old/new `L` components. This datum is called the **Primary Pairing Generation and Restriction Law** (`PPGRL`) in this document.

The State-Forced Derivation Principle rejects an externally chosen realization. It does not turn architectural constraints into a missing value recurrence. Until `PPGRL` is derived from an earlier retained distinction or ratified explicitly, selecting a familiar matrix law would be an external choice.

---

## 1. Authority and evidence classes

### PROVED from the primary authority

- Primitive selection depends only on the custody state and strict priority `B > Q > L`.
- The primary pairing mutates after custody advances.
- One updated primary object generates both chart restrictions and both directed transfers.
- The exact word prefix is retained and operation counts are not state-complete.
- `B` and `Q` preserve architectural rank and every latched axis.
- `L` retains the complete old pairing architecture, adds one active architectural axis, preserves two-slot arity, extends all four descendants, and performs no projection.
- The Domain-0 local active descendant ends as `i/4895` before the first `L`.

### CERTIFIED FINITELY in this package

- The custody simulator reproduces `BQQBBBQBQBBQBBL` from `(A,q,k,j)=(0,(1,1),0,1)`.
- The prefix-by-prefix local descendant reproduces every accepted Domain-0 row.
- Two complete *unlawful* coupled-state countermodels are rejected at their exact failed obligations: external primitive selection and independently mutated descendants.

### OPEN

- Global `Pair(-,-)` bifunctor.
- Primary pairing carrier, codomain, seed, and value law.
- Typed star semantics.
- Exact `Q` action type.
- Exact `B/Q/L` pairing recurrence.
- Exact restriction maps and transfer maps.
- Gauge category needed to compare algebraic presentations.
- Return map on primary-pairing equivalence classes.

---

## 2. Separation of the three pairing layers

| Layer | Exact content | Source status | What is still absent |
|---|---|---|---|
| Local ordered two-slot restriction interface | One `P_t`; placements `++`, `--`, `+-`, `-+`; every descendant induced from `P_t`; exact-word dependence | **PROVED** | Typed arguments, carrier, codomain, values |
| Global `Pair(-,-)` bifunctor | A pairing object defined functorially for arbitrary argument objects and maps | **OPEN** | Objects, morphisms, identity/composition laws, variance |
| Algebraic realization | Bilinear, sesquilinear, operator-valued, represented duality, quadratic/polarized, or another concrete law | **OPEN** | Realization axiom, seed, updates, gauge equivalence |

The primary authority calls the four displayed `ι*Pι` expressions the **intended algebraic shape** and says they state the required direction of construction. It does not type the star or derive global functoriality.

Contender A, the local architecture, is therefore **an incomplete description**, not a complete intrinsic law. If promoted to a complete law, it fails because it cannot calculate `P_{{t+1}}` or any `D_{{ab,t+1}}`.

---

## 3. Autonomous complete intrinsic transition

The retained state is

\[
\widehat X_t=
(X_t,P_t,\Omega_t^+,\Omega_t^-,T_t^{{+\to-}},T_t^{{-\to+}}).
\]

The selector is a predicate abbreviation, not a retained object:

\[
p_t=\Sigma_{{\rm cust}}(X_t),
\]

where

\[
\Sigma_{{\rm cust}}(X)=
\begin{{cases}}
B,&\operatorname{{CanB}}(X),\\
Q,&\neg\operatorname{{CanB}}(X)\land\operatorname{{CanQ}}(X),\\
L,&\neg\operatorname{{CanB}}(X)\land\neg\operatorname{{CanQ}}(X).
\end{{cases}}
\]

Any shorthand on the lifted state must factor through custody:

\[
\Sigma(\widehat X_t)=\Sigma_{{\rm cust}}(\pi_X(\widehat X_t)).
\]

The autonomous law has the form

\[
\widehat X_{{t+1}}
=\mathcal U_{{\Sigma_{{\rm cust}}(X_t)}}(\widehat X_t).
\]

Write

\[
D_{{++,t}}=\Omega_t^+,
\quad D_{{--,t}}=\Omega_t^-,
\quad D_{{+-,t}}=T_t^{{+\to-}},
\quad D_{{-+,t}}=T_t^{{-\to+}}.
\]

Completeness requires

\[
D_{{ab,t+1}}=R_{{ab,t+1}}(P_{{t+1}})
\]

for all four placements. The maps `R_ab,t+1` must themselves be fixed by the retained state. Independent descendant recurrences are forbidden.

### First missing datum

The authority does not specify the function `PPGRL` that returns `P_{{t+1}}` and the four restriction maps. Therefore the autonomous **interface** is complete, but the autonomous **value transition** is open.

---

## 4. Intrinsic-action equivalence

Two complete presentations `M` and `N` represent the same intrinsic action only if there is a family of representation isomorphisms `Φ_t` that satisfies all of the following:

1. **Custody identity:** `Φ_t` is the identity on `X_t`, including the exact word.
2. **Transition conjugacy:** for the custody-selected primitive `p_t`,
   \[
   \Phi_{{t+1}}\circ\mathcal U^M_{{p_t}}
   =\mathcal U^N_{{p_t}}\circ\Phi_t.
   \]
3. **Four-descendant commutation:** corresponding maps carry every `R^M_ab(P)` to `R^N_ab(Φ(P))` with the placement labels fixed.
4. **Latch preservation:** old sectors, active sector, architectural-axis index, and old/new decomposition are preserved.
5. **No projection:** equivalence is established in retained state, not by equal terminal outputs.
6. **Seed and history compatibility:** the initial primary object and every exact prefix are included.

The authority does not define the allowable class of `Φ_t` (linear, semilinear, dual, adjoint-preserving, operator conjugacy, or another gauge notion). Consequently no claimed transpose-versus-conjugate-transpose fork has yet been proved genuinely inequivalent.

```text
ACTION-EQUIVALENCE INTERFACE: PROVED
EXACT GAUGE/REPRESENTATION CATEGORY: NOT YET DERIVED
```

---

## 5. Repeated-star audit

### Ratified source expressions

1. Chart and transfer descendants:
   \[
   \iota_a^*P_t\iota_b.
   \]
   The authority explicitly calls this the **intended algebraic shape**.

2. Gauge presentation change:
   \[
   P\mapsto U^*PU.
   \]
   The authority explicitly calls this **schematic**.

### Non-authoritative uses

- `C_t*` and first-`L` reverse-relation candidates occur in task-level or convergence-route material, not as ratified value laws.
- `H=M+iJ` is a historical downstream overlap reconstruction, not the current primary seed.

### Result

The repeated glyph does not force one typed operation across all passages. The current source requires only a role: a left-side operation appropriate to whichever realization eventually makes the intended restriction and gauge expressions well typed.

A typed star may be induced by a later realization. It is not currently forced directly, and genuine independence from `Q` is not proved.

```text
STAR LAW FORCED DIRECTLY: FALSE
STAR AS SCHEMATIC ROLE MARKER: PROVED
STAR INDUCED BY A FUTURE REALIZATION: LAWFUL POSSIBILITY
STAR/Q JOINT TYPE LAW: NOT YET DERIVED
GENUINE STAR-SEMANTICS INDEPENDENCE: NOT YET DERIVED
```

Promoting `STAR_SEMANTICS_AXIOM` now would contradict the State-Forced Derivation Principle: it would insert a semantic choice before deriving that the complete retained state fails to select among complete inequivalent laws.

---

## 6. Exact local descendant scope

Before the first `L`, define the local active descendant by the accepted shorthand. On every Domain-0 prefix,

\[
a_t=\frac{{i^{{\#Q(W_t)}}}}{{u_tv_t}}.
\]

For `B:(u,v)\mapsto(v,u+v)`, the `Q` count is unchanged, hence

\[
a_{{t+1}}
=\frac{{i^q}}{{v(u+v)}}
=a_t\frac{{u}}{{u+v}}.
\]

For `Q`, the pair is unchanged and the `Q` count increases by one, hence

\[
a_{{t+1}}=ia_t.
\]

The complete trace is:

| step | selected | prefix | A | q | Q-count | k | j | local descendant |
|---:|:---:|---|---:|---|---:|---:|---:|---|
| 0 | `start` | `∅` | 0 | (1,1) | 0 | 0 | 1 | `1` |
| 1 | `B` | `B` | 0 | (1,2) | 0 | 0 | 1 | `1/2` |
| 2 | `Q` | `BQ` | 0 | (1,2) | 1 | 1 | 2 | `i/2` |
| 3 | `Q` | `BQQ` | 0 | (1,2) | 2 | 2 | 3 | `-1/2` |
| 4 | `B` | `BQQB` | 0 | (2,3) | 2 | 2 | 3 | `-1/6` |
| 5 | `B` | `BQQBB` | 0 | (3,5) | 2 | 2 | 3 | `-1/15` |
| 6 | `B` | `BQQBBB` | 0 | (5,8) | 2 | 2 | 3 | `-1/40` |
| 7 | `Q` | `BQQBBBQ` | 0 | (5,8) | 3 | 3 | 4 | `-i/40` |
| 8 | `B` | `BQQBBBQB` | 0 | (8,13) | 3 | 3 | 4 | `-i/104` |
| 9 | `Q` | `BQQBBBQBQ` | 0 | (8,13) | 4 | 4 | 5 | `1/104` |
| 10 | `B` | `BQQBBBQBQB` | 0 | (13,21) | 4 | 4 | 5 | `1/273` |
| 11 | `B` | `BQQBBBQBQBB` | 0 | (21,34) | 4 | 4 | 5 | `1/714` |
| 12 | `Q` | `BQQBBBQBQBBQ` | 0 | (21,34) | 5 | 5 | 6 | `i/714` |
| 13 | `B` | `BQQBBBQBQBBQB` | 0 | (34,55) | 5 | 5 | 6 | `i/1870` |
| 14 | `B` | `BQQBBBQBQBBQBB` | 0 | (55,89) | 5 | 5 | 6 | `i/4895` |
| 15 | `L` | `BQQBBBQBQBBQBBL` | 1 | (55,89) | 5 | 0 | 7 | `new active axis opened; old=i/4895` |

At the first `L`, `i/4895` is the completed retained old-axis descendant. The newborn active axis is distinct and begins unmutated.

This scalar constrains only the authority's **older active local trace functional**. The source does not identify it with a self-pairing, a matrix diagonal, a specific chart block, or a transfer block. Hermitian diagonal promotion remains rejected.

```text
DOMAIN-0 LOCAL DESCENDANT LAW: PROVED
FIRST COMPLETED OLD-AXIS DESCENDANT i/4895: PROVED
GLOBAL AXIS-INDEXED DESCENDANT RECURRENCE: NOT YET DERIVED
```

---

## 7. Intrinsic `B` boundary

The strongest forced complete signature is

\[
P_{{t+1}}=\mathcal B^\sharp(\widehat X_t,X_{{t+1}}),
\]

subject to:

- custody has already selected `B`;
- architectural rank is fixed;
- all latched sectors are retained;
- active arithmetic data changes from `(u,v)` to `(v,u+v)`;
- the accumulated `Q` phase is retained;
- all four descendants are regenerated from `P_{{t+1}}`;
- no projection occurs;
- the Domain-0 local trace obeys `a -> a u/(u+v)`.

The authority does not determine whether a concrete realization expresses this as pullback, value mutation, regeneration, conjugation, or another coordinate law.

```text
B ARCHITECTURAL ACTION: PROVED
B LOCAL TRACE UPDATE: PROVED ON DOMAIN 0
B COMPLETE PRIMARY-PAIRING VALUE LAW: NOT YET DERIVED
FIRST MISSING B DATUM: state-generated active-sector update map B^sharp
```

Metadata-only mutation is rejected because it fails to produce the required new primary object and four descendants.

---

## 8. Intrinsic `Q` and star boundary

The strongest forced signature is

\[
P_{{t+1}}=\mathcal Q^\sharp(\widehat X_t,X_{{t+1}}),
\]

subject to:

- fixed architectural rank;
- all latched sectors retained;
- arithmetic anchor retained;
- active pairing orientation advances by the quarter-turn witness;
- all four descendants are regenerated under that orientation;
- exact word and domain occupancy remain distinct after four visible quarter turns;
- no projection occurs;
- the Domain-0 local trace obeys `a -> i a`.

The authority does not specify whether the quarter-turn acts on the first argument, second argument, both, the pairing value, orientation metadata, or a combination. It also does not type the star. Therefore neither one can be used to derive the other.

```text
Q ARCHITECTURAL ACTION: PROVED
Q LOCAL +i TRACE UPDATE: PROVED ON DOMAIN 0
Q COMPLETE PRIMARY-PAIRING VALUE LAW: NOT YET DERIVED
STAR FORCES Q: NOT YET DERIVED
Q FORCES STAR: NOT YET DERIVED
COMMON PRIOR REALIZATION TYPES BOTH: LAWFUL POSSIBILITY, NOT PROVED
FIRST MISSING Q DATUM: typed active-orientation action Q^sharp
```

---

## 9. Intrinsic `L` boundary

`L` preserves two-slot arity while extending each argument architecture into old and new sectors. Its source-forced component signature is

\[
P_{{t+1}}=
\left(
P_{{\rm oo}},P_{{\rm on}},P_{{\rm no}},P_{{\rm nn}}
\right),
\]

with

\[
P_{{\rm oo}}=\operatorname{{Emb}}_t(P_t).
\]

The exact retained state must determine `P_on`, `P_no`, and `P_nn`. The authority does not supply those laws. It says the new axis is orthogonal, but it does not type orthogonality sufficiently to infer zero mixed values. The new active slot is unmutated, but its pairing normalization is not given.

```text
L OLD-OLD RETENTION: PROVED
L ARCHITECTURAL AXIS COUNT +1: PROVED
L TWO-SLOT ARITY: PROVED
L OLD-NEW VALUE: NOT YET DERIVED
L NEW-OLD VALUE: NOT YET DERIVED
L NEW-NEW VALUE: NOT YET DERIVED
L ZERO MIXED BLOCKS: NOT DERIVED
```

A standalone block matrix is not a complete model because it omits autonomous custody selection, exact-word dependence, the restriction family, and the next-prefix recurrence.

---

## 10. Head-to-head disposition

| Contender | Disposition | Classification | Certificate |
|---|---|---|---|
| A. Local ordered two-slot architecture | Survives | **INCOMPLETE DESCRIPTION** | It fixes source/target roles and four placements but not `P_{{t+1}}`, `R_ab`, seed, or values. |
| B. Genuine independent star semantics | Withheld | **NOT A COMPLETE INTRINSIC LAW** | No two complete lawful recurrences and no inequivalence theorem exist; preselecting a star is an external choice. |
| C. State-forced one intrinsic action | Required as the lawful research target; formula open | **NOT YET DERIVED** | `PPGRL`, typed `Q` action, `L` mixed/self components, and gauge equivalence are absent. |

### Contradiction certificates

- **A promoted as complete:** fails the complete-transition obligation because the next retained state is not calculable.
- **B promoted as an independent axiom:** fails the State-Forced Derivation Principle because it introduces an external semantic choice without an independence certificate.
- **C declared proved now:** fails the exact-recurrence obligation because no state-generated `B/Q/L` value map or restriction family has been supplied.

The current evidence neither proves several intrinsic laws nor proves coordinate equivalence among candidate algebraic presentations. It establishes a precise derivation boundary.

---

## 11. Complete countermodels used in the computational companion

Two deliberately unlawful but complete coupled recurrences are included only to test the hard constraints.

### COUNTERMODEL 1: external primitive input

The model contains custody, a primary object, four descendants, and complete updates, but accepts an external letter that can disagree with `Σ_cust(X)`. It is rejected at selector factorization.

### COUNTERMODEL 2: independent descendant mutation

The model uses custody-only selection and updates a primary object, but mutates one chart independently rather than applying `R_ab(P_{{t+1}})`. It is rejected at pairing-first descent.

Neither countermodel is evidence for lawful action independence. Both are complete negative controls for exact obligations.

---

## 12. Boundary-return cocycle

The accepted arithmetic boundary-return cocycle acts on custody-derived boundary data. No source-derived map currently sends a primary pairing or its equivalence class from `S_A^-` to `S_{{A+1}}^-`.

A lawful pairing-class return would require

\[
\kappa_P(\widehat X_{{A+1}}^-)
=\overline{\mathcal R}_P\bigl(\kappa_P(\widehat X_A^-)\bigr)
\]

for a derived class projector `κ_P` and return action `Rbar_P`. Both depend on the unresolved pairing recurrence and gauge category.

```text
PAIRING SIMPLIFICATION FROM EFFECTIVE INVARIANTS: NOT YET DERIVED
FIRST MISSING BRIDGE: exact all-prefix PPGRL plus a derived pairing-class projector and return action
```

---

## 13. Descriptive and Orthad boundaries

```text
D1 DOMAIN-PROPER EFFECTIVE INVARIANT: NOT YET DERIVED
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED
EXACT PRIMARY PAIRING RECURRENCE: NOT YET DERIVED
EXACT CHART MAPS: NOT YET DERIVED
EXACT DIRECTED TRANSFERS: NOT YET DERIVED
GAUGE/FQM MAP FROM d_A=±1: NOT YET DERIVED
```

The corrective descriptive pass is not reopened here.

---

## 14. Final status by evidence class

### PROVED

- Local ordered two-slot restriction architecture.
- One updated primary object must generate four descendants.
- Autonomous custody-only selector and complete-transition interface.
- Exact-word dependence.
- Fixed architectural rank under `B/Q`.
- Old architecture retention and one-axis extension under `L`.
- Domain-0 local descendant formula and endpoint `i/4895`.
- Repeated star is schematic rather than a currently typed source law.

### CERTIFIED FINITELY

- Exact Domain-0 custody and local-descendant trace.
- Rejection of the two complete unlawful countermodels.
- Exact hashes of the audit and convergence inputs.

### COUNTERMODEL

- Externally supplied primitive letter.
- Independently updated chart/transfer descendants.

### OBSERVED

- Multiple familiar algebraic realizations can be written down, but none qualifies here as a complete lawful all-prefix intrinsic recurrence.

### OPEN

- `PPGRL`.
- Explicit primary pairing type, seed, and `B/Q/L` values.
- Typed star and `Q` relation.
- Exact restriction maps and transfer maps.
- Exact gauge/equivalence category.
- Pairing-class boundary return.

```text
STATE-FORCED INTRINSIC ACTION: NOT YET DERIVED
GENUINE STAR-SEMANTICS INDEPENDENCE: NOT YET DERIVED
COMPLETE-MODEL INDEPENDENCE THEOREM: NOT YET DERIVED
LEAN SOURCE PRESENT; PROOF AND COMPILATION NOT VERIFIED
p5-b3 BRANCH STATUS: OPEN
```
