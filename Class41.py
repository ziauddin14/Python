import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sales_data.csv")

df = pd.read_csv(file_path, encoding="latin1")

df.head() 
df.info()
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# print(df.info())
print(df.isnull().sum().sort_values(ascending=False))

#Aisa feature add krdena jo pehly se data set men naa ho 'Feature Engeeniering' kehlata h 
df['REVENUE_CHECK'] = df['QUANTITYORDERED'] * df['PRICEEACH']
df['DIFFERENCE'] = df['SALES'] - df['REVENUE_CHECK']
print(df['DIFFERENCE'].describe())

#total revenue across the year
print(df['SALES'].sum())
#Average sale
print(df['SALES'].mean())
print(df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False))

#Top 5 countries by revenue(sales)
print(df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head())

#how much sales 
print(df.groupby('DEALSIZE')['SALES'].sum().sort_values(ascending=False).head())

#How many Dealsize
print(df['DEALSIZE'].value_counts())

#Revenue by year
print(df.groupby('YEAR_ID')['SALES'].sum().sort_values(ascending=False))