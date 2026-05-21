import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Dataset Load
# Loading the dataset (assuming the file is in the same directory)
try:
    data = pd.read_csv(r'D:\Python\Python\heart.csv')
except FileNotFoundError:
    data = pd.read_csv('heart.csv')

# 2. X, y separate
# 'target' is the target column
X = data.drop('target', axis=1)
y = data['target']

# 3. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Apply Logistic Regression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Making predictions and checking accuracy
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"Logistic Regression Model Accuracy: {accuracy}")


from sklearn.metrics import precision_score, recall_score, f1_score

print("Recall Score",recall_score(y_test, y_pred))
print("Precision Score",precision_score(y_test, y_pred))
print("F1 Score",f1_score(y_test, y_pred))

'''
cancer detection system

we have 1000 patients
990 healthy
10 actually have cancer

model predicts = everyone is healthy

Accuracy = 990 / 1000 = 0.99 = 99%

the model has failed completely, because it missed all cancer patients yet it is 99% accurate.

Confusion Matrix

Target 1 -> Disease
Target 0 -> No Disease

There are only 4 possible outcomes:

TP: Model predict disease and patient actually has disease
TN: Model predict no disease and patient actually has no disease
FP: Model predict disease and patient actually has no disease
FN: Model predict no disease and patient actually has disease

[[25,  4],
 [ 5, 27]]

[[TN, FP],
 [FN, TP]]

Accuracy = (TP + TN) / (TP + TN + FP + FN)
= 52 / 61 = 0.85

Precision: Out of all predicted positives, how many were truly positive

Precision = TP / (TP + FP)

Recall: How good are we at finding all positive cases.

Recall = TP / (TP + FN)

F1 score = 2 x (Precision x Recall) / (Precision + Recall)
'''
