# Machine Learning – Supervised Learning Exam

**Instructions:**

* Answer all questions
* Calculators are allowed
* Show calculations where required
* Do not assume missing data

pythonai200425_aibasic@gmail.com

---

## Question 1 – KNN (Classification)

Given the following training points with two features:

* A = (1,1) → Cat
* B = (2,2) → Dog
* C = (4,4) → Dog

A new point is given:

* Q = (2,1)

Using **KNN with K=2** and **Euclidean distance**, determine the predicted class for point Q

---

## Question 2 – Confusion Matrix (Open Question)

A binary classification model predicts whether a student **Passed** or **Failed**

Out of 20 samples:

* 8 samples were Pass and predicted Pass
* 3 samples were Pass and predicted Fail
* 2 samples were Fail and predicted Pass
* 7 samples were Fail and predicted Fail

Draw the **2×2 Confusion Matrix** (rows = true label, columns = prediction)

---

## Question 3 – Hyperparameters

Which of the following is **NOT** a hyperparameter

A. Number of neighbors K in KNN  
B. Polynomial degree in polynomial regression  
C. Maximum depth of a decision tree  
D. Weights learned during model training  
E. Threshold in logistic regression  

---

## Question 4 – Linear Regression Metrics

Given the regression model:

ŷ = 2x + 1

And the following observations:

(0,1), (1,3), (2,5), (3,9)

Calculate:

1. MSE
2. R²
3. Adjusted R²

Assume there is **one feature**

---

## Question 5 – Decision Tree (Classification)

A dataset contains 8 samples with one feature x and labels **Success / Fail**

At the root node there are 4 Success and 4 Fail samples

The data is:

x=1 → Success  
x=2 → Success  
x=3 → Success  
x=4 → Fail  
x=5 → Fail  
x=6 → Fail  
x=7 → Fail  
x=8 → Success  

Which split condition gives the **largest Gini Gain**

A. x ≤ 2  
B. x ≤ 3  
C. x ≤ 4  
D. x ≤ 7  

---

## Question 6 – Logistic Regression (Threshold)

A logistic regression model is defined as:

z = w₀x₀ + w₁x₁

Where:

* w₀ = 2
* w₁ = -1
* Threshold = 70%
* Bias = 0

For input x = (1,1)

After applying the sigmoid function, determine whether the output is:

A. Below the threshold
B. Above the threshold
C. Exactly on the threshold
D. Cannot be determined

---

## Question 7 – KNN (Regression)

Given the following training points:

* A = (1,1) → y = 10
* B = (2,2) → y = 20
* C = (4,4) → y = 40

A new point is given:

* Q = (2,1)

Using **KNN Regression with K=2** and Euclidean distance, calculate the predicted value for Q

---

## Question 8 – Confusion Matrix (Accuracy)

Given the following confusion matrix:

```
      Pred1  Pred2  Pred3
True1   3      1      0
True2   2      4      1
True3   0      1      5
```

Calculate the **Accuracy** of the model

---

## Question 9 – Overfitting

A model achieves very high accuracy on the training set but low accuracy on the test set

What does this indicate

A. Underfitting  
B. Overfitting  
C. Balanced model  
D. Unsupervised learning  

---

## Question 10 – SVM (Decision Surface)

A linear SVM model is defined by:

w₀x₀ + w₁x₁ + w₂x₂ + b = 0

Where:

* w₀ = 1
* w₁ = -1
* w₂ = 2
* b = -3

Rules:

* Above the surface → Intrusion detected
* Below the surface → No intrusion

Given point:

x = (2,1,1)

Determine the model decision

A. Intrusion detected  
B. No intrusion  
C. Point lies exactly on the surface  
D. Cannot be determined  

---

## Question 11 – Random Forest

What is **Out-of-Bag Error** in Random Forest

A. Error calculated on the test set only  
B. Error calculated using samples not selected in bootstrap sampling  
C. Error caused by too many trees  
D. Error that applies only to regression problems  

---

## Question 12 – Elbow Method

Polynomial regression models with one feature were trained with different degrees

Validation MSE results:

* Degree 1 → MSE = 50
* Degree 2 → MSE = 22
* Degree 3 → MSE = 18
* Degree 4 → MSE = 17

According to the **Elbow Method**, which degree should be selected

A. 1
B. 2
C. 3
D. 4

---

## Question 13 – KNN (Distance Calculation)

Four training points with three features:

A = (1,2,1)
B = (2,0,2)
C = (3,3,0)
D = (0,1,3)

New point:

Q = (2,2,2)

Using Euclidean distance, determine the **three nearest neighbors**

---

## Question 14 – MSE Calculation

Given:

y = [2,4,6]
ŷ = [3,5,4]

Calculate the **Mean Squared Error (MSE)**

---

## Question 15 – Standard Deviation

Given the dataset:

x = [4, 7, 10, 10, 13, 15, 15, 18, 20, 28]

Calculate the **population standard deviation**

---

## Question 16 – Supervised Learning

What characterizes **Supervised Learning**

A. The data has no labels  
B. The model learns using rewards and penalties  
C. The data includes input features and known output labels  
D. The model performs clustering only  

---

## Question 17 – Regression vs Classification

What is the main difference between **Regression** and **Classification** problems

A. Regression predicts categories while classification predicts numbers  
B. Regression predicts continuous values while classification predicts discrete classes  
C. Classification is always unsupervised  
D. There is no difference between them  

---

## Question 18 – Regression Tree (Final Leaf MSE: Weighted vs Unweighted)

A regression tree ends in a **final leaf** that contains **two groups** of samples:

- **Group A**:  
  - Number of samples: \( n_A = 2 \)  
  - Mean Squared errors: \( 5 \)

- **Group B**:  
  - Number of samples: \( n_B = 8 \)  
  - Mean Squared errors: \( 4 \)

Compute the **overall Mean Squared Error (MSE)** of the leaf

### Options
A.  4.2   
B.  4.5   
C.  4.0   
D.  5.0  

---

## Question 19 – Train vs Test

What is the role of the **Training Set** compared to the **Test Set**

A. Training is used for evaluation, test is used for learning  
B. Both are used for learning  
C. Training is used to learn model parameters, test is used to evaluate performance on unseen data  
D. Test set is used only for normalization  

---

## Question 20 – Random Forest Tasks

Which types of problems can **Random Forest** solve

A. Classification only  
B. Regression only  
C. Both classification and regression  
D. Unsupervised problems only  

---

## Question 21 – Decision Tree (Regression)

### Question

You are given a dataset with **one feature**:

**X = [4, 8, 10]**

You want to apply **polynomial regression with degree (power) = 2**

Which of the following correctly represents the transformed feature matrix
(including the bias term)?

**A)**

```
[
 1   4  
 1   8  
 1  10  
]
```
**B)**

```
[
 1   4   16
 1   8   64
 1  10  100
]
```

**C)**

```
[
 4   16
 8   64
10  100
]
```

**D)**

```
[
 1   16
 1   64
 1  100
]
```

---

## Question 22 – Polynomial Regression

What is the effect of increasing the **polynomial degree** in a regression model

A. Always reduces error on new data  
B. Increases model complexity and risk of overfitting  
C. Reduces number of features  
D. Converts regression into classification  

---

## Question 23 - Adjusted R²

You are comparing two regression models trained on the **same dataset**:

* **Model A**: uses 2 features
* **Model B**: uses 5 features

Both models have a similar **R² score**

Why is **Adjusted R²** preferred over **R²** in this situation?

### Options

**A)** Adjusted R² always increases when more features are added  
**B)** Adjusted R² penalizes models for adding features that do not improve the model significantly  
**C)** Adjusted R² ignores the number of features and only measures error  
**D)** Adjusted R² can only be used for polynomial regression  

---

## Question 24 – Logistic Regression Output

The output of **Logistic Regression** after applying the sigmoid function represents:

A. A class label directly  
B. A distance from the decision boundary  
C. A probability estimate  
D. A regression value  

---

## Question 25 – Evaluation Metric

Which metric is most commonly used to evaluate **classification accuracy**

A. Mean Squared Error  
B. Accuracy  
C. Variance  
D. Standard Deviation  

---

**End of Exam**
