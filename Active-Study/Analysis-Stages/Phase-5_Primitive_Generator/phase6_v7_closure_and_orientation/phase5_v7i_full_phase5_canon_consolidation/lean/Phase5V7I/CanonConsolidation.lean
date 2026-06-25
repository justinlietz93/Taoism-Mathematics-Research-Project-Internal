/-
Phase 5 v7i Lean surface.
Local execution pending. This file attacks the canon at the proposition level:
no odd folded-carrier closure is asserted, product-module closure is separated
from arbitrary-history classification, and hand-supplied c_ij is not generation evidence.
-/

namespace Phase5V7I

inductive ClaimStatus where
  | canon
  | supported_bounded
  | open_frontier
  | rejected
  deriving DecidableEq, Repr

structure CanonLayer where
  name : String
  status : ClaimStatus

structure Guardrail where
  name : String
  passed : Bool

-- Core statuses encoded as data, not proof of arithmetic.
def doubledCarrier : CanonLayer := { name := "Z/(2N)Z orientation-doubled cyclic carrier", status := ClaimStatus.canon }
def productPairwise : CanonLayer := { name := "product modules with native pairwise coupling tensors", status := ClaimStatus.supported_bounded }
def arbitraryHistory : CanonLayer := { name := "complete arbitrary QBL history classification", status := ClaimStatus.open_frontier }
def tripleTensor : CanonLayer := { name := "independent higher-order Weil tensor", status := ClaimStatus.rejected }

theorem no_even_only_law : doubledCarrier.status = ClaimStatus.canon := rfl

theorem arbitrary_history_not_closed : arbitraryHistory.status = ClaimStatus.open_frontier := rfl

theorem triple_tensor_rejected_in_tested_layer : tripleTensor.status = ClaimStatus.rejected := rfl

-- Guardrail: this is intentionally not a theorem claiming all product modules are classified.
def allProductModulesClassified : Bool := false

theorem no_full_product_overclaim : allProductModulesClassified = false := rfl

end Phase5V7I
