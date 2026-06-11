from numb3rs import validate


def test_double_digit():
    assert validate("10.99.99.99") is True
    assert validate("1.2.3.4") is True


def test_section_inalign():
    assert validate("1.") is False
    assert validate("1.1.") is False
    assert validate("1.1.1.") is False
    assert validate("1.1.1.1") is True
    assert validate("1.1.1.1.1") is False
    assert validate(" . ") is False


def test_boundry_numbers():
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.256") is False
    assert validate("-1.0.-255.-255") is False


def test_value():
    assert validate("cat") is False
