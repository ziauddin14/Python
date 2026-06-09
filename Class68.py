import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Dataset Load krna
df = pd.read_csv('heart.csv')
print("Dataset successfully loaded. Shape:", df.shape)

# 2. X aur Y ko alag krna (Target column ko drop krke X banana)
X = df.drop('target', axis=1)
y = df['target']
print("X shape (Features):", X.shape)
print("y shape (Target):", y.shape)

# 3. Train Test Split krna (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train set shape:", X_train.shape)
print("Test set shape:", X_test.shape)

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import  matplotlib.pyplot as plot

rf  = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# train krna 
rf.fit(X_train,y_train)

# prediction krna 
y_pred = rf.predict(X_test)

# accuracy check krna
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy)

# plot feature importance



from sklearn.tree import plot_tree
plot_tree(
    rf.estimators_[49],
    feature_names=X.columns,
    class_names= ['Disease', 'No Disease'],
    filled = True,
    rounded = True,
    max_depth=5,
    fontsize=3
        
)
plot.show()

'''
DT overfits very easily.

Random FOrest is a collection of many Decision Trees.

Ensemble: Multiple models working together.

Random: each tree is intentionally made slightly different.

How trees are made different:

1. Random Data Sampling: (Bootstrap sampling)

Row wise division in data.

2. Random Feature Selction: Each tree also sees only random features during splitting

TTree1: cholesterol, age
Tree2: heart rate, chest pain
Tree3:blood pressure, ECG

Feature wise division.

Voting Mechanism: 100 trees make predictions.

78 trees say: Heart disease
22 trees say: No disease

Final prediction : Heart disease

Hyperparameters in RF:

n_estimators: number of trees

max_depth: how deep the trees should be allowed to grow

random_state

Feature importances: RF can estimate feature importance

'''