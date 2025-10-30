#************Comprehensions in Python************
#Syntax of List Comprehension
# new_list = [expression for item in iterable if condition]
# List Comprehension
squares = [i**2 for i in range(1, 11)]
print(squares)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [num**2 for num in nums]
print(squares)

cel = [0, 10, 20, 30, 40, 50]
fah = [((9/5)*temp + 32) for temp in cel]
print(fah)

#find the first letter of each word in a sentence
words = ['Machine', 'Learning', 'is', 'fun']
first_letters = [word[0] for word in words]
print(first_letters)

#find the even numbers from a list comprehension 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# words = ['AI', 'Data', 'Science', 'is', 'the', 'future']
filtered_words = [word for word in words if len(word) > 3]
print(filtered_words) 

#output = [odd, even, odd, even, odd]
nums = [1, 2, 3, 4, 5]
output = ['even' if num % 2 == 0 else 'odd' for num in nums]
print(output)


#Output ==> convert into 1 Dimensional list using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
oneD_list = [num for row in matrix for num in row]
print(oneD_list)

#output  = [10,40,90]
a = [1,2,3]
b = [10,20,30]
# result = [x*y for x in a for y in b]
# print(result)
# result = [x*y for x,y in zip(a,b)]
result = [a[i] * b[i] for i in range(len(a))]
print(result)