from sklearn.neighbors import KNeighborsClassifier

X = [[1, 2], [2, 3], [3, 3],
     [6, 7], [7, 8], [8, 7]]
y = ['A', 'A', 'A', 'B', 'B', 'B']

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Class for [2, 2]:", model.predict([[2, 2]])[0])
print("Class for [7, 7]:", model.predict([[7, 7]])[0])
