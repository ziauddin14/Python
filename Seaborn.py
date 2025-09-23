import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 📊 Sample Data (Students Performance)
data = {
    "Student": ["Ali", "Sara", "Usman", "Ayesha", "Zia", "Hamza", "Fatima", "Bilal"],
    "Hours_Studied": [5, 7, 8, 3, 6, 9, 4, 2],
    "Marks": [78, 85, 90, 60, 82, 95, 70, 50],
    "Gender": ["M", "F", "M", "F", "M", "M", "F", "M"]
}

df = pd.DataFrame(data) 

# 🎨 Style & Palette
sns.set_style("darkgrid")
sns.set_palette("muted")

# 1️⃣ Relational Plot (Scatter)
sns.relplot(x="Hours_Studied", y="Marks", hue="Gender", data=df, kind="scatter", s=100)
plt.title("Scatter Plot: Hours vs Marks (by Gender)")
plt.show()

# 2️⃣ Categorical Plot (Bar)
sns.catplot(x="Student", y="Marks", data=df, kind="bar", hue="Gender", ci=None)
plt.title("Bar Plot: Student Marks (by Gender)")
plt.show()

# 3️⃣ Distribution Plot (Histogram with KDE)
sns.displot(df["Marks"], bins=5, kde=True, color="skyblue")
plt.title("Distribution of Marks")
plt.show()

# 4️⃣ Matrix Plot (Heatmap of Correlations)
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Correlation between Variables")
plt.show()
# 5️⃣ Regression Plot (Linear Regression)
sns.lmplot(x="Hours_Studied", y="Marks", data=df, hue="Gender")
plt.title("Regression Plot: Hours vs Marks (by Gender)")
plt.show()



#***********Seaborn Familt Pllots***************


# Sample Dataset
df = sns.load_dataset("tips")   # Built-in dataset (restaurant tips)

# ---------- 1. Relational Plots ----------
plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex")
plt.title("Scatter Plot: Bill vs Tip")
plt.show()

plt.figure(figsize=(6,4))
sns.lineplot(x="size", y="tip", data=df, marker="o", ci=None)
plt.title("Line Plot: Group Size vs Tip")
plt.show()


# ---------- 2. Categorical Plots ----------
plt.figure(figsize=(6,4))
sns.barplot(x="day", y="total_bill", data=df, hue="sex", ci=None)
plt.title("Bar Plot: Avg Bill by Day & Gender")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=df)
plt.title("Box Plot: Bill Distribution by Day")
plt.show()

plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="total_bill", data=df, hue="sex", split=True)
plt.title("Violin Plot: Bill Distribution by Day & Gender")
plt.show()


# ---------- 3. Distribution Plots ----------
plt.figure(figsize=(6,4))
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Histogram + KDE: Total Bill Distribution")
plt.show()

sns.displot(df, x="total_bill", col="sex", bins=15, kde=True)
plt.suptitle("Displot: Bills by Gender", y=1.05)
plt.show()


# ---------- 4. Matrix Plots ----------
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Correlation Matrix")
plt.show()

sns.clustermap(df.corr(numeric_only=True), cmap="viridis", annot=True)
plt.suptitle("Clustermap: Correlation Matrix", y=1.05)
plt.show()
