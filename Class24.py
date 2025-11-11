"""
Task
Keep asking the user which book they want to borrow
if the book exist and copies > 0 , lend the book ==> reduce the count by 1
if no copies availiable ,print 'Not Availiable'
"""

# books = {
#     "Python Basics": 3,
#     "Data Science 101": 5,
#     "Machine Learning": 2,
#     "Deep Learning Guide": 1,
# }
# while True:
#     print("Available Books and Copies:")
#     for b, c in books.items():
#         print(b, "-", c)
#     userInput = input("ENter the book which you want (or enter done to exit): ")

#     if userInput.lower() == "done":
#         break

#     if userInput in books:
#         if books[userInput] > 0:
#             books[userInput] -= 1
#             print(
#                 f"You have borrowed '{userInput}'. {books[userInput]} copies remaining."
#             )
#         else:
#             print(f"Sorry! ${userInput} is not avaliable in our stock")
#     else:
#         print(f"Sorry ${userInput} is not avaliable")
#     print(f"Current inventory: {books}\n")

"""
Task 
Ask User: Enter amount to withdraw
if amount is not divisible by 10, print error.
Otherwise, break the amount into minimum number of notes
Show count of each note
"""
# amount = int(input('Enter a amount: '))
# if amount %10 != 0:
#   print('ATM can only dispense amounts divisible by 10')
# else:
#   notes = [1000,500,100,50,20,10]
#   for note in notes:
#     count = amount // note
#     if count > 0:
#       print(note, 'x', count)
#     amount = amount % note

"""
Task 
A class has students with marks in 5 subjects each subject is out of 100
Rules
A student passes only if: OverAll percentage >= 50% AND No subject is below  35 marks BT there 
is a grace rule:
if only one subject is below 35, but total percentage >= 60% the student still passes
Input Example: Enter marks separated by spaces: 78, 55, 90, 20, 67 
"""

marks = input("Enter 5 Subject marks separated by spaces: ")
marks = marks.split()
marks = [int(marks[i]) for i in range(5)]
total_marks = sum(marks)
percentage = total_marks / 5
failed_subjects_count = 0

for m in marks:
    if m < 35:
        failed_subjects_count += 1

print(f"\nTotal Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

if failed_subjects_count == 0:
    print("Result: Student PASSES.")
elif failed_subjects_count == 1 and percentage >= 60:
    print("Result: Student PASSES with GRACE rule.")
else:
    print("Result: Student FAILS.")

'''
marks = list(map(int, input('ENter marks seprated by spaces:').split()))
percentage = sum(marks) / len(marks)
fils = 0
for m in marks:
  if m <35:
    fils += 1
  if fils ==0 and percentage >= 50:
    print('pass')
  elif fils == 1 and percentage >= 60:
    print('pass ith grace')
  else: 
    print('fail')
'''