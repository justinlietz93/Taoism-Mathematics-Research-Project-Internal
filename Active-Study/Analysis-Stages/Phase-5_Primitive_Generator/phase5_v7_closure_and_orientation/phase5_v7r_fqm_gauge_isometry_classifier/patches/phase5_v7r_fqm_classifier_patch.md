# Phase 5 v7r Patch

Replace:

```text
canonical coupling tensor C
```

with:

```text
canonical finite module gauge/isometry class; C is a coordinate presentation
```

Add classifier gate:

```text
canon(S) = canon(P^T S P)
```

Add rejection gate:

```text
radical(S) != {0} -> reject before FQM admission
```

Add warning gate:

```text
if 2 divides module order, require explicit 2-primary normalization policy before final canon
```
