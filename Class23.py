
# ***************Enumerates and Variables Unpacking***********
# Variable packing: putting multiple value into one variable
data = 10, 20, 30
print(data)
# convert into the tupple
# Unpacking variables: taking values out into multiple variables
a, b, c = data
print(c)

x = [1, 2, 3, 4, 5]
a, *b = x
print(a)  # pehli value 1 a men aye gi
print(b)  # baqi values b men jakr list print hojayegi

pairs = [(1, 2), (3, 4), (5, 6)]
for x, y in pairs:
    print(x + y)

a, b, c = "CAT"
print(c)

# variable swapping
x, y = 5, 10
y, x = x, y
print(y, x)


records = [(2, 4, 6), (1, 3, 5), (10, 20, 30)]
for x, y, z in records:
    print(x + y + z)

# sentence = input("Enter a sentence: ")
# words =sentence.lower().split()
# totalWords = len(words)
# totalUniq = len(set(words))
# print(totalUniq)
# print(totalWords)


# Check if a number is an Armsstrong number
# 153 is an Armstrong number because it has three digits, and \(1^{3}+5^{3}+3^{3}\) equals \(1+125+27=153\)
number = input("Enter a number: ")
sum_pf_cubes = sum(int(d) ** len(number) for d in number)

if sum_pf_cubes == int(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# Reverse a string manually
sentence = input("Enter a string: ")
reversed_s = ""
for char in sentence:
    reversed_s = char + reversed_s
print(reversed_s)


# Palindrome checker with same logic....
sentence = input("Enter a string: ")
reversed_s = ""
for char in sentence:
    reversed_s = char + reversed_s
if sentence == reversed_s:
    print("Its a Palindrome")
else:
    print("Not palindrome")







num_rows = int(input('Enter rows: '))
for i in range(1, num_rows + 1):
    for j in range(i):
        print(i, end="")
    print()
