# p5-b3-v2 Audit Results

## Verdict

```text
REVISE_NARROW_SCOPE

CANONICAL QBL-TO-AFFINE BOUNDARY-ORBIT SEMICONJUGACY: ADOPT
FULL AFFINE INTERVAL FACTOR FROM CANONICAL ORBIT: IMPOSSIBLE, ADOPT
CANONICAL ORBIT LANGUAGE = FULL AFFINE LANGUAGE: OPEN, ADOPT
EXACT BOUNDARY-RETURN COCYCLE: ADOPT
HIGHER-ORDER DESCRIPTIVE L: NOT YET DERIVED, ADOPT

INSTANTANEOUS-L CARRY CLAIM: SPLIT BY INDEX
p5-b3 BRANCH STATUS: OPEN
NEXT INTERACTION: p5-b3-v3
```

## Integrity and reproducibility

The uploaded archive passes the stated integrity claims.

```text
ZIP SHA-256:                         PASS
Document SHA-256:                    PASS
Manifest entries:                    48
Manifest hashes and byte counts:     PASS
Manifest coverage:                   PASS
Notebook code cells:                 13
Notebook PASS cells:                 13/13
Extracted figures:                   13
Clean rebuild:                       PASS
Byte-identical ZIP rebuild:          PASS
```

The clean rebuild was performed under the original package-root basename. The rebuilt archive SHA-256 was exactly:

```text
aaf8690e8a64ac531dce4be785b37139a0551be59bebf8279142a10953b311ec
```

## Mathematical findings

### 1. Canonical orbit semiconjugacy is correctly scoped

On the canonical pre-`L` states,

\[
\pi(S_A^-)=\lambda j_A+\beta-\nu(q_A)=E_A
\]

and the boundary return gives

\[
\pi(S_{A+1}^-)=2\pi(S_A^-)+\gamma-c_{A+1}.
\]

The map is surjective onto the canonical affine orbit by construction. The result is an exact state-internal arithmetic semiconjugacy between two countable orbit systems.

The topology chosen in the document is lawful but weak: the domain orbit is discrete because the retained domain counter is discrete and unique. The load-bearing content is the internal arithmetic coordinate and commuting law, not the topological label alone.

### 2. The full-interval obstruction is correct

The canonical QBL boundary orbit is countable. The complete affine interval is uncountable. Therefore no surjective factor map from the stated canonical orbit onto the full interval can exist.

This obstruction does not rule out a factor from a larger lawful family of QBL boundary states. No such family is currently derived.

### 3. Canonical language equality remains open

Every canonical carry block belongs to the full affine cylinder language. Equality is not established. Density of the canonical error orbit would suffice, but neither density nor equidistribution is proved.

The package correctly avoids transferring full-language complexity, entropy, non-soficity, mixing, or absence of finite Markov order to the shift-orbit closure of the single canonical itinerary.

### 4. The higher-order descriptive `L` conjecture remains live

The scalar cocycle does not contain the all-depth primary pairing, chart restrictions, directed transfers, or retained-axis extension. It therefore neither proves nor refutes an Orthad-level higher-order `L` recurrence.

The current written authority places the literal rank extension at `L` in those retained Orthad structures. Their exact recurrences remain the first missing bridge.

## Required correction: split the instantaneous carry claim

The package states:

```text
A. CARRY APPENDED AT INSTANTANEOUS PRIMITIVE L: FAIL
```

That sentence is safe only under a narrow reading: the primitive `L` mutation does not append the **future** carry `c_{A+1}` as a custody coordinate.

Two distinct statements must be separated:

```text
A1. JUST-COMPLETED CARRY c_A IS RECOVERABLE AT S_A^-: PASS
A2. FUTURE CARRY c_{A+1} IS APPENDED BY S_A^- ->L S_A^+: FAIL
```

At `S_A^-`, both `T_A=nu(q_A)` and the preceding boundary count `T_{A-1}` are part of the retained boundary history, so

\[
c_A=T_A-2T_{A-1}
\]

is already a lawful derived label of the completed return. It is not a newly appended primitive-custody coordinate. By contrast,

\[
c_{A+1}=T_{A+1}-2T_A
\]

cannot be known until the next domain has completed.

This indexing correction matters because the user's conjecture concerns grammar emerging at saturation. The result does not show that no carry label can be emitted at an `L` boundary. It shows that primitive `L` does not generate the next return's carry or add it as an independent retained axis.

## Nonblocking formal boundary

The Lean file proves the cumulative-index recurrence and the abstract cocycle algebra. It does not formalize:

- the canonical orbit state type;
- well-definedness and continuity of the restricted affine map;
- the semiconjugacy theorem as a dynamical-system theorem;
- the countability obstruction;
- canonical-language inclusion.

The package correctly reports:

```text
LEAN THEOREM SURFACE PRESENT; PROOF AND COMPILATION NOT VERIFIED
```

## Strategic disposition

Do not redirect `p5-b3-v3` toward equidistribution or an invented uncountable QBL family.

The current dependency order is:

```text
primitive custody
-> primary pairing
-> chart restrictions
-> directed transfers
-> fully retained lifted state
-> terminal projection
```

The next task should derive the primary pairing's type, seed, and exact per-letter mutation. That is the first missing object needed to test whether `L` creates an independent retained distinction at the descriptive layer.
