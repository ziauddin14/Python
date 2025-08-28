# Program to check if the input character is a vowel or consonant

# character = input("Enter a character: ").lower()

# if len(character) == 1 and character.isalpha():
#     if character in 'aeiou':
#         print(f"{character} is a vowel.")
#     else:
#         print(f"{character} is a consonant.")
# else:
#     print("Invalid input. Please enter a single alphabet character.")


# Task01
'''
input ==> total shopping amount
If amount >= 5000 ==> 20% discount
elif amount >= 3000 ==> 10% discount
elif amount >= 1000 ==> 5% discount
else no discount 
print final price after discount
'''

amount = float(input("Enter total shopping amount: "))
if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 10
elif amount >= 1000:
    discount = 5
else:
    discount = 0

final_price = amount - (amount * discount / 100)
print(f"Your discount is: {discount}%")
print(f"Your final amount is: {final_price}")