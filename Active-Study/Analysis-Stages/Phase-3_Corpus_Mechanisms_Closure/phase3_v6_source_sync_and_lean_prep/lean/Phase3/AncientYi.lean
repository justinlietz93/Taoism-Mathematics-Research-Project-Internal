import Phase3.ModularB

namespace Phase3
namespace AncientYi

/-- Digits are stored least-significant first. -/
def value : List Nat -> Nat
  | [] => 0
  | d :: ds => d + 8 * value ds

def allSeven : List Nat -> Bool
  | [] => false
  | [d] => d == 7
  | d :: ds => (d == 7) && allSeven ds

def succ : List Nat -> List Nat
  | [] => [1]
  | d :: ds => if d < 7 then (d + 1) :: ds else 0 :: succ ds

-- Proof obligation target: succ [7] = [0,1]
-- Proof obligation target: value (succ ds) = value ds + 1 for fixed-width nonterminal ds.

end AncientYi
end Phase3
