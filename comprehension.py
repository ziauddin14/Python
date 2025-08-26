# Practice Questions:
# 1:nums = [1,2,3,4,5,6,7,8,9]
# → List comprehension likho jo sirf odd numbers return kare.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_numbers = [num for num in nums if num % 2 != 0]
# print(odd_numbers)

# 2:sentence = "python is awesome"
# → List comprehension likho jo har word ke first letter nikal kar ek list banaye.
# sentence = "python is awesome"
# first_letters = [word[0] for word in sentence.split()]
# print(first_letters)

# 3: students = {"Ali":85,"Sara":60,"Bilal":90,"Ayesha":75}
# → Dict comprehension likho jo har student ke liye "Pass" ya "Fail" store kare (pass if marks ≥ 70).
# students = {"Ali": 85, "Sara": 60, "Bilal": 90, "Ayesha": 75}
# result = {name: ("Pass" if marks >= 70 else "Fail") for name, marks in students.items()}
# print(result)

# 4: nums = [1,2,2,3,4,4,5]
# → Set comprehension likho jo sab numbers ka cube store kare.
# nums = [1, 2, 2, 3, 4, 4, 5]
# cubes_set = {num ** 3 for num in nums}
# print(cubes_set)


# 🧩 Advanced Comprehension Challenges
# Q1. Nested List Comprehension
# Matrix =
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 👉 Task: List comprehension likho jo sirf diagonal elements (1,5,9) nikal le.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
# print(diagonal_elements)

# Q2. Conditional Dictionary Comprehension
# nums = range(1,11)
# 👉 Dict comprehension likho jisme:
# Key = number
# Value = "Even" agar number even ho
# Value = "Odd" agar number odd ho
# nums = range(1, 11)
# even_odd_dict = {num: ("Even" if num % 2 == 0 else "Odd") for num in nums}
# print(even_odd_dict)

# Q3. Filtering with Set Comprehension
# Sentence = "comprehension makes python powerful"
# 👉 Set comprehension likho jo sirf unique vowels (a,e,i,o,u) extract kare.
# sentence = "comprehension makes python powerful"
# vowels_set = {char for char in sentence if char in 'aeiou'}
# print(vowels_set)

# Q4. Dictionary with Calculation
# marks = {"Ali":85, "Sara":92, "Bilal":78, "Ayesha":88}
# 👉 Dict comprehension likho jisme:
# Key = student ka naam
# Value = marks ko percentage me convert karke (out of 100, bas + "%" lagao string ke sath).
# 👉 Expected jaisa: {"Ali":"85%", "Sara":"92%", ...}
# marks = {"Ali": 85, "Sara": 92, "Bilal": 78, "Ayesha": 88}
# percentage_dict = {name: f"{score}%" for name, score in marks.items()}
# print(percentage_dict)

# Q5. Nested Comprehension Challenge (thoda tough)
# 👉 Ek list banao using comprehension:
# Values: [(x,y) for x in range(3) for y in range(3)]
# Matlab har possible pair (x,y) store ho jae.
pairs_list = [(x, y) for x in range(3) for y in range(3)]
print(pairs_list)