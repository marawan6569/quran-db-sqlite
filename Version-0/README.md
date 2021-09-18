# بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ 

## Quran sqlite DB V.0 
### قاعدة بيانات لأيات القرأن الكريم الإصدار صفر 

### Columns: | الأعمدة
    - id (int)                     | 
    - verse_pk (text): like(S1V1)  | علامة مميزة لكل أية
        'S' for surah number       | 
        'V' for verse number       |
    - surah (int<surah number>)    | رقم السورة مثلا سورة الفاتحة رقم 1
    - verse (text)                 | نص الأية
    - numberInSurah (int)          | رقم الأية في السورة
    - numberInQuran (int)          | رقم الأية في القرأن
    - audio (text <link>)          | رابط تلاوة الأية


<hr>

all data fetched from [quran sutanlab api](https://api.quran.sutanlab.id/)