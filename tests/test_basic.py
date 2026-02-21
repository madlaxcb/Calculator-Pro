import pytest

from calculator import basic


def test_add():
    assert basic.add(1, 2) == 3
    assert basic.add(-1, 5) == 4


def test_subtract():
    assert basic.subtract(5, 2) == 3
    assert basic.subtract(2, 5) == -3


def test_multiply():
    assert basic.multiply(3, 4) == 12
    assert basic.multiply(-2, 3) == -6


def test_divide():
    assert basic.divide(10, 2) == 5
    assert basic.divide(3, 2) == 1.5

    with pytest.raises(ZeroDivisionError):
        basic.divide(1, 0)


def test_power():
    assert basic.power(2, 3) == 8
    assert basic.power(4, 0.5) == 2
