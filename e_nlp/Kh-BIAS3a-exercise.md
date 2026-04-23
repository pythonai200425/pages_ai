# תרגיל: Naive Bayes ב־NLP

## שלב 1: הגדרת הבעיה

יש לנו 35 ביקורות סרטים  
כל ביקורת כוללת טקסט ואת הסיווג שלה: חיובית או שלילית

המטרה: לחשב ידנית לאיזו קטגוריה שייך טקסט חדש בעזרת Naive Bayes

## שלב 2: הסתברויות בסיסיות (Prior)

מתוך 35 ביקורות:

- 25 חיוביות  
- 10 שליליות

לכן:

- P(positive) = 25 / 35  
- P(negative) = 10 / 35

## שלב 3: טבלת המילים (כמו בדוגמה)

**חיובי**:

| מילה   | מופעים |
|--------|--------|
| movie  | 10     |
| actor  | 2      |
| great  | 8      |
| film   | 4      |

סה"כ מילים בקטגוריה חיובית: 24

כלומר:

- P(movie | positive) = ___  
- P(actor | positive) = ___  
- P(great | positive) = ___  
- P(film | positive) = ___

**שלילי**:

| מילה   | מופעים |
|--------|--------|
| movie  | 8      |
| actor  | 10     |
| great  | 0      |
| film   | 2      |

סה"כ מילים בקטגוריה שלילית: 20

כלומר:

- P(movie | negative) = ___  
- P(actor | negative) = ___  
- P(great | negative) = ___  
- P(film | negative) = ___

## שלב 4: תרגיל חיזוי

ניקח טקסט חדש:

### "film actor"

חשב/י ידנית את שתי ההסתברויות הלא מנורמלות:

$$
Score(positive) = P(positive) \cdot P(film | positive) \cdot P(actor | positive)
$$

$$
Score(negative) = P(negative) \cdot P(film | negative) \cdot P(actor | negative)
$$

## שלב 5: החלטה

- אם Score(positive) > Score(negative) => סיווג **Positive**
- אם Score(negative) > Score(positive) => סיווג **Negative**

### תשובה סופית (למילוי הסטודנט)

"film actor" שייך לקטגוריית: __________
