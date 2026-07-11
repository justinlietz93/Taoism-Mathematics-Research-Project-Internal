# Descriptive Articulation Equivalence

## 1. Purpose

This criterion separates a new presentation of an existing path dynamics from admission of a genuinely new descriptive domain in the CF000 sense. It is pre-metric and realization-neutral.

Let a descriptive articulation class be represented by a lawful transition system

\[
\mathcal D=(X,\to,\mathcal R),
\]

where `X` is its admitted state class, `->` its lawful elementary transition relation, and `R` its admitted relation and observable vocabulary. Let `Path(D)` be the category whose objects are states and whose morphisms are finite lawful paths.

## 2. Same-class interpretation criterion

A presentation `E` is inside the same descriptive articulation class as `D` when there is an interpretation

\[
J:E\longrightarrow Path(D)
\]

with all of the following properties on the claimed object:

1. **State internality.** Every state of `E` is an existing `D` state, a declared subset of `D` states, or a tuple canonically recoverable from a finite `D` path.
2. **Transition internality.** Every `E` edge is interpreted as a finite lawful `D` path.
3. **Relation internality.** Every `E` label, observable, or relation is a function of the interpreted `D` states and paths.
4. **No fiber splitting beyond D.** There do not exist `e,e'` with identical complete `D` interpretation but a distinct `E` determination.
5. **Path recovery at the claimed strength.** When `E` claims a lossless recoding, `J` is full and faithful onto its image and has an inverse presentation. When `E` is a quotient or factor, its information loss is declared and is not treated as a new determination.

Under these conditions, `E` may be useful, intrinsic, and theorem-bearing while remaining a same-layer derived presentation.

## 3. Genuinely new descriptive-domain criterion

A new descriptive domain is admitted only when the new presentation adds a lawful internal determination that cannot be represented in the old articulation class by any state, finite path, section, first-return construction, path observable, quotient, or induced subsystem admitted there.

A direct certificate is a fiber split:

\[
D(z)=D(z'),\qquad \xi(z)\ne\xi(z'),
\]

where `D` is the complete old-class description and `xi` is the new determination. The split must not be recoverable from any lawful old-class finite path or relation. In CF000 language, the new determination is irreducible to the exhausted old domain rather than a renamed or reparameterized old determination.

## 4. Classification of common constructions

| Construction | Default status | Upgrade condition |
|---|---|---|
| Renaming | same class | never a new domain by naming alone |
| Fixed-length block recoding | same class if conjugate; factor if lossy | new domain only with a proved old-class fiber split |
| Variable-length return coding | induced same-layer presentation | new domain only if a relation not representable by the base path system is added |
| Quotient or factor | information-losing shadow | not a new domain by loss alone |
| Induced subsystem on a section | same-layer subsystem | new domain only with a proved irreducible determination |
| Topological orbit closure | mathematical completion of a code | becomes a QBL domain only after its added limit states are constructed as lawful QBL states |
| Genuinely new domain admission | new class | requires inherited stack, irreducible new determination, and a valid admission mechanism |

## 5. Negative controls

### Control A: variable-length return alphabet without a new domain

Take the successor system `n -> n+1` on nonnegative integers. Let the section be the triangular numbers `s_m=m(m+1)/2`. The first-return edge from `s_m` to `s_{m+1}` has length `m+1`; labeling it by parity creates a new two-symbol alphabet. Every state, edge, and label remains a function of the successor path. The induced presentation is same-layer.

### Control B: genuine fiber-splitting relation

Take an old one-coordinate description `D(x,b)=x` on `N x {0,1}`. Admit the second coordinate `xi(x,b)=b`. States `(x,0)` and `(x,1)` agree under the complete old description but differ under `xi`; no function of `x` can recover `b`. This is a genuine additional determination relative to the declared old class.

These controls show that variable return length and a new alphabet are insufficient, while an old-description fiber split is sufficient.
