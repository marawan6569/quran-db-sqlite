# بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ 

## Quran sqlite DB V.2.00 
### قاعدة بيانات لأيات القرأن الكريم الإصدار الأول 

### Columns: | الأعمدة
    - id (int)                     | 
    - verse_pk (text): like(S1V1)  | علامة مميزة لكل أية
        'S' for surah number       | 
        'V' for verse number       |
    - page (int)                   | رقم الصفحة 
    - hizbQuarter (int)            | الربع الذي تقع فيه الأية
    - juz (int)                    | الجزء الذي تقع فيه الأية
    - surah (int<surah number>)    | رقم السورة مثلا سورة الفاتحة رقم 1
    - verse (text)                 | نص الأية
    - verseWithoutTaskeel (text)   | نص الأية بدون تشكيل (للبحث فيه)
    - numberInSurah (int)          | رقم الأية في السورة
    - numberInQuran (int)          | رقم الأية في القرأن
    - audio (text <link>)          | رابط تلاوة الأية
    - aduio1 (text<link>)          | رابط احتياطي للتلاوة
    - aduio2 (text<link>)          | رابط احتياطي أخر للتلاوة
    - sajda (bool)                 | هل الأية تحتوي علي سجدة أم لا

<hr>

all data fetched from [quran sutanlab api](https://api.quran.sutanlab.id/)
