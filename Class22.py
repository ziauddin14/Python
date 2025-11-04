# *****************Sets in Python***********************
# Sets are ===> Unorder collection of unique items
# Use Cases: Remove Duplicates, set algebra(union/intersection), quick comparision between groups (students in two courses)...
# Sets are more reducing time compexity rather then list
# Syntax ==> name = {} .....without key value pairs
# You can't call set using brackets like list my_set[0] X
# my_set = {1,2,3}
# # Duplicate items are not allowed in sets
# my_set = {1,2,2,3}
# print(my_set)

# x = {1, 2, 3}
# x.add(4)
# x.remove(1)
# print(x)

# nums = [1,2,2,3,4,4]
# s1 = set(nums)    # second way of creating set
# print(s1)

# #For creating empty set you use the set() keyword with round brackets
# s2 = set()  #<====like this

# #You can easyly add multiple data  types in sets
# s3 = {'apple', 4}
# print(s3)


# #Basic method for sets
# fruits = {'apple', 'banana'}
# fruits.add('cherry')
# print(fruits)
# fruits.remove('banana')
# fruits.discard('banana') #discard remonve the element if present and doesnot give error if the element is not present
# x = fruits.pop()
# print(x)
# print(fruits)
# fruits.clear()
# print(fruits)

# Union ==> Joint all sets & Intersection ===> Pick the common one
A = {"Ali", "Sara", "Ahmed", "Zara"}
B = {"Sara", "bilal", "Zara", "Nida"}
A_union_B = A | B  # or A.union(B) <== second way
print(A_union_B)
A_Intersection_B = A & B  # or A.intersection(B) <===second way
print(A_Intersection_B)

A_diff = A - B  # Means those items who in  A not in B
print(A_diff)

B_diff = B - A  # Means those items who in  B not in A
print(B_diff)

# Set Comprehension
nums = [1, 2, 3, 2, 1, 4]
even_squres = {n**2 for n in nums if n % 2 == 0}
print(even_squres)


# isalpha() ==>The isalpha() method in Python is a built-in string method that checks if all characters within a string are alphabetic letters. It returns True if the string contains only letters (a-z, A-Z) and False otherwise. This includes cases where the string contains numbers, spaces, or special characters
# isdigit() ==> The isdigit() method in Python is a string method that checks if all characters in a given string are digits. It returns True if every character in the string is a digit (0-9), and False otherwise.

# find unique letters in sentence
sentence = "Data Science is fun"
unique_letters = {letter.lower() for letter in sentence if letter.isalpha()}
print(unique_letters)


# Create set of cubes using set comprehension
nums = [2, 4, 6, 7, 2, 4]
cube = {cube**3 for cube in nums}
print(cube)


# ZIP ==> combined 2 iterable and convert them into tupple
names = ["Ali", "Sara", "Ahmed"]
scores = [85, 90, 95]
print(list(zip(names, scores)))

a = [1, 2]
b = [10, 20, 30]
print(list(zip(a, b)))


marks = dict(zip(names,scores))
print(marks)



#ZIP method by using for loop
names2 = ['Ali', 'Sara', 'Ahmed']
marks2 = [85,55,78]
grades = ['A','D','C']
for names2,marks2,grades in zip(names2, marks2, grades):
  print(names2, marks2,grades)
  


#Enumerates
fruits = ['apple','banana','cherry']
for i, fruit in enumerate(fruits):
  print(i,fruit)
  
  
fruits = ['apple','banana','cherry']
for i, fruit in enumerate(fruits, start=1):
  print(i,fruit)