# 1. Ek list banao numbers = [10, 20, 30]
# 2. Usme 40 add karo (append)
# 3. Index 1 par 15 insert karo
# 4. Last item hatao (pop)
# 5. List ko sort karo
numbers = [10, 20, 30]
numbers.append(40)  # Step 2: Add 40 to the list
numbers.insert(1, 15)  # Step 3: Insert 15 at index 1
numbers.pop()  # Step 4: Remove the last item
numbers.sort()  # Step 5: Sort the list
# Print the final list
print(numbers)  # Output: [10, 15, 20, 30]

# (B) Tuple Practice
# 1. Ek tuple banao (5, 10, 15)
# 2. Usko unpack karke variables a, b, c me store karo
# 3. Print a+b+c
# 4. Try changing tuple[0] = 100 → error aani chahiye
tuple_numbers = (5, 10, 15)  # Step 1: Create a tuple
a, b, c = tuple_numbers  # Step 2: Unpack the tuple into variables
print(a + b + c)  # Step 3: Print the sum of a, b, and c
# Step 4: Uncommenting the next line will raise an error because tuples are immutable
# tuple_numbers[0] = 100  # This line will raise a TypeError if uncommented
print(tuple_numbers)  # Uncomment to see the tuple

# (C) Mixed List and Tuple Practice
# Ek list banao jisme 3 tuples ho:
students = [("Ali", 20), ("Sara", 22), ("Ahmed", 21)]

# Ab:
# 1. Second student ka naam print karo
# 2. Third student ki age print karo
# 3. Naya student ("Ayesha", 19) add karo list me
print(students[1][0])  # Step 1: Print the name of the second student
print(students[2][1])  # Step 2: Print the age of the third student
students.append(("Ayesha", 19))  # Step 3: Add a new student
print(students)  # Print the updated list of students