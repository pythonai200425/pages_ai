# 🎯 Random Forest לבעיות ריבוי מחלקות (Multiclass Classification)
  
בוא נבין איך עובד Random Forest כאשר יש יותר משתי מחלקות (labels), כמו למשל:
- זיהוי סוג פרח (setosa / versicolor / virginica)
- סיווג לקוחות לרמות סיכון (נמוך / בינוני / גבוה)
- חיזוי ציונים לפי רמות (A / B / C / D / F)
  
## ✅ איך זה עובד?
  
רנדום פורסט **תומך בצורה טבעית ב־מולטי קלאס**, בלי צורך בעטיפות מיוחדות
הוא פשוט בונה הרבה עצים, שכל אחד מהם מסוגל לתת תחזית על מחלקה אחת מתוך כמה
  
### תהליך העבודה:
1. כל עץ מתאמן על מדגם שונה (Bootstrapping)
2. בכל פיצול בעץ: נבחרת קבוצת תכונות אקראיות
3. כל עלה מסמן **מחלקה סופית אחת** מתוך כמה אפשריות
4. בסוף כל העצים מצביעים:
   - כל עץ נותן תחזית למחלקה מסוימת
   - המודל בוחר את המחלקה שקיבלה הכי הרבה קולות (רוב)
  
  
## 🔢 דוגמה:
נניח שיש לנו שלוש מחלקות: `A`, `B`, ו־`C`
  
אם חמישה עצים נתנו את התחזיות הבאות:
- עץ 1: `A`
- עץ 2: `C`
- עץ 3: `A`
- עץ 4: `B`
- עץ 5: `A`
  
התחזית הסופית תהיה:
```
רוב קולות → מחלקה A (3 קולות)
```
  
## 📦 איך זה מיושם בפייתון (עם Scikit-learn)?
  
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
  
# טוענים דאטה עם 3 מחלקות
X, y = load_iris(return_X_y=True)
  
# פיצול ל־Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
  
# מודל Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
  
# תחזית ודו"ח דיוק
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```
  
### הפלט ייראה כך:
```
              precision    recall  f1-score   support
  
           0       1.00      1.00      1.00        19
           1       1.00      1.00      1.00        13
           2       1.00      1.00      1.00        13
  
    accuracy                           1.00        45
```
  
## ✨ יתרונות ב־Multiclass:
  
- לא צריך שינוי מיוחד בקוד — עובד כמו ב־Binary
- מתאים לכל מספר מחלקות
- נותן תחזית מאוד יציבה ועמידה לרעש
  
  
## סיכום קצר
  
| נושא | Multiclass ב־Random Forest |
|------|----------------------------|
| צריך התאמות מיוחדות? | לא |
| תחזית סופית | רוב קולות בין העצים |
| תומך בכל מספר מחלקות? | כן |
| מדויק ויציב? | מאוד ✅ |
  
  
  