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

- P(movie | positive) = 10 / 24 = 0.42  
- P(actor | positive) = 2 / 24 = 0.08  
- P(great | positive) = 8 / 24 = 0.33  
- P(film | positive) = 4 / 24 = 0.17

**שלילי**:

| מילה   | מופעים |
|--------|--------|
| movie  | 8      |
| actor  | 10     |
| great  | 0      |
| film   | 2      |

סה"כ מילים בקטגוריה שלילית: 20

כלומר:

- P(movie | negative) = 8 / 20 = 0.4  
- P(actor | negative) = 10 / 20 = 0.5  
- P(great | negative) = 0 / 20 = 0  
- P(film | negative) = 2 / 20 = 0.1

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
