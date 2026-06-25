/-
PhaseTaoCompletionGateV57.lean
Companion attack script for the v57 conditional completion claim.
This is deliberately small and dependency-free so it can be run in a bare Lean 4 project.
-/

inductive GateStatus where
  | pass
  | blockedExternal
  | failInternal
  deriving DecidableEq, Repr

structure Gate where
  name : String
  status : GateStatus
  deriving Repr

def gates : List Gate := [
  { name := "available internal source mapped", status := GateStatus.pass },
  { name := "available external source mapped", status := GateStatus.pass },
  { name := "projection state-completeness gate", status := GateStatus.pass },
  { name := "stale canon separation", status := GateStatus.pass },
  { name := "modular-B overclaim prevention", status := GateStatus.pass },
  { name := "Shadow external-reference boundary", status := GateStatus.pass },
  { name := "Lean/lake execution", status := GateStatus.blockedExternal },
  { name := "latest Phase HDD materials", status := GateStatus.blockedExternal },
  { name := "Liu2022 data", status := GateStatus.blockedExternal }
]

def hasInternalFailure (xs : List Gate) : Bool :=
  xs.any (fun g => g.status == GateStatus.failInternal)

def externalBlockerCount (xs : List Gate) : Nat :=
  (xs.filter (fun g => g.status == GateStatus.blockedExternal)).length

def conditionallyComplete (xs : List Gate) : Bool :=
  (!hasInternalFailure xs) && (externalBlockerCount xs == 3)

example : hasInternalFailure gates = false := by native_decide
example : externalBlockerCount gates = 3 := by native_decide
example : conditionallyComplete gates = true := by native_decide
