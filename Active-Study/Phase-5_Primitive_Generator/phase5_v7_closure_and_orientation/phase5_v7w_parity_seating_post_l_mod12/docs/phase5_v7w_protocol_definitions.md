# Protocol Definitions

## Native retained variables

```text
s6       pre-L mod-6 seat
pL       L-created parity latch
εL       lens parity sign
s12      post-L retained mod-12 seat
χ12      terminal support/sign readout from s12
```

## Acceptance gates

```text
G1: no mod-6-only character reproduces χ12 on support.
G2: s12 = s6 + 6*pL reconstructs all residues 0..11.
G3: n=1 and n=7 share pre-L seat but separate post-L.
G4: χ12(s12(n)) = χ12(n) for tested support terms.
G5: terminal readout R does not mutate retained post-L seat.
```

## Kill conditions

```text
K1: post-L seat fails any residue reconstruction.
K2: n=1 and n=7 remain collapsed after L.
K3: χ12 is only recovered by injecting scalar cargo.
K4: supportless residues acquire nonzero character.
```
