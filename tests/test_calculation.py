"""tests/test_calculation.py
Test suite for the Calculation class in the calculator package.
Ensures that calculations are correctly created, computed, and represented.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import ArithmeticOperations as ao

@pytest.mark.parametrize("num1, num2, operation, expected_result", [
        # Addition tests
        (Decimal('2'), Decimal('3'), ao.addition, Decimal('5')),
        (Decimal('0.1'), Decimal('0.2'), ao.addition, Decimal('0.3')),
        # Subtraction tests
        (Decimal('5'), Decimal('3'), ao.subtraction, Decimal('2')),
        (Decimal('0.3'), Decimal('0.1'), ao.subtraction, Decimal('0.2')),
        # Multiplication tests
        (Decimal('2'), Decimal('3'), ao.multiplication, Decimal('6')),
        (Decimal('0.1'), Decimal('0.2'), ao.multiplication, Decimal('0.02')),
        # Division tests
        (Decimal('6'), Decimal('3'), ao.division, Decimal('2')),
        (Decimal('0.3'), Decimal('0.1'), ao.division, Decimal('3')),
        # Testing division by zero scenario
        (Decimal('1'), Decimal('0'), ao.division, "ZeroDivisionError"),
    ])
def test_compute(num1, num2, operation, expected_result):
    """Verify that compute method returns correct result for basic arithmetic operations."""
    if expected_result == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError):
            operation(num1, num2)
    else:
        calculation = Calculation(num1, num2, operation)
        assert calculation.compute() == expected_result, f"Incorrect calculation result for {operation.__name__}."

def test_create_calculation():
    """Ensure the factory method creates a Calculation instance as expected."""
    num1, num2 = Decimal('10'), Decimal('5')
    operation = ao.addition
    calculation = Calculation.create_calculation(num1, num2, operation)
    assert isinstance(calculation, Calculation), "create_calculation did not produce a Calculation instance."
    assert calculation.compute() == ao.addition(num1, num2), "Factory method instance did not compute correctly."

def test_calculation_repr():
    """Check that the Calculation instance is represented as expected."""
    calculation = Calculation(Decimal('1'), Decimal('2'), ao.addition)
    expected_repr = "Calculation(1, 2, addition)"
    assert repr(calculation) == expected_repr, "Calculation __repr__ does not match expected format."
