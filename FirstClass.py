#Calculator using Python
#This is a simple calculator that can perform addition, subtraction, multiplication, and division.
a = int(input("Enter first number: "))
operation = input("Enter operation: ")
b = int(input("Enter second number: "))

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
#This code is a simple calculator that takes two numbers and an operation as input and returns the result.
#It handles basic arithmetic operations and checks for division by zero.
# Strings: 
# nm = "Harry"
# print(nm[-4: -2])
