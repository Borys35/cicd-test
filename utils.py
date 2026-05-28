"""This module contains simple calculator functions."""


def add(a: int, b: int) -> int:
    """Returns the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Returns the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Returns the quotient of a and b."""
    return a / b


def convert_to_bin(n: int) -> str:
    """Converts int to binary string."""
    if n <= 0 or n > 100 or not isinstance(n, int):
        raise ValueError("Invalid input")
    
    return bin(n)[2:]