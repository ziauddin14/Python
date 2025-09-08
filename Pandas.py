import pandas as pd

# data = {
#     'Name': ['Zia', 'Ali', 'Sara', 'John'],
#     'Marks': [85, 90, 78, 92],
#     'Age': [20, 21, 19, 22]
# }

# df = pd.DataFrame(data)
# print(df)

# data = [60, 70, 80, 90, 100]
# s = pd.Series(data, index=['Zia', 'Ali', 'Sara', 'John', 'Doe'])
# print(s)

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
