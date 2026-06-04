import pytest
from bank import value


def test_only_hello():
    assert value("hello") == 0


def test_other_version_hello():
    assert value("Hello") == 0
    assert value("HeLlO!") == 0
    assert value("HELLO") == 0
    assert value("Hello you") == 0


def test_start_with_h():
    assert value("howddy!") == 20
    assert value("Helicopter") == 20


def test_notaplha():
    assert value("_hello") == 100
    assert value("1236hello") == 100


def test_white_space():
    assert value("  hello") == 0
    assert value("hello  ") == 0


def test_single_character():
    assert value("h") == 20


def test_just_hi():
    assert value("hi") == 20
