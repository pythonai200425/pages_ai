# תרגול פיצ'ר סקייל עם פייפליין

## מטרה

לאמן מודל **Logistic Regression** על דאטה נתון

לעשות אימון פעם אחת **בלי סקיילינג**, פעם אחת **עם StandardScaler**, לבדוק דיוק

אחר כך לבדוק בעזרת **Cross Validation**

לבסוף לבנות **Pipeline**  

לשמור לקובץ, לטעון, ולעשות חיזוי לדוגמה חדשה

### Setup Code

```python
import numpy as np

np.random.seed(0)

n = 200

# פיצ'רים בסקיילים שונים
salary = np.random.normal(100_000, 40_000, n)
kids = np.random.randint(0, 5, n)
experience = np.random.randint(1, 20, n)
credit_score = np.random.normal(680, 60, n)

X = np.column_stack([salary, kids, experience, credit_score])

# משתנה מטרה (0/1)
score = (
    0.00002 * salary
    + 0.4 * experience
    + 0.005 * credit_score
    - 0.8 * kids
    - 10
)

y = (score > 0).astype(int)
```

## Train/Test Split + Logistic Regression (No Scaling)

חלק את הנתונים ל־Train/Test

   * השתמש ב־`train_test_split`
   * `test_size=0.2`
   * `random_state=42`

אימן Logistic Regression **בלי שום סקיילינג**

   * השתמש ב־`LogisticRegression`
   * השתמש ב־ `max_iter=1000`

הדפס דיוק (Accuracy) על ה־Test

   * פ- `accuracy_score(y_test, y_pred)`

## Train with StandardScaler

בצע Standard Scaling על הפיצ’רים

   * פ- `StandardScaler`

אימן שוב Logistic Regression על הנתונים אחרי סקיילינג

הדפס דיוק על ה־Test

השווה בין

* פ- Accuracy בלי סקיילינג
* פ- Accuracy עם StandardScaler

## Improve with Cross Validation

חשב Cross Validation Accuracy

   * פ- `cross_val_score(model, X, y, cv=5, scoring="accuracy")`
   * הדפס ממוצע

## Convert to Pipeline (best practice)

צור Pipeline שמבצע

* פ- StandardScaler
* פ- LogisticRegression

הרץ Cross Validation על ה־Pipeline (cv=5)

הדפס mean

אימן את ה־Pipeline על כל הדאטה (`X`, `y`) בסוף

## Save & Load the Pipeline + Prediction

שמור את ה־Pipeline לקובץ

טען את ה־Pipeline מהקובץ

בצע Prediction עבור הדוגמה הבאה

```python
sample = np.array([[120_000, 2, 10, 720]])
```

4. הדפס

`pred` (0/1)
וגם `predict_proba` (הסתברות למחלקה 1)

יש לשלוח את הפתרון למייל:
📧 [pythonai200425+optimize1@gmail.com](mailto:pythonai200425+optimize1@gmail.com)