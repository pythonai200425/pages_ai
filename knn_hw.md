# 🧮 Exercise: Finding Nearest Neighbors 

We have a small dataset showing a relationship between X (the feature) and Y (the target value).  
Your goal is to find, for each point, its 3 closest neighbors based on X — and then calculate the **average Y** of those neighbors.  
After that, you’ll compare how close this average is to the real Y of the point.

## 📊 Dataset

| X | Y |
|----|----|
| 0.1 | 1.0 |
| 0.3 | 1.3 |
| 0.5 | 1.5 |
| 0.8 | 2.0 |
| 1.1 | 2.4 |
| 1.5 | 2.9 |
| 1.9 | 3.3 |
| 2.3 | 3.8 |
| 2.8 | 4.4 |
| 3.3 | 5.0 |
| 3.7 | 5.4 |
| 4.2 | 6.0 |

---

## 🧠 Step-by-step instructions

1. For each point (for example, X = 1.1), look for the 3 points with X values **closest to it**.  
   Example:  
   - For X = 1.1, the three nearest X values are 0.8, 1.5, and 0.5.  
   - The Y values of those are 2.0, 2.9, and 1.5.  
   - Their average is roughly **(2.0 + 2.9 + 1.5) / 3 = 2.13**.  
   - So, we can say the **predicted Y** for X = 1.1 is **about 2.13**.  
   - The **real Y** was 2.4, so the prediction is close — nice!

2. Repeat this process for every point in the table.

3. After you have all the averages, calculate how far (on average) your predicted Y values are from the real Y values.  
   This gives a simple idea of **how well the neighborhood method works**.

## ✏️ Questions

1. For each X, what are its 3 nearest neighbors?  
2. What is the average Y of those neighbors?  
3. Which points are predicted most accurately (closest to the real Y)?  
4. Where does the prediction seem off?

## 💡 Challenge

Try plotting the points (X on the x-axis, Y on the y-axis) and connect the dots with a smooth line.  
Then plot your “predicted averages” to see how the smoothed line compares to the original one.

## 📤 הגשה

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+knnhw@gmail.com](mailto:pythonai200425+knnhw@gmail.com)
