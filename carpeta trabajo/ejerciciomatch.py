# lenguaje= input("cual es tu lenguaje de programación favorito")

# match lenguaje:
#     case "python":
#         print("A mi me gusta python tambien")
#     case "Java" | "Javascript":
#         print("Bueno, bastente compricado...")
#     case _:
#         print(f"No tengo conocimiento de este {lenguaje}")

# parametro
# def mensaje():
#     print("hola ")
#     print("adios ")
# Pep-8 guia de codigo

# def mensaje(sNombre:str, sApellido:str, iEdad:int):
#     print(f"hola  {sNombre} {sApellido} y edad {iEdad}")
#     print("adios " + sNombre)

# #main ---------------------
# # for i in range(5):
# x= input("cual es tu nombre ")
# y= input("cual es tu apellidon ")
# z= int(input("cual es tu edad ")) 
# mensaje(x,y,z)

# def sumar(x, y):
#     return x+y

# def restar(x, y):
#     return x-y

# def multiplicar(x, y):
#     return x*y

# def dividir(x, y):
#     return x/y

# if __name__=="__main__":

#main ------------------ argumento
# resultado =sumar(20,50)
# print(resultado)

# Calculo=input()
# match sumar:
#     case "suma":
#         print("numero")
#     case "":
#         print("Bueno")
#     case _:
#         print(f" {}")


# Crear una función square(x) que devuelve la raíz cuadrada de un número. 



# como arquitecto
# quiero calcular metros cuadrados (m2)
# de una superficie (largo y ancho)
# para no tener que calcularlo de forma manual y
# posiblemente calcularlo incorectamente

def metros(largo,ancho):
    return largo + ancho

resultado=metros(2,4)
print(resultado)


# Trabajas en un restaurante de comida rápida. 
# Crear una función para pedir una hamburguesa, pizza o patatas fritas. 
# Devolver el precio (más impuestos) dependiendo de la comida deseada por el usuario. 

listadecomida={f"Hamburguesa":15 ,"Pizza":15 , "Patatas fritas":3 }
print(f"Bienvenido a nuestro restaurante de comida rápida ")
print(f"Aqui tiene nuestra comida para elegir" , [listadecomida])

pedido= input(f"Que quieres pedir ")

for k,v in listadecomida.items():
    print(k,v)


# for k in listadecomida.keys():
#     print(k)

# for v in listadecomida.values():
#     print(v)






# Crear una función para comprobar la edad de un usuario antes de que entre en una web para adultos. Si es menor a 18, devolver False.  

# Crear una función para convertir kilómetros a millas.

# Crear una función para mostrar la diferencia entre dos números enteros.

# Crear una función para comprobar si la primera letra de un string es mayúscula. Por ejemplo, “Google” devuelve True pero “google” devuelve False.

