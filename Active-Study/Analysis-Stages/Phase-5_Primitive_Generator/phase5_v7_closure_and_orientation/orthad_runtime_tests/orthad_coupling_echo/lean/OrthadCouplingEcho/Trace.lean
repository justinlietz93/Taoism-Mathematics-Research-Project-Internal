namespace OrthadCouplingEcho

inductive Chart where | A | B | C deriving DecidableEq, Repr
inductive Kind where | Q | B | L | P deriving DecidableEq, Repr

structure Event where
  kind : Kind
  a : Chart
  b : Option Chart
  sign : Int
  deriving Repr

def touches (e : Event) (c : Chart) : Bool :=
  e.a == c || e.b == some c

def dependent (x y : Event) : Bool :=
  match x.kind, y.kind with
  | Kind.P, _ => true
  | _, Kind.P => true
  | _, _ => touches x y.a || match y.b with | some c => touches x c | none => false

-- Formalization surface for the smoke package.
-- Next theorem target: the executable Foata layerer is invariant under adjacent swaps
-- where dependent x y = false.

def gateLabel (pass : Bool) : String :=
  if pass then "PASS" else "FAIL"

#eval gateLabel true

end OrthadCouplingEcho
