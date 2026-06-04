import pytest
from fuel import gauge
from fuel import convert


def test_x_and_y():
    assert convert("2/3") == 67
    assert convert("0/10") == 0
    assert convert("10/10") == 100
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-2/3")
    with pytest.raises(ValueError):
        convert("-1/-3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_percentage():
    assert gauge(67) == "67%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(2) == "2%"
    assert gauge(1) == "E"
