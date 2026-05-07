
import pandas as pd
df = pd.read_csv('Python\Real estate.csv')
df.head()
df.columns
df.drop('No', axis=1, inplace=True)
X = df.drop('Y house price of unit area', axis=1) #features
y = df['Y house price of unit area'] # target
print(X)
print(y)
#Train Test SPlit
'''
100
test_size=0.2 ..... 20%

X_train 80
y_train 80
X_test 20
y_test 20
'''
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
    
print(X_test)



from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
print(y_test)
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
print(mse)

r2 = r2_score(y_test, y_pred)
print(r2)

#r2: 0-1 : closer to 1: model is better

train_pred = model.predict(X_train) #prediction on data model has seen
test_pred = model.predict(X_test) # predictions on unseen data

print('Train R2:', r2_score(y_train, train_pred))
print('Test R2:', r2_score(y_test, test_pred))


'''
Linear regression woks only linear data 
real world data is not linear, mostly it is curved
instead of changing the model, we change the data 
by adding extra features from the existing data 

Example: y = mx + c  
         y = m1x + m2x2 + m3x3 + c 
         where x3 = x^2

that is called Polynomial Regression (not changing the model , we are  changing the data)

Feature Engineering : 
"Adding extra features from the existing data to improve the model performance"

In Polynomial Regression , we add extra features (like x^2, x^3, x^4, x^5) to the existing data to make it linear.

We can add features in two ways: 
1. manually 
2. automatically 
'''

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
poly_x = poly.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    poly_x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(r2)

#model ki complexity k ziyada hony sse kabhi bhi ye baat nhi samjhi ja skti k model bht acha h data aur model donon ka balanced hona zarori h 