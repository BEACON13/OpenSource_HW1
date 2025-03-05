"""Unit tests for Calculator component."""

from src.calculator.api import add, multiply, subtract


def test_addition() -> None:
    """Test addition operation."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtraction() -> None:
    """Test subtraction operation."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiplication() -> None:
    """Test multiplication operation."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
