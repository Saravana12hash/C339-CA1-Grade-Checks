
import pytest
from grade_pass import has_passed


# Test valid scores
@pytest.mark.parametrize(
    "score, expected",
    [
        (0, False),
        (49, False),
        (50, True),
        (51, True),
        (100, True),
    ]
)
def test_has_passed_valid(score, expected):
    result = has_passed(score)

    assert result is expected
    assert type(result) is bool


# Test invalid data types
@pytest.mark.parametrize(
    "score",
    [
        "50",
        50.5,
        None,
        True,
        False,
    ]
)
def test_has_passed_invalid_type(score):
    with pytest.raises(TypeError):
        has_passed(score)


# Test scores outside the permitted range
@pytest.mark.parametrize(
    "score",
    [
        -1,
        101,
    ]
)
def test_has_passed_out_of_range(score):
    with pytest.raises(ValueError):
        has_passed(score)
