# Loops in python
# Loops are used to repeat a block of code multiple times until a certain condition is met.
# In Python, there are two main types of loops: for loops and while loops.
# while loop code explanation firstly initializes a counter variable and then checks a condition the counter variable
# then increments or decrements based on the logic defined within the loop.
count = 1 #initialize
while count <= 5: #condition
    print("Count is", count)
    count += 1 #increment

# Reverse Counter from 50 to 01:
count = 50 
while count >= 1: 
    print("Count is", count)
    count -= 1

# Password Checker:
password = "python1234"
guess = ""
while guess != password:
    guess = input("Enter the password: ")
print("Access Granted!")


#for keyword is used to create a for loop, which iterates over a sequence (like a list, tuple, or string) or a range of numbers.
#in keyword is used to check if a value exists within a sequence.
#range keyword is used to generate a sequence of numbers. 2 parameters can be passed: start and end. end is exclusive. 3rd parameter is step.
# print even numbers from 2 to 20:
#FOR LOOP
for count in range(2, 21, 2):
    print("Count is", count)

#Add number from 1 to 10 using for loop
total = 0
for i in range(1, 11):
    total += i
print("Total is", total)

#Print table of 2 using for loop
for i in range(1, 11):
    print("2 x", i, "=", i * 2)

#DIffrence between For and Whie Loop : A for loop iterates over a sequence for a fixed number of times,
# while a while loop repeats as long as a condition remains true.
#Nested Loop ==> Loop inside another loop
for i in range(1, 6):
     for j in range(1, 6):
         print(i*j, end="\t") #\t is used to add a tab space
     print() # Print a new line after each row
     
     
#Take a input from user and count the vowel in that string using for loop without using if else condition
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in string:
    count += char in vowels
print("Number of vowels:", count)
