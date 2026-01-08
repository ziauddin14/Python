import pandas as pd

'''
Central Tendency Measures:
Mean: Average value of a numerical column
Mean is sensitive to extreme valiues , We use Median in that case
Data is symmetric (Normal Distribution)
No extreme values (Outliers : bht bahar ki value jiska apky data k sath koi lena dena nhi)
Example: Height of people, Scores in an exam, Sensor readings
We dont use mean when:
Salaries, Income, House Prices, Transaction Amounts
Median: Middle value when numerical data is sorted in order
Much more realistic 
Outliers ka asar nhi hota kiun bht chothi aur bht bari vakues ya to shoro men hogi ya end men kiun k data sorted hota hai
When to use Median:
Data is skewed (Not symmetric)
Financial data (Income, Salaries, Crypto Prices, House Prices, Real Estate Prices)
When Median is Weak:
Small datasets with many repeated values
Mode: Most frequently occurring value in a column (Most Repeated Value)
When to use Mode:
Categorical data (Colors, Brands, Cities, Countries)
Mode is useless when:
Numerical data with many unique values
continues data without repeated values
'''
data = {
    "EmpID": [301, 302, 303, 304, 305, 306, 307, 308],
    "Name": ["Ali", "Sara", "Ahmed", None, "Bilal", "Hina", "Usman", "Zara"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", None, "IT", "HR"],
    "City": ["Karachi", "Lahore", None, "Islamabad", "Karachi", "Lahore", "Karachi", None],
    "Salary": [60000, None, 85000, 120000, 58000, 110000, None, 62000],
    "Experience": [2, 5, None, 8, 1, 7, 6, None]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df) 
print(df.info()) # Get summary of DataFrame including non-null counts its must to know about null values
print(df.isnull())  # Check for null values in the DataFrame
print(df.isnull().sum())  # Count of null values in each column
#missing data is killer of Data Scientist
'''
How to handle missing data?
1. Remove rows with missing data
'''
df2 = df
df2 = df2.dropna()  # Remove rows with any null values
print("DataFrame after removing rows with missing data:", df2)

df3 = df
df3['Salary'].fillna(df3['Salary'].mean() , inplace=True)
#Insplace = true krdo to original df3 me hi changes ajayen gy
# Fill missing Salary values with the mean Salary
print("DataFrame after filling missing Salary with mean:", df3)

#*************Sorting Values******************
df4 = df
df4 = df4.sort_values(by='Salary')  # Sort DataFrame by Salary in ascending order
print("DataFrame sorted by Salary in ascending order:", df4)
df5 = df
df5 = df5.sort_values(by='Salary', ascending=False)  # Sort DataFrame by Salary in descending order
print("DataFrame sorted by Salary in descending order:", df5)

#*****How many employees in each department? (Value Counts)*****
dept_counts = df['Department'].value_counts()
print("Number of employees in each department:\n", dept_counts)
city_counts = df['City'].value_counts()
print("Number of employees in each city:\n", city_counts)   
#Which department has maximum employees without using idxmax
max_dept = dept_counts.index[0]
print("Department with maximum employees:", max_dept)
#Whcich city appears least
min_city = city_counts.index[-1]
print("City appear least :", min_city)
#What is highest salary after cleaning data
print(df['Salary'].max())

 
#Fill Missing values with mode, median, mean
df6 = df
df6['Department'].fillna(df6['Department'].mode()[0], inplace=True)  # Fill missing Department with mode
df6['City'].fillna(df6['City'].mode()[0], inplace=True)  # Fill missing City with mode
df6['Experience'].fillna(df6['Experience'].mean(), inplace=True)  # Fill missing Experience with mean
df6['Salary'].fillna(df6['Salary'].median(), inplace=True)  # Fill missing Salary with median   
print("DataFrame after filling missing values:\n", df6)