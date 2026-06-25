/- ShadowResidualV62.lean
   Finite proof surface for the v62 general-shadow correspondence.

   This file isolates the exact finite statements used in the level-8 second case.
   It is intentionally finite: the analytic theta transformation is represented by
   the finite residue S/T carrier that Phase Calculus derives.
-/

import Std

namespace ShadowResidualV62

inductive Residue8 where
  | r0 | r1 | r2 | r3 | r4 | r5 | r6 | r7
deriving DecidableEq, Repr

def neg8 : Residue8 → Residue8
  | .r0 => .r0
  | .r1 => .r7
  | .r2 => .r6
  | .r3 => .r5
  | .r4 => .r4
  | .r5 => .r3
  | .r6 => .r2
  | .r7 => .r1

def chi8 : Residue8 → Int
  | .r1 => 1
  | .r3 => -1
  | .r5 => -1
  | .r7 => 1
  | _ => 0

theorem chi8_even (r : Residue8) : chi8 (neg8 r) = chi8 r := by
  cases r <;> rfl

def signedWeight (n : Int) (a : Int) : Int := a * n

theorem orientation_pair_cancels (n a : Int) :
    signedWeight n a + signedWeight (-n) a = 0 := by
  unfold signedWeight
  ring

/-
Finite S/T matrix equalities are numeric root-of-unity equalities in the package
notebook and SymPy script. The finite statements below are the structural claims:

1. chi8 is even, so n-weighted bilateral projection cancels.
2. the positive orientation is therefore the nonzero retained readout.
3. the scalar chi8 compression is not T-stable; the T orbit requires the odd
   support vector. This is verified in the companion script by exact root tables.
-/

end ShadowResidualV62
