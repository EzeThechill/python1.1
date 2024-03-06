import sqlite3
conn = sqlite3.connect('pelis.db')
#conn.execute("CREATE TABLE Peliculas (id integer, nombre text, duracion integer)")
sData =[(1,"Tiburon",3),(2,"Jones",2)]

cur = conn.cursor()
cur.executemany("INSERT INTO Peliculas (id, nombre, duracion)VALUES (?, ?, ?);", sData)

conn.close