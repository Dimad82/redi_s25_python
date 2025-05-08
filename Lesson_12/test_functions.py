# test_functions.py

from functions import sum, sub

def test_sum():
    assert sum(5,1) == 6

def test_sub():
    assert sub(5,1) == 4