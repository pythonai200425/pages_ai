# תרגיל – Hierarchical Clustering KMEAN PCA

חברת שיווק מחזיקה דאטה של לקוחות, והפעם נשתמש בקובץ **`wine_dataset.csv`** הנמצא בתוך ספריית **CSV**. החברה רוצה לקבץ את הלקוחות (או במקרה זה, סוגי היין) לקבוצות דומות, בלי לדעת מראש כמה קבוצות יש

## קובץ הנתונים

* שם הקובץ: **wine_dataset.csv**

## משימות

1. טען את הקובץ `CSV/wine_dataset.csv` ל־DataFrame בשם `df`
2. שמור רק עמודות מספריות (נקה עמודות טקסט אם קיימות)
3. בצע **Scaling** לכל העמודות המספריות באמצעות `StandardScaler` או `MinMaxScaler`
4. בנה **Hierarchical Clustering** עם `linkage` ושיטת `ward` על הנתונים המנורמלים
5. צייר **Dendrogram** עם `dendrogram` ובחר מספר קבוצות (k) בהתאם לתרשים
6. חתוך את העץ באמצעות `fcluster` ל־k קבוצות והוסף את התוויות כעמודה `cluster` ל־DataFrame
7. הדפס ספירה של כמה דגימות יש בכל קבוצה באמצעות `value_counts`
8. צור ב- KMEAN את אותו מספר הקבוצות וספור כמה יש בכל קבוצה. האם יצא מספרים זהים? מדוע לדעתך
9. נסה לצמצם את מספר הפיצ'רים באמצעות PCA, הדפס את רמת השונות אחרי הוספת כל PCA כפי שעשינו בכיתה  

**Submission email**: [pythonai200425+unsuphw@gmail.com](mailto:pythonai200425+unsuphw@gmail.com)
