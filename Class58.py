import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hours = np.array([1,2,3,4,5])
marks = np.array([30,40,50,60,70])
plt.scatter(hours,marks)
plt.xlabel("hours studied")
plt.ylabel("marks scored")
plt.title("hours studied vs marks scored")
plt.show()
'''
ML is a process of teaching computers to learn patterns
 from data and make predictions or decisions 
without being explicitly programmed.

Types of Machine Learning
1. Supervised Learning: this is like learning with a teacher
                in this we have labeled data and we train the model
                based on the labeled data.
                example: 
                   y=mx+c (linear regression)
                   classification (spam detection)
                   classification (cat vs dog)


2. Unsupervised Learning : this is like learning without a teacher
                in this we don't have labeled data.
                we have only data and we train the model based on the data.
                example: 
                    1. clustering (k-means)
                    2. dimensionality reduction (pca)
                    3. association rule learning (apriori)

3. Reinforcement Learning: this is like learning with a trial and error
                in this we have a agent and we train the model based on the 
                rewards and punishments.
                example: 
                    1. game playing
                    2. robotics
                    3. self driving cars
                    4. recommendation system

ML Pipeline:
1: Collect Data : 
2: Clean Data : 
3: Train Model : 
4: Test Model : 
5: Make Prediction : 
'''


