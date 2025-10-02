# Default Parameters
def greet(name='Guest'):
    print('Hello, welcome to python class', name)
greet()
greet('Zia Uddin')
greet('Ali')
# Keyword Arguments
def introduce(name, age):
    print(f'Name: {name}, Age: {age}')
introduce(age=30, name='Zia Uddin')
# Variable Scope
x = 10  # Global variable
def display():
    x = 5  # Local variable
    print('Inside display function:', x)
display()
print('Outside display function:', x)

#global keyword
def set_global():
    global y
    y = 20 
set_global()
print(y) 

'''
write a function power(base, exxponent=2) that returns base raised to the power of exponent. If only base is given, square it. If both are given, compute normally.
'''
def power(base, exponent=2):
    return base ** exponent
print(power(3))        
print(power(2, 3))     
'''
write a function calculate_bill(price, tax=0.05, discount=0.10) that Adds tax to price subtract discount returns the final amount
'''
def calculate_bill(price, tax=0.05, discount=0.10):
    print((price + (price*tax))*discount)
calculate_bill(100)
calculate_bill(200, 0.08)

'''
Create a global variables counter = 0
write a fuunction increment() that increase counter by 1
call it 3 times and print the counter each time
'''
counter = 0
def increment():
    global counter
    counter += 1
    print(counter)
increment()
increment()
increment()

'''
write a function bank_balance() with a local variable balance = 1000
print balance inside the function.
try printing balance outside (should give error)
'''
def bank_balance():
    balance = 1000
    print('Inside bank_balance function:', balance)
bank_balance()
# print('Outside bank_balance function:', balance)  # This will give an error

'''
create a function set_global_name() that sets a global variable name.
Ask user for input inside the function print name outside the function to confirm its stored globally.
'''
name = ""
def set_global_name():
    global name
    name = input("Enter your name: ")
set_global_name()
print("Global name variable:", name)