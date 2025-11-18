# 🏃‍♂️ Logistic Regression – Brisk Activity Homework

**Story:**
x = minutes of brisk activity per day
y = whether the person hit 10k steps that day (1 = yes, 0 = no)

### Dataset

| x (minutes) | y (hit 10k steps) |
| ----------: | ----------------: |
|           5 |                 0 |
|          12 |                 0 |
|          18 |                 0 |
|          22 |                 0 |
|          28 |                 0 |
|          35 |                 0 |
|          42 |                 0 |
|          48 |                 1 |
|          55 |                 1 |
|          63 |                 1 |
|          72 |                 1 |
|          85 |                 1 |

## 📝 Exercise Requirements

**demo code:**  
https://github.com/pythonai200425/17.11.2025/blob/main/log_2.ipynb

### **1️⃣ Train Logistic Regression Model**

* Fit a logistic regression model using scikit-learn with `solver='liblinear'` on the table above  
* Print `intercept_` and `coef_`  

### **2️⃣ Print the Confusion Matrix**

Use the model to predict all given x values, then print the confusion matrix in text form

### **3️⃣ Calculate Accuracy**

Compute and print the model accuracy (in percent)

## **4️⃣ Find x for Confidence = 0.70**

**Decision boundary for 70%**: solve for $x$ such that $p(y=1\mid x) = 0.70$  

Print the closest x

### **5️⃣ Predict for x = 46**

Use the trained model to predict if someone with 46 minutes of brisk activity will hit 10k steps

### **6️⃣ Plot the Graph and Decision Boundary**

Create a plot showing:

* The data points
* The logistic regression curve
* The decision boundary line

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+loghwf@gmail.com](mailto:pythonai200425+loghwf@gmail.com)
