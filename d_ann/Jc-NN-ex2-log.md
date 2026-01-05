
# רגרסיה לוגיסטית ב- ANN

**תרגיל**: 
חברת אשראי רוצה לחזות האם לקוח יחזיר את ההלוואה שלו (1=החזיר, 0=לא החזיר) על סמך ההכנסה השנתית שלו (באלפי שקלים). להלן נתונים היסטוריים:

| הכנסה שנתית (אלפי ש"ח) | החזיר הלוואה (1=כן, 0=לא) |
|------------------------|---------------------------|
| 30                     | 0                         |
| 35                     | 0                         |
| 40                     | 0                         |
| 45                     | 0                         |
| 50                     | 0                         |
| 55                     | 1                         |
| 60                     | 0                         |
| 65                     | 1                         |
| 70                     | 1                         |
| 75                     | 1                         |
| 80                     | 1                         |
| 85                     | 1                         |
| 90                     | 1                         |

מה ההסתברות שלקוח עם הכנסה שנתית של 58 אלף ש"ח יחזיר את ההלוואה?

### נראה כיצד ניתן לפתור את הבעיה ב- ANN

* Better to run it in Pycharm using python 3.12

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler

# ----- data -----
X = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90], dtype=float)\
       .reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1], dtype=float).reshape(-1, 1)

# scale input
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

# ----- ANN: single neuron sigmoid -----
model = Sequential([Dense(1, activation='sigmoid', input_shape=(1,))])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# train
model.fit(X_s, y, epochs=2000, verbose=0)

# ----- predictions -----
probs = model.predict(X_s, verbose=0)
preds = (probs > 0.5).astype(int)

print("X: ", [30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
print("Predicted probabilities:", np.round(probs.ravel(), 3))
print("Predicted classes:", preds.ravel())

print()
print('prediction for 58K:')
print(model.predict(scaler.transform([[58]])))
```

Output:
```
X:  
 [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
Predicted probabilities: 
 [0.416 0.436 0.457 0.477 0.498 0.519 0.539 0.56  0.58  0.6   0.62  0.639 0.658]
Predicted classes: 
 [0 0 0 0 0 1 1 1 1 1 1 1 1]

prediction for 58K:
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 28ms/step
[[0.53929484]]
```

