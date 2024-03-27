# Advanced Python Calculator for Software Engineering Graduate Course
by *Nagesh Kanneganti* [__IS_601 Midterm__]

---

## 1. Design Patterns

- __Facade Pattern__

I used the [__Facade Pattern__](https://github.com/NageshKanneganti/midterm/blob/40f9fd350acccb255748562b7d0e9f3692323a1d/app/__init__.py#L14-L155) to simplify the interaction with the application's complex subsystems, providing a unified interface for starting the application, loading plugins, and handling commands.
> The `App` class serves as the facade, encapsulating the complexities of loading plugins and handling commands. Clients interact with the `App` facade without needing to understand the internal workings of these subsystems. By encapsulating the initialization process, loading of plugins, and registration of commands, the App facade shields clients from the implementation details of these subsystems. Clients only need to know how to interact with the App class, making the application more maintainable and easier to use.
```python
class App:
    def __init__(self):
        # Encapsulate the initialization process
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Encapsulate the process of loading plugins
        # ...

    def register_plugin_commands(self, plugin_module):
        # Encapsulate the process of registering commands from plugins
        # ...
    
    ...
```
> The `App` facade provides a unified interface for starting the application and interacting with its features. Clients interact with the `App` class to start the application and execute commands, abstracting away the complexity of the underlying subsystems.
```python
if __name__ == "__main__":
    # Initialize and start the application
    App().start()
```
> In summary, the Facade Pattern in this context simplifies the usage of the application by providing a clear and unified interface while encapsulating the complexities of its subsystems.
<br>

- __Command Pattern__

I use the [__Command Pattern__](https://github.com/NageshKanneganti/midterm/blob/ef3d1889b8da5de5a2139a4045a9c1eb0665abb6/app/commands/__init__.py#L8-L33) to enhance modularity and flexibility.
> Each concrete command class, like `AddCommand`, `DivideCommand`, `MultiplyCommand`, and `SubtractCommand`, encapsulates a specific operation within its execute method. (Along with `HistoryCommand`) 
```python
class AddCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "add"
        self.description = "Add two numbers together."

    def execute(self, *args):
        logging.info("Executing addition command")
        user_input_prompt = "Operation: Addition\n"
        execute_operation(user_input_prompt, self.name)

class DivideCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "divide"
        self.description = "Divide two numbers from one another."

    def execute(self, *args):
        logging.info("Executing division command")
        user_input_prompt = "Operation: Division\n"
        execute_operation(user_input_prompt, self.name)

class MultiplyCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "multiply"
        self.description = "Multiply two numbers together."

    def execute(self, *args):
        logging.info("Executing multiplication command")
        user_input_prompt = "Operation: Multiplication\n"
        execute_operation(user_input_prompt, self.name)

class SubtractCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "subtract"
        self.description = "Subtract two numbers from one another."

    def execute(self, *args):
        logging.info("Executing subtraction command")
        user_input_prompt = "Operation: Subtraction\n"
        execute_operation(user_input_prompt, self.name)
```
> This encapsulation allows for uniform invocation of diverse operations through a common interface defined by the `Command` superclass. 
```python
class Command:
    def __init__(self):
        """Constructor for command class"""
        self.name = ""  # Command name for menu display
        self.description = ""  # Command description for menu display

    def execute(self, *args, **kwargs):
        raise NotImplementedError("Command execution not implemented.")
```
> The `CommandHandler` class serves as the invoker, maintaining a dictionary of registered commands and facilitating their dynamic execution based on user input or other triggers. 
```python
class CommandHandler:
    def __init__(self):
        self.commands = {} # A dictionary to store command instances keyed by their names.

    def register_command(self, command):
        if command.name in self.commands:
            logging.warning(f"Command '{command.name}' is already registered. Overwriting.")
        self.commands[command.name] = command
        logging.info(f"Command '{command.name}' registered successfully.")

    def get_commands(self):
        return [(cmd.name, cmd.description) for cmd in self.commands.values()]

    def execute_command(self, name, *args):
        command = self.commands.get(name)
        if not command:
            logging.error(f"Command '{name}' not found.")
            raise KeyError
        try:
            command.execute(*args)
        except Exception as e:
            logging.error(f"Error executing command '{name}': {e}")
```
> By interacting with commands solely through the Command interface, the `CommandHandler` remains decoupled from the specific implementations of individual commands. This decoupling promotes flexibility, as new commands can be added or existing ones modified without necessitating changes to the `CommandHandler` or other components of the system.
<br>

- __Factory Method__, __Singleton__, & __Strategy Patterns__

I use the [__Factory Method Pattern__](https://github.com/NageshKanneganti/midterm/blob/ef3d1889b8da5de5a2139a4045a9c1eb0665abb6/app/calculator/calculation.py#L30-L47) to encapsulate and delegate the instantiation of Calculation objects within the Calculation class itself. This pattern allows for greater flexibility and decoupling by delegating the creation logic to a separate method, `create_calculation`, facilitating easy modifications to the instantiation process without affecting the client code.
> The `create_calculation` class method acts as a factory that takes operands and an operation as its arguments. It then returns a new instance of the Calculation class configured with these inputs. This method abstracts the instantiation logic from the client, promoting a loose coupling between the object creation and its usage.
```python
class Calculation:
    def __init__(self, num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    @classmethod
    def create_calculation(cls, num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return cls(num1, num2, operation)
```
> Employing the Factory Method Pattern in this way encapsulates object creation, enhancing the `Calculation` class's adaptability. It centralizes changes—such as more complex initialization or new calculation types—within the `create_calculation` method, minimizing impact on the broader application. This approach streamlines creation, boosting code maintainability and scalability by isolating creation logic.
<br>

I use the [__Singleton Pattern__](https://github.com/NageshKanneganti/midterm/blob/ef3d1889b8da5de5a2139a4045a9c1eb0665abb6/app/calculator/calculations.py#L27-L58) to ensure that there is only one, globally accessible history of calculations within the application, managed through the CalculationHistory class.
> The `_history` attribute is a class-level attribute. This means it is shared across all instances of the CalculationHistory class. Any modification to _history through any instance (or directly via the class) will be reflected across the entire application, maintaining a single state of the calculation history.
```python
class CalculationHistory:
    _history: List[Calculation] = []  # Class-level attribute to store instances of Calculation
```
> All methods within `CalculationHistory` are class methods (@classmethod). These methods operate on the class level rather than the instance level. This further enforces the Singleton pattern, as these methods ensure that the operations on the calculation history are performed on a global state (_history) rather than any instance-specific state.
```python
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls._history.append(calculation)
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls._history

    @classmethod
    def clear_history(cls):
        cls._history.clear()

    @classmethod
    def get_latest_history(cls) -> Optional[Calculation]:
        if cls._history:
            return cls._history[-1]
        else:
            return None
```
<br>

I used the [__Strategy Pattern__](https://github.com/NageshKanneganti/midterm/blob/40f9fd350acccb255748562b7d0e9f3692323a1d/app/calculator/operations.py#L9-L77) to decouple the implementation of various arithmetic operations from the main application logic, allowing for flexibility and extensibility in handling different operations.
> Each static method encapsulates a specific arithmetic operation, providing a common interface for performing calculations. This design allows the caller to choose and switch between different strategies (operations) dynamically.
```python
class ArithmeticOperations:
    @staticmethod
    def addition(num1: Decimal, num2: Decimal) -> Decimal:
        return num1 + num2

    @staticmethod
    def subtraction(num1: Decimal, num2: Decimal) -> Decimal:
        return num1 - num2

    @staticmethod
    def multiplication(num1: Decimal, num2: Decimal) -> Decimal:
        return num1 * num2

    @staticmethod
    def division(num1: Decimal, num2: Decimal) -> Decimal:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            return num1 / num2

```
> In my [calculator/calc_utils.py](https://github.com/NageshKanneganti/midterm/blob/40f9fd350acccb255748562b7d0e9f3692323a1d/app/calculator/calc_utils.py#L9-L36) module, I utilize these strategies by invoking the corresponding static methods from the `ArithmeticOperations` class based on user input. For example:
```python
def perform_operation(num1: Decimal, num2: Decimal, operation_name: str) -> str:
    operation_callable = getattr(ArithmeticOperations, operation_name, None)
    if operation_callable is None:
        return f"Unknown operation: {operation_name}"
    else:
        result = operation_callable(num1, num2)
        return f"The result of {num1} {operation_name} {num2} is equal to {result}"
```
> Here, the `perform_operation` function dynamically selects the appropriate strategy (operation) based on the operation_name provided by the user. This demonstrates the dynamic nature of the Strategy Pattern, where the choice of strategy can vary at runtime.

---

## 2. Description of Environment Variables
[__Environment Variables__]()
> Description
```python
# environment variables
```

---

## 3. Utilizing Logging
[__Logging__]()
> Description
```python
# logging
```

---

## 4. LBYP vs EAFP
- __Look Before You Leap ([*if/else*]())__:
> Description
```python
# if/else demonstrating LBYP
```
<br>

- __Easier to Ask for Forgivness than Permission ([*try/except*]())__:
> Description
```python
# try/except demonstrating EAFP
```

---

## 5. Video
[Calculator Demo Video]()