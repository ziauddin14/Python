import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
marks = [85, 90, 78, 88, 76]

plt.plot(subjects, marks, label="Student A")

plt.xlabel("Subjects")     # X-axis label
plt.ylabel("Marks")        # Y-axis label
plt.title("Student Marks") # Title
plt.grid(True)             # Grid lines
# plt.legend()               # Legend
plt.show()


#*******Random Variable Discrete **************
import random
# Roll dice 1000 times
rolls = [random.randint(1, 6) for _ in range(1000)]

plt.hist(rolls, bins=6, edgecolor='black', rwidth=0.8)
plt.xlabel("Dice Number")
plt.ylabel("Frequency")
plt.title("Dice Roll Simulation (1000 rolls)")
plt.grid(True)
plt.show()


#************Continuous Variable Simulation (Height)********************
import numpy as np

# Random heights around mean=170 cm with std=10
heights = np.random.normal(170, 10, 1000)

plt.hist(heights, bins=30, edgecolor='black')
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.title("Random Continuous Variable: Heights")
plt.grid(True)
plt.show()

