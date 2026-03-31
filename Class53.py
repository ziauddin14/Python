import pandas as pd
import openpyxl as op 
s1 = pd.Series([12,24,36,12,18,12,14]) # isky undar 2 cheezy hoti hai numoy ki array aur index,
# pd.Serieses ki Data Type saem hi hogi
print(s1)
s2 = pd.Series([12,24,36,12,18,12,14], index=['a','b','c','d','e','f','g']) # isky indes ko ham 
# apni marzi se set kar sakte hai, agar ham index nahi denge to default index 0 se start hota hai'
# inko lavebls kehty hyn 
print(s2)

# s1 men se wo vlues print krwao jo 13  se bari hon 
print(s1[s1 > 13]) # This will print the values in s1 that are greater than 13
print(s2[s2 > 12]) # This will print the values in s2 that are greater than 12 along with their corresponding labels

#s1 men ny 4th index print krwao
print(s1[4]) # This will print the value at index 4 of s1

df = pd.read_excel('C:\\Users\\User\\OneDrive\\Desktop\\Python-master\\Python-master\\employees.xlsx') # This will read the Excel file and create a DataFrame   
print(df) # This will print the entire DataFrame

print(df['Designation']) # This will print the values in the 'Designation' column of the DataFrame

df['Bonus'] = 50000 # This will add a new column called 'Bonus' to the DataFrame with a value of 50000 for all rows
print(df) # This will print the updated DataFrame with the new 'Bonus' column

df['Bonus1'] = [50000 if des == 'Manager' else 40000 if des == 'Accountant' else 30000 if des == 'Officer' 
else 20000 for des in df['Designation']] # This will add a new column called 'Bonus1' to the DataFrame with different values based on the 'Designation' column
print(df)

df['Bonus2'] = [40000 if age >= 50 else 30000 if age >= 40 else 20000 if age >= 30 else 10000 if age >= 20 else 5000 for age in df['Age']] # This will add a new column called 'Bonus2' to the DataFrame with different values based on the 'Age' column
print(df)

df['Bonus3'] = [salary * 0.5 if salary >= 200000 else salary * 0.25 if salary >= 150000 else salary * 0.15 if salary >= 75000 else 0.1 * salary for salary in df['Salary']] # This will add a new column called 'Bonus3' to the DataFrame with different values based on the 'Salary' column
print(df)

def bonus(sal):
    if sal >= 200000:
        return sal * 0.5
    elif sal >= 150000:
        return sal * 0.25
    elif sal >= 75000:
        return sal * 0.15
    else:
        return 0.1 * sal
df['Bonus4'] = df['Salary'].apply(bonus) # This will add a new column called 'Bonus4' to the DataFrame by applying the bonus function to the 'Salary' column
print(df)

#Doing same task using lambda function
df['Bonus5'] = df['Salary'].apply(lambda sal: sal * 0.5 if sal >= 200000 
else sal * 0.25 if sal >= 150000
else sal * 0.15 if sal >= 75000
else 0.1 * sal) # This will add a new column called 'Bonus5' to the DataFrame by applying a lambda function to the 'Salary' column
print(df)


df['Bonus6'] = x.apply(lambda row:
                      row['Salary']*0.5 if row['Age']>=50
                      else row['Salary']*0.4 if row['Age']>=40
                      else row['Salary']*0.3 if row['Age']>=30
                      else row['Salary']*0.2 if row['Age']>=20
                      else row['Salary']*0.1, axis=1) # This will add a new column called 'Bonus6' to the DataFrame by applying a lambda function to each row of the DataFrame based on the 'Age' and 'Salary' columns
print(df)