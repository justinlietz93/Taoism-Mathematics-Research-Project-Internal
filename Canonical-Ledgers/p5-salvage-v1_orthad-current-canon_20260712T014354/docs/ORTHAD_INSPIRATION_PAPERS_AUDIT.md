# Orthad Inspiration Papers Audit

## Audit question

Do the supplied papers support the original vision of an Orthad as two opposed matrices that both mutate immediately under each primitive, each according to its own orientation?

## Verdict

```text
YES AS STRUCTURAL INSPIRATION
NO AS A DERIVED QBL LAW
```

The Yin-Yang overset-grid papers strongly support the shape of the vision: two complementary local realizations of one global field, related by reversible coordinate transformations, evolved in local coordinates, and coupled through overlap transfer.

They do not derive the `B/Q/L` matrix actions, the exact meaning of opposition, or a primary pairing.

## Strongest direct findings

### 1. Two equal-status patches

The Yin and Yang patches are geometrically identical and neither is the privileged global grid. The Yang patch is a rotated version of the Yin patch.

This supports two equal-status Orthad matrices rather than one main matrix plus a secondary correction matrix.

### 2. Opposition as orientation, not scalar sign

The coordinate map in the axis-free Yin-Yang construction is built from rotations and satisfies `M^-1 = M`.

This gives a precise external example of an involutive opposition relation: switch orientation twice and return to the starting chart.

It does not mean the two Orthad matrices are negatives of each other.

### 3. One event, two local evolutions

The same physical transport equation is written and solved in each rotated coordinate system. Local components differ because the coordinate frames differ.

This is a close analogue of one `B`, `Q`, or `L` event immediately mutating both Orthad matrices through different orientation-sensitive actions.

### 4. Transfer is active and typed

Data crossing the overlap is not copied blindly. Coordinates and vector components are transformed, and local boundary values are interpolated from the complementary patch.

This supports active bidirectional transfer maps with their own update burden.

### 5. Agreement is weaker than conservation

Overset interpolation can produce locally plausible values while losing global conservation. Additional constraints are required.

This supports the requirement that Orthad overlap consistency must preserve an invariant of the retained object, not only numerical equality at selected entries.

## Useful formal languages

### Cech cohomology

Useful for transition functions, overlap consistency, and cocycle conditions. It may describe when two local matrix views glue into one global retained structure.

### Cellular sheaves

Useful for attaching local data and enforcing compatibility through restriction maps. It may support a computational consistency layer over a graph of states or chart regions.

Caution: sheaf language should not be allowed to pre-decide that the matrices are passive restrictions of a prior pairing.

### Homotopy lifting

Useful for distinguishing visible return from lifted-state return and for formalizing retained path/sheet history.

### Asynchronous automata

Useful for the idea that one shared action updates several local components according to their local states and then synchronizes them.

## Supplemental rather than core

- Trace monoids: exact word order and partial commutation.
- Domain decomposition and transmission PDEs: interface coupling tools.
- Solar magnetic topology and MHD: physical analogues of polarity, reconnection, and invariant topology.
- Finite quadratic modules and Weil representations: downstream algebraic targets after the Orthad-to-FQM bridge is proved.

## Formalization consequences

The papers support this shell:

\[
U_t=\Sigma(X_t),
\]

\[
M^+_{t+1}=\Phi^+_{U_t}(X_t,\mathcal O_t),
\qquad
M^-_{t+1}=\Phi^-_{U_t}(X_t,\mathcal O_t),
\]

\[
T^{+\to-}_{t+1}=\Psi^{+\to-}_{U_t}(X_t,\mathcal O_t),
\qquad
T^{-\to+}_{t+1}=\Psi^{-\to+}_{U_t}(X_t,\mathcal O_t).
\]

All four updates belong to one tick. The next primitive is not determined until the complete updated state exists.

The papers do not determine the functions `Phi` or `Psi`.

## Main correction to the previous trunk

The statement

```text
one primary object is upstream of two chart restrictions and two transfers
```

was stronger than the original vision and stronger than the inspiration papers establish.

The repaired statement is:

```text
two opposed matrix realizations and their bidirectional transfer data must evolve
coherently as one driven Orthad state at every primitive tick.
```

A common primary pairing remains one candidate explanation of that coherence. It is not yet the ratified causal order.
