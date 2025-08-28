# # Task 01
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
        
#     def show_details(self):
#         print(f"This is {self.brand} {self.model} and it costs {self.price} dollars.")
        
# m1 = Mobile("Samsung", "S22", 1200)
# m1.show_details()

# # Task 02
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def info(self):
#         print(f"Book: {self.title} by {self.author}, Pages: {self.pages}")

# b1 = Book("1984", "George Orwell", 328)
# b1.info()
# b2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
# b2.info()
# b3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# b3.info()

# # Task 03
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#     def make_sound(self):
#         print(f"The {self.name} goes '{self.sound}'")
        
# a1 = Animal("Dog", "Woof")
# a2 = Animal("Cat", "Meow")
# a3 = Animal("Cow", "Moo")

# a1.make_sound()
# a2.make_sound()
# a3.make_sound()

# Task 04 Advanced
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")

acc = BankAccount("Alice", 1000)
acc.display_balance()
acc.deposit(500)
acc.withdraw(200)