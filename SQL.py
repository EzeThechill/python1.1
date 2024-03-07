# import sqlite3
# conn = sqlite3.connect('pelis.db')
# #conn.execute("CREATE TABLE Peliculas (id integer, nombre text, duracion integer)")
# sData =[(1,"Tiburon",3),(2,"Jones",2), (2, "Coste",1)]

# nombre= input("¿Que peli?")
# cur = conn.cursor()
# cur.executemany("INSERT INTO Peliculas (id, nombre, duracion)VALUES (?, ?, ?);", sData)
# sSQL = f"INSERT INTO Peliculas(id, nombre, duracion)VALUES (?, ?, ?);"
# conn.execute(sSQL, (3,nombre, 2))
# # conn.rollback() tirar para atras
# # conn.commit()guardar los cambios
# conn.commit()

# conn.close

import sqlite3
COL_ID=0
COL_NOMBRE=1
COL_DURACION=2

conn= sqlite3.connect('pelis.db')

cur = conn.cursor()

cur.execute("SELECT * FROM Peliculas;")

rows =cur.fetchall()

for row in rows:
    # print(type(row)) #(2, 'indiana jones', 2)
    print((row[COL_DURACION])) # lista

conn.close()

while True:

    accion = int(input("que quieres? 1. SELECT, 2. INSERT, 3 UPDATE 4. DELETE"))
    
    if accion ==1:
        id = input("Cual es el tu id ? ")
    elif accion ==2:
        nombre = input("Cual es el nombre de la pelicula")
