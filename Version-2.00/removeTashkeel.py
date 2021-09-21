from pyarabic.araby import strip_diacritics
import sqlite3
db = sqlite3.connect('quran.db')
cr = db.cursor()

Vers_id = 1
for i in range(1, 6237):
    cr.execute(f'SELECT verse FROM verses WHERE id == {i}')
    verse = cr.fetchall()[0][0]
    verse = verse.replace('۞', '')
    verse = verse.replace('۩', '')
    ayahWithoutTashkeel = strip_diacritics(verse)
    cr.execute(f'UPDATE verses SET verseWithoutTaskeel = "{ayahWithoutTashkeel}" WHERE id = {i}')

db.commit()
db.close()