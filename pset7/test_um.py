from um import count


def test_single_word():
    assert count("um") == 1


def test_multiple():
    assert count("um, good ....um, delicicous, ummmm") == 2
    assert count("yo, um, nice, um, very um... um.") == 4


def test_upper_case():
    assert count("UM, hello") == 1
    assert count("hello, Um") == 1
    assert count("yo, uM!") == 1


def test_hidden_in_other_words():
    assert count("hum, hello") == 0
    assert count("ummmi, hi") == 0
    assert count("hiummmi, hello") == 0


def test_with_special_characters():
    assert count("hello, it's an um.... umbrella") == 1
    assert count("hi, what a um*** thing") == 1


def test_with_spaces():
    assert count("hi,   um  good") == 1
