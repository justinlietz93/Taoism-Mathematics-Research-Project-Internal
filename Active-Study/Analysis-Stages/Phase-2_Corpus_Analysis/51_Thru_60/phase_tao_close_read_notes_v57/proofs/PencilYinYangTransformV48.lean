-- PencilYinYangTransformV48.lean
-- Coordinate-level attack of the Pencil Code Yin-Yang transform witness.
-- Map T(x,y,z)=(-x,-z,-y).  It is involutive and norm-preserving.

def T (p : Int × Int × Int) : Int × Int × Int :=
  (-p.1, -p.2.2, -p.2.1)

theorem T_involutive (p : Int × Int × Int) : T (T p) = p := by
  cases p with
  | mk x yz =>
    cases yz with
    | mk y z =>
      simp [T]

theorem T_norm_sq_preserved (x y z : Int) :
  let p : Int × Int × Int := (x,y,z)
  let q := T p
  q.1*q.1 + q.2.1*q.2.1 + q.2.2*q.2.2 = x*x + y*y + z*z := by
  simp [T]
  ring
