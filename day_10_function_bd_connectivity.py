#DATA BASE CONNECTIVITY FILE-1

import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS CARS")
cur.execute('''CREATE TABLE cars(id INT,Name Text,Price INT)''')
print("tables cars created")
cur.execute("INSERT into cars values(1,'Audi',52643)")
cur.execute("INSERT into cars values(2,'Merceders',57127)")

cur.execute("INSERT into cars values(3,'Nana',32127)")
cur.execute("INSERT into cars values(4,'THAR',88888)")
cur.execute("INSERT into cars values(5,'Nwift',23643)")
cur.execute("INSERT into cars values(6,'Alto',27554)")
cur.execute("INSERT into cars values(7,'Baleno',45566)")

con.commit()
print("values in table car inserted.")


