# # password = input("Enter a password: ")

# # has_num = False
# # has_lowercase = False
# # has_uppercase = False
# # has_symbol = False

# # if len(password) < 8:
# #     print("Weak")
# # else:
# #     for ch in password:  
# #         if ch.isdigit():
# #             has_num = True
# #         elif ch.islower():
# #             has_lowercase = True
# #         elif ch.isupper():
# #             has_uppercase = True
# #         elif not ch.isalnum():
# #             has_symbol = True

# #     if has_num and has_lowercase and has_uppercase and has_symbol:
# #         print("Very Strong")
# #     else:
# #         print("Weak Password")

# # books = ['Python Crash Course', 'AI Basics', 'Data Science 101']
# # while True:
# #     print("\n Menu")
# #     print("1: Search A Book: ")
# #     print("2: Add new Book: ")
# #     print("3: Remove A Book: ")
# #     print("4: Show all Book: ")
# #     print("5: exit")
# #     choice = int(input("Choose an Option (1 - 5)"))
# #     if choice == 1:
# #         book = input("Write a Book Name what you want: ")
# #         if book in books:
# #             print("Book Found!")
# #         else:
# #             print("Book Not avaliable!")
# #     elif choice == 2:
# #         book = input("Enter a name what you wanna a Add: ")
# #         if book in book:
# #             print("Book Already Exist!")
# #         else:
# #             books.append(book)
# #             print("Book Added Successfully!")
# #     elif choice == 3:
# #         if book in books:
# #             books.remove(book)
# #             print("Book Remove Successfully!")
# #         else:
# #             print("Book Not Found!")
# #     elif choice == 4:
# #         print("\nAvaliable Books")
# #         for b in books:
# #             print("-", b)
# #     elif choice == 5:
# #         print("Exiting Programm, Good Bay!")
# #         break
# #     else:
# #         print("Invalid Choice , write between 1 - 5")
# import random
# questions = [{'question':'What is the capital of France?',
#               'options':['paris','london','rome'],
#               'answer':'paris'},
#              {'question':'2+2?',
#               'options':['4','6','8'],
#               'answer':'4'},
#              {'question':'python is a_____',
#               'options':['language', 'car', 'book'],
#               'answer':'language'},
#              {'question':'Bashaar is ____',
#               'options':['animal', 'human', 'costum'],
#               'answer':'animal'},
#              ]


# score  = 0
# selected_question = random.sample(questions, 3)
# for q in selected_question:
#     print('\n', q['question'])
#     for opt in q['options']:
#         print("-", opt)
    
#     user_answer = input("ENter a Answer :")
    
#     if user_answer.lower() == q['answer'].lower():
#         print("Correct Answer!")
#         score += 10
#     else:
#         print("Wrong Answer!")

# print("Total Score", score)
 
print({1,2,3}&{2,3,4})