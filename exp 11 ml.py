from sklearn.tree import DecisionTreeClassifier

# Income (thousands), missed payments
X = [[20, 4], [25, 3], [30, 2],
     [60, 0], [70, 0], [55, 1]]
y = ['Low', 'Low', 'Medium',
     'High', 'High', 'High']

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

print("Credit score category:",
      model.predict([[65, 0]])[0])
