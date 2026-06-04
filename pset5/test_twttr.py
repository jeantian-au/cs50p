import pytest
from twttr import shorten


def test_single_character():
    assert shorten("a") == ""
    assert shorten("b") == "b"


def test_word():
    assert shorten("twitter") == "twttr"
    assert shorten("anemarieloyu") == "nmrly"


def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""


def test_all_consonants():
    assert shorten("bdgfkh") == "bdgfkh"


def test_phrase():
    assert shorten("you could make believe") == "y cld mk blv"


def test_case_sensitive():
    assert shorten("dElicIoUs") == "dlcs"


def test_not_alphabetic():
    assert shorten("123456") == "123456"
    assert shorten("disco: 05a5e5i5o5u!") == "dsc: 055555!"


def test_null():
    assert shorten("") == ""
