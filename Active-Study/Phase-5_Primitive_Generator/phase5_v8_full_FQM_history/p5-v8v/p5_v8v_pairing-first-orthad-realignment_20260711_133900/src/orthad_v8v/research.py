from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from .primitive import exact_word, independent_oracle, trace_first_crossing_and_next_b

STAMP = "20260711T133900"
EXPECTED_WORD = "BQQBBBQBQBBQBBL"
EXPECTED_WORD_WITH_NEXT_B = EXPECTED_WORD + "B"


STATUSES: dict[str, str] = {
    "PRIMITIVE_CUSTODY": "PASS",
    "PRIMITIVE_FIRST_CROSSING": "PASS",
    "FIRST_L_CARRY": "PASS",
    "FIRST_NEXT_DOMAIN_B": "PASS",
    "ACTIVE_AXIS_LOCAL_SHORTHAND": "PASS",
    "FIRST_TRUE_GAP": "PRIMARY_PAIRING_TYPE_SEED_AND_MUTATION",
    "ORTHAD_EXISTS_FROM_FIRST_PRIMITIVE_TICK": "ARCHITECTURAL_LAW",
    "EXACT_PRIMARY_PAIRING_TYPE": "NOT_YET_DERIVED",
    "EXACT_PRIMARY_PAIRING_SEED": "NOT_YET_DERIVED",
    "B_PAIRING_MUTATION": "NOT_YET_DERIVED",
    "Q_PAIRING_MUTATION": "NOT_YET_DERIVED",
    "L_PAIRING_EXTENSION": "NOT_YET_DERIVED",
    "EXACT_PRIMARY_PAIRING_RECURRENCE": "NOT_YET_DERIVED",
    "EXACT_CHART_MAPS": "NOT_YET_DERIVED",
    "EXACT_DIRECTED_TRANSFERS": "NOT_YET_DERIVED",
    "OVERLAP_DOMAIN": "NOT_YET_DERIVED",
    "COCYCLE": "NOT_RUN",
    "TERMINAL_PROJECTION": "NOT_RUN",
    "GAUGE_FQM_WEIL_DESCENT": "NOT_RUN",
    "NATIVE_SUCCESSOR_ON_Z12": "DOWNSTREAM_COORDINATE_QUESTION",
    "QBL_TO_AFFINE_FACTOR_MAP": "NOT_YET_DERIVED",
    "INTERNAL_ORTHAD_SEED_FROM_AFFINE_MAP": "NOT_LICENSED",
    "MHD_ORTHAD_READINESS": "NOT_READY",
}


def typed_state_ledger() -> list[dict[str, str]]:
    return [
        {"symbol": "A_t", "type": "Nat", "role": "domain counter", "status": "DERIVED"},
        {"symbol": "q_t=(u_t,v_t)", "type": "ordered positive integer pair, 1<=u<=v", "role": "carried balanced-refinement pair", "status": "DERIVED"},
        {"symbol": "theta_t", "type": "(pi/2)*Int, represented exactly by phase_quarters", "role": "carried global phase", "status": "DERIVED"},
        {"symbol": "k_t", "type": "Fin(N_A), N_A=6*2^A", "role": "domain-local phase-position index", "status": "DERIVED"},
        {"symbol": "j_t", "type": "positive Nat with j=j_start(A)+k", "role": "global phase-position index", "status": "DERIVED"},
        {"symbol": "W_t", "type": "free monoid {B,Q,L}*", "role": "exact ordered executed primitive word", "status": "DERIVED"},
        {"symbol": "Xi_t", "type": "dependent custody-state sum over A", "role": "primitive custody state", "status": "DERIVED"},
        {"symbol": "r_t", "type": "Nat, separate from k_t", "role": "architectural pairing-rank counter", "status": "ARCHITECTURAL_CONSTRAINT"},
        {"symbol": "P_t", "type": "unknown pairing object on an unknown retained axis object", "role": "generative primary pairing", "status": "NOT_YET_DERIVED"},
        {"symbol": "Omega_t_plus", "type": "pullback/restriction of P_t along unknown iota_plus", "role": "plus chart restriction", "status": "NOT_YET_DERIVED"},
        {"symbol": "Omega_t_minus", "type": "pullback/restriction of P_t along unknown iota_minus", "role": "minus chart restriction", "status": "NOT_YET_DERIVED"},
        {"symbol": "T_t_plus_to_minus", "type": "mixed block induced by P_t and chart maps", "role": "directed plus-to-minus transfer", "status": "NOT_YET_DERIVED"},
        {"symbol": "T_t_minus_to_plus", "type": "mixed block induced by P_t and chart maps", "role": "directed minus-to-plus transfer", "status": "NOT_YET_DERIVED"},
        {"symbol": "Xi_hat_t", "type": "dependent lifted record (Xi_t,P_t,Omega+/-,T+-,T-+)", "role": "fully retained lifted state", "status": "SCHEMA_DERIVED_VALUES_OPEN"},
        {"symbol": "⌞Xi_hat_t⌝", "type": "wrapper/reader over Xi_hat_t", "role": "Orthad", "status": "ARCHITECTURAL_LAW"},
    ]


def pairing_type_assessment() -> dict[str, Any]:
    return {
        "status": "NOT_YET_DERIVED",
        "structural_constraints": [
            "P_t is primary and not chart-local",
            "both chart restrictions and both mixed transfers must be induced from P_t",
            "P_t exists from the first primitive tick",
            "B and Q preserve architectural rank",
            "L retains the old block, appends one orthogonal axis, and raises architectural rank by one",
        ],
        "rejected_identifications": [
            "Bloch sphere",
            "Z/12Z carrier",
            "one chart matrix",
            "terminal character",
            "finished FQM quadratic form",
            "imported Weil operator",
            "affine 7/8/9 coordinate",
        ],
        "type_alternatives_not_separated_by_sources": [
            "bilinear form",
            "sesquilinear form",
            "quadratic refinement with polarized pairing",
            "operator-valued pairing",
            "general morphism H_t -> D(H_t) in a category with duality",
        ],
        "missing_object": {
            "name": "PAIRING_TYPE_DATUM",
            "notation": "D_P=(K,H_0,D_or_sigma,variance,symmetry_law)",
            "meaning": "coefficient object, retained axis object, duality/involution, argument variance, and symmetry/adjoint law",
        },
        "local_shorthand_boundary": "exp(i*theta_t)/(u_t*v_t) is a licensed local descendant and does not type P_t",
    }


def pairing_seed_assessment() -> dict[str, Any]:
    return {
        "status": "NOT_YET_DERIVED",
        "missing_map": "eta_P : (Xi_0,W_0,D_P) -> P_0",
        "reason": "Xi_0 and the custody law contain no equation selecting one element of a pairing space",
        "abstract_counterexample": {
            "carrier": "one-dimensional Q-module",
            "P1": "P1(x,y)=x*y",
            "P2": "P2(x,y)=2*x*y",
            "distinct_witness": "P1(1,1)=1 != 2=P2(1,1)",
            "same_custody": "both may be paired with the same Xi_0 when no seed map is supplied",
        },
    }


def mutation_assessments() -> dict[str, Any]:
    return {
        "B": {
            "status": "NOT_YET_DERIVED",
            "licensed_local_trace": "phase retained; denominator changes from u*v to v*(u+v)",
            "missing_map": "B_pairing : (P_t,Xi_t,Xi_{t+1},W_{t+1}) -> P_{t+1}",
        },
        "Q": {
            "status": "NOT_YET_DERIVED",
            "licensed_local_trace": "local shorthand multiplies by i; arithmetic denominator retained",
            "missing_map": "Q_pairing : (P_t,Xi_t,Xi_{t+1},W_{t+1}) -> P_{t+1}",
        },
        "L": {
            "status": "NOT_YET_DERIVED",
            "architectural_obligations": [
                "retain the complete old pairing block",
                "latch the completed active axis",
                "append one new orthogonal active axis",
                "architectural rank changes 1->2 at the first L",
            ],
            "conditional_block_consequence": "if P is a scalar-valued form and orthogonal means P(old,new)=0, the mixed birth block is zero in a compatible basis",
            "not_instantiated": "the pairing type is missing, so no numeric C_t or p_new is emitted",
            "missing_map": "L_pairing : (P_t,Xi_t,Xi_{t+1},W_{t+1}) -> P_{t+1}",
            "remaining_seed_component": "new-axis pairing datum p_new",
        },
    }


def z12_assessment() -> dict[str, Any]:
    return {
        "status": "FINITE_DOUBLED_PHASE_ORIENTATION_CARRIER_AND_SHADOW_SKELETON",
        "retains": ["six local phase positions", "two orientation hands", "finite chi12 shadow support when the downstream FQM layer is supplied"],
        "discards": ["exact pair (u,v)", "unbounded exact word W", "domain counter beyond chosen quotient", "full phase-quarter count", "primary pairing", "chart and transfer data"],
        "cannot_be_full_retained_state": "the infinite exact-word set cannot inject into a twelve-element set",
        "successor_status": "DOWNSTREAM_COORDINATE_QUESTION",
    }


def affine_boundary() -> dict[str, str]:
    return {
        "AFFINE_GLOBAL_THRESHOLD_BRIDGE": "PROVED",
        "QBL_TO_AFFINE_FACTOR_MAP": "NOT_YET_DERIVED",
        "INTERNAL_ORTHAD_SEED_FROM_AFFINE_MAP": "NOT_LICENSED",
        "possible_future_factor_shapes": "Xi_hat_A -> (E_A,c_A) OR ⌞Xi_hat_A⌝ -> (E_A,c_A); source object not selected",
    }


def mhd_readiness() -> dict[str, Any]:
    missing = [
        "primary pairing recurrence",
        "two chart maps",
        "two directed transfer laws",
        "overlap-domain definition",
        "cocycle or route-consistency test bound to the clean recurrence",
        "vector component transformation law",
        "tensor component transformation law",
        "units and grid-geometry verification",
        "field-valued channel definition",
    ]
    return {
        "DATA_READER_READINESS": "EXTERNAL_INTAKE_EXISTS; NOT TESTED IN THIS PASS",
        "GEOMETRIC_READINESS": "NOT_READY",
        "ORTHAD_READINESS": "NOT_READY",
        "PROJECTION_READINESS": "NOT_READY",
        "MHD_ORTHAD_READINESS": "NOT_READY",
        "missing": missing,
    }


def blank_orthad_layer(architectural_rank: int) -> dict[str, Any]:
    return {
        "status": "NOT_INSTANTIATED_DUE_TO_PAIRING_TYPE_GAP",
        "architectural_rank": architectural_rank,
        "value": None,
    }


def causal_trace(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    rank_before = 1
    for row in rows:
        primitive = row["selected_primitive"]
        rank_after = rank_before + 1 if primitive == "L" else rank_before
        result.append(
            {
                "step_index": row["step_index"],
                "Xi_t": row["before"],
                "CanB": row["can_b_before"],
                "CanQ": row["can_q_before"],
                "selected_primitive": primitive,
                "Xi_t_plus_1": row["after"],
                "P_t": blank_orthad_layer(rank_before),
                "P_t_plus_1": blank_orthad_layer(rank_after),
                "Omega_t_plus": blank_orthad_layer(rank_before),
                "Omega_t_plus_1_plus": blank_orthad_layer(rank_after),
                "Omega_t_minus": blank_orthad_layer(rank_before),
                "Omega_t_plus_1_minus": blank_orthad_layer(rank_after),
                "T_t_plus_to_minus": blank_orthad_layer(rank_before),
                "T_t_plus_1_plus_to_minus": blank_orthad_layer(rank_after),
                "T_t_minus_to_plus": blank_orthad_layer(rank_before),
                "T_t_plus_1_minus_to_plus": blank_orthad_layer(rank_after),
                "Xi_hat_t": {"schema": "Xi_t + P_t + two restrictions + two transfers", "value_status": "PARTIAL_SCHEMA_ONLY"},
                "Xi_hat_t_plus_1": {"schema": "Xi_t+1 + P_t+1 + two restrictions + two transfers", "value_status": "PARTIAL_SCHEMA_ONLY"},
                "projection_performed": False,
            }
        )
        rank_before = rank_after
    return result


def snapshots(rows: list[dict[str, Any]]) -> dict[str, Any]:
    l_index = next(i for i, row in enumerate(rows) if row["selected_primitive"] == "L")
    return {
        "before_first_L": rows[l_index]["before"],
        "immediately_after_first_L": rows[l_index]["after"],
        "immediately_after_first_next_domain_B": rows[l_index + 1]["after"],
    }


def pairing_subtraces(rows: list[dict[str, Any]], primitive: str) -> list[dict[str, Any]]:
    return [
        {
            "step_index": row["step_index"],
            "prefix_before": row["prefix_before"],
            "prefix_after": row["prefix_after"],
            "primitive": primitive,
            "custody_before": row["before"],
            "custody_after": row["after"],
            "local_shorthand_before": row["active_axis_before"],
            "local_shorthand_after": row["active_axis_after"],
            "P_before": None,
            "P_after": None,
            "pairing_status": "NOT_YET_DERIVED",
        }
        for row in rows
        if row["selected_primitive"] == primitive
    ]


def verify_baseline(rows: list[dict[str, Any]]) -> dict[str, Any]:
    word = exact_word(rows)
    word_with_next_b = exact_word(rows, include_next_b=True)
    oracle = independent_oracle()
    l_index = next(i for i, row in enumerate(rows) if row["selected_primitive"] == "L")
    before_l = rows[l_index]["before"]
    after_l = rows[l_index]["after"]
    next_b = rows[l_index + 1]["after"]
    checks = {
        "word": word == EXPECTED_WORD,
        "word_with_next_b": word_with_next_b == EXPECTED_WORD_WITH_NEXT_B,
        "oracle_word": oracle[-2][1] == EXPECTED_WORD and oracle[-1][1] == EXPECTED_WORD_WITH_NEXT_B,
        "floor_pair": before_l["pair"] == [55, 89],
        "floor_product": before_l["pair_product"] == 4895,
        "q_count": before_l["phase_quarters"] == 5,
        "phase_witness": before_l["phase_label"] == "i",
        "L_pair_carry": after_l["pair"] == [55, 89],
        "L_phase_carry": after_l["phase_quarters"] == 5,
        "L_k_reset": after_l["k"] == 0,
        "L_j": after_l["j"] == 7,
        "next_pair": next_b["pair"] == [89, 144],
        "local_axis": rows[l_index]["active_axis_before"]["local_shorthand"] == "i/4895",
    }
    return {"pass": all(checks.values()), "checks": checks, "values": {"word": word, "word_with_next_b": word_with_next_b, "before_L": before_l, "after_L": after_l, "after_next_B": next_b}}


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
