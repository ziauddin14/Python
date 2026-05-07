'''
R2 compare your model vs a dumb baseline (predicting the avg)
marks = [40, 50, 60]
avg = 50
basleline prediction --> 50 marks for each student 
if your model is not better then avg  -> it's useless
How to calculate R2? 
R2 = 1 - (SS res / SS tot)
SS res = Residual sum of squres:
SUM ( y actual - y predicted)2

SS tot=  total sum of squres: SUM(y actual - y mean)2
R2 tells us how much better we are compared to just preicting the average 
R2 = 1: perfect model
R2 = 0: same as predicting the mean 
R2 = 0.7 -> Model explains 70% of the variation 
R2 < 0 -> Wors then average,  ,model is garbage.

Overfitting: happens when a model memorize the training data 
instead of learning patterns.
High Training R2
low test R2

Underfitting: happens when the model is too simple to learn patterns.
Low training R2
Low test R2

What is R2?
The R2 score tells you how well your model explains the data compared to just guessing
the average
agar iski vallus 1 aagai to bht behtreen model h 
agar negative men aaagai to bekar h aur averag ese bhi gaya guzra h kisi bhi kaam ka nhi h 
agar average bat raha hota to 0 value aajati h 
agar 1 se bari value ati h iska matlab h model overfit 
agar 0.2 0.3 0.4 0.5 aagai to iska matlab ye h k model underfit h 


Data Leakage: 



'''


import pandas as pd
df = pd.read_csv('Real estate.csv')
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