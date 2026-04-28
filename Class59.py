#Linear Regression: finding a relationship between input and output
# triwes to draw ka straight line covering maximum points and mainting a least distance from every point 
# Equation of th e Straight line: y = mx +c
# y= output (predictid value)
# x = input 
# m = slop (rate of change) grediant
# c = y-intercept: the point where the line crosses y-axis :starting point

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

hours = np.array([1,2,3,4,5,6])
marks = np.array([30,40,50,60,70,80])

X = hours.reshape(-1, 1) # COnverting array to 2D for input to LR model
y = marks
model = LinearRegression() # create model

#Model Trainig: internallly find slop, find intercepr, minimizes MSE (mean square error)  
# MSE = 1/n((y_pred - y_true)^2) -> sum of (predicted - actual)^2 divided by total number of samples
model.fit(X,y)
y_pred = model.predict(X)
print('Predictions: ', y_pred)
print('Predicted score for 7 hours: ', model.predict([[7]]))
print('Slop: ', model.coef_)
print('Intercept: ', model.intercept_)