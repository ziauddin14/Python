import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the dataset
# Dataset path is 'Python\Heart_Disease_Prediction.csv'
df = pd.read_csv(r'Python\Heart_Disease_Prediction.csv')

print("--- Dataset Head ---")
print(df.head())

# 2. Encode target variable 'Heart Disease' to numeric values: Presence -> 1, Absence -> 0
df['Heart Disease'] = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})

# 3. Define Features (X) and Target (y)
X = df.drop(columns=['Heart Disease'])
y = df['Heart Disease']

print("\nFeatures (X) shape:", X.shape)
print("Target (y) shape:", y.shape)

from sklearn.preprocessing import StandardScaler

# 4. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nX_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# === STEP 1: Linear Regression WITHOUT Scaling ===
print("\n=== 1. Linear Regression (Without Scaling) ===")
model_raw = LinearRegression()
model_raw.fit(X_train, y_train)

y_pred_raw = model_raw.predict(X_test)

mse_raw = mean_squared_error(y_test, y_pred_raw)
r2_raw = r2_score(y_test, y_pred_raw)

print(f"Mean Squared Error (MSE): {mse_raw:.4f}")
print(f"R2 Score: {r2_raw:.4f}")


# === STEP 2: Linear Regression WITH Scaling ===
print("\n=== 2. Linear Regression (With StandardScaler) ===")

# Apply StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n--- First 5 rows of scaled X_train ---")
print(X_train_scaled[:5])

# Fit Linear Regression on Scaled Data
model_scaled = LinearRegression()
model_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = model_scaled.predict(X_test_scaled)

mse_scaled = mean_squared_error(y_test, y_pred_scaled)
r2_scaled = r2_score(y_test, y_pred_scaled)

print("\n--- Evaluation Metrics (With Scaling) ---")
print(f"Mean Squared Error (MSE): {mse_scaled:.4f}")
print(f"R2 Score: {r2_scaled:.4f}")

print("\nPredictions on Test Data (Scaled model):")
print(y_pred_scaled)
'''
Categorical Data men Regression nhi use krega Q k uske nateeje nhi hote 
-yeh sirf Numerical Data ke liye use krega 
-isky liye hum Classification algorithem use krege 
-Classification use kre k liye hum Logistic Regression use kre ge \
-Logistid regression uses sigmoid function to keep the predictions between 0-1 (0% to 100%)
-Sigmoid function takes any number as input and compresses it into a value between 0 and 1
Logistic regression doea not directly predict the catogories .it predict the probabilities intead
09, 1, 0.20
by default probability >= 0.5
output = 1
if probability <=0.5
output = 0
cutoff point by default is 0.45 this cutoff point is called Decision Boundary
Logictic Regression is used in: 
1.Medical Diagnosis
2.Fraud Detection
3.Email Spam Detection
4.Credit Scoring
5.Customer Churn Prediction
6. Loan Approvl 
'''

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_scaled,y_train)
y_pred = model.predict(X_test_scaled)
print(y_pred)
print(y_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))

#Actual Probabilities calculated by Logistic Regression
print("\n--- Actual Probabilities (0-1) ---")
probas = model.predict_proba(X_test_scaled)
print("Probability of 0:", probas[:, 0])
print("Probability of 1:", probas[:, 1])
