# from dataclasses import dataclass, astuple

# @dataclass
# class Empleado:
#     id: int
#     name: str
# import sqlite3

# conn= sqlite3.connect('test.db')
# cursor= conn.cursor()

# e=Empleado(5, 'Jon')
# print(astuple(e))
# cursor.execute("INSERT INTO empleados (id, name) VALUES (?, ?);", (e.name, e.salario))
# # (5,"Jon")
# conn.close

import sqlite3

conn = sqlite3.connect("pelis2.db")

conn.execute("CREATE TABLE Empleados (id INTEGER PRIMARY KEY AUTOINCREMENT, id integer, nombre text, salario float )")

conn.close