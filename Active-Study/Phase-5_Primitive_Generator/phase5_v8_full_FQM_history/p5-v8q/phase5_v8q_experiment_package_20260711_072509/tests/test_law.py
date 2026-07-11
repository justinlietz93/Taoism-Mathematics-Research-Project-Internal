from primitive_custody.domain.law import capacity, domain_start_j, positions


def test_domain_zero_capacities() -> None:
    assert [capacity(j) for j in range(1, 7)] == [2, 4, 64, 256, 1024, 4096]


def test_domain_position_counts() -> None:
    assert positions(0) == 6
    assert positions(1) == 12
    assert domain_start_j(0) == 1
    assert domain_start_j(1) == 7
