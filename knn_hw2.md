# KNN Regression – Homework

In this homework we practice KNN regression in three stages
We use **3 features** (X1, X2, X3) and one continuous target y

## Dataset for Questions 1–2

Use this dataset:

```python
import numpy as np

X_data = np.array([
    [0.5, 1.0, 0.2],
    [1.0, 1.5, 0.4],
    [1.5, 2.0, 0.6],
    [2.0, 2.5, 0.8],
    [2.5, 3.0, 1.0],
    [3.0, 3.5, 1.3],
    [3.5, 4.0, 1.5],
    [4.0, 4.5, 1.8],
])

Y_data = np.array([2.1, 2.8, 3.5, 4.2, 4.9, 5.7, 6.4, 7.2])
```

# 1 – Manual KNN (k = 3) Without sklearn

### Task

1. Input a new point (X1, X2, X3)
2. Compute Euclidean distances to every point in `X_data`
3. Find the 3 nearest neighbors
4. Compute the average of their Y values
5. Print the neighbors, distances, and predicted Y

### Example Code

```python
# input
x1 = float(input("Enter X1: "))
x2 = float(input("Enter X2: "))
x3 = float(input("Enter X3: "))
```
# 2 – KNN Using sklearn (k = 3)

### Task

1. Fit a `KNeighborsRegressor` with `k=3`
2. Input a new point from the user
3. Predict its Y value

# 3 – KNN on ~100 Samples + Choosing Optimal k

### Code Template

```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

np.random.seed(42)

# generate 100 points
X = np.random.uniform(0, 10, size=(100, 3))
noise = np.random.normal(0, 1, 100)
y = 2*X[:,0] + 0.5*X[:,1] - 1*X[:,2] + noise

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

k = 3
model = KNeighborsRegressor(n_neighbors=k)
model.fit(X_train, y_train)
pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)

print(f"k={k}, MSE={mse}")
```

# Your Task

1. Try k values from **3 to 9**
2. Compute and store the MSE for each k
3. Plot k vs MSE using matplotlib
4. Select the optimal k (smallest MSE) and explain why

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+knnhw2@gmail.com](mailto:pythonai200425+knnhw2@gmail.com)