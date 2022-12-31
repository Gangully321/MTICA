#DATA BASE CONNECTIVITY FILE-2

import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("SELECT * FROM Cars")
rows=cur.fetchall()
#print(rows)
for row in rows:
    print(row)

for row in rows:
    print("{0:3}|{1:15}|{2:>5}".format(row[0],row[1],row[2]))

