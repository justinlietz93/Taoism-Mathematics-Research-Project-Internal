from __future__ import annotations

import sympy as sp

p0, p1, p2, d = sp.symbols("p0 p1 p2 d", integer=True)
# Oriented transition from i to j is p_j - p_i over an abelian module.
t01 = p1 - p0
t12 = p2 - p1
t20 = p0 - p2
legal_residual = sp.simplify(t01 + t12 + t20)
illegal_residual = sp.simplify(t01 + t12 + (t20 + d))

print("legal_triangle_residual =", legal_residual)
print("corrupted_triangle_residual =", illegal_residual)
print("PASS" if legal_residual == 0 and illegal_residual == d else "FAIL")
