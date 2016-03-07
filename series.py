# -*- coding: utf-8 -*-
def sum_sequence_iterative(n, a=0, b=1):
    """Return nth number in sum sequence. Defaults to a=0, b=1. Iterative."""
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        c = a + b
        for x in range(3, n):
            a = b
            b = c
            c = a + b
            print(a, b, c)
        return c


def fibonacci_iterative(n):
    """Return nth number in Fibonacci sequence. Iterative."""
    return sum_sequence_iterative(n)


def lucas_iterative(n):
    return sum_sequence_iterative(n, 2, 1)


def fibonacci(n):
    """Return Nth Number of Fibonacci Sequence."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return nth Number of Lucas Sequence."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """Return Nth num in the sum series, give A and B as starting numbers."""
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sum_series(n - 1) + sum_series(n - 2)


if __name__ == "__main__":
    print(u"This module defines functions that implement mathematical series")
    print(u"")
    print(u"The first series of 'iterative' functions operate the same way as their \
        non-iterative counterparts. The two series' of functions are just \
        built in different ways.")
    print(u"")
    print(u"fibonacci(n):")
    print(fibonacci.__doc__)
    print(u"fibonacci(5) would return %s" % fibonacci(5))
    print(u"")
    print(u"lucas(n):")
    print(lucas.__doc__)
    print(u"lucas(5) would return %s" % lucas(5))
    print(u"")
    print(u"sum_series(n):")
    print(sum_series.__doc__)
    print(u"Without optional args, sum_series returns fibonacci(n)")
    print(u"sum_series(8, 6, 7) would return %s" % sum_series(8, 6, 7))
    print(u"")
