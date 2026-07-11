from __future__ import annotations

from .state import CustodyState


PRIMITIVES = ("B", "Q", "L")


def positions(A: int) -> int:
    if A < 0:
        raise ValueError("A must be nonnegative")
    return 6 * (2**A)


def domain_start_j(A: int) -> int:
    if A < 0:
        raise ValueError("A must be nonnegative")
    return 1 + 6 * ((2**A) - 1)


def expected_j(A: int, k: int) -> int:
    return domain_start_j(A) + k


def capacity(j: int) -> int:
    if j < 1:
        raise ValueError("j must be one-based")
    if j == 1:
        return 2
    if j == 2:
        return 4
    return 2 ** (2 * j)


def next_pair(state: CustodyState) -> tuple[int, int]:
    return state.v, state.u + state.v


def can_q(state: CustodyState) -> bool:
    return state.k < positions(state.A) - 1


def can_b(state: CustodyState) -> bool:
    cap = capacity(state.j)
    if state.k < positions(state.A) - 1:
        u1, v1 = next_pair(state)
        return u1 * v1 <= cap
    return state.pair_product < cap


def floor_reached(state: CustodyState) -> bool:
    return (not can_b(state)) and (not can_q(state))


def selected_primitive(state: CustodyState) -> str:
    if can_b(state):
        return "B"
    if can_q(state):
        return "Q"
    return "L"


def validate_state(state: CustodyState) -> None:
    if state.u < 1 or state.v < state.u:
        raise ValueError("pair must satisfy 1 <= u <= v")
    if state.k < 0 or state.k >= positions(state.A):
        raise ValueError("k outside active domain")
    if state.j != expected_j(state.A, state.k):
        raise ValueError("j is inconsistent with A and k")
    if any(letter not in PRIMITIVES for letter in state.word):
        raise ValueError("word contains a nonprimitive symbol")
