import sqlite3
db = sqlite3.connect('quran.db')
cr = db.cursor()

Vers_id = 1
for i in range(1, 6237):
    cr.execute(f'SELECT verseWithoutTaskeel FROM verses WHERE id == {i}')
    verse = cr.fetchall()[0][0]

    ayahWithoutSpace = verse.strip()
    cr.execute(f'UPDATE verses SET verseWithoutTaskeel = "{ayahWithoutSpace}" WHERE id = {i}')

db.commit()
db.close()