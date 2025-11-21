# SVM – Exercise 1: Distances to a Hyperplane in 4D

We work in 4-dimensional space with features ($$x_1, x_2, x_3, x_4$$)

The separating hyperplane (decision surface) is:

$$2x_1 - x_2 + x_3 + x_4 - 4 = 0$$

That is, the weight vector and bias are:

$$w = (2, -1, 1, 1),\quad b = -4$$


## Tasks

Given a hyperplane in **n-dimensional space**:

$$w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b = 0$$

and a point:

$$x = (x_1, x_2, \dots, x_n)$$

### 1. Absolute Distance Formula

$$\text{Distance}(x) = \frac{|\mathbf{w} \cdot \mathbf{x} + b|}{\sqrt{w_1^2 + w_2^2 + \dots + w_n^2}}$$

### 2. Signed Distance Formula

$$\text{SignedDistance}(x) = \frac{\mathbf{w} \cdot \mathbf{x} + b}{\sqrt{w_1^2 + w_2^2 + \dots + w_n^2}}$$


## Example for Your Hyperplane

Given the plane:

$$2x_1 - x_2 + x_3 + x_4 - 4 = 0$$

Its weight vector is:

$$w = (2, -1, 1, 1)$$

So the denominator is:

$$\sqrt{2^2 + (-1)^2 + 1^2 + 1^2} = \sqrt{7}$$

Final formulas:

$$\text{Distance}(x) = \frac{|2x_1 - x_2 + x_3 + x_4 - 4|}{\sqrt{7}}$$

$$\text{SignedDistance}(x) = \frac{2x_1 - x_2 + x_3 + x_4 - 4}{\sqrt{7}}$$

---

### Example Calculation for a Point

Let’s use $P_1 = (0, 0, 0, 0)$:

Plug into the formula:

$$
2x_1 - x_2 + x_3 + x_4 - 4 = 2 \times 0 - 0 + 0 + 0 - 4 = -4
$$

So,

$$
	ext{Distance}(P_1) = \frac{|-4|}{\sqrt{7}} = \frac{4}{\sqrt{7}} \approx 1.512
$$

$$
	ext{SignedDistance}(P_1) = \frac{-4}{\sqrt{7}} \approx -1.512
$$

Since $2x_1 - x_2 + x_3 + x_4 - 4 = -4 < 0$, $P_1$ is **below** the hyperplane.

---

## Given Points in R^4

- P1 = (0, 0, 0, 0)
- P2 = (2, 0, 0, 0)
- P3 = (1, 1, 1, 1)
- P4 = (3, -1, 0, 2)
- P5 = (0, 2, 1, 1)
- P6 = (4, 1, -1, 0)
- P7 = (1, 0, 2, 1)
- P8 = (2, 1, 0, 3)
- P9 = (0, -1, 0, 3)
- P10 = (3, 2, 1, 0)

---

## Starter NumPy Code

```python
import numpy as np

# 10 points in R^4: [x1, x2, x3, x4]
points = np.array([
    [0, 0, 0, 0],   # P1
    [2, 0, 0, 0],   # P2
    [1, 1, 1, 1],   # P3
    [3, -1, 0, 2],  # P4
    [0, 2, 1, 1],   # P5
    [4, 1, -1, 0],  # P6
    [1, 0, 2, 1],   # P7
    [2, 1, 0, 3],   # P8
    [0, -1, 0, 3],  # P9
    [3, 2, 1, 0],   # P10
], dtype=float)

w = np.array([2, -1, 1, 1], dtype=float)
b = -4.0
