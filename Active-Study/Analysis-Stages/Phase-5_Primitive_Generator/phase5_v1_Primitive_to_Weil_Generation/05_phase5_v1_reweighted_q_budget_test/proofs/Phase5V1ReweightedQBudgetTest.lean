import Std.Data.Int.Basic

namespace Phase5ReweightedQ

def budget (r : Nat) : Nat := 4 ^ r

def prefix : Nat -> Nat
| 0 => 0
| n+1 => prefix n + budget n

theorem prefix_mod_four_constant (r : Nat) (h : r > 0) : prefix r % 4 = 1 := by
  induction r with
  | zero => contradiction
  | succ n ih =>
      cases n with
      | zero => decide
      | succ k =>
          have hb : budget (Nat.succ (Nat.succ k)) % 4 = 0 := by
            unfold budget
            simp [Nat.pow_succ]
          have hp : prefix (Nat.succ k) % 4 = 1 := ih (by omega)
          unfold prefix
          omega

end Phase5ReweightedQ
