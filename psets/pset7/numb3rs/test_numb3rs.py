# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

from numb3rs import validate

def test_range_validate():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("255.2555.255.255") == False
    assert validate("127.512.0.1") == False
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True


def test_non_numeric_validate():
    assert validate("cat.dog.bird.eagle") == False
    assert validate("255.cat.213.233") == False
    assert validate("123.123.cat.dog") == False
    assert validate("!@#.$%¨.&*(.)_+") == False