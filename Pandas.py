import pandas as pd

data = {
    'Name': ['Zia', 'Ali', 'Sara', 'John'],
    'Marks': [85, 90, 78, 92],
    'Age': [20, 21, 19, 22]
}

df = pd.DataFrame(data)
print(df)

data = [60, 70, 80, 90, 100]
s = pd.Series(data, index=['Zia', 'Ali', 'Sara', 'John', 'Doe'])
print(s)

# 📝 Practice Problems (Pandas Series)
# Q1:
# Ek list [5, 10, 15, 20, 25] ko Pandas Series me convert karo.
# Phir uska index aur values print karo.
data = [5, 10, 15, 20, 25]
s = pd.Series(data)
print("Index:", s.index, "Values:", s.values)

# Q2:
# Ek Series banao dictionary se:
# {'Math': 85, 'English': 78, 'Science': 92, 'History': 74}
# "Science" ka score print karo.
# Saare subjects ka average score calculate karo.
data = {'Math': 85, 'English': 78, 'Science': 92, 'History': 74}
s = pd.Series(data)
print("Science Score:", s['Science'])
print("Average Score:", s.mean())

# Q3:
# Ek Series banao students ke marks ki:
# [50, 60, 70, 80, 90] with custom index ['Ali','Sara','John','Zia','Doe'].
# "Sara" aur "Doe" ke marks print karo.
# Check karo kitne students ke marks 70 se upar hain.
data = [50, 60, 70, 80, 90]
index = ['Ali', 'Sara', 'John', 'Zia', 'Doe']
s = pd.Series(data, index=index)
print("Sara's & Doe's Marks:", s['Sara'] + s['Doe'])
print("Students with marks above 70:", (s > 70).sum())

# ************************📝 Practice Problems – Pandas DataFrame************************
# Problem 1: DataFrame Create & View
# Ek DataFrame banao jisme ye data ho:
# Name: Ali, Zain, Sara, Ahmed, Hina
# Age: 18, 20, 19, 21, 22
# Marks: 85, 90, 78, 88, 95
# Pehli 3 rows dikhane ka code likho.
# Aakhri 2 rows dikhane ka code likho.
# DataFrame ka summary aur shape check karo.
# Column names print karo.
data = {
    'Name': ['Ali', 'Zain', 'Sara', 'Ahmed', 'Hina'],
    'Age': [18, 20, 19, 21, 22],
    'Marks': [85, 90, 78, 88, 95]
}
df = pd.DataFrame(data)
print(df.head(3))  # First 3 rows
print(df.tail(2))  # Last 2 rows
print(df.info())   # Summary
print("Shape:", df.shape)  # Shape
print("Columns:", df.columns)  # Column names


# Problem 2: Selection & Filtering
# Sirf Marks column print karo.
# Sirf Name aur Marks column ek sath print karo.
# Row number 2 ka data iloc ka use karke print karo.
# Row number 1 ka Name aur Marks column loc ka use karke print karo.
# Sirf un students ka data print karo jinke Marks > 85 hain.
print(df['Marks'])  # Marks column
print(df[['Name', 'Marks']])  # Name and Marks columns
print(df.iloc[2])  # Row number 2
print(df.loc[1, ['Name', 'Marks']])  # Row number 1
print(df[df['Marks'] > 85])  # Students with Marks > 85

# Problem 3: Sorting & Modification
# Marks ke basis pe ascending order me data sort karo.
# Marks ke basis pe descending order me data sort karo.
# Naya column Grade add karo jisme aap Marks ke basis pe A, B, C grade do.
# Age column delete karo.
print(df.sort_values(by='Marks'))  # Ascending order
print(df.sort_values(by='Marks', ascending=False))  # Descending order
df['Grade'] = pd.cut(df['Marks'], bins=[0, 80, 90, 100], labels=['C', 'B', 'A'])  # Adding Grade column
print(df)
df.drop(columns=['Age'], inplace=True)  # Deleting Age column
print(df)

# Problem 4: Missing Values
# Ek naya column Sports banao jisme kuch values NaN ho.
# Missing values ko "Cricket" se fill karo.
# Missing values wali rows delete karo.\
df['Sports'] = ['Football', None, 'Tennis', None, 'Badminton']  # Adding Sports column with NaN values
print(df)
df['Sports'].fillna('Cricket', inplace=True)  # Filling NaN values
print(df)
df.dropna(inplace=True)  # Dropping rows with NaN values
print(df)
print(df.isnull().sum())  # Checking for missing values


# Problem 5: Statistics & File Handling
# Marks ka mean, max, min, sum nikalna hai.
# Apna DataFrame ek CSV file me save karo.
# CSV file ko dobara load karo aur pehli 5 rows dikhayo.
print("Mean Marks:", df['Marks'].mean())
print("Max Marks:", df['Marks'].max())
print("Min Marks:", df['Marks'].min())
print("Sum of Marks:", df['Marks'].sum())
df.to_csv('students.csv', index=False)  # Saving to CSV
 df_loaded = pd.read_csv('students.csv')  # Loading from CSV
 print(df_loaded.head())  # First 5 rows of loaded CSV
 print(df_loaded)


#**************************Pandas Indexing & Selection**************************
# Q1 – loc (label-based)
# John ke English marks print karo.
# Q2 – iloc (position-based)
# 3rd row (index=2 → John) aur 1st column (index=0 → Math) ka value print karo.
# Q3 – Conditional Selection
# Wo students print karo jinke Math marks ≥ 80 hain.
# Q4 – Fancy Indexing
# Ali aur Sara ke Science aur English marks ek sath print karo.

data = {
    'Math': [85, 70, 90, 60, 75],
    'English': [78, 65, 88, 72, 80],
    'Science': [92, 75, 85, 70, 95]
}
students = ['Ali', 'Sara', 'John', 'Zia', 'Doe']

df = pd.DataFrame(data, index=students)
print(df)

print(df.loc['John', 'English'])  # John ka English score
print(df.iloc[2, 0])  # John ka Math score
print(df[df['Math'] > 80])  # Students jinke Math score 80 se upar hain
print(df.loc[['Ali', 'Sara'], ['Science', 'English']])  # Ali aur Sara ke Science aur English scores


# ****************Pandas Data Cleaning********************

# import pandas as pd

# data = {
#     'Name': ['Ali', 'Sara', 'Ali', None, 'Hina '],
#     'Marks': ['85', '90', None, '75 ', '95'],
#     'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi']
# }

# df = pd.DataFrame(data)

# # 1. Fill missing values
# df['Name'] = df['Name'].fillna('Unknown').str.strip().str.lower()
# df['Marks'] = df['Marks'].str.strip().astype(float)
# df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# # 2. Remove duplicates
# df = df.drop_duplicates()

# print(df)

# Practice Problem 02*************
# import pandas as pd

# data = {
#     'Product': ['Mobile ', 'Laptop', None, 'Tablet', 'Laptop', 'Camera '],
#     'Price': ['20000', '55000', '30000 ', None, '55000', '15000 '],
#     'Quantity': [5, None, 10, 7, 5, None],
#     'City': ['Lahore', 'Karachi', 'Karachi', 'Islamabad', 'Karachi', 'Lahore']
# }

# df = pd.DataFrame(data)
# df['Product'] = df['Product'].fillna("Unknown")
# df['Quantity'] = df['Quantity'].fillna(0)

# df['Price'] = df['Price'].str.strip()
# df['Price'] = pd.to_numeric(df['Price'])
# df['Price'] = df['Price'].fillna(df['Price'].median())

# df['Product'] = df['Product'].str.strip().str.lower()

# df = df.drop_duplicates()

# df['Quantity'] = df['Quantity'].astype('Int16')

# print(df)


# Practice Problem 03******************
# import pandas as pd

# data = {
#     'Customer': ['Aisha ', ' Bilal', 'Aisha ', None, 'Omar', 'Zara'],
#     'Age': ['25', '30 ', None, '40', '22', '30'],
#     'Purchase': ['1000', '2000', '1000', '3000 ', None, '2000'],
#     'City': ['Karachi', 'Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Lahore']
# }

# df = pd.DataFrame(data)
# print(df)

# df['Customer'] = df['Customer'].str.strip().str.lower()
# df['Customer'] = df['Customer'].fillna("Unknown")
# df['Purchase'] = df['Purchase'].fillna(0)
# df['Purchase'] = pd.to_numeric(df['Purchase'])

# df['Age'] = df['Age'].str.strip()
# df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# df['Age'] = df['Age'].fillna(df['Age'].mean())


# df = df.drop_duplicates()

# print(df)

# 📌 Practice Problem 4 (Data Cleaning)
import pandas as pd

data = {
    'Employee': [' Ali', 'Sara ', None, 'Hina', 'Ali', 'Zeeshan '],
    'Salary': ['50000 ', '60000', None, '55000', '50000', '70000 '],
    'Dept': ['IT', 'HR', 'HR', 'Finance', 'IT', None],
    'Experience': ['2', '5 ', '3', None, '2', '10']
}

df = pd.DataFrame(data)
print("Before Cleaning:\n", df)

df['Employee'] = df['Employee'].str.strip().str.lower()
df['Employee'] = df['Employee'].fillna("Unknown")
df['Dept'] = df['Dept'].str.strip().str.lower()
df['Dept'] = df['Dept'].fillna("Unknown")

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())


df['Experience'] = pd.to_numeric(df['Experience'], errors='coerce')
df['Experience'] = df['Experience'].fillna(df['Experience'].mean())

print("After Cleaning:\n", df)


df_loaded = pd.read_csv('students.csv')  # Loading from CSV
print(df_loaded.head())  # First 5 rows of loaded CSV
print(df_loaded)

# ***********************📊 Practice Problems (Pandas GroupBy)****************
# Problem 1 (Easy)
# Ek CSV me data hai:
# Name	Class	Marks
# Ali	10	85
# Sara	10	92
# Ahmed	9	78
# Ayesha	9	88
# Umar	10	75
# 👉 Task: Har class ka average marks nikalna.

data = {
    'Name': [' Ali', 'Sara ','Ahmed', 'Ayesha','Umar'],
    'Class': ['10', '10','9','9','10'],
    'Marks': [85,92,78,88,75],
}
df = pd.DataFrame(data)
grouped = df.groupby("Class")['Marks'].mean()
print(grouped)

# Problem 2 (Medium)
# Ek sales dataset hai:
# Region	Product	Sales
# North	A	120
# North	B	90
# South	A	100
# South	B	150
# East	A	200
# 👉 Task: Har region ka total sales aur max sales product nikalna.
data = {
    'Region': [' North', 'North ','South', 'South','East'],
    'Product': ['A', 'B','A','B','A'],
    'Sales': [120,90,100,150,200],
}
df = pd.DataFrame(data)
totalSale = df.groupby("Region")['Sales'].sum()
# print("Total Sales by Region:\n", totalSale)
max_sale = df.loc[df.groupby("Region")["Sales"].idxmax()]
print(max_sale)


# Problem 3 (Tricky)
# Ek students dataset hai:
# Name	Class	Subject	Marks
# Ali	10	Math	85
# Ali	10	Science	80
# Sara	10	Math	90
# Sara	10	Science	95
# Ahmed	9	Math	70
# 👉 Task: Har class ke har subject ka highest marks nikalna (yani topper per subject per class).
data = {
    'Name': [' Ali', 'Ali ','Sara', 'Sara','Ahmed'],
    'Class': ['10', '10','10','10','9'],
    'Subject':['Math','Science','Math','Science','Math'],
    'Marks': [85,80,90,95,70],
}
df = pd.DataFrame(data)
highst_marks = df.loc[df.groupby(["Class","Subject"])["Marks"].idxmax()]
print(highst_marks)


=======
# ****************Pandas Data Cleaning********************

# import pandas as pd

# data = {
#     'Name': ['Ali', 'Sara', 'Ali', None, 'Hina '],
#     'Marks': ['85', '90', None, '75 ', '95'],
#     'City': ['Lahore', 'Karachi', 'Lahore', 'Islamabad', 'Karachi']
# }

# df = pd.DataFrame(data)

# # 1. Fill missing values
# df['Name'] = df['Name'].fillna('Unknown').str.strip().str.lower()
# df['Marks'] = df['Marks'].str.strip().astype(float)
# df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# # 2. Remove duplicates
# df = df.drop_duplicates()

# print(df)

# Practice Problem 02*************
# import pandas as pd

# data = {
#     'Product': ['Mobile ', 'Laptop', None, 'Tablet', 'Laptop', 'Camera '],
#     'Price': ['20000', '55000', '30000 ', None, '55000', '15000 '],
#     'Quantity': [5, None, 10, 7, 5, None],
#     'City': ['Lahore', 'Karachi', 'Karachi', 'Islamabad', 'Karachi', 'Lahore']
# }

# df = pd.DataFrame(data)
# df['Product'] = df['Product'].fillna("Unknown")
# df['Quantity'] = df['Quantity'].fillna(0)

# df['Price'] = df['Price'].str.strip()
# df['Price'] = pd.to_numeric(df['Price'])
# df['Price'] = df['Price'].fillna(df['Price'].median())

# df['Product'] = df['Product'].str.strip().str.lower()

# df = df.drop_duplicates()

# df['Quantity'] = df['Quantity'].astype('Int16')

# print(df)


# Practice Problem 03******************
# import pandas as pd

# data = {
#     'Customer': ['Aisha ', ' Bilal', 'Aisha ', None, 'Omar', 'Zara'],
#     'Age': ['25', '30 ', None, '40', '22', '30'],
#     'Purchase': ['1000', '2000', '1000', '3000 ', None, '2000'],
#     'City': ['Karachi', 'Lahore', 'Karachi', 'Islamabad', 'Lahore', 'Lahore']
# }

# df = pd.DataFrame(data)
# print(df)

# df['Customer'] = df['Customer'].str.strip().str.lower()
# df['Customer'] = df['Customer'].fillna("Unknown")
# df['Purchase'] = df['Purchase'].fillna(0)
# df['Purchase'] = pd.to_numeric(df['Purchase'])

# df['Age'] = df['Age'].str.strip()
# df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# df['Age'] = df['Age'].fillna(df['Age'].mean())


# df = df.drop_duplicates()

# print(df)

# 📌 Practice Problem 4 (Data Cleaning)
import pandas as pd

data = {
    'Employee': [' Ali', 'Sara ', None, 'Hina', 'Ali', 'Zeeshan '],
    'Salary': ['50000 ', '60000', None, '55000', '50000', '70000 '],
    'Dept': ['IT', 'HR', 'HR', 'Finance', 'IT', None],
    'Experience': ['2', '5 ', '3', None, '2', '10']
}

df = pd.DataFrame(data)
# print("Before Cleaning:\n", df)

df['Employee'] = df['Employee'].str.strip().str.lower()
df['Employee'] = df['Employee'].fillna("Unknown")
df['Dept'] = df['Dept'].str.strip().str.lower()
df['Dept'] = df['Dept'].fillna("Unknown")

df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())


df['Experience'] = pd.to_numeric(df['Experience'], errors='coerce')
df['Experience'] = df['Experience'].fillna(df['Experience'].mean())

# print("After Cleaning:\n", df)


# ***********************📊 Practice Problems (Pandas GroupBy)****************
# Problem 1 (Easy)
# Ek CSV me data hai:
# Name	Class	Marks
# Ali	10	85
# Sara	10	92
# Ahmed	9	78
# Ayesha	9	88
# Umar	10	75
# 👉 Task: Har class ka average marks nikalna.

data = {
    'Name': [' Ali', 'Sara ','Ahmed', 'Ayesha','Umar'],
    'Class': ['10', '10','9','9','10'],
    'Marks': [85,92,78,88,75],
}
df = pd.DataFrame(data)
grouped = df.groupby("Class")['Marks'].mean()
print(grouped)

# Problem 2 (Medium)
# Ek sales dataset hai:
# Region	Product	Sales
# North	A	120
# North	B	90
# South	A	100
# South	B	150
# East	A	200
# 👉 Task: Har region ka total sales aur max sales product nikalna.
data = {
    'Region': [' North', 'North ','South', 'South','East'],
    'Product': ['A', 'B','A','B','A'],
    'Sales': [120,90,100,150,200],
}
df = pd.DataFrame(data)
totalSale = df.groupby("Region")['Sales'].sum()
# print("Total Sales by Region:\n", totalSale)
max_sale = df.loc[df.groupby("Region")["Sales"].idxmax()]
print(max_sale)


# Problem 3 (Tricky)
# Ek students dataset hai:
# Name	Class	Subject	Marks
# Ali	10	Math	85
# Ali	10	Science	80
# Sara	10	Math	90
# Sara	10	Science	95
# Ahmed	9	Math	70
# 👉 Task: Har class ke har subject ka highest marks nikalna (yani topper per subject per class).
data = {
    'Name': [' Ali', 'Ali ','Sara', 'Sara','Ahmed'],
    'Class': ['10', '10','10','10','9'],
    'Subject':['Math','Science','Math','Science','Math'],
    'Marks': [85,80,90,95,70],
}
df = pd.DataFrame(data)
highst_marks = df.loc[df.groupby(["Class","Subject"])["Marks"].idxmax()]
print(highst_marks)

