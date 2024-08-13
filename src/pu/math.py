"""Based on For the Love of Go
https://github.com/bitfield/ftl-code/blob/main/8.2/calculator.go
"""

from math import sqrt as math_sqrt


def add(value: int, b: int) -> int:
    """Add takes two numbers and returns the result of adding them together."""
    return value + b


def subtract(value: int, b: int) -> int:
    """Subtract takes two numbers a and b, and returns the result of subtracting b from a."""
    return value - b


def multiply(value: int, b: int) -> int:
    """Multiply takes two numbers a and b, and returns their product."""
    return value * b


def divide(value: int, b: int) -> float:
    """Divide takes two numbers and returns the result of dividing the first by the second.

    Raises:
        ZeroDivisionError: if the second value is zero."""
    if b == 0:
        msg = "division by zero not allowed"
        raise ZeroDivisionError(msg)
    return value / b


def sqrt(value: int) -> float:
    """Sqrt returns the square root of its input.

    Raises:
        ArithmeticError: for negative inputs."""
    if value < 0:
        msg = f"square root of negative number not allowed: {value}"
        raise ArithmeticError(msg)
    return math_sqrt(value)
