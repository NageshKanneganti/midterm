"""app/plugins/divide/__init__.py"""
from app.commands import Command
from app.calculator.calc_utils import calculate_and_print

class DivideCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "divide"
        self.description = "Continuously divide two numbers. Type 'exit' to return to the main menu."

    def execute(self, *args):
        print("Operation: Division")
        print("\tContinuously enter two numbers separated by space to perform division.")
        print("\tType 'exit' at any time to return to the main menu.")
        print("\t\t[Example]: 4 2")

        while True:
            user_input = input("[Divide]:  ")

            if user_input.lower() == 'exit':
                print("Exiting division operation.\n")
                break

            try:
                num1_str, num2_str = self.parse_input(user_input)
                calculate_and_print(num1_str, num2_str, "divide")
                print("You can continue dividing or type 'exit' to return to the main menu.\n")
            except Exception as e:
                print(f"Error: {e}\nPlease try again or type 'exit' to exit.\n")

    @staticmethod
    def parse_input(user_input: str):
        """
        Parses the user input into components for addition operation.

        Parameters:
        - user_input (str): A string input by the user in the format "<operand1> <operand2>".

        Returns:
        - tuple: A tuple containing the first and second operands.

        Raises:
        - ValueError: If the input format is incorrect.
        """
        parts = user_input.split()
        if len(parts) != 2:
            raise ValueError("Invalid input format. Please use: <operand1> <operand2>")
        
        num1, num2 = parts
        return num1, num2
