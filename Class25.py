
#----------------------Basic Python Coding Practice---------------#

"""
input a password.check if it's strong: 
Atleast 8 characters contain both letters and numbers 
contains at least one special character
"""

password = input("Enter a password: ")

has_letter = False
has_number = False
has_special = False
special_chars = "!@#$"

for ch in password:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_number = True
    elif ch in special_chars:
        has_special = True

if len(password) >= 8 and has_letter and has_number and has_special:
    print("Strong Password!")
else:
    print("Weak Password. Make sure it has:")
    print("- At least 8 characters")
    print("- Both letters and numbers")
    print("- At least one special character")


#input a sentence ,count vowels and consonents
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for ch in sentence:
    if ch.isalpha():         
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)


#check if an email is valid: 
# Must contain @ and . 
# Must not start or end with @ or . 
# Only one @ alloed
email = input("Enter an email: ")
has_at = False
has_dot = False
at_count = 0
if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
    print("Invalid email!")
else:
    for ch in email:
        if ch == "@":
            at_count += 1
            has_at = True
        elif ch == ".":
            has_dot = True

    if has_at and has_dot and at_count == 1:
        print("Valid email!")
    else:
        print("Invalid email!")


#input a sentence ==> crate a dictionary {word: lenght}
# but only for words>= 4 letters create it with dict comprehension 
sentence = input("Enter a sentence: ")
word_lengths = {word: len(word) for word in sentence.split() if len(word) >= 4}
print(word_lengths)



#take a input Make a dictionary showing how many times each character apeears?
text = input("Enter a string: ")
char_count = {}
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print(char_count)



#Replace All vowels with * in string
text = input("Enter a string: ")
for vow in text:
    if vow in "aeiouAEIOU":
        vow = vow.replace(vow, "*")
    print(vow)