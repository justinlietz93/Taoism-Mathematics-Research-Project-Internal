from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
import importlib.util
import json
import math
import shutil
import sys

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("model", HERE / "20260711T145038_model.py")
model = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(model)


@dataclass
class Custody:
    A: int = 0
    u: int = 1
    v: int = 1
    phase_quarters: int = 0
    k: int = 0
    j: int = 1
    word: str = ""

    def pair(self) -> list[int]:
        return [self.u, self.v]


def positions(A: int) -> int:
    return 6 * (2 ** A)


def capacity(state: Custody) -> int:
    if state.j == 1:
        return 2
    if state.j == 2:
        return 4
    return 2 ** (2 * state.j)


def next_pair(state: Custody) -> tuple[int, int]:
    return state.v, state.u + state.v


def can_q(state: Custody) -> bool:
    return state.k < positions(state.A) - 1


def can_b(state: Custody) -> bool:
    nu, nv = next_pair(state)
    if state.k < positions(state.A) - 1:
        return nu * nv <= capacity(state)
    return state.u * state.v < capacity(state)


def step(state: Custody) -> tuple[str, Custody]:
    before = Custody(**asdict(state))
    if can_b(before):
        nu, nv = next_pair(before)
        state.u, state.v = nu, nv
        state.word += "B"
        return "B", state
    if can_q(before):
        state.phase_quarters += 1
        state.k += 1
        state.j += 1
        state.word += "Q"
        return "Q", state
    state.A += 1
    state.k = 0
    state.j += 1
    state.word += "L"
    return "L", state


def primitive_trace() -> list[dict]:
    state = Custody()
    rows: list[dict] = []
    while True:
        before = Custody(**asdict(state))
        primitive, state = step(state)
        rows.append({
            "step": len(rows) + 1,
            "before": asdict(before),
            "can_b": can_b(before),
            "can_q": can_q(before),
            "capacity": capacity(before),
            "selected": primitive,
            "after": asdict(state),
        })
        if primitive == "L":
            break
    before = Custody(**asdict(state))
    primitive, state = step(state)
    rows.append({
        "step": len(rows) + 1,
        "before": asdict(before),
        "can_b": can_b(before),
        "can_q": can_q(before),
        "capacity": capacity(before),
        "selected": primitive,
        "after": asdict(state),
    })
    return rows


def matrix_rank_2x2(matrix: list[list[int]]) -> int:
    if all(value == 0 for row in matrix for value in row):
        return 0
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return 2 if determinant != 0 else 1


def write_docs() -> None:
    out = ROOT / "outputs"
    docs = ROOT / "docs"
    trace_dir = ROOT / "trace"

    model.write_csv(out / f"{model.STAMP}_pairing_representability_source_ledger.csv", model.SOURCE_ROWS)
    model.write_json(out / f"{model.STAMP}_inference_rules.json", model.INFERENCE_RULES)
    model.write_json(out / f"{model.STAMP}_claim_model.json", model.CLAIM_MODEL)

    rows = primitive_trace()
    with (trace_dir / f"{model.STAMP}_primitive_trace.jsonl").open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True) + "\n")
    lrow = next(row for row in rows if row["selected"] == "L")
    next_b = rows[rows.index(lrow) + 1]
    sanity = {
        "word": lrow["after"]["word"],
        "floor_pair": [lrow["before"]["u"], lrow["before"]["v"]],
        "floor_product": lrow["before"]["u"] * lrow["before"]["v"],
        "Q_steps": lrow["after"]["word"].count("Q"),
        "phase_witness": ["1", "i", "-1", "-i"][lrow["after"]["phase_quarters"] % 4],
        "after_L": lrow["after"],
        "after_next_B": next_b["after"],
        "pass": lrow["after"]["word"] == model.EXPECTED_WORD and next_b["after"]["pair"] if False else True,
    }
    sanity["pass"] = (
        sanity["word"] == model.EXPECTED_WORD
        and sanity["floor_pair"] == [55, 89]
        and sanity["floor_product"] == 4895
        and sanity["Q_steps"] == 5
        and sanity["phase_witness"] == "i"
        and sanity["after_L"]["A"] == 1
        and sanity["after_L"]["k"] == 0
        and sanity["after_L"]["j"] == 7
        and [sanity["after_next_B"]["u"], sanity["after_next_B"]["v"]] == [89, 144]
    )
    model.write_json(out / f"{model.STAMP}_primitive_sanity_check.json", sanity)

    orth_cases = {
        "block_convention": "[[P_old,C_right],[C_left,p_new]], where C_right=P(old,new) and C_left=P(new,old)",
        "cases": [
            {"case": "right_orthogonality_only", "forced": ["C_right=0"], "not_forced": ["C_left=0"]},
            {"case": "left_orthogonality_only", "forced": ["C_left=0"], "not_forced": ["C_right=0"]},
            {"case": "two_sided_orthogonality", "forced": ["C_right=0", "C_left=0"], "not_forced": []},
            {"case": "symmetric_or_Hermitian_plus_right", "forced": ["C_right=0", "C_left=0"], "not_forced": []},
            {"case": "no_symmetry_law", "forced": [], "not_forced": ["either mixed block"]},
        ],
        "counterexample": {
            "matrix": [[1, 1], [0, 1]],
            "old_axis": [1, 0],
            "new_axis": [0, 1],
            "P_new_old": 0,
            "P_old_new": 1,
            "conclusion": "left orthogonality does not force right orthogonality",
        },
    }
    model.write_json(out / f"{model.STAMP}_first_L_mixed_block_cases.json", orth_cases)

    rank_rows = [
        {"rank_notion": "architectural_axis_count", "status": "DERIVED", "first_L_effect": "1->2", "reason": "literal source obligation"},
        {"rank_notion": "argument_object_rank_or_dimension", "status": "NOT_YET_DERIVED", "first_L_effect": "open", "reason": "axis is not proved to be a basis vector or free generator"},
        {"rank_notion": "block_matrix_size", "status": "CONDITIONAL_ON_REPRESENTATION", "first_L_effect": "1 block->2 blocks", "reason": "requires a block presentation"},
        {"rank_notion": "pairing_morphism_rank", "status": "NOT_YET_TYPED", "first_L_effect": "open", "reason": "representability and rank function absent"},
        {"rank_notion": "nondegenerate_pairing_rank", "status": "NOT_YET_TYPED", "first_L_effect": "open", "reason": "nondegeneracy absent"},
    ]
    model.write_csv(out / f"{model.STAMP}_pairing_rank_semantics.csv", rank_rows)
    rank_example = {
        "old_matrix": [[1]],
        "extended_matrix_with_p_new_zero": [[1, 0], [0, 0]],
        "old_block_size": 1,
        "new_block_size": 2,
        "old_algebraic_rank": 1,
        "new_algebraic_rank": matrix_rank_2x2([[1, 0], [0, 0]]),
        "conclusion": "block size increases while algebraic rank does not",
    }
    model.write_json(out / f"{model.STAMP}_rank_zero_birth_counterexample.json", rank_example)

    representability = {
        "source_forced_object": "Pair(A,B) with contravariant pullback in both slots",
        "candidate_model": "P:H->D(H)",
        "status": "NOT_YET_DERIVED",
        "missing_axiom": "For every H, a representing dual object D(H) and a natural isomorphism Pair(A,H) ~= Hom(A,D(H)), natural in A and compatible with pullback in H.",
        "finite_dimensionality_assumed": False,
        "currying_assumed": False,
        "reflexivity_assumed": False,
        "perfectness_assumed": False,
    }
    model.write_json(out / f"{model.STAMP}_pairing_representability.json", representability)

    gauge = {
        "licensed_relation": "equivalence generated by lawful source-authorized representation changes G_law",
        "full_Aut_H_quotient": "ADMISSIBLE_MODEL_NOT_DERIVED",
        "reason": "source says a lawful basis change may act by U*PU, not that all automorphisms are lawful",
        "exact_primary_seed": "NOT_YET_DERIVED",
    }
    model.write_json(out / f"{model.STAMP}_seed_gauge_quotient_boundary.json", gauge)

    provenance = []
    for path, role in [
        (ROOT / "inputs" / f"{model.STAMP}_p5_v8w_ACCEPTED_BASELINE.zip", "accepted baseline"),
        (ROOT / "inputs" / f"{model.STAMP}_p5_v8w_AUDIT_AND_p5_v8x_TASK.zip", "task source"),
        (ROOT / "inputs" / f"{model.STAMP}_QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2.md", "primary authority"),
        (ROOT / "inputs" / f"{model.STAMP}_orthad-diagram-v5.png", "architecture diagram"),
    ]:
        provenance.append({"role": role, "path": str(path.relative_to(ROOT)), "sha256": model.sha256(path), "bytes": path.stat().st_size})
    model.write_csv(out / f"{model.STAMP}_baseline_and_source_provenance.csv", provenance)

    source_interface = """# Source-forced pairing interface

## Derived interface

The four ratified expressions require one primary **two-slot pairing object** and contravariant restriction in each argument. The weakest interface used here is:

```text
objects A,B in a retained-argument class C
Pair(A,B)                         pairing objects with two slots
(f,g)^*: Pair(A,B) -> Pair(A',B')
    for f:A'->A and g:B'->B
P_t in Pair(H_t,H_t)
```

The pullback obeys identity and composition in both slots. Then every chart block has the common form

```text
Omega_plus  = (iota_plus,iota_plus)^* P_t
Omega_minus = (iota_minus,iota_minus)^* P_t
T_plus_minus  = (iota_minus,iota_plus)^* P_t
T_minus_plus  = (iota_plus,iota_minus)^* P_t
```

At this layer `*` names first-slot pullback. It is not yet an adjoint, conjugate transpose, scalar involution, or duality functor.

A scalar-valued form, a represented morphism `H_t -> D(H_t)`, and a kernel/profunctor realization are models of this interface. None is forced by the source text.

```text
SOURCE_FORCED_PAIRING_INTERFACE: DERIVED
```
"""
    (docs / f"{model.STAMP}_source_forced_pairing_interface.md").write_text(source_interface, encoding="utf-8")

    pairing_repr_doc = """# Pairing representability

The two-slot pullback interface does not imply a dual object or a curried morphism. To derive

```text
P_t : H_t -> D(H_t)
```

one needs the exact representability axiom

```text
for every H, there exists D(H) and a natural isomorphism
Pair(A,H) ~= Hom(A,D(H))
natural in A and compatible with pullback in H.
```

No source row supplies this axiom. Finite-dimensionality, reflexivity, currying, and perfectness are not assumed.

```text
PAIRING_REPRESENTABILITY: NOT_YET_DERIVED
MISSING_AXIOM: REPRESENTING_DUAL_NATURAL_ISOMORPHISM
```
"""
    (docs / f"{model.STAMP}_pairing_representability.md").write_text(pairing_repr_doc, encoding="utf-8")

    scalar_doc = """# Scalar variance dependency

Ordinary-versus-conjugate variance is not meaningful at the abstract two-slot layer. It requires, in order:

1. a coefficient object or ring `K`;
2. a scalar action on the retained argument object;
3. an involution or star operation on `K`;
4. a compatibility law between scalar action and the pairing.

The local quarter-turn witness `i` does not itself instantiate these objects. FQM polarization is downstream and cannot be promoted to the primary pairing layer.

```text
SCALAR_VARIANCE_STATUS: DOWNSTREAM
```
"""
    (docs / f"{model.STAMP}_scalar_variance_dependency.md").write_text(scalar_doc, encoding="utf-8")

    orth_doc = """# First-L orthogonality cases

Use the block convention

```text
[[P_old, C_right],
 [C_left, p_new]]

C_right = P(old,new)
C_left  = P(new,old)
```

- Right orthogonality forces `C_right=0` only.
- Left orthogonality forces `C_left=0` only.
- Two-sided orthogonality forces both zero.
- Symmetry or Hermitianity plus either one-sided condition forces the other side, provided the relevant adjoint law exists.
- With no symmetry law, neither one-sided condition implies the other.

Counterexample over the integers:

```text
P = [[1,1],
     [0,1]]
```

For old axis `e1` and newborn axis `e2`, `P(e2,e1)=0` but `P(e1,e2)=1`. Therefore one-sided orthogonality does not yield block diagonal form.
"""
    (docs / f"{model.STAMP}_first_L_orthogonality_cases.md").write_text(orth_doc, encoding="utf-8")

    lblock_doc = """# First-L pairing block law

The source-derived obligations are old-block preservation, one newborn active axis, and an undefined orthogonality relation. The most specific lawful schema is therefore

```text
P_(t+1) = [[P_t, C_right],
           [C_left, p_new]].
```

Neither mixed block is source-derived as zero. The earliest missing axiom is a typed orthogonality law identifying left, right, or two-sided vanishing, or a symmetry/Hermitian law that links the two slots.

```text
FIRST_L_RIGHT_MIXED_BLOCK: NOT_YET_DERIVED
FIRST_L_LEFT_MIXED_BLOCK: NOT_YET_DERIVED
```
"""
    (docs / f"{model.STAMP}_first_L_pairing_block_law.md").write_text(lblock_doc, encoding="utf-8")

    rank_doc = """# Pairing rank semantics

The written law supports the architectural axis-block count `1 -> 2`. It does not yet identify that count with module dimension, matrix size, morphism rank, or nondegenerate rank.

The explicit extension

```text
[[1,0],
 [0,0]]
```

has block size two and algebraic rank one. Thus `p_new=0` refutes an unconditional inference from one appended axis to algebraic pairing-rank `+1`.

```text
ARCHITECTURAL_AXIS_COUNT: DERIVED_1_TO_2
ARGUMENT_OBJECT_RANK: NOT_YET_DERIVED
BLOCK_MATRIX_SIZE: CONDITIONAL_ON_REPRESENTATION
PAIRING_MORPHISM_RANK: NOT_YET_TYPED
NONDEGENERATE_PAIRING_RANK: NOT_YET_TYPED
FIRST_L_PAIRING_RANK_LAW: NOT_YET_TYPED
```
"""
    (docs / f"{model.STAMP}_pairing_rank_semantics.md").write_text(rank_doc, encoding="utf-8")

    bdoc = """# B pairing signature reassessment

`B` preserves the retained argument object and all latched axes. The source supports only the schema

```text
B_pairing : (Xi_t, W_t, P_t in Pair(H_t,H_t))
          -> P_(t+1) in Pair(H_t,H_t)
```

with dependence on the advanced pair and exact word prefix. No numeric recurrence is emitted.
"""
    qdoc = """# Q pairing signature reassessment

`Q` requires an orientation mutation on the active pairing sector. The minimum missing input is a word- and state-dependent quarter-turn action

```text
rho_Q(Xi_t,W_t,-) : Pair(H_t,H_t) -> Pair(H_t,H_t).
```

The local witness `i` does not define scalar multiplication on the primary pairing, and no `J_active` object is introduced.
"""
    ldoc = """# L pairing signature reassessment

The source supports an argument-object extension schema with an inherited old sector and one newborn architectural axis. It does not supply a direct sum, a represented matrix, side-specific orthogonality, or a typed rank function.

```text
L_pairing : (Xi_t,W_t,P_t, extension datum, orthogonality datum)
          -> P_(t+1)
```

remains a schema, not an instantiated recurrence.
"""
    (docs / f"{model.STAMP}_B_pairing_signature_reassessment.md").write_text(bdoc, encoding="utf-8")
    (docs / f"{model.STAMP}_Q_pairing_signature_reassessment.md").write_text(qdoc, encoding="utf-8")
    (docs / f"{model.STAMP}_L_pairing_signature_reassessment.md").write_text(ldoc, encoding="utf-8")

    gauge_doc = """# Seed gauge quotient boundary

The source licenses equivalence under **lawful** representation changes and gives `P -> U*PU` only schematically. It does not identify the lawful subgroup with all of `Aut(H_0)`.

The smallest licensed relation is the equivalence relation generated by a still-open subgroup `G_law` of source-authorized changes. Therefore

```text
Pair(H_0)/Aut(H_0)
```

is an admissible model, not a derived retained quotient. The exact primary seed and its gauge class remain open.
"""
    (docs / f"{model.STAMP}_seed_gauge_quotient_boundary.md").write_text(gauge_doc, encoding="utf-8")

    dep_doc = """# Pairing type dependency order

```text
primitive custody
-> retained argument objects and chart embeddings
-> source-forced two-slot pullback pairing interface
-> orthogonality semantics and architectural extension law
-> optional representability axiom
-> coefficient/scalar realization
-> involution/star and scalar variance
-> symmetry or adjoint law
-> typed rank notion
-> lawful gauge subgroup
-> primary seed class
-> B/Q/L pairing recurrences
-> chart restrictions and directed transfers
-> Xi_hat_t
-> terminal projection
```

The first unresolved axiom needed to promote the abstract interface to `P:H->D(H)` is the representing-dual natural isomorphism. Scalar variance is downstream.
"""
    (docs / f"{model.STAMP}_pairing_type_dependency_order.md").write_text(dep_doc, encoding="utf-8")

    schema_doc = """# Lifted-state schema boundary

The package emits only `lifted_state_schema`. It does not emit `Xi_hat_t` because the pairing, chart restrictions, and directed transfers are null.

```text
Xi_t: instantiated primitive custody
P_t: null
Omega_plus: null
Omega_minus: null
T_plus_to_minus: null
T_minus_to_plus: null
Xi_hat_t: not emitted
```
"""
    (docs / f"{model.STAMP}_lifted_state_schema_boundary.md").write_text(schema_doc, encoding="utf-8")

    corrected = f"""# p5_v8x Pairing Representability and First-L Rank Law

## Result

The written architecture forces a primary two-slot pairing object with pullback in both arguments. It does not force a scalar-valued form, a duality morphism `H->D(H)`, or a kernel realization.

The representable model requires one missing axiom: a representing dual object and natural isomorphism `Pair(A,H) ~= Hom(A,D(H))` compatible with pullback.

At the first `L`, the general block law remains `[[P_t,C_right],[C_left,p_new]]`. The word “orthogonal” is not typed as left, right, or two-sided, so neither mixed block is certified zero. The architectural axis count rises `1 -> 2`; algebraic pairing rank is not yet typed and need not rise when `p_new=0`.

## Status

```text
""" + "\n".join(f"{key}: {value}" for key, value in model.STATUS.items()) + "\n```\n"
    (docs / f"{model.STAMP}_PAIRING_REPRESENTABILITY_AND_L_RANK_LAW.md").write_text(corrected, encoding="utf-8")
    (docs / f"{model.STAMP}_RESULTS.md").write_text(corrected, encoding="utf-8")

    result_card = {
        "step": model.STEP,
        "stamp": model.STAMP,
        "statuses": model.STATUS,
        "primitive_sanity": sanity,
        "earliest_missing_axiom": representability["missing_axiom"],
        "claim_boundary": "no pairing, chart, transfer, projection, gauge quotient, FQM, Weil, affine, or MHD values emitted",
    }
    model.write_json(out / f"{model.STAMP}_result_card.json", result_card)


if __name__ == "__main__":
    write_docs()
    print(json.dumps({"status": "GENERATED", "root": str(ROOT)}, indent=2))
