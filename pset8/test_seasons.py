from seasons import convert_minutes


def test_one_year():
    assert convert_minutes(525600) == "Five hundred twenty-five thousand, six hundred"


def test_zero():
    assert convert_minutes(0) == "Zero"


def test_convert_minutes_two_years():
    assert convert_minutes(1051200) == "One million, fifty-one thousand, two hundred"
