from dataclasses import dataclass, astuple
import sqlite3

@dataclass
class Empleado:
    id: int
    name: str
    salario: float


conn= sqlite3.connect('pelis2.db')
cursor= conn.cursor()

nombre = input("Cual es tu nombre")
salario = input("Cual es tu salario")
e=Empleado(5, nombre, salario)
print(astuple(e))
cursor.execute("INSERT INTO empleados (id, name) VALUES (?, ?, ?);", astuple(e))
# (5,"Jon")
conn.comint
conn.close