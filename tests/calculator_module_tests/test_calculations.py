"""tests/test_calculations.py
Test suite for the CalculationHistory class in the calculator package.
This module tests the functionality of the CalculationHistory class, including
adding calculations to the history, retrieving the history and the most recent
calculation, and clearing the history.
"""
from decimal import Decimal
from app.calculator.calculation import Calculation
from app.calculator.operations import ArithmeticOperations as ao
from app.calculator.calculations import CalculationHistory as ch

def setup_function(function):
    """Setup for tests clears the calculation history before each test function is run."""
    ch.clear_history()

def test_add_calculation():
    """Test adding a single calculation to the history."""
    calc = Calculation(Decimal('1'), Decimal('2'), ao.addition)
    ch.add_calculation(calc)
    assert calc in ch.get_history(), "Calculation should be in history after addition."

def test_get_history():
    """Test retrieving the entire calculation history."""
    calc1 = Calculation(Decimal('1'), Decimal('2'), ao.addition)
    calc2 = Calculation(Decimal('3'), Decimal('4'), ao.subtraction)
    ch.add_calculation(calc1)
    ch.add_calculation(calc2)
    history = ch.get_history()
    assert history == [calc1, calc2], "The history should contain all added calculations."

def test_clear_history():
    """Test clearing the calculation history."""
    calc = Calculation(Decimal('1'), Decimal('2'), ao.addition)
    ch.add_calculation(calc)
    ch.clear_history()
    assert not ch.get_history(), "The history should be empty after clearing."

def test_get_latest_history():
    """Test retrieving the most recent calculation from the history."""
    calc1 = Calculation(Decimal('1'), Decimal('2'), ao.addition)
    calc2 = Calculation(Decimal('3'), Decimal('4'), ao.subtraction)
    ch.add_calculation(calc1)
    ch.add_calculation(calc2)
    latest_calc = ch.get_latest_history()
    assert latest_calc == calc2, "The latest calculation should be the most recently added."

def test_get_latest_history_empty():
    """Test that get_latest_history returns None when the history is empty."""
    ch.clear_history()  # Ensure the history is empty
    latest_calc = ch.get_latest_history()
    assert latest_calc is None, "get_latest_history should return None when the history is empty."
