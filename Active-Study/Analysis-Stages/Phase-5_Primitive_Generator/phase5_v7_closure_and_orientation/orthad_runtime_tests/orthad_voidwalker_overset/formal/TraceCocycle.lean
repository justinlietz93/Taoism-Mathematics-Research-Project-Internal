/-
Small formal surface for the harness.
This is intentionally not a proof of the full Orthad theorem. It records the
local algebraic gate used by the smoke runtime: potential-derived oriented
transfers close around a triangle, while a corrupted latch leaves a residual.
-/

import Std

namespace OrthadVoidwalkerOverset

variable {G : Type} [AddCommGroup G]

abbrev T (p : Nat -> G) (i j : Nat) : G := p j - p i

theorem triangle_cocycle_zero (p : Nat -> G) (i j k : Nat) :
    T p i j + T p j k + T p k i = 0 := by
  simp [T]
  abel

theorem corrupted_triangle_residual (p : Nat -> G) (i j k : Nat) (d : G) :
    T p i j + T p j k + (T p k i + d) = d := by
  simp [T]
  abel

end OrthadVoidwalkerOverset
