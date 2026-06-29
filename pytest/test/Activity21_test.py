import pytest

def test_sum():
    num = 10
    assert 3+7 == num
    assert 2+8 == num
    assert 12 + (-2) == num
    assert 10 + 0 == num
    # assert 12 +1 == num


def test_difference():
    num = 5
    assert 7-2 == num
    assert 8-3 == num
    assert 5-0  == num
    assert -5 - (-10) == num


def test_product():
    num = 15
    assert 5*3 == num
    assert 3*5 == num
    assert 15*1  == num
    assert 1 *15 == num
    assert -5 * -3 == num

def test_div():
    num = 20
    assert 100/5 == num
    assert 200/10 == num
    
