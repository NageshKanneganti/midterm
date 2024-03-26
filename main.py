"""main.py: Main module for a command-line calculator.
This module captures user input from the command line, performs arithmetic operations
using the Calculator class, and handles invalid inputs and exceptions.
"""
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

def perform_operation(num1: Decimal, num2: Decimal, operation_name: str) -> str:
    """
    Attempts to perform the specified arithmetic operation on two operands.
    
    Args:
        num1 (Decimal): The first operand.
        num2 (Decimal): The second operand.
        operation_name (str): The operation to perform.
        
    Returns:
        str: A message with the result of the operation or an error.
    """
    # Mapping of operation names to Calculator class methods
    operation_mapping = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide,
    }

    try:
        # Retrieve the corresponding method from the mapping
        operation_callable = operation_mapping.get(operation_name)
        if operation_callable is None:
            raise ValueError(f"Unknown operation: {operation_name}")

        # Execute the operation
        result = operation_callable(num1, num2)
        return f"The result of {num1} {operation_name} {num2} is equal to {result}"
    except ZeroDivisionError:
        return "An error occurred: Cannot divide by zero"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"An unexpected error occurred: {e}"

def calculate_and_print(num1_str, num2_str, operation_name):
    """
    Validates the input, performs the operation, and prints the result or an error message.
    
    Args:
        num1_str (str): The first operand as a string.
        num2_str (str): The second operand as a string.
        operation_name (str): The name of the operation to perform.
    """
    try:
        num1_decimal = Decimal(num1_str)
        num2_decimal = Decimal(num2_str)
    except InvalidOperation:
        print(f"Invalid number input: {num1_str} or {num2_str} is not a valid number.")
        return
    
    result_message = perform_operation(num1_decimal, num2_decimal, operation_name)
    print(result_message)

def main():
    """
    Main entry point of the program. Parses command-line arguments and executes the operation.
    """
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, num1, num2, operation_name = sys.argv
    calculate_and_print(num1, num2, operation_name)

if __name__ == '__main__': # pragma: no cover
    main()