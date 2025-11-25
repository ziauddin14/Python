#*****************Inheritance in Python******************
'''
Inheritance: help you avoid repeating code. Instead of rewriting same attributes
and methods again and again, you put them in a common place and let other classes inherit from it.
Types of Inheritance:
1: Single Inheritance ==> One parent one child
2: Multilevel Inheritance ==> Grand Parent to grand child
3: Multiple In heritance ====> single class inherite more then one independent classes
'''
class dog:
    def sound(self):
        print("Bark")
class cat:
    def sound(self):
        print("Meow")

#With inheritance
class Animal:
    def sound(self):
        print("Some Sound")
    def speak(self):
        print("Animal Speaking")    
class Dog(Animal):
    def bark(self):
        print("Woof")
class Cat(Animal):
    pass
# Now Dog and cat both automatically get .sound()

d = Dog()
d.sound()

#Method Overriding
class Animal1:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal1):
    def speak(self):
        print("Bark!")
d = Dog()
d.speak()  # Outputs: Bark!


#Inheritance Broken with Constructor      
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        self.roll = roll
        self.name = name

#If inherite constructor in child then use super() keyword in child
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s = Student('Ali', 13)
print(s.name, s.roll)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(self.name, "has", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def show_info(self):
        print(self.name, "has", self.salary , "and ", self.team_size)
        
em = Employee("Zia", 17)
em.show_info()
mn = Manager("ABC", 2000, 10)
mn.show_info()