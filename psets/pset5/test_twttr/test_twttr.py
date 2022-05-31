# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten


def test_only_vowels_shorten():
    assert shorten("aeiou") == ""


def test_only_consonants_shorten():
    assert shorten("cdfgh") == "cdfgh"


def test_only_numbers_shorten():
    assert shorten("12345") == "12345"


def test_mixed_case_shorten():
    assert shorten("AbCdEfG") == "bCdfG"


def test_punct_shorten():
    assert shorten(",.;:!?~") == ",.;:!?~"


def test_all_shorten():
    assert shorten("Computer Science 50") == "Cmptr Scnc 50"