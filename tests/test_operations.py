"""Tests for the ArithmeticOperations class in calculator/operations.py
This suite uses pytest for parameterized tests of the arithmetic operations (addition, subtraction,
multiplication, and division), ensuring functionality across a range of Decimal inputs.
"""
from decimal import Decimal
import pytest
from calculator.operations import ArithmeticOperations as op

class TestArithmeticOperations:
    """Test operations using parametrized test data"""
    @pytest.mark.parametrize("num1, num2, operation, expected", [
        # Addition tests
        (Decimal('2'), Decimal('3'), op.addition, Decimal('5')),
        (Decimal('0.1'), Decimal('0.2'), op.addition, Decimal('0.3')),
        # Subtraction tests
        (Decimal('5'), Decimal('3'), op.subtraction, Decimal('2')),
        (Decimal('0.3'), Decimal('0.1'), op.subtraction, Decimal('0.2')),
        # Multiplication tests
        (Decimal('2'), Decimal('3'), op.multiplication, Decimal('6')),
        (Decimal('0.1'), Decimal('0.2'), op.multiplication, Decimal('0.02')),
        # Division tests
        (Decimal('6'), Decimal('3'), op.division, Decimal('2')),
        (Decimal('0.3'), Decimal('0.1'), op.division, Decimal('3')),
        # Testing division by zero scenario
        (Decimal('1'), Decimal('0'), op.division, "ZeroDivisionError"),
    ])
    def test_operations(self, num1, num2, operation, expected):
        """Parameterized test for arithmetic operations with varied inputs and expected outputs."""
        if expected == "ZeroDivisionError":
            with pytest.raises(ZeroDivisionError):
                operation(num1, num2)
        else:
            assert operation(num1, num2) == expected, f"Failed {operation.__name__} with {num1} and {num2}"
