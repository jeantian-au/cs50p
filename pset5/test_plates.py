import pytest
from plates import is_valid

# this demonstrate three kinds of ways of usig pytest.parametrize:


# 1:  pytest.param(..., id="...") 内联
@pytest.mark.parametrize(
    "plates, expected",
    [
        pytest.param("", False, id="no_letter"),
        pytest.param("a", False, id="one_letter"),
        pytest.param("ab", True, id="two_letter"),
        pytest.param("tjjgood", False, id="more_than_six_letter"),
    ],
)
def test_check_length(plates, expected):
    assert is_valid(plates) is expected


@pytest.mark.parametrize(
    "plates, expected",
    [
        pytest.param("ps", True, id="alphabet_alphabet"),
        pytest.param("9J", False, id="number_alphabet"),
        pytest.param("v1", False, id="alphabet_number"),
        pytest.param("50", False, id="number_number"),
    ],
)
def test_check_first_two(plates, expected):
    assert is_valid(plates) is expected


# 2:  bare tuples + ids=[...] 分离
@pytest.mark.parametrize(
    "plates,expected",
    [("!p", False), ("py.?", False), ("_no@&*", False)],
    ids=["exclamation_mark", "dot_questions_mark", "other_characters"],
)
def test_check_special_character(plates, expected):
    assert is_valid(plates) is expected


# 3. bare tuples,无 id
@pytest.mark.parametrize(
    "plates, expected",
    [("cs5", True), ("cs0", False), ("cs5000", True), ("cspyi0", False)],
)
def test_check_first_number(plates, expected):
    assert is_valid(plates) is expected


@pytest.mark.parametrize(
    "plates, expected", [("cs50", True), ("cs50p", False), ("cs5py", False)]
)
def test_check_alphabet_after_number(plates, expected):
    assert is_valid(plates) is expected
