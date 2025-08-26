# Q1. Create a set with numbers {1,2,3,4,5}.
# Add 6
# Remove 3
# Print final set

numbers_set = {1, 2, 3, 4, 5}
numbers_set.add(6)
numbers_set.remove(3)
print(numbers_set)

# Q2. Given:
# A = {10, 20, 30}
# B = {20, 40, 50}
# Find:
# A ∪ B
# A ∩ B
# A − B
A = {10, 20, 30}
B = {20, 40, 50}
union_set = A.union(B)
intersection_set = A.intersection(B)
difference_set = A.difference(B)
print("A ∪ B:", union_set)
print("A ∩ B:", intersection_set)
print("A − B:", difference_set)

# #Q3. Create dictionary:
# student = {"name":"Sara", "age":21, "marks":92}
# Add new key "grade":"A"
# Update age = 22
# Delete marks
student = {"name": "Sara", "age": 21, "marks": 92}
student["grade"] = "A"
student["age"] = 22
del student["marks"]
print(student)

# Q4. Create dict of 3 cities with their population. Print all cities using .keys() and all populations using .values().
cities_population = {"New York": 8419600, "Los Angeles": 3980400, "Chicago": 2716000}
print("Cities:", cities_population.keys())
print("Populations:", cities_population.values())

# Q5. Given students dict:
# marks = {"Ali":70, "Sara":85, "Ahmed":90, "Ayesha":60}
# Find and print topper’s name.
marks = {"Ali": 70, "Sara": 85, "Ahmed": 90, "Ayesha": 60}
topper = max(marks, key=marks.get)
print("Topper's name:", topper)