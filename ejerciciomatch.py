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
def mensaje(sNombre:str, sApellido:str, iEdad:int):
    print(f"hola  {sNombre} {sApellido} y edad {iEdad}")
    print("adios " + sNombre)

#main ---------------------
# for i in range(5):
x= input("cual es tu nombre ")
y= input("cual es tu apellidon ")
z= int(input("cual es tu edad ")) 
mensaje(x,y,z)

 
