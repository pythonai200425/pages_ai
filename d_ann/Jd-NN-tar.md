## ⭐ ANN Exercise 

### רקע:

חברת אשראי רוצה לחזות האם לקוח יחזיר את ההלוואה שלו (1=חזר, 0=לא חזר) על סכום ההכנסה השנתית שלו ( באלפי ש"ח)

### נתונים היסטוריים:

| החזר הלוואה (1=כן, 0=לא) | הכנסה שנתית (אלפי ש"ח) |
| ------------------------ | ---------------------- |
| 0                        | 30                     |
| 0                        | 35                     |
| 0                        | 40                     |
| 0                        | 45                     |
| 0                        | 50                     |
| 1                        | 55                     |
| 0                        | 60                     |
| 1                        | 65                     |
| 1                        | 70                     |
| 1                        | 75                     |
| 1                        | 80                     |
| 1                        | 85                     |
| 1                        | 90                     |

### שאלות:

1. אמן רשת נוירונים למציאת הקשר בין ההכנסה השנתית להחזר ההלוואה
2. מה הסתברות שלקוח עם הכנסה השנתית של 58 אלף ש"ח יחזיר את ההלואה?

Code sample:

```python
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# שלב 1: הכנסת הנתונים
X = np.array([[30], [35], [40], [45], [50], [55], [60], [65], [70], [75], [80], [85], [90]], dtype=float)
y = np.array([[0], [0], [0], [0], [0], [1], [0], [1], [1], [1], [1], [1], [1]], dtype=float)

# שלב 2: נורמליזציה
# StandardScaler

# שלב 3: בניית המודל

# שלב 4: קומפילציה ואימון

# הסתברות החזר ל-58 אלף ש"ח
income_58 = scaler.transform(np.array([[58]]))

```

**Submission email**: [pythonai250824+anndhw@gmail.com](mailto:pythonai250824+anndhw@gmail.com)