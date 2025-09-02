class Student:
    # Class Attribute (common for all students)
    school = "NextGen Coders"

    def __init__(self, name, age, student_id):
        # Instance Attributes (har student ka alag data)
        self.name = name
        self.age = age
        self.student_id = student_id

    # Instance Method (specific student ka intro)
    def introduce(self):
        return f"Hello! I am {self.name}, {self.age} years old, ID: {self.student_id}."

    # Class Method (school ka naam update karna)
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        return f"School updated to: {cls.school}"

    # Static Method (general info jo kisi ek student se related nahi)
    @staticmethod
    def school_info():
        return "This system manages students of coding schools."


# 🔹 Objects (students)
s1 = Student("Ali", 20, 101)
s2 = Student("Zia", 22, 102)

# Instance Methods
print(s1.introduce())
print(s2.introduce())

# Class Method
print(Student.change_school("AI Coders"))

# Ab dono ka school change hogya
print(s1.school)
print(s2.school)

# Static Method
print(Student.school_info())
