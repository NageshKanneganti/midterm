"""tests/test_calculator.py
Test suite for the Calculator class in the calculator package. Tests the Calculator's ability
to correctly perform arithmetic operations (addition, subtraction, multiplication, division)
and records each operation in the calculation history.
"""
from decimal import Decimal
import pytest
from calculator import Calculator
from calculator.calculations import CalculationHistory as ch

@pytest.fixture(autouse=True)
def clear_history_before_tests():
    """Ensure a clean history for each test"""
    ch.clear_history()
    yield

@pytest.mark.parametrize("operation, num1, num2, expected", [
    (Calculator.add, Decimal('5'), Decimal('3'), Decimal('8')),
    (Calculator.subtract, Decimal('10'), Decimal('4'), Decimal('6')),
    (Calculator.multiply, Decimal('7'), Decimal('6'), Decimal('42')),
    (Calculator.divide, Decimal('8'), Decimal('2'), Decimal('4')),
])
def test_arithmetic_operations(operation, num1, num2, expected):
    """Test that calculator performs arithmetic operations correctly and records them."""
    result = operation(num1, num2)
    assert result == expected, f"Failed {operation.__name__} operation with {num1} and {num2}"
    # Verify the operation is recorded in history
    assert len(ch.get_history()) == 1, "History should contain one calculation after operation."

def test_division_by_zero():
    """Test division by zero is handled as expected."""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(Decimal('1'), Decimal('0'))
