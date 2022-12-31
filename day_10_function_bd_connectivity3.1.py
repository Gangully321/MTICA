#DATA BASE CONNECTIVITY FILE-3.2

import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute("SELECT * FROM Cars")
rows=cur.fetchall()
#print(rows)
for row in rows:
    print(row)
