# Multiple variable assignment
x = y = z = 100
print(x, y, z)
# We can assign diffrent data types thrrow multiple assignment operator

# String repetation
a = "Hello"
b = a * 3
print(b)
# String concatenation
c = a + " World"
print(c)

# String Slicing
d = "PAKISTAN"
print(d[0:5])  # Output: PAKIS
print(d[6:])   # Output: TAN
print(d[:5])   # Output: PAKIS
print(d[:])    # Output: PAKISTAN
# Rule of slicing is that it will not include the last index
# Stepping parameter in slicing
print(d[0:11:2])  # Output: PAIAN
print(d[::2])    # Output: PAIAN
# Reverse string
print(d[::-1])  # Output: NATSIKAP
# index[start:end:step]

# Take a string "Artificial Intelligence" and:
#     print first 5 letters
#     print last 3 letters      
#     reverse the string
#     print every 2nd character

s = "Artificial Intelligence"
print(s[:5])          # Output: Artif
print(s[-3:])         # Output: ence
print(s[::-1])       # Output: ecnetneI lacifitra
print(s[::2])        # Output: Aifc ntnlgnc

# Task02
# Ask the user for a sentence and: 
#     count the total number of characters
#     count the number of spaces
#     replace all spaces with -

sentence = input("Enter a sentence: ")
total_characters = len(sentence)
print("Total characters:", total_characters)
space_count = sentence.count(" ")
print("Total spaces:", space_count)
modified_sentence = sentence.replace(" ", "-")
print("Modified sentence:", modified_sentence)
# print all character except last 3 character
sentence = "Artificial"
print("All characters except last 3:", sentence[:-3])

# Task03
# word = "MACHINELARNING"
# PRINT EVERY 2ND CHARACTER FROM START
# PRINT EVERY 2ND CHARACTER FROM THE END
# REVERSE ONLY FIRST 6 CHARACTERS

word = "MACHINELARNING"
print("Every 2nd character from start:", word[::2])
print("Every 2nd character from end:", word[::-2])
print("Reversed first 6 characters:", word[:6][::-1])

# palindrome kia hota h 
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Examples include "madam", "racecar", and "A man, a plan, a canal, Panama!"
# Check if a string is palindrome or not
sentence = input("Enter a string: ")
if sentence == sentence[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
