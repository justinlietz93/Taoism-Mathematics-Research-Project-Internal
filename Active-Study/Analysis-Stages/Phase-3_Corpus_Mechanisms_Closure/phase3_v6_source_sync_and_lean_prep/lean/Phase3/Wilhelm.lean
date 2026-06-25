import Phase3.Core

namespace Phase3
namespace Wilhelm

abbrev Carrier := Fin 6 -> Bool

def flipLine (c : Carrier) (i : Fin 6) : Carrier :=
  fun j => if j = i then !c j else c j

structure LineState where
  carrier : Carrier
  selected : Fin 6

def step (s : LineState) : LineState :=
  { carrier := flipLine s.carrier s.selected, selected := s.selected }

def carrierProjection (s : LineState) : Carrier := s.carrier

-- Phase 3 v5 theorem target:
-- carrierProjection alone is not transition-complete because selected line changes the next carrier.

end Wilhelm
end Phase3
