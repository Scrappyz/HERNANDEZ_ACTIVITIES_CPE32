# Defining a Function
def greet():
    print("Hello, world!")

# Reasons of Using Functions
# - Modularize code
# - Encapsulate repetitive tasks
# - Improve code readability and maintainability

# Types of Functions in Python
# - Built-in functions (e.g., print(), len())
# - User-defined functions
# - Anonymous functions (lambda functions)

# Advantages of User-Defined Function
# - Reusability
# - Modular programming
# - Improved code readability
# - Easy debugging and maintenance

# Rules in Declaring a Function in Python
# - Function blocks must be indented
# - Function name must be followed by parentheses ()
# - Parameters (if any) must be placed within these parentheses
# - Function body must be indented

# Python Function Syntax
# def function_name(parameters):
#     """docstring"""
#     statement(s)

# Function Argument and Parameter
def greet_with_name(name):
    print(f"Hello, {name}!")

# The Return Statement
def add(x, y):
    return x + y

# Calling the Functions
greet()  # Output: Hello, world!
greet_with_name("Alice")  # Output: Hello, Alice!
result = add(3, 5)
print("The sum is:", result)  # Output: The sum is: 8
