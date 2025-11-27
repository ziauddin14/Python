# ************Polymorphism in OOP ***********************
"""
Many forms
"""


class Dog:
    def speak(self):
        return "Bark!"


class Cat:
    def speak(self):
        return "Meow!"


class Cow:
    def speak(self):
        return "Moo!"


animals = [Dog(), Cat(), Cow()]
for a in animals:
    print(a.speak())  # <====This is Polymorphism


# ***************Polymorphism with Loop
class Shape:
    def area(self):
        return "No area"


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


class Square(Shape):
    def area(self):
        return 4 * 4


s1 = Circle()
s2 = Square()
for s in (s1, s2):
    print(s.area())


# ***********Polymorphism with Functions
def make_sound(animal):
    print(animal.speak())


make_sound(Dog())
make_sound(Cat())

# ************Polymorphism in Loops
for obj in [Dog(), Cat(), Cow()]:
    print(obj.speak())


class Car:
    def move(self):
        return "Car is Drive"


class Plan:
    def move(self):
        return "Plan is Flying"


class Ship:
    def move(self):
        return "Ship is Sailling"


for m in [Car(), Plan(), Ship()]:
    print(m.move())


# ********For inherite parent class all thing we use supr() keyword******
class Person:
    def show(self):
        print("Person info")


class Student(Person):
    def show(self):
        super().show()
        print("Student Info")


s1 = Student()
s1.show()


# ********Practise************
class Employee:
    def work(self):
        print("Emplyee is working")


class Developer(Employee):
    def work(self):
        print("Dev is Develop")


class Designer(Employee):
    def work(self):
        print("Designer is Designing")


d0 = Employee()
d1 = Developer()
d2 = Designer()
d0.work()
d1.work()
d2.work()


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Triangle(6,8), Rectangle(7,9)]
for s in shapes:
    print('Area: ', s.area())
  