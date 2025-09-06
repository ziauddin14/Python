# # # 📝 NumPy Practice Problems (Arrays, Indexing & Slicing) # # # # #
# # # 🔹 Q1: Create a NumPy array
# # # Ek NumPy array banao jisme 1 se 10 tak ke numbers ho.
import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Q1 Array:", arr)

# # # 🔹 Q2: Indexing
# # # Array = [5, 10, 15, 20, 25, 30]
# # # First element print karo
# # # Third element print karo
# # # Last element print karo
arr2 = np.array([5, 10, 15, 20, 25, 30])
first_element = arr2[0]
third_element = arr2[2]
last_element = arr2[-1]
print("Q2 First element:", first_element)
print("Q2 Third element:", third_element)
print("Q2 Last element:", last_element)

# # # 🔹 Q3: Slicing
# # # Array = [10, 20, 30, 40, 50, 60, 70, 80]
# # # Elements 2 se 5 (inclusive of 2, exclusive of 5) print karo
# # # Pehle 4 elements print karo
# # # Last ke 3 elements print karo
arr3 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
slice_2_to_5 = arr3[2:5]
first_4_elements = arr3[:4]
last_3_elements = arr3[-3:]
print("Q3 Elements 2 to 5:", slice_2_to_5)
print("Q3 First 4 elements:", first_4_elements)
print("Q3 Last 3 elements:", last_3_elements)

# # # 🔹 Q4: Modify element
# # # Array = [2, 4, 6, 8, 10]
# # # Index 2 pe jo element hai usse 100 bana do
# # Array print karo
arr4 = np.array([2, 4, 6, 8, 10])
arr4[2] = 100
print("Q4 Modified Array:", arr4)

# # # 🔹 Q5: Slice update
# # # Array = [1, 2, 3, 4, 5, 6, 7]
# # # Index 2 se 4 tak ke elements ko [99, 100, 101] se replace karo
arr5 = np.array([1, 2, 3, 4, 5, 6, 7])
arr5[2:5] = [99, 100, 101]
print("Q5 Updated Array:", arr5)

# # # 🚀 Bonus Challenge
# # # Array = [10, 20, 30, 40, 50, 60]
# # # Sirf even index wale elements print karo (0, 2, 4, …)
arr6 = np.array([10, 20, 30, 40, 50, 60])
even_index_elements = arr6[::2]
print("Bonus Challenge Even index elements:", even_index_elements)

# # 🔹 Q6: 2D Array Indexing
marks = np.array([
    [80, 75, 90],   # Ali
    [60, 85, 70],   # Sara
    [90, 95, 88]    # John
])

# # # 🔹 Q1: Sara ke saare marks print karo
sara_marks = marks[1]
print("Q1 Sara ke marks:", sara_marks)

# # # 🔹 Q2: John ka Science mark print karo
john_science_mark = marks[2, 2]
print("Q2 John ka Science mark:", john_science_mark)

# # # 🔹 Q3: Sirf English ke marks print karo (sab students ke)
english_marks = marks[:, 1]
print("Q3 English ke marks:", english_marks)

# # # 🔹 Q4: Sara ke English mark ko 100 kar do aur updated array print karo
marks[1, 1] = 100
print("Q4 Updated Marks Array:\n", marks)

# # # 🔹 Q5: Har student ke average marks nikaalo (row-wise average)
average_marks = np.mean(marks, axis=1)
print("Q5 Average Marks of each student:", average_marks)

# # 🔹 Q1: Zeros
# # Ek 3×4 matrix banao jisme sirf 0 ho.
zeros_matrix = np.zeros((3, 4))
print("Q1 Zeros Matrix:\n", zeros_matrix)

# # 🔹 Q2: Ones
# # Ek 2×5 matrix banao jisme sirf 1 ho.
ones_matrix = np.ones((2, 5))
print("Q2 Ones Matrix:\n", ones_matrix)

# # 🔹 Q3: Identity Matrix
# # Ek 4×4 identity matrix banao.
identity_matrix = np.eye(4)
print("Q3 Identity Matrix:\n", identity_matrix)

# # 🔹 Q4: Reshape
# # np.arange(1, 13) ka use karke ek 3×4 matrix banao.
reshaped_matrix = np.arange(1, 13).reshape(3, 4)
print("Q4 Reshaped Matrix:\n", reshaped_matrix)

# # 🔹 Q5: Challenge
# # Ek 5×5 identity matrix banao aur uske diagonal elements ko 9 bana do.
challenge_matrix = np.eye(5) * 9
print("Q5 Challenge Matrix:\n", challenge_matrix)

#NumPy Vactorized Operations:
# ❓ Question 1
# np.arange(1,13).reshape(3,4) par column-wise mean nikaalo.
arr = np.arange(1,13).reshape(3,4)
mean = arr.mean(axis=0)
print("Q1 Column-wise mean:", mean)

# ❓ Question 2
# Ek 4 students × 3 subjects ka random marks table banao (50 se 100 ke beech random numbers).
# np.random.randint(50, 101, size=(4,3))
# ⚡ Ab tasks:
# Har student ke min, max, mean nikaalo (row-wise).
# Har subject ke marks check karo, aur batao kis subject me overall max score aaya (column-wise).
marks = np.random.randint(50, 101, size=(4,3))
print("Marks Table:\n", marks)
min = marks.min(axis=1)
max = marks.max(axis=1)
mean = marks.mean(axis=1)
print("Row-wise Min:", min)
print("Row-wise Max:", max)
print("Row-wise Mean:", mean)
overall_max_subject = marks.max(axis=0)
print("Column-wise Overall Max Scores:", overall_max_subject)   


# ❓ Question 3 (Z-score Normalization)
# Ek array of marks banao:
# marks = np.array([65, 70, 80, 90, 75])
# ⚡ Task:
# In marks ka mean aur standard deviation nikaalo.
# Har mark ka z-score calculate karo formula se:
# 𝑧
# =
# (
# 𝑥
# −
# mean
# )
# std
# z=
# std
# (x−mean)
# Output me z-scores print karo.
marks = np.array([65, 70, 80, 90, 75])
mean = marks.mean()
std = marks.std()
z_scores = (marks - mean) / std
print("Z-scores:", z_scores)

# ***************Numpy Practice Problems (Array Operations)*****************
matirix = np.arange(1, 26).reshape(5, 5)
print("5x5 Matrix:\n", matirix)
print("2nd Row:", matirix[1])
print("Last Column:", matirix[:, -1])
print("Diagonal Elements:", np.diag(matirix))
print("Sum of All Elements:", matirix.sum())
students = np.random.randint(0, 101, 50)
print("Students Marks:", students)
print("Mean Marks:", students.mean())
print("Median Marks:", np.median(students))
print("Standard Deviation of Marks:", students.std())
print("Top 5 Marks:", np.sort(students)[-5:])

# Problem 1: Zero Border Matrix
# Ek 6×6 matrix banao jisme border ke elements 1 ho aur andar ke elements 0 ho.
border_matrix = np.ones((6, 6))
border_matrix[1:-1, 1:-1] = 0
print("Border Matrix:\n", border_matrix)

# Problem 2: Replace Maximum with 0
# Ek 5×5 random matrix banao aur usme sabse bada number ko 0 se replace karo.
random_matrix = np.random.randint(1, 101, (5, 5))
print("Original Random Matrix:\n", random_matrix)
random_matrix[random_matrix == random_matrix.max()] = 0
print("Matrix after Replacing Max with 0:\n", random_matrix)

# Problem 3: Row-wise Maximum
# Ek random 4×5 matrix banao aur har row ka maximum element print karo.
random_matrix_4x5 = np.random.randint(1, 101, (4, 5))
print("Random 4x5 Matrix:\n", random_matrix_4x5)
row_wise_max = random_matrix_4x5.max(axis=1)
print("Row-wise Maximum Elements:", row_wise_max)

# Problem 4: Normalize Data
# Ek array banao [10, 20, 30, 40, 50].
# Isko normalize karo formula se:
# normalized = (x - min) / (max - min)
data = np.array([10, 20, 30, 40, 50])
normalized_data = (data - data.min()) / (data.max() - data.min())
print("Normalized Data:", normalized_data)
