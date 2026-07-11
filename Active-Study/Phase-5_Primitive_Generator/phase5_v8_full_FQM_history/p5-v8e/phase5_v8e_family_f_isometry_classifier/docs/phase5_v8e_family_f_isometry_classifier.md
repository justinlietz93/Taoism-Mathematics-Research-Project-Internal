# Phase 5 v8e: Family-F Isometry Classifier

## Scope

Family F presentations are coupling graphs whose vertices are doubled-cyclic carriers and whose edges are representative-invariant pairwise bilinear couplings.

## Graph decomposition

If the coupling graph splits into connected components, then all cross-component edge coefficients are zero. Therefore

```text
b = direct_sum b_component
q = direct_sum q_component
```

and the isometry class of the whole presentation is the multiset of connected component classes.

## Size-2 classifier

For each pair `(D1,D2)` in `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 24, 32]` with `D1*D2 <= 1024`, the classifier enumerates exact automorphisms of `Z/D1Z x Z/D2Z` and computes orbit classes of all representative-invariant edge residues.

This is a classifier on the stated bounded size-2 range because equality is decided by exact orbit membership, not by a structural key.

## Invariant audit

The requested compact invariant set was computed, including Gauss-Milgram signature and p-primary signatures. It fails to separate all exact orbit classes for named even 2-primary pairs. Those failures are recorded as residual walls, not widened into a false closure.

## Rank >= 3 blocker

Archival v7t/v7u routing generated connected components of size >= 3. v8e does not classify those components. They remain blocking open.
