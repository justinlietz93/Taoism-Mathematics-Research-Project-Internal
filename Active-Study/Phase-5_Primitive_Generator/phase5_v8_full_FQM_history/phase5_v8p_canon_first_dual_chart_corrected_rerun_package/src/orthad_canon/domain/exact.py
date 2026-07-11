from __future__ import annotations

from .models import ExactEntry, ExactMatrix


def zero_entry() -> ExactEntry:
    return ExactEntry(0, 0)


def matrix_digest_rows(matrix: ExactMatrix) -> tuple[tuple[int, int, int, int], ...]:
    rows: list[tuple[int, int, int, int]] = []
    for i, row in enumerate(matrix):
        for j, entry in enumerate(row):
            rows.append((i, j, entry.support, entry.phase_mod24 % 24))
    return tuple(rows)


def matrix_changed_cells(left: ExactMatrix, right: ExactMatrix) -> int:
    n = max(len(left), len(right))
    changed = 0
    for i in range(n):
        for j in range(n):
            a = left[i][j] if i < len(left) and j < len(left[i]) else zero_entry()
            b = right[i][j] if i < len(right) and j < len(right[i]) else zero_entry()
            if a != b:
                changed += 1
    return changed


def phase_orientation(phase_mod24: int) -> int:
    phase = phase_mod24 % 24
    if phase in (0, 12):
        return 0
    if phase in (4, 8):
        return 1
    if phase in (16, 20):
        return -1
    return 0
