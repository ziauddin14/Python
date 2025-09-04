#set a secret number, ask user for input, let user guess the number, if user guesses wrong 
# print if number higher then secret number "your number is to high and if number is lower then secret numer
# print your number is to low until user guesses the correct number by usinf for loop and if else condition

# secret_number = 5
# guess = 0
# while guess != secret_number:
#     guess = int(input("Guess the secret number (between 1 and 10): "))
#     if guess < secret_number:
#         print("Your number is too low.")
#     elif guess > secret_number:
#         print("Your number is too high.")
#     else:
#         print("Congratulations! You've guessed the correct number.")



# range()function can be used to generate a sequence of numbers, 
# which can be useful for creating loops that iterate a specific number of times.
# The range() function can take one, two, or three arguments:
# range(end): Generates numbers from 0 to end-1.
# range(start, end): Generates numbers from start to end-1. 

#is Code ko rook ne ke liye hum break statement ka use karenge
# break statement loop ko turant rok deta hai, chahe loop ka condition true ho ya false.

'''
Create a simple menu-driven ATM simulation:
Ask the user to log in using PIN.
Show a menu with options: Check Balance, Deposit, Withdraw, Exit.
Keep showing the menu untill user exits.
This integrate:
while loop
if-else condition
break statement
User input
'''
correct_pin = "1234"
balance = 1000

while True:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Login successful.")
        break
    else:
        print("Incorrect PIN. Please try again.")

while True:
    print("***ATM Menu:***")
    print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print("Your current balance is:",balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited:", amount, ". New balance:", balance)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print("Withdrew:", amount, ". New balance:", balance)
    elif choice == "4":
        print("Exiting. Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please select again.")