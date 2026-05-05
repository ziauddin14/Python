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