import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset load karna
df = pd.read_csv('https://raw.githubusercontent.com/sharmaroshan/Heart-UCI-Dataset/master/heart.csv')

# Gender-wise count plot for Heart Disease
# Dataset mein sex = 1 (Male) aur sex = 0 (Female) hai
# Dataset mein target = 1 (Disease) aur target = 0 (No Disease) hai

plt.figure(figsize=(12, 5))

# 1. Aurton (Women) ka Plot
plt.subplot(1, 2, 1) # 1 row, 2 columns, pehla plot
sns.countplot(x='target', data=df[df['sex'] == 0], palette='Set2')
plt.title('Heart Disease Count in Women (Female)')
plt.xlabel('Target (0 = No Disease, 1 = Heart Disease)')
plt.ylabel('Patient Count')
plt.xticks([0, 1], ['No Disease', 'Heart Disease']) # X-axis k labels ko samajhne me asaan banana

# 2. Mardon (Men) ka Plot
plt.subplot(1, 2, 2) # 1 row, 2 columns, doosra plot
sns.countplot(x='target', data=df[df['sex'] == 1], palette='Set1')
plt.title('Heart Disease Count in Men (Male)')
plt.xlabel('Target (0 = No Disease, 1 = Heart Disease)')
plt.ylabel('Patient Count')
plt.xticks([0, 1], ['No Disease', 'Heart Disease']) # X-axis k labels

plt.tight_layout()
plt.show()

print("\n--- Duplicated Rows ---")
print("Total Duplicates:", df.duplicated().sum())

# Duplicates ko remove karne ke liye:
df = df.drop_duplicates()
print("Duplicates remove karne ke baad rows bachi:", df.shape[0])

# Chest Pain Type (cp) ka Count Plot with hue='target'
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', hue='target', data=df, palette='viridis')
plt.title('Heart Disease based on Chest Pain Type')
plt.xlabel('Chest Pain Type (cp)')
plt.ylabel('Patient Count')
plt.legend(title='Target', labels=['No Disease', 'Heart Disease'])
plt.show()

# Histogram for thalach (Maximum Heart Rate Achieved) with hue='target'
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='thalach', hue='target', kde=True, palette='coolwarm', bins=20, multiple='dodge')
plt.title('Distribution of Maximum Heart Rate Achieved (thalach)')
plt.xlabel('Maximum Heart Rate Achieved (thalach)')
plt.ylabel('Count')
plt.show()

# Average Maximum Heart Rate by Target
print("\n--- Average Maximum Heart Rate (thalach) by Target ---")
avg_thalach = df.groupby('target')['thalach'].mean()
print("Target 0 (No Disease) ki average heart rate:", round(avg_thalach[0], 2))
print("Target 1 (Heart Disease) ki average heart rate:", round(avg_thalach[1], 2))
avg_chol = df.groupby('target')['chol'].mean()
print("Average cholesterol level by target:", avg_chol)

avg_sex = df.groupby('sex')['target']._value_counts(normalize=True).unstack()
print("Average heart disease by sex:", avg_sex)

#creat a box plot y label pr target aur y axis pr age rakhna 
sns.boxplot(x=df['target'],y=df['age'])
plt.show()




# Correlation Heatmap
correlation_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(12,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt='.2f')
plt.title('Correlation Heatmap of Features')
plt.show()