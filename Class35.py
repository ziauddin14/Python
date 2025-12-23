#Recursion: A function that calls itself to solve a samller part of the same problem
'''
Rules to follw:
1: a recursive function must call itself
2: a recursive function must have a base case to stop the recursion

Note:  IF there is no base case, the function will call itself infinitely and result in a stack overflow error.
Clarify your base case before writing the recursive case. otherwise you may end up with infinite recursion.
'''

def count_down (n):
    #Base Case
    if n <= 0:
        return
    print(n)
    count_down(n-1)  #Recursive Case
    
count_down(5)



def say_hello (n):
    #Base Case
    if n <= 0:
        return
    print("Hello")
    say_hello(n-1)  #Recursive Case
    
say_hello(3)


def sum_nunbers(n):
    if n == 1:   #Base Case
        return 1
    return n + sum_nunbers(n-1)  #Recursive Case

result = sum_nunbers(5)
# Expected: 5 + sum_nunbers(4)
# Expected: 5 + 4 + sum_nunbers(3)
# Expected: 5 + 4 + 3 + sum_nunbers(2)
# Expected: 5 + 4 + 3 + 2 + sum_nunbers(1)
# Expected: 5 + 4 + 3 + 2 + 1 = 15
print(result)  # Output: 15

def factorial(n):
    if n == 0:   #Base Case
        return 1
    return n * factorial(n-1)  #Recursive Case
result = factorial(5)
print(result)  # Output: 120

#Reverse a string using recursion
def reverse_string(s):
    if s == "":  #Base Case
        return s
    return  reverse_string(s[1:])+ s[0]  #Recursive Case
result = reverse_string("hello")
'''
Explantion:
Expected: reverse_string("ello") + "h"
Expected: (reverse_string("llo") + "e") + "h"
Expected: ((reverse_string("lo") + "l") + "e") + "h"
Expected: (((reverse_string("o") + "l") + "l") + "e") + "h"
Expected: ((((reverse_string("") + "o") + "l") + "l") + "e") + "h"
Expected: (((( "" + "o") + "l") + "l") + "e") + "h" = "olleh" 
'''
print(result)  # Output: "olleh"

#character count in a string using recursion
def char_count(s):
    if s == "":  #Base Case
        return 0
    return 1 + char_count(s[1:])  #Recursive Case
result = char_count("hello")
'''
Explanation:
Expected: 1 + char_count("ello")
Expected: 1 + (1 + char_count("llo"))
Expected: 1 + (1 + (1 + char_count("lo")))
Expected: 1 + (1 + (1 + (1 + char_count("o"))))
Expected: 1 + (1 + (1 + (1 + (1 + char_count
("")))))
Expected: 1 + (1 + (1 + (1 + (1 + 0
)))) = 5
'''
print(result)  # Output: 5

#Sum of digits in a number using recursion
def sum_of_digits(n):
    if n == 0:  #Base Case
        return 0
    return n % 10 + sum_of_digits(n // 10)  #Recursive Case
result = sum_of_digits(4664)
'''
Explanation:
Expected: 4 + sum_of_digits(466)
Expected: 4 + (6 + sum_of_digits(46))
Expected: 4 + (6 + (6 + sum_of_digits(4)))
Expected: 4 + (6 + (6 + (4 + sum_of_digits(0))))
Expected: 4 + (6 + (6 + (4 + 0))) = 20
'''
print(result)  # Output: 20