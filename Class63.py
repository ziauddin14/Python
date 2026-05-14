'''
Regularization: is a technique used to reduce overfitting by penalizing large coefficients

Types of Regularization
1. Lasso Regression (L1 Regularization)
2. Ridge Regression (L2 Regularization)

Ridge Regression (L2 Regularization):  
MSE :Measure pridiction error (how far the prediction from the actual value)
Penalty : sum of the square of the coefficients

Formula : MSE + alpha * sum(coefficients^2)
 
 Lamda / Alpha : this cotrols how strict the penalty is
 if  alpha = 0 => No regularization (Only train the model)
 if alpha = 1 => Regularization (train the model + penalty)
 if alpha = inf => All coefficients become 0


 Lasso Regression (L1 Regularization): 
MSE :Measure pridiction error (how far the prediction from the actual value)
Penalty : sum of the absolute values of the coefficients

Formula : MSE + alpha * sum(|coefficients|)

Regularzation is highly sensitive to feature scaling

Ridge Regression vs Lasso Regression : 

Ridge Regression:  => coefficients are reduced toward zero but never become exactly zero (shrink)
Lasso Regression => coefficients can become exactly zero (feature selection) => It can be used for feature selection

if one featur has value in thousands and another feature has value in single digit, the panelty becoms unfair.

'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('Python\Real estate.csv')
print(df.head())
# Remove the 'No' column as requested
# Check if 'No' column exists before dropping
if 'No' in df.columns:
    df = df.drop(columns=['No'])
print(df.head())
# Define features (X) and target (y)
# Assuming 'Y house price of unit area' is the target variable
X = df.drop(columns=['Y house price of unit area'])
y = df['Y house price of unit area']

print("Features (X) shape:", X.shape)
print("Target (y) shape:", y.shape)
# Perform an 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
# Apply StandardScaler to the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("X_train_scaled (first 5 rows):\n", X_train_scaled[:5])
print("X_test_scaled (first 5 rows):\n", X_test_scaled[:5])
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train_scaled, y_train)
y_pred = ridge_model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
print(r2)
from sklearn.linear_model import Lasso
lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train_scaled, y_train)
y_pred = lasso_model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
print(r2)