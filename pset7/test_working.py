from working import convert
import pytest


def test_no_min():
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
    assert convert("9:30 AM to 10 PM") == "09:30 to 22:00"
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"


def test_twelve_oclock():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:01 AM to 12:59 PM") == "00:01 to 12:59"


def test_out_of_range_time():
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 1 PM")
    with pytest.raises(ValueError):
        convert("2:100 AM to 12:00 PM")
    with pytest.raises(ValueError):
        convert("10 AM to 24 PM")
    with pytest.raises(ValueError):
        convert("1:60 AM to 12:60 PM")


def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM  5 PM")
