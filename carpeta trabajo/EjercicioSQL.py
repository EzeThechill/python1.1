import sqlite3

conn = sqlite3.connect("pelis2.db")

# conn.execute("CREATE TABLE Peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, La id integer, nombre text, duracion integer )")



while True:

    accion = int(input("Que quieres hacer? 1. SELECT, 2. INSERT, 3 UPDATE, 4. DELETE, 5. CLOSE " ))
    
    if accion ==1:
        sSQL= "SELECT * FROM Peliculas"
        cur= conn.cursor()
        cur.execute(sSQL)
        filas =cur.fetchall()
        print("Estas son las peliculas para ver" )
        for fila in filas:
            print(fila)
    elif accion ==2:
        nombre = input("Cual es el nombre de la pelicula ")
        duracion = input("Cual es la duracion ")
        cur = conn.cursor()
        sSQL = "INSERT INTO Peliculas (nombre, duracion) VALUES (?,?)"
        cur.execute(sSQL, (nombre, duracion) )
        conn.commit()
    
    elif accion ==3:
        id = input("Cual quieres borrar? ")
        duracion = input("Que duracion tiene? ")
        
        cur = conn.cursor()
        sSQL = "UPDATE INTO Peliculas SET duracion = ? WHERE id = ?"
        cur.execute(sSQL, (duracion, id) )
        conn.commit()
    
    elif accion ==4:
        id = input("Cual quieres borrar? ")
        
        cur = conn.cursor()
        sSQL = "DELETE FROM Peliculas WHERE id = " + id
        cur.execute(sSQL)
        conn.commit()


    elif accion ==5:
        print("Cerrado")
        conn.close
        break
    
    elif accion ==6:
        nombre = input("Que peli buscas? ")
        nombre = nombre + "%"
        sSQL = "SELECT * FROM Peliculas WHERE nombre LIKE ? "
        cur = conn.cursor()
        cur.execute(sSQL, (nombre,))
        filas = cur.fetchall()
        for fila in filas:
            print(fila)
        conn.commit()

