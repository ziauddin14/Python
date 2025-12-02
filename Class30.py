class Student:
    school_name = 'ABC School Name'   #Class Attribute
    
    def __init__(self, name):
        self.name = name   #Object Attribute
    
s1 = Student('Zia')
print(s1.school_name)

#Class attributes belong to the class, not the object
#Every object sees the same value
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
b1 = BankAccount(120000)
b1.__balance = 2222        
print(b1.get_balance())

class Student:
    def __init__(self, name, grade):
        self.__grade = grade
        self.name = name
    
    def get_grade(self): # Getter
        return self.__grade
    
    def set_grade(self, new_grade): # Setter
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid Grade")

class Dog:
    count = 0 #Class Variables
    
    def __init__(self, name):
        self.name = name
        Dog.count += 1
d1 = Dog('Tommy')
d2 = Dog('Snoopy')
print(Dog.count)

class MathTools:
    @staticmethod
    def add(a,b):
        return(a+b)
m1 = MathTools
print(m1.add(2,3))

class Employee:
    company = "Google"
    def change_company(cls, new_company):
        cls.company = new_company
e1 = Employee
print(e1.company)

e2 = Employee

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @classmethod
    def from_string(cls, data):
        name, marks = data.split('-')
        return cls(name, int(marks))
s = Student('Hamza', 94)
s2 = Student.from_string('Ali-88')


class Laptop:
    def __init__(self, price):
        self.__price = None
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Error: Price must be greater than 0")


# l1 = Laptop(50000)
# print("Laptop Price:", l1.get_price())
# l1.set_price(65000)
# print("Updated Price:", l1.get_price())
# l1.set_price(-200)   

class Employee:
    percent = 10
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def change_raise_percent(cls, raise_percent):
        cls.percent = raise_percent
    def apply_raise(self):
        increase = self.salary * (type(self).percent / 100)
        self.salary += increase
e1 = Employee("Ali", 50000)
e2 = Employee("Sara", 70000)
e1.apply_raise()
e2.apply_raise()
print(e1.name, e1.salary)
print(e2.name, e2.salary)
Employee.change_raise_percent(20)
e1.apply_raise()
print("After new raise:", e1.salary)

class Student:
    # class variable
    total_students = 0

    def __init__(self):
        # private attribute
        self.__marks_list = []
        Student.total_students += 1

    # getter (returns a copy)
    def get_marks(self):
        return self.__marks_list.copy()

    # method: add_mark()
    def add_mark(self, mark):
        if not isinstance(mark, (int, float)):
            raise ValueError("Mark must be a number")
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100")
        self.__marks_list.append(mark)

    # method: avg()
    def avg(self):
        if len(self.__marks_list) == 0:
            return 0
        return sum(self.__marks_list) / len(self.__marks_list)

    # static method: check_pass(avg)
    @staticmethod
    def check_pass(avg):
        return avg >= 50

    # class method: show_total_students()
    @classmethod
    def show_total_students(cls):
        return cls.total_students


# Example usage:
s1 = Student()
s1.add_mark(60)
s1.add_mark(80)
s1.add_mark(40)

print("Marks:", s1.get_marks())
print("Average:", s1.avg())
print("Passed:", Student.check_pass(s1.avg()))
print("Total Students:", Student.show_total_students())
