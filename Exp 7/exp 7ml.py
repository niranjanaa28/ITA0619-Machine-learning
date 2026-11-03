from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print("Prediction for 2.5:", model.predict([[2.5]])[0])
print("Prediction for 5.5:", model.predict([[5.5]])[0])
