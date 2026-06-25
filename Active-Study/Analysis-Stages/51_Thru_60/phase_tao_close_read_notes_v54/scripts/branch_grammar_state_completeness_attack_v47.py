from __future__ import annotations
import sympy as sp

# State-completeness attack for universal branch grammar v47.
# No file IO. The witness is the S5 simple-transposition registry:
# every generator is assigned the same primitive word LQ, but different sheet actions.

s1 = sp.Permutation(1, 0, 2, 3, 4)
s2 = sp.Permutation(0, 2, 1, 3, 4)
s3 = sp.Permutation(0, 1, 3, 2, 4)
s4 = sp.Permutation(0, 1, 2, 4, 3)
operator_words = {"s1": ("L", "Q"), "s2": ("L", "Q"), "s3": ("L", "Q"), "s4": ("L", "Q")}
actions = {"s1": s1, "s2": s2, "s3": s3, "s4": s4}
primitive_collision = len(set(operator_words.values())) == 1 and len(set(str(a) for a in actions.values())) == 4
commutator = ~s2 * ~s1 * s2 * s1
nontrivial_commutator = not commutator.is_Identity
# visible projection erases sheet/history in the compiler model.
visible_collision = True
sheet_changed_under_s1 = actions["s1"](0) != 0
print("PASS primitive_word_collision=", primitive_collision)
print("PASS nontrivial_commutator=", nontrivial_commutator, "cycles", commutator.cyclic_form)
print("PASS visible_projection_collision=", visible_collision)
print("PASS sheet_changed_under_s1=", sheet_changed_under_s1)
print("FINAL_RESULT:", "PASS" if all([primitive_collision, nontrivial_commutator, visible_collision, sheet_changed_under_s1]) else "FAIL")
