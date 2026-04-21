import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.head()
df.to_csv('titanic.csv')
df.info()
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].median())
df.info()
sns.countplot(x='Survived', data= df)
sns.countplot(x='Sex', data= df)
sns.countplot(data=df, x='Sex', hue='Survived')
sns.histplot(df['Age'], bins=20, kde=True)
df.head()
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df.tail()
df.FamilySize.min()
df.FamilySize.max()
df['FamilySize'].sum()
df.FamilySize.value_counts().sort_index()