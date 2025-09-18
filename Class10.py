# 2 Dimensional list (list inside list)
list = ["Apple", ["chaunsa", "ritol", "sindhri"], "mango"]
print(list[1][2])

list = ["Apple", ["chaunsa", "ritol", "sindhri"], "mango", ["red", "green", "blue"]]
# This is also 2 Dimensional list

# 3 Dimansional List (list inside another list)
list = ["Apple", ["chaunsa", [1, 2, 3], "sindhri"], "mango", ["red", "green", "blue"]]
print(list[1][1][1])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[row][column]
print(matrix[2][1])

for i in matrix:
    print(i)

# Nested Loops
for i in matrix:
    for col in i:
        print(col)


marks = [[80, 90, 70], [60, 75, 85], [95, 88, 92]]
studentNumber = 1
for row in marks:
    total = 0
    for col in row:
        total += col
    print(f'Student {studentNumber}: {total / len(row)}')
    studentNumber += 1


# n = int(input("Enter any number: "))
# total = 0
# for i in range(n):
#     total += i
# print("The total numbers of sum from 1 to your's is: ",  total)


for i in range(2, 11):         
    for j in range(1, 11):     
        print(i, "X", j, "=", i * j)


# text = input("Enter a string: ")
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text  

# print("Reversed string:", reversed_text)

num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))

for i in range(num1, num2):
    num1 += num2
print()