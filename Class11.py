#*******Tuple********
#Tuple is immutable
# Non-prrimitive data type ==> collection of items, ordered, indexed, allows duplicate values
# Tuple is defined by using () round brackets
#type of() function is used to check the data type of a variable  print(type(my_tuple))
#len() function is used to check the length of a variable
#Unpacking ==> ek variable ko multiple variables men break kar dena
person = ("Umaima", 19, "Teacher")
name,age,job = person
print(name,age,job)

numbers = (1,2,3,4,5,6,7)
print(numbers[1:4])

'''
Create a tuple of 5 Countries
Print th 3rd country
Unpack them into variables
Slice the first 3 countries
'''
countries = ("Pakistan", "Saudi Arab", "Palastine", "Afghanistan", "Iran")
print(countries[2])
country1,country2,country3,country4,country5 = countries
print(country1,country2,country3,country4,country5)
print(countries[0:3])


#************Dictionary*****************
#Non-primitive data type
student = {'name': 'Umaima', 'age': 19, 'marks': 85}
print(student['name'])
print(student.get('age'))
print(student.keys())
print(student.values())
print(student.items())
print(type(student))
student['grade'] = 'A+'
print(student)
del student['age']
print(student)

#print a key and its value using for loop
for k in student:
    print(f"{k}: {student[k]}")
    
#Nested Dictionary
#print each student's details using a for loop
students = {
    'student1': {'name': 'Ali', 'age': 20, 'marks': 90},
    'student2': {'name': 'Aisha', 'age': 21, 'marks': 95},
    'student3': {'name': 'Ahmed', 'age': 19, 'marks': 85}
}
for studentid, details in students.items():
    print(studentid, ":")
    for key, value in details.items():
        print(key, "=", value)
        
#Fibonacci series by using loops
# n = int(input("Fibonacci series ke kitne numbers chahiye? "))
# a, b = 0, 1
# print("Fibonacci series:")
# for _ in range(n):
#     print(a)
#     a, b = b, a + b
# print()
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
terms = int(input("How many terms do you want in the series?"))
print("Fibonacci Series:")
print(num1, num2, end=' ')
for i in range(terms -2):
    next_num = num1 + num2
    print(next_num, end=' ')
    num1 = num2
    num2 = next_num