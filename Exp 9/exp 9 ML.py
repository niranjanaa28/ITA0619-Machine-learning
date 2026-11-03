Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])

linear = LinearRegression().fit(X, y)

poly = make_pipeline(
    PolynomialFeatures(2),
    LinearRegression()
)
poly.fit(X, y)

print("Linear prediction:", round(linear.predict([[6]])[0], 2))
print("Polynomial prediction:", round(poly.predict([[6]])[0], 2))
print("Linear MSE:", round(mean_squared_error(y, linear.predict(X)), 2))
print("Polynomial MSE:", round(mean_squared_error(y, poly.predict(X)), 2))
