# Basic Calculator Program

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation! Please enter one of +, -, *, /")








