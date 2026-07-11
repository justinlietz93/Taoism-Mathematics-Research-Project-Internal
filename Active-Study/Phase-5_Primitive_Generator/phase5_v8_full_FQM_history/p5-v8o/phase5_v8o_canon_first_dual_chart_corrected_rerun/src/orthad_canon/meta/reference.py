from __future__ import annotations

from fractions import Fraction

from sympy import kronecker_symbol


def shadow_reference(n: int) -> dict:
    return {
        "address_n": n,
        "character_reference": int(kronecker_symbol(12, n)),
        "magnitude_reference": n,
        "exponent_reference": str(Fraction(n * n, 24)),
    }
