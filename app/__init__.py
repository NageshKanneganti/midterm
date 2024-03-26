"""app/__init__.py
This module provides an interactive command-line interface for performing arithmetic operations.
It utilizes the Calculator class from the calculator package to execute operations and display
results based on user input. The App class facilitates this interaction through a simple REPL loop.
"""
from app.calculator.calc_utils import calculate_and_print

class App:
    """
    App class to provide a command-line REPL for arithmetic operations.

    The class supports starting an interactive loop where users can input arithmetic expressions,
    which are then evaluated using the Calculator class. The result of each operation is displayed
    back to the user.
    """

    @staticmethod
    def parse_input(user_input: str):
        """
        Parses the user input into components of an arithmetic expression.

        Parameters:
        - user_input (str): A string input by the user in the format "<operand1> <operation> <operand2>".

        Returns:
        - tuple: A tuple containing the first operand, the operation name, and the second operand.

        Raises:
        - ValueError: If the input format is incorrect.
        """
        parts = user_input.split()
        if len(parts) != 3:
            raise ValueError("Invalid input format. Please use: <operand1> <operand2> <operation>")
        
        num1, num2, operation = parts
        return num1, num2, operation

    @staticmethod
    def start():
        """
        Starts the REPL loop, processing user input for arithmetic operations until 'exit' is typed.
        Displays a welcoming message with instructions and available operations at the start.
        """
        # Display a welcoming message and instructions for using the calculator
        print("Welcome to the Calculator App.")
        print("\tAvailable operations: add, subtract, multiply, divide")
        print("\t[Enter your calculation in the format: operand1 operand2 operation]")
        print("\t\tExample: 2 3 add")
        print("Type 'exit' to exit the application.\n")

        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            try:
                num1_str, num2_str, operation_name = App.parse_input(user_input)
                # Utilize the existing utility function to validate inputs, perform the operation, and print the result.
                calculate_and_print(num1_str, num2_str, operation_name)
            except Exception as e:
                # Any exceptions, such as parsing errors or arithmetic errors, are caught and displayed to the user.
                print(f"Error: {e}")
