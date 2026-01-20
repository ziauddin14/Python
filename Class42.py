'''
Spread of the data:
How much do the values vary? 
[12,15, 20,19,22]
Mean = 18
sum [6, 3, 2 , 1, 4] = 16 <==== standard deviation
[36,9,4,1,16] = 66 <==== variance

Quartiles:(Quantiles / Percentiles)
Q1: 25% of the data
Q2: 50% of the data (Median)
Q3: 75% of the data
IQR(Interquartile Range) = Q3 - Q1

Outliers:
Upper Fence = Q3 + 1.5 * IQR
Lower Fence = Q1 - 1.5 * IQR

Outliers are the data points that fall below the lower fence or above the upper fence.
outliers is not a bad thing , it's just question of how to handle them.

Skew: 
Skew is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. 
Positive Skew: Right tail is longer
Negative Skew: Left tail is longer
Symmetric: Both tails are equal
'''

'''
#Find Mean, median, mode,Q1, Q2, Q3, IQR, Upper Fence, Lower Fence, Outliers
data = [8,10,12,13,15,18,20,22,25,90]
mean = 24
median = 16.5
mode = No mode
Q1 = 12
Q2 = 15
Q3 = 22
IQR = Q3 - Q1 = 10
Upper Fence = Q3 + 1.5 * IQR = 37
Lower Fence = Q1 - 1.5 * IQR = -3 
Outliers = [90]

'''
import pandas as pd
import numpy as np
# data = [8,10,12,13,15,18,20,22,25,90]
# data = pd.Series(data)
# print("Mean:", data.mean())
# print("Median:", data.median())
# print("Mode:", data.mode().values)
# print("Q1:", data.quantile(0.25))
# print("Q2:", data.quantile(0.50))
# print("Q3:", data.quantile(0.75))
# IQR = data.quantile(0.75) - data.quantile(0.25)
# print("IQR:", IQR)
# upper_fence = data.quantile(0.75) + 1.5 * IQR
# lower_fence = data.quantile(0.25) - 1.5 * IQR
# print("Upper Fence:", upper_fence)
# print("Lower Fence:", lower_fence)
# outliers = data[(data > upper_fence) | (data < lower_fence)]
# print("Outliers:", outliers.values)
# print("Describe:", data.describe())

data = [3,4,5,6,7,7,8,9,10]
data = pd.Series(data)
print("Mean:", data.mean())
print("Median:", data.median())
print("Mode:", data.mode().values)
print("Q1:", data.quantile(0.25))
print("Q2:", data.quantile(0.50))
print("Q3:", data.quantile(0.75))
IQR = data.quantile(0.75) - data.quantile(0.25)
print("IQR:", IQR)
upper_fence = data.quantile(0.75) + 1.5 * IQR
lower_fence = data.quantile(0.25) - 1.5 * IQR
print("Upper Fence:", upper_fence)
print("Lower Fence:", lower_fence)
outliers = data[(data > upper_fence) | (data < lower_fence)]    
print("Outliers:", outliers.values)
print("Describe:", data.describe())