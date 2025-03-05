"""API for the Calculator component."""

from .calculator import Calculator


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return Calculator.add(a, b)


def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return Calculator.subtract(a, b)


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return Calculator.multiply(a, b)
