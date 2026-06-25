# v59 Shadow Residual Correction

## Classification

Axiom-core bridge correction / retained-orientation channel repair.

## Corrected result

The v58 obstruction proof is retained. The v58 verdict is replaced.

The Shadow Residual does **not** remain external to the lift. It closes inside the lift as a retained-orientation quantum-modular channel. The scalar bilateral projection is the zero projection; that zero is the state-completeness gate firing, not a failure of custody.

## Correct theorem split

### Proved

Let

```math
R(\tau)=\sum_{n\ge 1}\chi_{12}(n)\,n\,q^{n^2/24},
```

with

```math
\chi_{12}(n)=
\begin{cases}
+1,&n\equiv 1,11\pmod {12},\\
-1,&n\equiv 5,7\pmod {12},\\
0,&(n,6)>1.
\end{cases}
```

The character is even:

```math
\chi_{12}(-n)=\chi_{12}(n).
```

Therefore

```math
\chi_{12}(-n)(-n)=-\chi_{12}(n)n.
```

The bilateral scalar Jacobi derivative cancels term by term:

```math
\sum_{n\in\mathbb Z}\chi_{12}(n)nq^{n^2/24}=0.
```

This proves scalar/bilateral closure fails and orientation data is required.

### Structural identification

The positive-half series is a partial theta / false theta object:

```math
R(\tau)=\sum_{n\ge 1}\chi_{12}(n)nq^{n^2/24}.
```

Its shadow candidate is the same oriented support and sign pattern with the `n` weight removed:

```math
\Theta_\chi^+(\tau)=\sum_{n\ge 1}\chi_{12}(n)q^{n^2/24}.
```

By Euler's eta expansion,

```math
\Theta_\chi^+(\tau)=\eta(\tau).
```

Equivalently, the even bilateral normalization is

```math
\frac12\sum_{n\in\mathbb Z}\chi_{12}(n)q^{n^2/24}=\eta(\tau).
```

Thus the weight arithmetic is consistent: a weight-3/2 false theta has a weight `2 - 3/2 = 1/2` shadow, and the candidate is `\eta`.

### Correct bridge interpretation

The scalar projection is not state-complete. That is not a reason to keep the Shadow external. It is the ordinary signal that the projected witness has erased retained state.

The Shadow lives in the retained orientation / half-lattice / residue-vector channel. The symmetric scalar projection annihilates that channel. The lift exists to carry exactly this kind of state.

The correct statement is:

```text
Shadow Residual closes inside the lift as a retained-orientation quantum-modular channel.
The scalar bilateral readout is the zero projection.
The zero projection is the state-completeness gate firing.
The explicit vector-valued multiplier/completion remains the finite open task.
```

## Required replacement: Note 66 bridge interpretation/result

Replace the stale block:

```text
Shadow Residual remains external to Phase custody, but the reason is now sharper:
Shadow uses a terminal oriented unary-theta readout channel.
It is compatible with Jacobi-variable derivative machinery only after retaining residue/orientation state.
A scalar readout without that retained state is not state-complete.
```

with:

```text
Shadow Residual closes inside Phase custody as a retained-orientation quantum-modular channel. The scalar bilateral Jacobi derivative vanishes because the symmetric projection annihilates the oriented half-lattice channel. This is the state-completeness gate firing, not evidence that the Shadow is external.

The honest closure target is the oriented half-lattice / residue-vector unary-theta channel. The n-weighted positive half is the weight-3/2 false-theta Shadow Residual. The same support and signs with n^0 weighting give eta, the weight-1/2 shadow. The remaining task is explicit: construct the two-orientation vector-valued completion and its multiplier system.
```

## Required replacement: blocker row

Replace:

```csv
External,Modular forms / Shadow residual,reference-bridge-open,92,exact Jacobi/unary-theta transformation proof; Shadow remains external
```

with:

```csv
Internal/Bridge,Modular forms / Shadow residual,retained-orientation-channel-open,94,two-orientation vector-valued unary-theta completion; explicit weight-3/2 multiplier and eta shadow proof pending
```

## Required replacement: dependency graph row

Replace status/verdict fields equivalent to:

```csv
C09_shadow_external_reference,Shadow Residual remains external comparison/reference; it is not loaded into the lifted state.,...,REFERENCE_OPEN,Prove residual is generated as carried state inside the lift rather than terminal comparison channel.,Jacobi/unary-theta transformation proof for residual channel.
```

with:

```csv
C09_shadow_retained_orientation_channel,Shadow Residual closes inside the lift as a retained-orientation quantum-modular channel; scalar bilateral readout is the zero projection.,C03_corrected_orthad_custody,C02_state_completeness_gate,POSITIVE_HALF_FALSE_THETA_IDENTIFIED; EXPLICIT_MULTIPLIER_PENDING,Construct the two-orientation vector-valued unary-theta completion and prove its weight-3/2 multiplier with eta as shadow.,Vector-valued unary-theta multiplier proof and Eichler-integral completion for chi12 n q^(n^2/24).
```

## Required replacement: cross-corpus kernel row

Replace:

```csv
Zagier / Shadow modular forms,external,PASS,OPEN,N/A,N/A,PASS,PASS,EXTERNAL_REFERENCE_NOT_LOADED
```

with:

```csv
Zagier / Shadow modular forms,retained_orientation_channel,PASS,OPEN,N/A,N/A,PASS,PASS,RETAINED_ORIENTATION_CHANNEL / QUANTUM_MODULAR / EXPLICIT_MULTIPLIER_PENDING
```

Replace:

```csv
Zagier / Shadow modular forms,external,"q-series support, character, exponent law, derivative/readout variable choice",eta/q-derivative/scalar coefficient sequence,OPEN; Shadow remains external reference,"Shadow residual n coefficient aligns with Jacobi/unary theta derivative path, not ordinary q-derivative.",EXTERNAL_REFERENCE_NOT_LOADED
```

with:

```csv
Zagier / Shadow modular forms,retained_orientation_channel,"q-series support, character, exponent law, derivative/readout variable choice, half-lattice orientation",eta/q-derivative/scalar coefficient sequence,OPEN; explicit multiplier pending,"Shadow residual n coefficient aligns with oriented half-lattice Jacobi/unary-theta derivative path. The scalar bilateral channel cancels; the retained-orientation channel carries the object.",RETAINED_ORIENTATION_CHANNEL / QUANTUM_MODULAR / EXPLICIT_MULTIPLIER_PENDING
```

## Required replacement: Follow spec

Replace:

```text
In follow, the Shadow Residual is not loaded into the lift. It is the external reference, the true pattern on the wall that the projected readout is compared against. The transport never touches it. The lifted object evolves on its own; the Orthad reads it; the readout is checked against the residual's known expression at that depth.
```

with:

```text
In follow, the Shadow Residual is not loaded as scalar cargo and is not regenerated by a mod-6 phase trick. It is carried only as retained orientation: half-lattice side, residue-vector channel, cusp-path, and multiplier data. The scalar bilateral readout projects this channel to zero. The Orthad readout must therefore be vector-valued/oriented before scalar comparison. The external written q-series remains the reference expression, but the Shadow channel itself is internal to the lift once orientation custody is retained.
```

## Status ledger

| Item | Status |
|---|---|
| Scalar/bilateral Jacobi derivative obstruction | PROVED |
| Requirement for orientation / half-lattice / residue-vector state | PROVED |
| Positive-half series identified as false theta / partial theta | STRUCTURAL_IDENTIFICATION |
| n^0 support/sign shadow candidate equals eta | FINITE_COEFFICIENT_VERIFIED; STANDARD_IDENTITY_USED |
| Shadow closes inside lift as retained orientation channel | STRUCTURAL_IDENTIFICATION |
| Explicit two-component vector-valued multiplier/completion | OPEN_FINITE_TASK |

## Next computation

Build the two-orientation vector-valued object

```math
\mathbf R(\tau)=
\begin{pmatrix}
R_+(\tau)\\
R_-(\tau)
\end{pmatrix},
\qquad
R_+(\tau)=\sum_{n\ge1}\chi_{12}(n)nq^{n^2/24},
\qquad
R_-(\tau)=-R_+(\tau)
```

as the derivative/orientation channel, then construct the corresponding non-holomorphic Eichler-integral completion with shadow

```math
\eta(\tau)=\sum_{n\ge1}\chi_{12}(n)q^{n^2/24}.
```

The closure gate is the explicit weight-3/2 transformation law under the relevant congruence generators, including the exact multiplier matrix on the two orientation components.
