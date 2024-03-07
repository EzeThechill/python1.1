import sqlite3

conn = sqlite3.connect("pelis2.db")

# conn.execute("CREATE TABLE Peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, La id integer, nombre text, duracion integer )")

peliculas=("India", "La Noche", "El Dia", "El Circo")

while True:

    accion = int(input("que quieres? 1. SELECT, 2. INSERT, 3 UPDATE 4. DELETE 5. CLOSE" ))
    
    if accion ==1:
        sSQL= "SELECT * FROM Peliculas"
        cur= conn.cursor()
        cur.execute(sSQL)
        filas =cur.fetchall()
        print("Estas son las peliculas para ver" [peliculas] )
        for fila in filas:
            print(fila)
    elif accion ==2:
        nombre = input("Cual es el nombre de la pelicula ")
        duracion = input("Cual es la duracion ")
        cur = conn.cursor()
        sSQL = "INSERT INTO Peliculas (nombre, duracion) VALUES (?,?)"
        cur.execute(sSQL, (nombre, duracion) )
        conn.commit()
    elif accion ==5:
        print("cerrado")
        conn.close
        break
    else:
        pass

