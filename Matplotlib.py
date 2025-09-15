import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
marks = [85, 90, 78, 88, 76]

plt.hist(subjects, marks, label="Student A")

plt.xlabel("Subjects")     # X-axis label
plt.ylabel("Marks")        # Y-axis label
plt.title("Student Marks") # Title
plt.grid(True)             # Grid lines
# plt.legend()               # Legend
plt.show()
