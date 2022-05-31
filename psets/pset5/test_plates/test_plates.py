# https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from plates import is_valid


def test_length_is_valid():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCEDF") == True
    assert is_valid("ABCDEFG") == False


def test_start_is_valid():
    assert is_valid("AB") == True
    assert is_valid("A1") == False
    assert is_valid("12") == False
    assert is_valid("2B") == False


def test_number_is_valid():
    assert is_valid("AB55") == True
    assert is_valid("ABC05") == False
    assert is_valid("ABAA50") == True
    assert is_valid("ABC54A") == False


def test_punct_is_valid():
    assert is_valid("CS50!") == False
    assert is_valid("!S 234") == False
    assert is_valid("!.,;#@") == False
