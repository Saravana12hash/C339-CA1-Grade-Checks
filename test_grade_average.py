
import pytest
from grade_average import calculate_average


@pytest.mark.parametrize(
    "mark_one, mark_two, expected",
    [
        (0, 0, 0.0),
        (100, 100, 100.0),
        (50, 50, 50.0),
        (50, 51, 50.5),
        (60, 61, 60.5),
        (40, 80, 60.0),
    ]
)
def test_calculate_average_valid(mark_one, mark_two, expected):
    result = calculate_average(mark_one, mark_two)
    assert result == expected
    assert type(result) is float


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        ("50", 60),
        (50, "60"),
        (50.5, 60),
        (50, 60.5),
        (None, 50),
        (50, None),
        (True, 50),
        (50, False),
    ]
)
def test_calculate_average_invalid_type(mark_one, mark_two):
    with pytest.raises(TypeError):
        calculate_average(mark_one, mark_two)


@pytest.mark.parametrize(
    "mark_one, mark_two",
    [
        (-1, 50),
        (50, -1),
        (101, 50),
        (50, 101),
    ]
)
def test_calculate_average_out_of_range(mark_one, mark_two):
    with pytest.raises(ValueError):
        calculate_average(mark_one, mark_two)