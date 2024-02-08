# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Get input from the user for numbers and operator
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation based on the operator entered
if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
else:
    print("Error: Invalid operator!")
