# ***********Lambda Function**********
# Lambda function is a small anonymuos (nameless) function written un one line of code.
# It can take any number of arguments, but can only have one expression.
# Memory efficient and faster than normal functions.


# #simple squre function:
def square(x):
    return x * x


result = square(5)
print("Square using normal function:", result)

# #same function using lambda
square_lambda = lambda x: x * x
result_lambda = square_lambda(5)
print("Square using lambda function:", result_lambda)

# #add lambda function
add = lambda a, b: a + b
print(add(5, 8))


# # even number checking by using lambda function
even = lambda n: n % 2 == 0
print(even(5))

# maximum number finder using lambda function
max_num = lambda x, y: x if x > y else y
print(max_num(25, 89))

# write a program of even odd checker using lambda function
num = int(input("Enter a Number: "))
even_odd_checker = lambda number: "Even" if number % 2 == 0 else "Odd"
print(even_odd_checker(num))


# *********************map() Function in Python:***************
# The map() function in Python applies a given function to each item in an iterable (like a list or tuple)
# and returns a map object (an iterator) containing the results ======> seqeunce men multiple iterable de sakty hyn
squre = lambda x: x**2
nums = [1, 2, 3, 4, 5]
result = list(map(squre, nums))
print(result)

a = [1, 2, 3]
b = [4, 5, 6]
result = list(map(lambda x, y: x + y, a, b))
print(result)

"""
Tasks: Use Map to :
convert a list celsius temps into Fehnrenhiet (F = C x 9/5 + 32)
"""
temps_lits = [20, 35, 36, 10, 12]
fehrenhiet_temps = list(map(lambda c: (c * 9 / 5 + 32), temps_lits))
print(fehrenhiet_temps)

# Add 10 to each number in a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x + 10, nums))
print(result)

# Capitalize all names in a list
names = ["zia", "madam", "baba"]
result = list(map(lambda x: x.upper(), names))
print(result)


# ***************filter FUnction**************
# filter elements based on a condition (True/False)
# filter(function, iterable) <=== syntax

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)

# startswith()  <=====funtion
names = ["zia", "madam", "baba"]
a_name = list(filter(lambda n: n.startswith("z"), names))
print(a_name)

# Filter Positive Numbers:
nums = [-2, 5, 0, -8, 3]
pos_num = list(filter(lambda x: x > 0, nums))
print(pos_num)


# Print countries which contains 5 characters
countries = ["Pakistan", "China", "Saudi Arabia", "Italy"]
result = list(filter(lambda x: len(x) == 5, countries))
print(result)


# ****************reduce function*****************
# reduce() function (from functools) applies a function cumulatively to an iterable, reducing it to a single value.
from functools import reduce

nums = [2, 3, 4]
multi = reduce(lambda a, b: a * b, nums)
print(multi)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, nums))
print(sum_even)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_squre_even = reduce(
    lambda a, b: a + b, map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums))
)
print(sum_squre_even)
