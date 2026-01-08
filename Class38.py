import numpy as np
data = np.array([
    [101, 'Alice', 'Math', 83 , 'Karachi'],
    [102, 'Bob', 'Science', 78 , 'Lahore'],
    [103, 'Charlie', 'English', 85 , 'Islamabad'],
    [104, 'David', 'Math', 90 , 'Karachi'],
    [105, 'Eva', 'Science', 88 , 'Lahore']
])
'''
Definition of Pandas: Pandas is a powerful open-source data analysis and manipulation library for Python. It provides data structures
like DataFrames and Series that make it easy to handle and analyze structured data. Pandas offers a wide range of functionalities for data cleaning, 
transformation, aggregation, and visualization, making it a popular choice for data scientists and analysts.
Note: Columns length must be same in all rows.
'''
import pandas as pd
  
data = {
    'StudentID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Subject': ['Math', 'Science', 'English', 'Math', 'Science'],
    'Score': [83, 78, 85, 90, 88],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore']
}
df = pd.DataFrame(data)
print(df.head(2))  # Display first 5 rows of the DataFrame
print(df.tail(2))  # Display last 5 rows of the DataFrame
print(df.shape)  # Get the shape of the DataFrame (rows, columns)
print(df.columns)  # Get the column names of the DataFrame
print(df.dtypes)  # Get the data types of each column
print(df['Score'])  # Print only the Marks column
print(df[['Name', 'Score']])  # Print Name and Marks columns
print(df['City'] == 'Karachi')  # Filter rows where City is Karachi
karachi_students = df[df['City'] == 'Karachi'] # Get rows where City is Karachi
print(karachi_students)
#Aise students chahiye jo karachi k hon aur subject math ho
karachi_math_students = df[(df['City'] == 'Karachi') & (df['Subject'] == 'Math')]
print(karachi_math_students)
print(df['Score'].mean())  # Calculate average score
print(df['Score'].max())   # Find maximum score
print(df['Score'].min())   # Find minimum score
#Average score by subject without groupby aur any methods
#filter first , then calculate perform operations
math_scores = df[df['Subject'] == 'Math']['Score'].mean()
print("Average Math Score:", math_scores)



data = {
    "EmpID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Bilal", "Hina", "Usman", "Zara"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "City": ["Karachi", "Lahore", "Karachi", "Islamabad", "Karachi", "Lahore", "Karachi", "Islamabad"],
    "Salary": [60000, 90000, 85000, 120000, 58000, 110000, 95000, 62000],
    "Experience": [2, 5, 4, 8, 1, 7, 6, 3]
}

df = pd.DataFrame(data)
print(df[['Name', 'Salary', 'Department']])  # Print Name, Salary, and Department columns
print(df[df['City'] == 'Karachi'])  # Filter rows where City is Karachi
print(df[(df['Department'] == 'IT') & (df['City'] == 'Karachi')])  # Employees in IT department from Karachi
print(df['Salary'].max())  # Find maximum salary
print(df[df['Department'] == 'HR']['Salary'].mean())  # Average salary in HR department
#Show names of employees with sakary above more then average salary
average_salary = df['Salary'].mean()
high_earners = df[df['Salary'] > average_salary]['Name']
print(high_earners)
#List of employees with experience more than 5 years and salary above 90000
experienced_high_earners = df[(df['Experience'] > 5) & (df['Salary'] > 90000)]
print(experienced_high_earners)
#From Finance department find minimum salary
min_finance_salary = df[df['Department'] == 'Finance']['Salary'].min()
print(min_finance_salary)
#Count how many employees are from islamabad
islamabad_count = df[df['City'] == 'Islamabad'].shape[0]
print(islamabad_count)
#Find average salary of IT emplooyees who have experience more then 3 years
avg_it_salary_exp_gt_3 = df[(df['Department'] == 'IT') & (df['Experience'] > 3)]['Salary'].mean()
print(avg_it_salary_exp_gt_3)