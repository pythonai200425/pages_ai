# Regression Exercise — Discover the Relationship 🏋️‍♂️📊

**Goal**: Use a scatter plot to visually guess the type of relationship between the variables, then choose the appropriate regression model

## Dataset 1

This dataset represents the relationship between **hours spent in the gym per week** (X) and **muscle mass gain in kg** (Y)

| x (hours/week) | y (kg muscle gain) |
| -------------: | -----------------: |
|              0 |                3.1 |
|              1 |                5.0 |
|              2 |                7.2 |
|              3 |                8.9 |
|              4 |               11.2 |
|              5 |               12.8 |
|              6 |               15.2 |
|              7 |               17.1 |
|              8 |               19.2 |
|              9 |               21.0 |

## Dataset 2

This dataset represents the relationship between **daily weightlifting load in kg** (X) and **muscle strength score** (Y)

| x (load kg) | y (strength score) |
| ----------: | -----------------: |
|          -5 |              -20.5 |
|          -4 |              -15.2 |
|          -3 |               -7.6 |
|          -2 |               -0.8 |
|          -1 |                3.2 |
|           0 |                2.1 |
|           1 |                4.7 |
|           2 |                6.0 |
|           3 |                4.9 |
|           4 |                1.6 |
|           5 |               -3.8 |

---

## Your tasks

1. 📈 Plot the data (scatter plot) for each dataset and **decide visually** what kind of pattern it shows
2. 🔍 If the pattern looks linear, fit **Linear Regression**; if it looks curved, fit **Polynomial Regression** (degree=2)
3. 📊 **For both models**: Calc and print **MSE, R²** 
4. 📉 **For Polynomial Regression only**: Calc and print **Adjusted R²**  
5. 📈 **Draw** the graph of the regression line + observation points for the **Linear Regression**  
6. 📈 **Draw** the graph of the regression parabola + observation points for the **Polynoial Regression**  
7. **Predict** (using model.predict) the value of 4.5 hours in the first model, and 0.5 load-kg in the second model

###💡 Theoretical Questions — Test Your Understanding (Bonus)  
8. 🧾 What’s the difference between model.score and the r2_score function?  
9. 🎯 Why do we need to calculate Adjusted R² instead of just relying on R²?  
A. 🌀 In the parabola function aX² + bX + c, explain how each parameter (a, b, c) affects the shape and position of the parabola  
B. 🧮 Considering your previous answer, why does PolynomialFeatures create 3 features?  
C. 🧱 In PolynomialFeatures(degree = 2), the first feature is always 1 — why do we need it?  

**Bonus**:  
Try solving the curved parabola with LinearRegression and check the R². how much it proved when using **Polynomial Regression** (degree=2)?


## 📤 הגשה

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+linpol2hw@gmail.com](mailto:pythonai200425+linpol2hw@gmail.com)
