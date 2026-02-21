"""Basic arithmetic operations."""

from __future__ import annotations

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference (a - b)."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient (a / b).

    Raises:
        ZeroDivisionError: if ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Raise ``a`` to the power of ``b``."""
    return a ** b
