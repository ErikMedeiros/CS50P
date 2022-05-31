# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value


def test_uppercase_value():
    assert value("HELLO") == 0
    assert value("HEAD") == 20
    assert value("OTHER") == 100


def test_lowercase_value():
    assert value("hello") == 0
    assert value("head") == 20
    assert value("other") == 100

def test_spaces_value():
    assert value("   hello") == 100
    assert value("hello   ") == 0
    assert value("   head") == 100
    assert value("head   ") == 20
    assert value("   other") == 100

def test_punct_value():
    assert value("!@#$Hello") == 100
    assert value("hello!@#$") == 0
    assert value("head!@#$") == 20