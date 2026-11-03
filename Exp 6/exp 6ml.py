from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

X_train = [[1, 20], [2, 21], [8, 80],
           [9, 85], [1, 22], [8, 78]]
y_train = ['Low', 'Low', 'High',
           'High', 'Low', 'High']

X_test = [[2, 19], [9, 82], [3, 25], [7, 75]]
y_test = ['Low', 'High', 'Low', 'High']

model = GaussianNB()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Predictions:", pred.tolist())
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred, labels=['Low', 'High']))
print("Accuracy:", accuracy_score(y_test, pred))
