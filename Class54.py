import pandas as pd
import openpyxl as op 

df = pd.read_excel('employees.xlsx') 
print(df)

# loc and iloc
#loc: yeh label based indexing ke liye use hota hai, jisme hum row aur column ke labels ka use karke data access karte hai
#iloc: yeh integer based indexing ke liye use hota hai, jisme hum row aur column ke integer position ka use karke data access karte hai
print(df.loc[15, 'Age']) # This will print the value in the 'Age' column for the row with index 15 using loc
print(df.iloc[15, 2]) # This will print the value in the 3rd column (index 2) for the row with index 15 using iloc

#Univariate Analysis: ek waqt men sirf ek variable ko analyze krna, iske liye ham value_counts() function ka use krte hai
print(df['Designation'].value_counts().sum())# This will print the count of each unique value in the 'Designation' column

emp = pd.read_excel('employees.xlsx')
print(emp)
print(emp.Designation.unique()) # This will print the unique values in the 'Designation' column of the emp DataFrame
print(emp.Department.unique()) # This will print the unique values in the 'Department' column of the emp DataFrame
print(emp.Department.value_counts()) # This will print the count of each unique value in the 'Department' column of the emp DataFrame   
print(emp.Age.max()) # This will print the maximum value in the 'Age' column of the emp DataFrame
print(emp.Age.min()) # This will print the minimum value in the 'Age' column of the emp DataFrame
print(emp.Age.mean()) # This will print the mean (average) value of the 'Age' column of the emp DataFrame
print(emp.Age.median()) # This will print the median value of the 'Age' column of the emp DataFrame
print(emp.Age.std()) # This will print the standard deviation of the 'Age' column of the emp DataFrame
print(emp.Age.var()) # This will print the variance of the 'Age' column of the emp DataFrame
print(emp[emp['Designation'] == 'Manager']['Age'].max()) # This will print the maximum age of employees with the designation 'Manager' in the emp DataFrame
print(emp[emp['Designation'] == 'Officer']['Age'].mean()) # This will print the mean age of employees with the designation 'Officers' in the emp DataFrame
print(emp[emp['Designation'] == 'Office Boy']['Age'].min()) # This will print the minimum age of employees with the designation 'Office Boys' in the emp DataFrame

import matplotlib.pyplot as plt
freq = emp['Designation'].value_counts() # This will count the frequency of each unique value in the 'Designation' column of the emp DataFrameplt.bar(freq.index, freq.values) # This will create a bar plot with the unique values in the 'Designation' column on the x-axis and their corresponding frequencies on the y-axis
plt.pie(freq.values, labels=freq.index, autopct='%1.1f%%') # This will create a pie chart with the unique values in the 'Designation' column as labels and their corresponding frequencies as values, with percentages displayed on the chart
plt.savefig("pie_chart.png") # This will display the plots


import seaborn as sns
sns.boxplot(emp.Salary) # This will create a box plot for the 'Salary' column of the DataFrame
plt.savefig("box_plot.png") # This will save the box plot as an image file named "box_plot.png"

#find the outliers in the Salary column using IQR method
#Q1, Q3, IQR, lower bound, upper bound
Q1 = emp['Salary'].quantile(0.25) # This will calculate the
Q3 = emp['Salary'].quantile(0.75) # This will calculate the
IQR = Q3 - Q1 # This will calculate the Interquartile Range
lower_bound = Q1 - 1.5 * IQR # This will calculate the lower bound
upper_bound = Q3 + 1.5 * IQR # This will calculate the upper bound
outliers = emp[(emp['Salary'] < lower_bound) | (emp['Salary'] > upper_bound)] # This will filter the DataFrame to find the rows where the 'Salary' value is less than the lower bound or greater than the upper bound, which are considered outliers
print(outliers) # This will print the rows of the DataFrame that are considered outliers