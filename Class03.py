# we are learning boolean data type
# Logical Operators
# >, <, >=, <=, ==, !=
# a = 8
# b = 15
# print(not (a > 5 and b == 15))
# print(not (5 >= 5))
# print((2 < 3 and 4 > 1) or not (6==6))
# PEMDAS ROLE ===> Paranthesis(), Exponents**, Multiplication, Division, Adition, Subtraction
# print(2 + 3 * 4) #14
# print((2 + 3) * 4)  #20
# print(10 - 2**2)  #6
# print(100 / 10 + 5)  #15
# print(5 + 2 * 3**2)  #23
# a = 4
# b = 2
# c = 3
# print(a + b * c)
# print((a + b) * c)
# print(a + b / c)
# print((a + b) / c)
# print((2 + 3 * 4) ** 2)
# is answer men python ka ye role lagta h agar ek jaga multiplication ye division ho
# ya sirf adition ye subtraction ho to wahan python left to right solve krta hoa jata h
# print(100 / 10 * 2)
# print(100 / (10 * 2))
# print(2 + 3 - 7)
# Task 01
name = "Zia Uddin"
age = 17
city = "Karachi"
print("My name is",name,"and my age is", age, "I live in ", city)
# Task 02
num = int(input("Enter the number: "))
print(num * 2)
# Task 03
print("Hello" + "My Name is " + name + " I m " + str(age) + " year old")
# Task 04
lenght = float(input("Enter the Lenght: "))
width = float(input("Enter the width: "))
area = lenght * width
print("Your Area is", area)
# Task 05
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


