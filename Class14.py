#  ##***************************************Python Surprise Test ***************************************
 
#  #Ask for user's name and grade
# name = input("Enter your name: ")
# Grade = int(input("Enter your class: "))

# # Ask for 5 subject marks and store them into a list
# marks = []
# for i in range(1, 6):
#     mark = float(input(f"Enter marks for subject {i}: "))
#     marks.append(mark)
# maxMarks = max(marks)
# minMarks = min(marks)
# # Functions for total, average, and grade
# def total(marks):
#     return sum(marks)

# def average(total):
#     return total / 5

# def grade(average):
#     if average >= 90:
#         return "A+"
#     elif average >= 80:
#         return "A"
#     elif average >= 70:
#         return "B"
#     elif average >= 60:
#         return "C"
#     else:
#         return "F"

# # Call functions
# Total = total(marks)
# Average = average(Total)
# student_grade = grade(Average)

# #  Give feedback using logical operators
# if student_grade == "A+" or student_grade == "A":
#     feedback = "Excellent work! Keep it up!"
# elif student_grade == "B" or student_grade == "C":
#     feedback = "Good job!"
# else:
#     feedback = "You need to improve."

# print("----- Student Report -----")
# print(f"Name: {name}")
# print(f"Class: {Grade}")
# print(f"Marks: {marks}")
# print(f"Total Marks: {Total}")
# print(f"Average: {Average}")
# print(f"Grade: {student_grade}")
# print(f"Feedback: {feedback}")
# print(f"Marks marks: {maxMarks}")
# print(f"Min Marks: {minMarks}")












# Program for 3 Students Marks Report

def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total / 5

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

print(" Student Marks Report System \n")

# Loop for 3 students
for s in range(1, 4):
    print(f"\n Enter Details for Student {s}")
    name = input("Enter student's name: ")
    grade = input("Enter student's class/grade: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = calculate_total(marks)
    average = calculate_average(total)
    student_grade = calculate_grade(average)

    # Feedback using logical operators
    if student_grade == "A+" or student_grade == "A":
        feedback = "Excellent work Keep it up!"
    elif student_grade == "B" or student_grade == "C":
        feedback = "Good job"
    else:
        feedback = "You need to improve. "

    print("\n----- Student Report -----")
    print(f"Name: {name}")
    print(f"Class: {grade}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {student_grade}")
    print(f"Feedback: {feedback}")
