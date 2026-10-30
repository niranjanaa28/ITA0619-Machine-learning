import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Input dataset (XOR problem)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1
)

# Create ANN model using backpropagation
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='tanh',
    solver='lbfgs',
    max_iter=2000,
    random_state=1
)

# Train the model
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)

print("Actual Output:", y_test)
print("Predicted Output:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test all XOR inputs
print("\nXOR Predictions:")
print(model.predict(X))
