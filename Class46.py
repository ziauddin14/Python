import pandas as pd 
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

# df = pd.read_csv('movie.csv')
df = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Python-master\Python-master\movie.csv")
#----------------------Data Cleaning -----------------------#

print(df.head())
print(df['Runtime'].head())
print(df['Runtime'].dtype)
df['Runtime'] = df['Runtime'].astype(str).str.replace('min', '', regex=False).str.strip()
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

# #-------Gross rating distribution--------
plt.hist(df['Gross'], bins=30)
plt.title('Revenue Distribution')
plt.xlabel('Revenue')
plt.ylabel('Frequancy')
plt.show()
#------------ Data Analysis----------------#

#top 10 movie by revenue only name aur revenue 
top_gross = df.sort_values(by='Gross', ascending=False).head()
print(top_gross[['Series_Title', 'Gross']])

#Runtime Distribution
plt.hist(df['Runtime'].dropna(), bins=10)
plt.title('Runtime Distribution')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()

# Genre Revenue Analysis
df['Single_Gnere'] = df['Genre'].str.split(',').str[0]

genre_revenue = df.groupby(df['Single_Gnere'])['Gross'].mean().sort_values(ascending=False)
print(genre_revenue)

genreRevenu = genre_revenue.plot(kind='bar')
plt.show()


#Director Performance
director_performance = df.groupby(df['Director'])['Gross'].mean().sort_values(ascending=False).head(10)
director_plot = director_performance.plot(kind='bar')
plt.show()