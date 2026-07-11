# First-L orthogonality cases

Use the block convention

```text
[[P_old, C_right],
 [C_left, p_new]]

C_right = P(old,new)
C_left  = P(new,old)
```

- Right orthogonality forces `C_right=0` only.
- Left orthogonality forces `C_left=0` only.
- Two-sided orthogonality forces both zero.
- Symmetry or Hermitianity plus either one-sided condition forces the other side, provided the relevant adjoint law exists.
- With no symmetry law, neither one-sided condition implies the other.

Counterexample over the integers:

```text
P = [[1,1],
     [0,1]]
```

For old axis `e1` and newborn axis `e2`, `P(e2,e1)=0` but `P(e1,e2)=1`. Therefore one-sided orthogonality does not yield block diagonal form.
