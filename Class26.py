#****************OOP(Object Oriented Programming)***************** lets us create this things in code
'''
Bank Account = Data + Action
**Data: balance, account number, account type
**Actionas: deposit(), withdraw()


**********4 Core Concepts of OOP:****************
1: Class: Blueprint / design/ template / schema / structure  etc : A car desing
2: Object: A real thing built from the blueprint(Class).  Sonata, civic, Altas
3: Attributes: Data stored inside an object. like, color of car, weight of car, etc,
4: Methods: Functionas that belong to an object . like, car.start(), car.drift()
'''

class Student:
    def __init__(self, name,age):   #This is  constructor function this fn runs automatically when object create
        self.name = name
        self.age = age   
        
    
    def show_details(self):
        print(f"My Name is {self.name} and I'm {self.age} years old.")    
    
    def is_dult(self):
        if self.age > 18:
            print(f"{self.name} is adult")
        else:
            print(f"{self.name} is not adult")

s1 = Student("Zia", 17) # object s1 created from class student
s1.show_details()
s1.is_dult()
s2 = Student("Umaima", 19)
s2.show_details()
s2.is_dult()
s3 = Student("Noor", -1)
s3.show_details()
s3.is_dult()


#*********Basic Calculator Class***********
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

calc = Calculator(10, 5)
print(calc.add())       
print(calc.subtract())  
print(calc.multiply())  
print(calc.divide())    

    
    