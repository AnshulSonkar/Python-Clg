# Practical project: Custom Operation System
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


def calculate(operation, a, b):
    return operation(a, b)


print("Addition:", calculate(add, 20, 10))
print("Subtraction:", calculate(subtract, 20, 10))
print("Multiplication:", calculate(multiply, 20, 10))
print("Division:", calculate(divide, 20, 10))

