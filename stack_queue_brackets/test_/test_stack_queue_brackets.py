import pytest
from stack_queue_brackets import validate_brackets


def test_one():
    actual = validate_brackets("{}")
    expected = True
    assert actual == expected


def test_two():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected


def test_three():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_four():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected


def test_five():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected


def test_six():
    actual = validate_brackets("[({}]")
    expected = False
    assert actual == expected


def test_seven():
    actual = validate_brackets("(](")
    expected = False
    assert actual == expected


def test_eight():
    actual = validate_brackets("{(})")
    expected = False
    assert actual == expected


def test_nine():
    actual = validate_brackets("{")
    expected = False
    assert actual == expected


def test_ten():
    actual = validate_brackets(")")
    expected = False
    assert actual == expected


def test_eleven():
    actual = validate_brackets("[}")
    expected = False
    assert actual == expected


def test_twelve():
    actual = validate_brackets("")
    expected = True
    assert actual == expected

def test_thirteen():
    actual = validate_brackets(")(")
    expected = False
    assert actual == expected



