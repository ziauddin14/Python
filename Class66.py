import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


from sklearn.metrics import classification_report
result = classification_report(y_test, y_pred)
print(result)

for i in range(1,11):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train_scaled, y_train)
  y_pred = knn.predict(X_test_scaled)
  print(i, accuracy_score(y_test, y_pred))

'''
KNN (K-Nearest Neigbors)

KNN does not learn formulae. It memorizes the training data (X, y) and compares new points to existing points.

K means how many neigbors sto look at.

Larger K makes predictions smoother and more stable

how does KNN decide near or far. it uses distance (Euclidean) which is basically geometric distance.

KNN works entirely on distances and due to this, feature scaling becomes extremely important.

KNN is a lazy learner because during training, it almost does nothing. it simply stores the training data. the real work happens during prediction.

KNN is simle, intuitive, beginner friendly, powerful for small datasets.

KNN can learn non linear patterns naturally. Curved boundaries irregular patterns without complex equations.

Limitations:

1. Slow prediction
2. Sensitive to scaling
3. Sensitive to noise
4. Struggles with huge datasets.

Overfitting in KNN
when k=1 model becomes extremely sensitive . this often causes overfitting.


'''