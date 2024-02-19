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


 
