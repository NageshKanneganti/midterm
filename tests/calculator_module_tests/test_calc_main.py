"""tests/test_calc_main.py: Tests for the main module of the command-line calculator application.

This test suite verifies the functionality of:
- Symbol to operation name mapping within the calculator's main interface.
- The calculate_and_print function, ensuring it accurately processes inputs and outputs the
  correct results or error messages based on various operation scenarios.
"""
import sys
from decimal import Decimal
from unittest.mock import patch
import pytest
from app.calculator import Calculator
from calc_main import calculate_and_print, perform_operation, main

# Tests for calculate_and_print & OperationCommand
@pytest.mark.parametrize("num1_str, num2_str, operation_str, expected_output", [
    ("5", "3", "add", "The result of 5 add 3 is equal to 8\n"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8\n"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20\n"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5\n"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero\n"),
    ("9", "3", "unknown", "Unknown operation: unknown\n"), # Test for unknown operation
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number.\n"), # Testing invalid number input
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.\n") # Testing another invalid number input
])
def test_calculate_and_print(capsys, num1_str, num2_str, operation_str, expected_output):
    """Test the calculate_and_print function with various input scenarios.

    This test verifies that calculate_and_print correctly handles and processes
    different types of inputs (valid numbers, invalid numbers, known and unknown operations),
    producing the appropriate output or error message.

    Args:
        capsys: Pytest fixture for capturing print statements.
        num1_str (str): The first number as a string.
        num2_str (str): The second number as a string.
        operation_str (str): The operation to be performed.
        expected_output (str): The expected output to be printed.
    """
    calculate_and_print(num1_str, num2_str, operation_str)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_perform_operation_unexpected_exception():
    """Test the perform_operation function's ability to handle unexpected exceptions gracefully."""
    # Example operation name to mock
    operation_name = 'add'
    # Exception message to simulate
    exception_message = "mock unexpected exception"

    # Setup the mock to replace the specified operation with one that raises an exception
    with patch.object(Calculator, operation_name, side_effect=Exception(exception_message)):
        # Call perform_operation and expect it to handle the unexpected exception
        result_message = perform_operation(Decimal('1'), Decimal('2'), operation_name)

        # Expected result format, adjust as necessary to match your error handling output
        expected_result = f"An unexpected error occurred: {exception_message}"
        assert result_message == expected_result, "The function did not handle an unexpected exception as expected."

# Testing main function
def test_main_invalid_arguments(capsys):
    """Test main function with invalid number of command-line arguments"""
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    print(repr(captured.out.strip()))  # This will show hidden characters like \n
    assert captured.out.strip() == "Usage: python main.py <number1> <number2> <operation>"

def test_main_correct_arguments(capsys):
    """Test providing the correct number of command-line arguments."""
    test_input = ["calculator_main.py", "5", "3", "add"]
    expected_output = "The result of 5 add 3 is equal to 8\n"
    sys.argv = test_input
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_output
