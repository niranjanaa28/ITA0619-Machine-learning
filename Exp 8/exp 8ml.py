from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)

print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
print("Prediction for x=6:", model.predict([[6]])[0])
