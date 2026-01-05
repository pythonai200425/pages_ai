# Regression Tree – MSE, Split Quality, and R²

<img src="images/tree1.png" width="35%"/>


In this exercise, you will practice **manual calculations** for a regression tree split and then **verify your results** using scikit-learn

We are given the following dataset:

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([2, 4, 6, 8, 10, 12, 14]).reshape(-1, 1)
y = np.array([1, 2, 5, 8, 12, 14, 15])
```

We will consider a **regression tree of depth 1** (one split, two leaves) with the condition:

> Split condition: `x <= 9`

1. Compute the **MSE at the root** (before any split):

2. **Identify the samples** in each leaf:

   * **Left leaf (True)**: all points where `x <= 9`
   * **Right leaf (False)**: all points where `x > 9`

2. For the **left leaf (True)** MSE and Mean

3. For the **right leaf (False)** MSE and Mean

4. The **weighted MSE** 

5. The **MSE gain** of the split as the reduction in MSE compared to the root

---

## Let scikit-learn Build the Tree

Now we let scikit-learn build a regression tree of depth 1 and compare to our manual work

1. Complete the following code:

```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([2, 4, 6, 8, 10, 12, 14]).reshape(-1, 1)
y = np.array([1, 2, 5, 8, 12, 14, 15])

# Regression tree with depth 1
tree = DecisionTreeRegressor(
    criterion="squared_error",  # MSE criterion
    max_depth=1,
    random_state=42
)

# Train the tree

# Predictions

# calc MSE and R square

# Show the tree structure
rules = export_text(tree, feature_names=["x"])
print(rules)
```

2. Compute the **MSE** and **R²** of the tree predictions on all training points

## Bonus (Optional)

* Try changing `max_depth` to `2` or `3` and see how the tree changes.
* Recompute MSE and R². Does the performance improve? Does it look like the tree might be overfitting on such a small dataset?

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+decreghw@gmail.com](mailto:pythonai200425+decreghw@gmail.com)