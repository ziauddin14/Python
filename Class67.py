import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Dataset Load krna
df = pd.read_csv('heart.csv')
print("Dataset successfully loaded. Shape:", df.shape)

# 2. X aur Y ko alag krna (Target column ko drop krke X banana)
X = df.drop('target', axis=1)
y = df['target']
print("X shape (Features):", X.shape)
print("y shape (Target):", y.shape)

# 3. Train Test Split krna (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train set shape:", X_train.shape)
print("Test set shape:", X_test.shape)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

dtc = DecisionTreeClassifier(
    criterion='entropy',
    # max_depth=3,
    random_state=42,
)
dtc.fit(X_train, y_train)

y_pred = dtc.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(20,10))
plot_tree(
    dtc, 
    feature_names=X.columns,
    class_names=['No Disease', 'Disease'],
    filled=True,
    fontsize=10,
    rounded=True,
    impurity=True,
    node_ids=True
)
plt.show()