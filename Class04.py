# Example 01:
print(10 + 5 * 2)
# Example 02:
print(100 / 10 * 2)
# Example 03:
print("AI" + " " + "Rocks")
# Example 04:
print(len("Data Science"))
# Example 05:
print(5 > 3 and 2 < 1)
# Make the variable with value of 2 and print it the add 1 and print it again and 
# add 1 and print it again
x = 2
print(x)
x += 1
print(x)
x += 1
print(x)
# Conditional Statement (IF ELSE CONDITION)
age = int(input("Enter Your Age Please: "))
if age>= 18 :
    print("Congratulation! You are eligible for Vote")
else:
    print("Sorry! You are not eligible for Vote ")
# Class Task:
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
print("Sum is:", num1 + num2)
print("Product is:",num1 * num2)
if num1 > num2:
    print("Number1 is Greater then Second")
else:
    print("Number2  is Greater then First")
# When if condition is false then he run the else block
# When you want to take multiple conditions then you use (elif)
marks = float(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid Numbers")
elif marks >= 90:
    print("Your Grade is: A")
elif marks >= 80 :
    print("Your Grade is: B")
elif marks >= 70:
    print("Your Grade is: C")
elif marks >= 60:
    print("Your Grade is: D")
else:
    print("Your Grade is: Fail ")
# Class Task: Takes temperature as input If above ==> Print "Hot" If between 20 and 30 ==> Print "Warm" Else "Cold"
temperature = float(input("Enter the temperature: "))
if temperature > 30:
    print("Hot")
elif temperature > 20 and temperature <= 30:
    print("Warm")
else:
    print("Cold")
# Even and Odd Number Checker
num = int(input("Enter your Number:"))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")   