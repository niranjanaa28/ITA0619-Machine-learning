from sklearn.tree import DecisionTreeClassifier

X = [
    [0, 0], [0, 1], [1, 0],
    [1, 1], [0, 0], [1, 0]
]
y = ['No', 'No', 'Yes', 'Yes', 'No', 'Yes']

model = DecisionTreeClassifier(
    criterion='entropy', random_state=0
)
model.fit(X, y)

print("Prediction:", model.predict([[1, 1]])[0])
