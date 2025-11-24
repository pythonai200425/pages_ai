# Gini Impurity בעצי החלטה
  
## מהו Gini Impurity?
  
Gini Impurity (אי-טוהר ג'יני)
  
  מדד המשמש באלגוריתמים של עצי החלטה כדי לקבוע כיצד לפצל את הנתונים בצורה אופטימלית. המדד מודד את ההסתברות שפריט שנבחר באקראי מקבוצה יתויג בצורה שגויה אם התיוג נעשה לפי התפלגות התוויות באותה קבוצה.
  
במילים פשוטות, Gini Impurity מודד כמה "טהור" או "הומוגני" הוא צומת בעץ - האם הוא מכיל בעיקר דגימות מקטגוריה אחת או תערובת של כמה קטגוריות
  
## למה צריך את Gini Impurity?
  
בעצי החלטה, אנחנו צריכים קריטריון לקבוע:
1. **באיזה משתנה (feature) להשתמש** לפיצול הנתונים
2. **באיזה ערך סף (threshold)** לבצע את הפיצול
  
אי-טוהר ג'יני עוזר לנו לענות על שאלות אלו מהסיבות הבאות:
  
1. **קריטריון לפיצול אופטימלי**: הוא מאפשר לאלגוריתם להעריך איזה פיצול יוביל לקבוצות טהורות יותר של נתונים
2. **מדידת שיפור**: באמצעות השוואת ה-Gini Impurity לפני ואחרי פיצול אפשרי, האלגוריתם יכול לחשב את ה"רווח המידע" ולבחור את הפיצול שמייצר את הירידה הגדולה ביותר באי-טוהר
3. **מניעת התאמת יתר (overfitting)**: שימוש במדד זה מוביל לפיצולים בעלי משמעות במקום פיצולים שרירותיים
4. **יעילות חישובית**: חישוב Gini Impurity מהיר יחסית לעומת מדדים אחרים
  
## הנוסחה של Gini Impurity
  
הנוסחה המתמטית של Gini Impurity היא:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%20\sum_{c%20\in%20C}%20p_c(1-p_c)"/></p>  
  
  
כאשר:
- **Q** מסמל צומת מסוים בעץ ההחלטה
- **G(Q)** הוא ערך ה-אי-טוהר ג'יני של אותו צומת Q
- **C** הוא קבוצת הקטגוריות (מחלקות) בצומת
- **<img src="https://latex.codecogs.com/gif.latex?p_c"/>** הוא ההסתברות שאובייקט בצומת משתייך לקטגוריה c
- **<img src="https://latex.codecogs.com/gif.latex?1-p_c"/>** הוא ההסתברות שאובייקט בצומת לא משתייך לקטגוריה c
- **<img src="https://latex.codecogs.com/gif.latex?\sum"/>** מסמל סכימה על כל הקטגוריות בצומת Q
  
נוסחה שקולה נוספת שמשתמשים בה לעתים קרובות:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%201%20-%20\sum_{c%20\in%20C}%20p_c^2"/></p>  
  
  
לסיווג בינארי (שתי קטגוריות בלבד), הנוסחה מתפשטת ל:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%201%20-%20[(p_1)^2%20+%20(p_2)^2]"/></p>  
  
  
## חישוב Gini Impurity - דוגמה
  
נניח שיש לנו קבוצת נתונים עם 10 דגימות:
- 7 דגימות שייכות לקטגוריה A
- 3 דגימות שייכות לקטגוריה B
  
נחשב את Gini Impurity של הצומת:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%201%20-%20[(7/10)^2%20+%20(3/10)^2]"/></p>  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%201%20-%20[0.49%20+%200.09]"/></p>  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%201%20-%200.58"/></p>  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(Q)%20=%200.42"/></p>  
  
  
ערך זה (0.42) מעיד על כך שהצומת אינו טהור לחלוטין. 
- כאשר G(Q) = 0, הצומת טהור לחלוטין (כל הדגימות שייכות לאותה קטגוריה)
- כאשר G(Q) = 0.5 (בסיווג בינארי), הצומת בעל אי-טוהר מקסימלי (חלוקה שווה בין הקטגוריות)
  
## חישוב Gini Impurity בעץ החלטה
  
נניח שיש לנו מערכת נתונים פשוטה עם שני מאפיינים (X1, X2) וקטגוריה יעד (Y) כפי שמוצג בטבלה:
  
| X1 | X2 | Y |
|----|----|----|
| 1  | 3  | A  |
| 2  | 1  | A  |
| 3  | 2  | B  |
| 4  | 3  | B  |
| 5  | 1  | A  |
| 6  | 2  | B  |
  
נחשב את Gini Impurity של הצומת השורש:
- 3 דגימות מקטגוריה A (p_A = 3/6 = 0.5)
- 3 דגימות מקטגוריה B (p_B = 3/6 = 0.5)
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(root)%20=%201%20-%20[(0.5)^2%20+%20(0.5)^2]%20=%201%20-%200.5%20=%200.5"/></p>  
  
  
  
 #### חישוב Gini של השורש (Root)
  
סופרים כמה מכל קטגוריה:
  
- A: 3 דגימות → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{3}{6}"/></p>  
  
- B: 3 דגימות → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_B%20=%20\frac{3}{6}"/></p>  
  
  
נחשב Gini impurity בשורש:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(root)%20=%201%20-%20(0.5^2%20+%200.5^2)%20=%201%20-%20(0.25%20+%200.25)%20=%200.5"/></p>  
  
  
**✂️ נבחן פיצול לפי X1 <= 3**
  
####  קבוצה שמאלית (X1 <= 3):
  
- דגימות: (1,A), (2,A), (3,B)  
- A: 2 מתוך 3 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{2}{3},%20p_B%20=%20\frac{1}{3}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(left)%20=%201%20-%20\left(\left(\frac{2}{3}\right)^2%20+%20\left(\frac{1}{3}\right)^2\right)%20=%201%20-%20\left(\frac{4}{9}%20+%20\frac{1}{9}\right)%20=%201%20-%20\frac{5}{9}%20=%20\frac{4}{9}%20\approx%200.44"/></p>  
  
  
####  קבוצה ימנית (X1 > 3):
  
- דגימות: (4,B), (5,A), (6,B)  
- A: 1 מתוך 3 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{1}{3},%20p_B%20=%20\frac{2}{3}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(right)%20=%201%20-%20\left(\left(\frac{1}{3}\right)^2%20+%20\left(\frac{2}{3}\right)^2\right)%20=%201%20-%20\left(\frac{1}{9}%20+%20\frac{4}{9}\right)%20=%201%20-%20\frac{5}{9}%20=%20\frac{4}{9}%20\approx%200.44"/></p>  
  
  
#### חישוב Gini הכולל לאחר הפיצול:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G_{weighted}%20=%20\frac{3}{6}%20\cdot%200.44%20+%20\frac{3}{6}%20\cdot%200.44%20=%200.44"/></p>  
  
  
#### רווח (Gain) מהפיצול:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gain%20=%20G(root)%20-%20G_{weighted}%20=%200.5%20-%200.44%20=%200.06"/></p>  
  
  
####  ✂️ נבחן פיצול לפי X2 <= 2
  
**קבוצה שמאלית (X2 <= 2):**
  
- דגימות: (2,A), (3,B), (5,A), (6,B)  
- A: 2, B: 2 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20p_B%20=%200.5"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(left)%20=%201%20-%20(0.5^2%20+%200.5^2)%20=%200.5"/></p>  
  
  
**קבוצה ימנית (X2 > 2):**
  
- דגימות: (1,A), (4,B)  
- A: 1, B: 1 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20p_B%20=%200.5"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(right)%20=%200.5"/></p>  
  
  
### Gini משוקלל:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G_{weighted}%20=%20\frac{4}{6}%20\cdot%200.5%20+%20\frac{2}{6}%20\cdot%200.5%20=%200.5"/></p>  
  
  
### רווח:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gain%20=%200.5%20-%200.5%20=%200"/></p>  
  
  
#### ✅ מסקנה:
  
- הפיצול לפי **X1** מפחית את Gini ל-0.44 → רווח (Gain) של **0.06**
- הפיצול לפי **X2** לא משפר את Gini כלל
  
🔮 לכן עדיף לפצל לפי **X1 ≤ 3**
  
---
  
## כיצד Gini Impurity עוזר בבניית עץ החלטה
  
תהליך בניית עץ החלטה באמצעות Gini Impurity כולל את השלבים הבאים:
  
1. **חישוב Gini Impurity של הצומת הנוכחי**
2. **עבור כל מאפיין אפשרי**:
   - עבור כל נקודת פיצול אפשרית במאפיין:
     - פיצול הנתונים
     - חישוב Gini Impurity המשוקלל של צמתי הבנים הנוצרים
     - חישוב הרווח (Gini Gain)
3. **בחירת המאפיין ונקודת הפיצול** שמספקים את הרווח המקסימלי
4. **יצירת צמתי בנים** באמצעות הפיצול הזה
5. **חזרה על התהליך באופן רקורסיבי** על כל צומת בן עד שמתקיים קריטריון עצירה
  
היתרונות של שימוש ב-Gini Impurity:
  
1. **בחירת פיצולים אופטימליים**: עוזר לבחור פיצולים שמפרידים את הקטגוריות בצורה טובה
2. **שיפור הדיוק**: מוביל לפיצולים שמשפרים את יכולת החיזוי של העץ
3. **בניית עץ מאוזן**: עוזר בבניית עץ שאינו נוטה יותר מדי לכיוון קטגוריה מסוימת
4. **שליטה בגודל העץ**: ניתן להגדיר סף מינימלי לרווח (Gini Gain) כדי למנוע פיצולים מיותרים
  
## סיכום
  
אי-טוהר ג'יני הוא כלי חשוב באלגוריתמים של עצי החלטה שעוזר לקבוע כיצד לפצל את הנתונים באופן אופטימלי. הוא מודד את מידת האי-טוהר של צומת ומאפשר השוואה בין פיצולים שונים כדי לבחור את הטוב ביותר.
  
המדד משתלב בתהליך הבנייה של עץ ההחלטה ומוביל ליצירת עץ שמפריד את הקטגוריות ביעילות ומשפר את הדיוק של המודל. ככל שערך ה-Gini Impurity קטן יותר, כך הצומת טהור יותר וההבדלה בין הקטגוריות טובה יותר.
  
<a id="example" >--</a>
# דוגמא בפייטון

נניח שיש לנו מערכת נתונים פשוטה עם שני מאפיינים (X1, X2) וקטגוריה יעד (Y) כפי שמוצג בטבלה:
  
| X1 | X2 | Y |
|----|----|----|
| 1  | 3  | A  |
| 2  | 1  | A  |
| 3  | 2  | B  |
| 4  | 3  | B  |
| 5  | 1  | A  |
| 6  | 2  | B  |

<img src="images/dec10.png" style="widht: 70%" />

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import numpy as np

# Data
X = np.array([
    [1, 3],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 1],
    [6, 2]
])

y = np.array(['A', 'A', 'B', 'B', 'A', 'B'])

# Model
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
clf.fit(X, y)

# Predictions
y_pred = clf.predict(X)

# Metrics
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred, average='macro')
recall = recall_score(y, y_pred, average='macro')
f1 = f1_score(y, y_pred, average='macro')
cm = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)

print("Accuracy:", accuracy)
print("Precision (macro):", precision)
print("Recall (macro):", recall)
print("F1 Score (macro):", f1)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", report)
```

Output:
```
Accuracy: 1.0
Precision (macro): 1.0
Recall (macro): 1.0
F1 Score (macro): 1.0
Confusion Matrix:
 [[3 0]
  [0 3]]
Classification Report:
               precision    recall  f1-score   support

           A       1.00      1.00      1.00         3
           B       1.00      1.00      1.00         3

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6
```

1. **Accuracy (דיוק)**  
   - אחוז התחזיות הנכונות מתוך כלל התחזיות  
   - מתאים כשיש **איזון** בין הקטגוריות

2. **Precision (דיוק חיובי)**  
   - כמה מתוך התחזיות שהיו **חיוביות** היו נכונות  
   - חשוב כשעלות של **False Positives** גבוהה

3. **Recall (רגישות)**  
   - כמה מתוך כל המקרים **החיוביים האמיתיים** זוהו נכון  
   - חשוב כשעלות של **False Negatives** גבוהה

4. **F1 Score**  
   - ממוצע הרמוני של **Precision** ו-**Recall**  
   - טוב כשיש **אי-איזון** בין הקטגוריות

   ממוצע הרמוני שווה למספר המספרים חלקי סכום ההופכיים שלהם

5. **Confusion Matrix**  
   - טבלה שמציגה את מספר התחזיות בכל קטגוריה: True Positives, False Positives, True Negatives, False Negatives

