import numpy as np
from sklearn.mixture import GaussianMixture

X = np.array([[1], [1.5], [2], [8], [8.5], [9]])

model = GaussianMixture(
    n_components=2,
    random_state=0,
    n_init=5
)
model.fit(X)

labels = model.predict(X)

print("Cluster labels:", labels.tolist())
print("Cluster means:",
      sorted(round(float(m[0]), 2) for m in model.means_))
