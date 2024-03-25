# Advanced Python Calculator for Software Engineering Graduate Course
by *Nagesh Kanneganti* [__IS_601 Midterm__]

---

## 1. Design Patterns

- __Facade Pattern__

[__Facade Pattern__]()
> Description
```python
# example of facade pattern
```
<br>

- __Command Pattern__

[__Command Pattern__]()
> Description
```python
# example of command pattern
```
<br>

- __Factory Method__, __Singleton__, & __Strategy Patterns__

I use the [__Factory Method Pattern__](https://github.com/NageshKanneganti/midterm/blob/main/calculator/calculation.py) to encapsulate and delegate the instantiation of Calculation objects within the Calculation class itself. This pattern allows for greater flexibility and decoupling by delegating the creation logic to a separate method, `create_calculation`, facilitating easy modifications to the instantiation process without affecting the client code.
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

I use the [__Singleton Pattern__](https://github.com/NageshKanneganti/midterm/blob/main/calculator/calculations.py) to ensure that there is only one, globally accessible history of calculations within the application, managed through the CalculationHistory class.
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

[__Strategy Pattern__]()
> Description
```python
# example of strategy
```

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