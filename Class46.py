import pandas as pd 
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

df = pd.read_csv('movie.csv')

#----------------------Data Cleaning -----------------------#

print(df.head())
print(df['Runtime'].head())
print(df['Runtime'].dtype)
df['Runtime'] = df['Runtime'].replace('min', '')
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')
print(df['Runtime'])

# change Released Year type
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
print(df['Released_Year'].dtype)
print(df.info())

print(df.isnull().sum())

#fill the null values with median
df['Meta_score'] = df['Meta_score'].fillna(df['Meta_score'].median())
print(df['Meta_score'].isnull().sum())
df['Gross'] = df['Gross'].fillna(df['Gross'].median())
print(df.isnull().sum())
df['Certificate'] = df['Certificate'].fillna(df['Certificate'].mode()[0])
print(df.isnull().sum())

#----------IMDB rating distribution------------------#
plt.figure(figsize=(8, 6))
plt.hist(df['IMDB_Rating'], bins=100, color='blue', edgecolor='black')
plt.title('Distribution of IMDB Ratings')
plt.xlabel('IMDB Rating')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()
