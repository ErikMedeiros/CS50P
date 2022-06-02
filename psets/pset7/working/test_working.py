# https://cs50.harvard.edu/python/2022/psets/7/working/

from working import convert
from pytest import raises


def test_invalid_format_convert():
    with raises(ValueError):
        convert("10:10 PM")
        convert("10 AM")
        convert("10")
        convert("")


def test_12_hour_convert():
    assert convert("12:34 PM to 1:12 PM") == "12:34 to 13:12"
    assert convert("1:12 PM to 12:34 AM") == "13:12 to 00:34"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_correctness_convert():
    assert convert("5:42 AM to 8:03 AM") == "05:42 to 08:03"
    assert convert("4:56 PM to 7 AM") == "16:56 to 07:00"
    assert convert("2 PM to 3 PM") == "14:00 to 15:00"
