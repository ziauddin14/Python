'''
Distance to MRT Station: 5000
Number of conv stores : 5
The value 5k is bigger so it matters more to the ML model.

Feature Scaling: is the process of bringing all inputs features
to a similar scale so that the model treats them fairly

Methods of Feature Scaling
1. Standardization (Standard Scaler):
scale features by substructing the mean and dividing by the standard deviation.
 this transforms the data so that features have zero mean and variance :1, 
 which helps many machine learning model perform better
 Formula : X scaled = =(X -  \(\mu \)  )/ \(\sigma \)
 \(\mu \)  = mean 
 \(\sigma \)  = standard deviation  
 
Formula : X scaled = =(X - Xmin)/(Xmax - Xmin)
 Xmin = minimum value of the feature
 Xmax = maximum value of the feature
 
2. Normalization (Min Max Scaler)
Scale features by dividing by the maximum value, this transforms the data so that features have values between 0 and 1

Formula : X scaled = =(X - Xmin)/(Xmax - Xmin)
 Xmin = minimum value of the feature
 Xmax = maximum value of the feature

model.score() method : is use for checking the model performance in R2 value on testing data 
.fit():  learns the parameters (mean, std, min, max)
.fit_transform():  learns the parameters (mean, std, min, max) and transform 
.transform(): use for transform data only not learn

Important note: When we scaling the data we should fit only on training data , we should not fit on testing data , because we should not use testing data for training the model, it is test data after training the model
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import r2_score

# Data load karna
df = pd.read_csv('Python\Real estate.csv')
X = df.drop('Y house price of unit area', axis=1)
y = df['Y house price of unit area']

# Split karna
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- RESULTS COMPARISON ---")

# 1. Simple Linear Regression (No Scaling)
model1 = LinearRegression()
model1.fit(X_train, y_train)
r1 = r2_score(y_test, model1.predict(X_test))
print(f"1. Simple Linear Regression (R1): {r1:.4f}")

# 2. Linear Regression (With Standard Scaler)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model2 = LinearRegression()
model2.fit(X_train_scaled, y_train)
r2 = r2_score(y_test, model2.predict(X_test_scaled))
print(f"2. Linear Regression + Scaler (R2): {r2:.4f}")

# 3. Simple Polynomial Regression (No Scaling)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model3 = LinearRegression()
model3.fit(X_train_poly, y_train)
r3 = r2_score(y_test, model3.predict(X_test_poly))
print(f"3. Simple Polynomial (R3): {r3:.4f}")

# 4. Polynomial Regression (With Standard Scaler)
# Polynomial features ko scale karna
scaler_poly = StandardScaler()
X_train_poly_scaled = scaler_poly.fit_transform(X_train_poly)
X_test_poly_scaled = scaler_poly.transform(X_test_poly)

model4 = LinearRegression()
model4.fit(X_train_poly_scaled, y_train)
r4 = r2_score(y_test, model4.predict(X_test_poly_scaled))
print(f"4. Polynomial + Scaler (R4): {r4:.4f}")
