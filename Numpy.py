# # # 📝 NumPy Practice Problems (Arrays, Indexing & Slicing)
# # # 🔹 Q1: Create a NumPy array
# # # Ek NumPy array banao jisme 1 se 10 tak ke numbers ho.
# import numpy as np 
# # arr = np.array([1,2,3,4,5,6,7,8,9,10])
# # print("Q1 Array:", arr)

# # # 🔹 Q2: Indexing
# # # Array = [5, 10, 15, 20, 25, 30]
# # # First element print karo
# # # Third element print karo
# # # Last element print karo
# # arr2 = np.array([5, 10, 15, 20, 25, 30])
# # first_element = arr2[0]
# # third_element = arr2[2]
# # last_element = arr2[-1]
# # print("Q2 First element:", first_element)
# # print("Q2 Third element:", third_element)
# # print("Q2 Last element:", last_element)

# # # 🔹 Q3: Slicing
# # # Array = [10, 20, 30, 40, 50, 60, 70, 80]
# # # Elements 2 se 5 (inclusive of 2, exclusive of 5) print karo
# # # Pehle 4 elements print karo
# # # Last ke 3 elements print karo
# # arr3 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
# # slice_2_to_5 = arr3[2:5]
# # first_4_elements = arr3[:4]
# # last_3_elements = arr3[-3:]
# # print("Q3 Elements 2 to 5:", slice_2_to_5)
# # print("Q3 First 4 elements:", first_4_elements)
# # print("Q3 Last 3 elements:", last_3_elements)

# # # 🔹 Q4: Modify element
# # # Array = [2, 4, 6, 8, 10]
# # # Index 2 pe jo element hai usse 100 bana do
# # # Array print karo
# # arr4 = np.array([2, 4, 6, 8, 10])
# # arr4[2] = 100
# # print("Q4 Modified Array:", arr4)

# # # 🔹 Q5: Slice update
# # # Array = [1, 2, 3, 4, 5, 6, 7]
# # # Index 2 se 4 tak ke elements ko [99, 100, 101] se replace karo
# # arr5 = np.array([1, 2, 3, 4, 5, 6, 7])
# # arr5[2:5] = [99, 100, 101]
# # print("Q5 Updated Array:", arr5)

# # # 🚀 Bonus Challenge
# # # Array = [10, 20, 30, 40, 50, 60]
# # # Sirf even index wale elements print karo (0, 2, 4, …)
# # arr6 = np.array([10, 20, 30, 40, 50, 60])
# # even_index_elements = arr6[::2]
# # print("Bonus Challenge Even index elements:", even_index_elements)

# # 🔹 Q6: 2D Array Indexing
marks = np.array([
    [80, 75, 90],   # Ali
    [60, 85, 70],   # Sara
    [90, 95, 88]    # John
])

# # 🔹 Q1: Sara ke saare marks print karo
sara_marks = marks[1]
print("Q1 Sara ke marks:", sara_marks)

# # 🔹 Q2: John ka Science mark print karo
john_science_mark = marks[2, 2]
print("Q2 John ka Science mark:", john_science_mark)

# # 🔹 Q3: Sirf English ke marks print karo (sab students ke)
english_marks = marks[:, 1]
print("Q3 English ke marks:", english_marks)

# # 🔹 Q4: Sara ke English mark ko 100 kar do aur updated array print karo
marks[1, 1] = 100
print("Q4 Updated Marks Array:\n", marks)

# # 🔹 Q5: Har student ke average marks nikaalo (row-wise average)
average_marks = np.mean(marks, axis=1)
print("Q5 Average Marks of each student:", average_marks)

# 🔹 Q1: Zeros
# Ek 3×4 matrix banao jisme sirf 0 ho.
zeros_matrix = np.zeros((3, 4))
print("Q1 Zeros Matrix:\n", zeros_matrix)

# 🔹 Q2: Ones
# Ek 2×5 matrix banao jisme sirf 1 ho.
ones_matrix = np.ones((2, 5))
print("Q2 Ones Matrix:\n", ones_matrix)

# 🔹 Q3: Identity Matrix
# Ek 4×4 identity matrix banao.
identity_matrix = np.eye(4)
print("Q3 Identity Matrix:\n", identity_matrix)

# 🔹 Q4: Reshape
# np.arange(1, 13) ka use karke ek 3×4 matrix banao.
reshaped_matrix = np.arange(1, 13).reshape(3, 4)
print("Q4 Reshaped Matrix:\n", reshaped_matrix)

# 🔹 Q5: Challenge
# Ek 5×5 identity matrix banao aur uske diagonal elements ko 9 bana do.
challenge_matrix = np.eye(5) * 9
print("Q5 Challenge Matrix:\n", challenge_matrix)
