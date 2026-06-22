from working_v2 import convert
from working_v2 import h_24


def test_twelve_oclock():
    assert h_24("12 AM") == "00:00"
    assert h_24("12 PM") == "12:00"
    assert h_24("12:30 AM") == "00:30"


def test_no_minute():
    assert h_24("10 AM") == "10:00"
    assert h_24("1 PM") == "13:00"
    assert h_24("12")


def test_PM():
    assert h_24("9 PM") == "21:00"
    assert h_24("12:30 PM") == "12:30"


def test_invalid_input():
    assert convert("9 AM to 5 PM") == ("9 AM", "5 PM")
    assert convert("12 AM to 1 PM") == ("12 AM", "1 PM")
    assert convert("13 PM to 1 PM") == "Invalid input"
    assert convert("5 am to 6 pm") == "Invalid input"
    assert conver("0 am to 6 pm")
