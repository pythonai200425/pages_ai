# Homework: SVM classifier – Apples vs Bananas

We have a small dataset of apples and bananas with two numeric features: size and weight

## Data Table

| Index | Fruit  | Feature 1 | Feature 2 |
| ----: | ------ | --------- | --------- |
|     1 | Apple  | 3         | 150       |
|     2 | Apple  | 4         | 130       |
|     3 | Apple  | 2         | 160       |
|     4 | Apple  | 3         | 140       |
|     5 | Apple  | 3.5       | 145       |
|     6 | Banana | 7         | 120       |
|     7 | Banana | 6         | 110       |
|     8 | Banana | 8         | 115       |
|     9 | Banana | 7.5       | 125       |
|    10 | Banana | 6.5       | 118       |

<img src="images/svm_hw.jpg" style="width: 50%" />

## Starter Python Code

```python
import numpy as np

apples = np.array([[3, 150], [4, 130], [2, 160], [3, 140], [3.5, 145]])
bananas = np.array([[7, 120], [6, 110], [8, 115], [7.5, 125], [6.5, 118]])

# Combine features and create labels (-1 for apples, 1 for bananas)
X = np.vstack([apples, bananas])
labels = np.array([-1, -1, -1, -1, -1, 1, 1, 1, 1, 1])
```
### Demo code:

<a href="https://github.com/pythonai200425/24.11.2025/blob/main/svm_2.ipynb">https://github.com/pythonai200425/24.11.2025/blob/main/svm_2.ipynb</a>

## Tasks

### Task 1 – Plot the data

* Create a scatter plot
* Apples = one color, Bananas = another
* Feature 1 on X-axis, Feature 2 on Y-axis
* Add title and legend

### Task 2 – Train an SVM model

* Use scikit-learn `SVC(kernel="linear")` or `LinearSVC`
* Fit the model
* Print coefficients and intercept

### Task 3 – Draw the decision boundary and margins

* Draw decision boundary (where decision_function = 0)
* Draw margins (where decision_function = +1 and -1)
* Overlay on scatter plot

### Task 4 – Confusion matrix & accuracy

* Predict labels on X
* Compute confusion matrix
* Compute accuracy
* Print both


יש לשלוח את הפתרון למייל:
📧 [pythonai200425+svmhwf@gmail.com](mailto:pythonai200425+svmhwf@gmail.com)