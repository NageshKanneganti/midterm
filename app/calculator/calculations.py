"""calculator/calculations.py
Defines the CalculationHistory class for managing a shared history of calculations
performed within the calculator application. This class offers class methods to add
calculations to the history, retrieve the full history or the most recent calculation,
and clear the history. The history is maintained as a class-level list, allowing easy
access and modification across different parts of the application.
"""
from typing import List, Optional
from app.calculator.calculation import Calculation

class CalculationHistory:
    """Manages the history of calculations performed by the calculator.
    
    This class offers class methods to add calculations to the history,
    retrieve the full history or the most recent calculation, and clear
    the history. The history is maintained as a class-level list, allowing
    easy access and modification across different parts of the application.
    """
    _history: List[Calculation] = []  # Class-level attribute to store instances of Calculation

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a calculation to the history.
        
        Args:
            calculation (Calculation): The calculation to add to the history.
        """
        cls._history.append(calculation)
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history.
        
        Returns:
            List[Calculation]: The list of calculations.
        """
        return cls._history

    @classmethod
    def clear_history(cls):
        """Clear the calculation history."""
        cls._history.clear()

    @classmethod
    def get_latest_history(cls) -> Optional[Calculation]:
        """Retrieves the most recent calculation & returns None if there are no calculations in history."""
        if cls._history:
            return cls._history[-1]
        else:
            return None
