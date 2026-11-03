from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target,
    test_size=0.2, random_state=42,
    stratify=iris.target
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:",
      round(accuracy_score(y_test, pred) * 100, 2), "%")
print("Predicted flower:",
      iris.target_names[pred[0]])
