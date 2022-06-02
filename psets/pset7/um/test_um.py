# https://cs50.harvard.edu/python/2022/psets/7/um/

from um import count

def test_zero_count():
    assert count("") == 0
    assert count("hello wold") == 0
    assert count("hmmm, yummy!") == 0
    assert count("ummmmmm") == 0


def test_case_insensitive_count():
    assert count("Hmmm, yummy!") == 0
    assert count("hello, um, world!") == 1
    assert count("HELLO, UM, WORLD") == 1

def test_correct_count():
    assert count("hello") == 0
    assert count("ummmmmm") == 0