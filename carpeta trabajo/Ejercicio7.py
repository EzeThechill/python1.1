# Ejercicio 1.a:
# Usar un diccionario para gestionar las características de un coche. 
# Por ejemplo, modelo, color, …Practicar añadir una característica, borrar, conseguir, ….


print("Bienvenido a Nuestra tienda de coches")

coche1={"Modelo ": "a123" ,"Color ": "Rojo","Caracteristica ": "Rapido"}

coche1.update({"Precio ": 20.000})
coche1.pop("Caracteristica ")

print(coche1)

for k , v in coche1.items():
    print(k , v)
    












# ABARTH ,500C, 500,124 Spider
# ALFA ROMEO, Giulietta, MiTo, 4C, Giulia, Stelvio
# ASTON MARTIN, DB9
# Vantage V8
# Vanquish
# Vantage V12
# Rapide
# AUDI
# A4
# A8
# A3
# TT
# A5
# A4 Allroad Quattro
# A6
# A7
# Q3
# Q5
# S5
# A1
# A6 Allroad Quattro
# S7
# S6
# S8
# RS4
# RS5
# R8














# Ejercicio 1.b:
# Colocar dos diccionarios de coches en un array (lista), para tener una estructura que pueda guardar varios tipos de coches.

# Ejercicio 2:
# Preguntar a 3 usuarios por su nombre, y la comida que más les gusta. Guardar su nombre y comida en un diccionario.
