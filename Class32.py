# import random

# start_num = int(input("Enter a Starting Point: "))
# ending_num = int(input("Enter an Ending Number: "))

# secret = random.randint(start_num, ending_num)
# print("Welcome to the Guessing Game!")

# count = 0   
# max_tries = 3

# while count < max_tries:
#     user_input = int(input("Guess the Number: "))
#     count += 1

#     if user_input == secret:
#         print("You Won!")
#         break
#     else:
#         remaining = max_tries - count
#         print("Wrong Guess!")
#         print("Tries Left:", remaining)
#         if secret > user_input:
#             print("Your NUmber is to high!")
#         else:
#             print("Your Number is too Low!")

# if count == max_tries and user_input != secret:
#     print("You Lost! The secret number was:", secret)

# import random

# print("1: Easy Level: (Tries 5 )")
# print("2: Medium Level: (Tries 4 )")
# print("3: Hard Level: (Tries 3 )")

# choice = int(input("ENter your Choice (1/2/3)"))
# if choice == 1:
#     start_num = 1
#     end_num = 10
#     max_tries = 5
# elif choice == 2:
#     start_num = 1
#     end_num = 20
#     max_tries = 4
# elif choice == 3:
#     start_num = 1
#     end_num = 50
#     max_tries = 3
# else:
#     print("Invalid Choice")

# secret = random.randint(start_num, end_num)
# print("Welcome to the Guessing Game!")

# count = 0   
# max_tries = 3

# while count < max_tries:
#     user_input = int(input("Guess the Number: "))
#     count += 1

#     if user_input == secret:
#         print("You Won!")
#         break
#     elif secret > user_input:
#         print("Your NUmber is to high!")
#         remaining = max_tries - count
#         print("Wrong Guess!")
#         print("Tries Left:", remaining)
#     elif secret < user_input:
#         print("Your NUmber is to low!")
#         remaining = max_tries - count
#         print("Wrong Guess!")
#         print("Tries Left:", remaining)

# if count == max_tries and user_input != secret:
#     print("You Lost! The secret number was:", secret)

#Adding Score System: easy: 10(-2), medium:50(-5), hard:100(-10)
#Replay  option

import  random 
def playGame():
    choice = int(input("Enter 1 for easy, 2 for medium, 3 for hard difficulty: "))
    while choice != 1 and choice !=2 and choice !=3:
        print("Enter a valid choice: ")
        choice = int(input("Enter 1 for easy, 2 for medium, 3 for hard difficulty: "))
    if choice == 1:
        secret = random.randint(1,10)
        trials = 5
        score = 2
        panelty = 