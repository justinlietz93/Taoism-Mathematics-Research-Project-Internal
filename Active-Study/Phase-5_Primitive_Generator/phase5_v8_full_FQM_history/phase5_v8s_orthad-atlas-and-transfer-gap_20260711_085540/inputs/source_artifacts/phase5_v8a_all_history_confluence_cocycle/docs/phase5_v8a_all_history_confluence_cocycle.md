# Phase 5 v8a: All-History Confluence + Cocycle Compatibility Attack

## Objective

Recover the old all-history blocker and attack it directly:

```text
admissible retained QBL history
  -> support-derived legal rewrites
  -> trace/Foata normal form
  -> Orthad lens transition records T
  -> cocycle compatibility
```

## Classification

`Axiom-core / formal-combinatorial closure layer`

## Result

```text
ALL_HISTORY_CONFLUENCE_AND_COCYCLE_COMPATIBILITY_CLOSED_CONDITIONALLY_FOR_DEFINED_ADMISSIBLE_RETAINED_QBL_SYSTEM
```

## Definitions

### Event alphabet

The retained event alphabet is:

```text
Q_a
B_a
L_a
O_ab
R_a
```

where `a,b` are chart/axis indices.

### Support-derived independence

Two events are legally swappable exactly when retained write/read supports, birth supports, and edge supports do not conflict.

This means independence is not hand-labeled. It is derived from event support.

### Foata normal form

For a finite history `h`, each event is seated at the first layer after all prior dependent events.

This gives the canonical trace normal form used by the confluence gate.

### Transition cochain

The lens transition assignment is treated as an exact cochain:

```text
T_ab = lambda_b - lambda_a      mod 12
```

Equivalently, multiplicative notation gives:

```text
T_ab T_bc T_ca = 1
```

for every admitted chart triangle.

## Closure claim

For every finite history inside the stated admissible retained-history system:

```text
legal rewrite equivalence preserves:
  Foata normal form
  retained compiler signature
  exact transition cocycle class
```

This is conditional on the explicit admissibility definition. It does not yet prove that every possible future physical Orthad implementation admits no extra event outside this support semantics.

## Hard gates

```text
critical pair checks: PASS
diamond checks: PASS
random legal rewrite checks: PASS
cocycle checks: PASS
gauge checks: PASS
negative controls: PASS
```

## Boundary

This pass closes the old all-history blocker only after replacing the vague target:

```text
arbitrary QBL history
```

with the controlled target:

```text
finite admissible retained QBL history under explicit support-derived independence
```

That correction is necessary. Without it, arbitrary can include histories with undefined birth order, illegal edge access, or projector mutation.
