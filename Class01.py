# Python/index.py
# This script performs basic arithmetic operations
# a = 3
# b = 2
# print("Sum:", a + b)
# print("Difference:", a - b)
# print("Product:", a * b)
# print("Division:", a / b)
# print("Remainder:", a % b)
# print("Exponentiation:", a ** b)
# print("Floor Division:", a // b)
# This script calculates the user's age after 5 years
# age = int(input("Enter your current age: "))
# futureAge = age + 5
# print("Your age after 5 years will be:", futureAge)
# Type Casting: Convert one datatype into another
# str(a)  # Convert integer to string
# int("123")  # Convert string to integer
# float("3.14")  # Convert string to float
# bool(1)  # Convert integer to boolean 
# Calculator
# Collect input from user and perform all arithmetic operations
a = float(input("Enter first number: "))
operation = input("Enter operation: ")
b = float(input("Enter second number: "))

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation!"
print("Result:", result)
