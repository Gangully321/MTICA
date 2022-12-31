#DATA BASE CONNECTIVITY FILE-3.2

import sqlite3 
carData=[
    (1, 'Audi', 52643),
    (2, 'Merceders', 57127),
    (3, 'Nana', 32127),
    (4, 'THAR', 88888),
    (5, 'Nwift', 23643),
    (6, 'Alto', 27554),
    (7, 'Baleno', 45566)]

con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS CARS")
cur.execute("CREATE TABLE cars(id INT,Name Text,Price INT)")



cur.executemany("INSERT into cars values(?,?,?)",carData)
cur.execute("INSERT into cars values(2,'Merceders',57127)")
con.commit()
con.close()
print("values inserted.")


