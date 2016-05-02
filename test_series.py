# -*- coding: utf-8 -*-
import pytest

FIB_LIST = [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
]

LUC_LIST = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
]


@pytest.mark.parametrize('n, c', FIB_LIST)
def test_fibonacci_iterative(n, c):
    from series import fibonacci_iterative
    assert fibonacci_iterative(n) == c


@pytest.mark.parametrize('n, c', LUC_LIST)
def test_lucas_iterative(n, c):
    from series import lucas_iterative
    assert lucas_iterative(n) == c


@pytest.mark.parametrize('n, c', FIB_LIST)
def test_fibonacci(n, c):
    from series import fibonacci
    assert fibonacci(n) == c


@pytest.mark.parametrize('n, c', LUC_LIST)
def test_lucas(n, c):
    from series import lucas
    assert lucas(n) == c


def test_sum_series():
    from series import sum_series
    assert sum_series(1, 6, 7) == 6
    assert sum_series(2, 6, 7) == 7
    assert sum_series(3, 6, 7) == 13
    assert sum_series(8, 6, 7) == 139
