# Student Result Program with error handling
# This is my own code for a student result program that includes error handling for invalid inputs.
try:
    marks = int(input("Enter your marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    elif marks >= 50:
        print("Grade: E")
    else:
        print("You have failed.")

except ValueError as e:
    print(f"Invalid input: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Thank you for using the Student Result Program.")
 
# End of the program        
        
# Improving this program by ChatGPT
# Student Result Program with Error Handling and Retry

# while True:
#     try:
#         marks = int(input("Enter your marks (0-100): "))
#         if marks < 0 or marks > 100:
#             raise ValueError("Marks must be between 0 and 100.")

#         # Grading system
#         if marks >= 90:
#             grade = "A"
#         elif marks >= 80:
#             grade = "B"
#         elif marks >= 70:
#             grade = "C"
#         elif marks >= 60:
#             grade = "D"
#         elif marks >= 50:
#             grade = "E"
#         else:
#             grade = "F"

#         print(f"Your Grade: {grade}")

#         if marks >= 50:
#             print("Congratulations! 🎉 You passed.")
#         else:
#             print("Sorry 😔 You failed.")
#         break  # correct input mil gaya → loop se nikal jao

#     except ValueError as e:
#         print(f"Invalid input: {e}, please try again.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}, please try again.")

# finally:
#     print("Thank you for using the Student Result Program.")
# # End of the improved program