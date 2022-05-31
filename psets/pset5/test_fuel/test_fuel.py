# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

from pytest import raises
from fuel import convert, gauge


def test_int_convert():
    assert convert("1/2") == 50
    assert convert("4/5") == 80
    assert convert("1/1") == 100
    assert convert("0/12") == 0

    with raises(ValueError):
        convert("cat/dog")
        convert("1/dog")
        convert("cat/1")
        convert("3/2")
        convert("12/2")


def test_zero_convert():
    with raises(ZeroDivisionError):
        convert("1/0")
        convert("12/0")
        convert("0/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(38) == "38%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
