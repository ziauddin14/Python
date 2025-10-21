#****Worm up exceptions handling in python****
'''
Ask the user for two integers and print thier division result. Handle: Non-numeric input , Division by Zero
'''
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = num1 / num2
except ValueError:
    print("Error: Non-numeric input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of {num1} divided by {num2} is {result}")
finally:
    print("Thank you for using the division calculator.")

#****************Library and Modules in Python*****************
# import math   <== math is a module

#write a program for square root of any number
import math
print("Square Root Calculator")
input_number = float(input("Enter a number to find its square root: "))
print(math.sqrt(input_number))

#Calculate cos90 
# import math
# print(math.cos(90))

#Value of Pi
# import math
# print("Value of Pi is:", math.pi)

# Calculate the square root of a number, and the value of pi using 'from import' statement
#Pora module nhi ayega sirf jo chize hum import karenge wo ayegi
# from math import sqrt, pi

#Aliesing: hum kisi bhi function ko alies(apna naam) de sakte hain
# import math as m

#How to install external modules using pip for VS Code terminal
# pip install module_name 

#Example of an external module 
# from pptx import Presentation


#Some examples of math module functions
import math as m 
a = 9
print("Square root of", a, "is:", m.sqrt(a))
print("Value of Pi is:", m.pi)
print("Ceiling value of 4.3 is:", m.ceil(4.3))
print("Floor value of 4.7 is:", m.floor(4.7))
print("Sine of 90 degrees is:", m.sin(m.radians(90)))
print("Cosine of 0 degrees is:", m.cos(m.radians(0)))
print("Factorial of 5 is:", m.factorial(5))
print("Tangent of 45 degrees is:", m.tan(m.radians(45)))

#Exercise :
'''
Ask user for angles in degrees , print sin cos and tan values of that angle'''
angle = float(input("Enter an angle in degrees: "))
radian = m.radians(angle)
print(f"Sine of {angle} degrees is: {m.sin(radian)}")
print(f"Cosine of {angle} degrees is: {m.cos(radian)}")
print(f"Tangent of {angle} degrees is: {m.tan(radian)}")

#Problem 2: Ask user for a number and print its cube and factorial using math module
number = int(input("Enter a number to find its cube and factorial: "))
print(f"Cube of {number} is: {m.pow(number, 3)}")
print(f"Factorial of {number} is: {m.factorial(number)}")

#Problem 3: calculate the area of a circle using Pi (radius is 33 cm)
radius = 33
area = m.pi * m.pow(radius, 2)
print(f"Area of the circle with radius {radius} cm is: {area} cm²")






#time library in python ===> best for delay in program execution    
import time
print("One")
time.sleep(2)  # wait for 2 seconds
print("Two")
# time.time()  # returns current time in seconds since 1 January 1970
print("Current time in seconds since 1 January 1970:", time.time())
# time.ctime()  # returns current time in a readable format
print("Current time:", time.ctime())