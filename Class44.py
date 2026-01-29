import pandas as pd 

df = pd.read_csv('Heart_Disease_prediction.csv')

print(df.info())
print(df.head(2))
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.mean(numeric_only=True), '\n', df.median(numeric_only=True))
print(df.skew(numeric_only=True))
print(df.groupby('Heart Disease').mean(numeric_only=True))
print(df.groupby('Sex')['Heart Disease'].value_counts())
data = df[
    (df['Age'] > 55) &
    (df['Cholesterol'] > 240) &
    (df['Max HR'] < 120)
]
print(data)

# Which age group has the highest heart disease rate?
# df["AgeGroup"] = pd.cut(df["Age"], bins=[0,30,40,50,60,70,100] , labels=["0-29","30-39","40-49","50-59","60-69","70+"])
# # age_group_hd = df.groupby('AgeGroup')['Heart Disease'].mean().sort_values(ascending=False)
# print(age_group_hd)


# Does cholesterol strongly predict heart disease? using correlation
# Convert 'Heart Disease' column to numeric (map string values to numbers)
df['Heart Disease'] = pd.factorize(df['Heart Disease'])[0]
correlation = df['Cholesterol'].corr(df['Heart Disease'])
print("Correlation between Cholesterol and Heart Disease:", correlation)


# Is max heart rate lower in heart disease patients?
heart_disease_max_hr = df[df['Heart Disease'] == 1]['Max HR'].mean()
no_heart_disease_max_hr = df[df['Heart Disease'] == 0]['Max HR'].mean()
print("Average Max HR for patients with heart disease:", heart_disease_max_hr)
print("Average Max HR for patients without heart disease:", no_heart_disease_max_hr)

# Which combination of features indicates highest risk? using correlation matrix
correlation = df['Cholesterol'].corr(df['Heart Disease'])
correlation = df['Age'].corr(df['Heart Disease'])
correlation = df['FBS over 120'].corr(df['Heart Disease'])
correlation = df['Max HR'].corr(df['Heart Disease'])
print("Correlation between Age and Heart Disease:", correlation)
print("Correlation between FBS over 120 and Heart Disease:", correlation)
print("Correlation between Max HR and Heart Disease:", correlation)
