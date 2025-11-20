#*************OOPs in Python****************
'''
Method is a function written inside a class.
but with one superpower if automatically recieves the object it's working on that's called as "self"
Think of self as a variable that holds the object itself.
three types of methods:
1: Isntance methods: Most common, Take self, works with object. Example: def drive(self): pass
2: Class methods: Take cls instead of self, works with class level data : Example def from_model(cls, model): returm cls(model)
3: Static methods: No self or cls, Utility function inside the class. Example: def convert_miles_to_km (miles): return miles * 1.6
'''
class Car:
    def start(self):
        print("Car started")
c = Car()
c.start()  # calling method start using object c of class Car


''''
Encapsulation: Protecting you stuff
Restricting access to internal data so nobody messes it up.
In Python:
_name >>> You should not touch this. But you can
__name >>> No Seriously, don't touch this.
Encapsulation is not about security, it's about preventing accidently use cases.
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner  = owner
        self.__balance = balance    # private
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    
class Laptop:
    count = 0 
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        Laptop.count += 1 
    def info(self):
        print(f"Laptop Brand: {self.brand}, RAM: {self.ram}GB")
l = Laptop("Dell", 16)
l.info()
l = Laptop("Dell", 16)
l.info()
l2 = Laptop("HP", 8)
l2.info()
print(f"Total Laptops: {Laptop.count}")