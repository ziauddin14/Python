import pandas as pd

data = {
    "EmpID": [401,402,403,404,405,406,407,408,409,410],
    "Name": ["Ali","Sara","Ahmed","Ayesha","Bilal","Hina","Usman","Zara","Omar","Noor"],
    "Department": ["IT","IT","HR","HR","Finance","Finance","IT","HR","Finance","IT"],
    "City": ["Karachi","Lahore","Karachi","Islamabad","Karachi","Lahore","Karachi","Karachi","Islamabad","Lahore"],
    "Salary": [90000,85000,60000,65000,120000,110000,95000,62000,130000,88000],
    "Experience": [5,4,2,3,8,7,6,2,9,4]
}
df = pd.DataFrame(data)
print(df.isnull())
#IT men kaam krny walo ki average salary kya hai
print(df['Salary'][df['Department'] == 'IT'].mean())
#Whcih department pays highest salary
highest_salary = df['Department'].value_counts().index[0]
print(highest_salary)

#group by department and calculate average salary
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)
avg_salary_by_dept = df.groupby('Department')['Salary'].min()
print(avg_salary_by_dept)
avg_salary_by_dept = df.groupby('Department')['Salary'].max()
print(avg_salary_by_dept)

#Aggregation functions
agg_salary_by_dept = df.groupby('Department')['Salary'].agg(['mean', 'min', 'max', 'sum'])
print(agg_salary_by_dept)

groupby_city_Depart = df.groupby(['Department', 'City'])['Salary'].mean()
print(groupby_city_Depart)

#Count employes who work in each depart
count_employees = df.groupby('Department')['EmpID'].count()
print(count_employees)

ave_salary = df.groupby('Department')['Salary'].mean().reset_index()
print(ave_salary)

#Find average salary by city
city_ave = df.groupby('City')['Salary'].mean()
print(city_ave)

#Find maximum salary in each department
max_salary_by_dept = df.groupby('Department')['Salary'].max()
print(max_salary_by_dept)

#Find department wise average experiance
avg_experience_by_dept = df.groupby('Department')['Experience'].mean()
print(avg_experience_by_dept)

#Find averge salary of IT employees in karachi
it_karachi_avg_salary = df['Salary'][(df['Department'] == 'IT') & (df['City'] == 'Karachi')].mean()
print(it_karachi_avg_salary)

#Find department +city wise avg saary sorted  highest to lowest
dept_city_avg_salary = df.groupby(['Department', 'City'])['Salary'].mean().sort_values(ascending=False)
print(dept_city_avg_salary)

#Find departments where average salary > 90000
high_salary_depts = df.groupby('Department')['Salary'].mean()[df.groupby('Department')['Salary'].mean() > 90000]
print(high_salary_depts)

#FInd departments whose avg salary is above company's overall avg sakary
company_avg_salary = df['Salary'].mean()
high_salary_depts = df.groupby('Department')['Salary'].mean()[df.groupby('Department')['Salary'].mean() > company_avg_salary]
print(high_salary_depts)

#Find depart with at least 3 employess
depts_with_min_employees = df.groupby('Department').size()[df.groupby('Department').size() >= 3]
print(depts_with_min_employees)

#find departs where avg salary > 85000 and employees count >= 3
high_salary_high_count_depts = df.groupby('Department').filter(lambda x: (x['Salary'].mean() > 85000) and (len(x) >= 3))['Department'].unique()
print(high_salary_high_count_depts)

#For each city , find what percentage of total salary expense it contributes
city_salary_total = df.groupby('City')['Salary'].sum()
city_salary_percentage = (city_salary_total / city_salary_total.sum() * 100)
print(city_salary_percentage)

#**************Pandas Series****************
'''
# Pandas Series - A one-dimensional labeled array capable of holding any data type 
# It's like a column in a DataFrame or a dictionary with index labels

# Definition:
# A Series is an ordered collection of data with an associated array of labels (index)
# Syntax: pd.Series(data, index=None)

# Pros of Pandas Series:
# 1. Easy indexing - Access elements by label or position
# 2. Flexible data types - Can hold integers, floats, strings, objects, etc.
# 3. Alignment - Automatically aligns data based on index labels
# 4. Built-in operations - Mean, sum, std, etc. work directly on Series
# 5. Missing data handling - Handles NaN values gracefully
# 6. Memory efficient - Optimized for numerical operations
# 7. Integration - Works seamlessly with DataFrames and NumPy arrays

# Example:
series_example = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(series_example)
print(series_example['a'])  # Access by label
print(series_example.mean())  # Built-in operations
'''