# class Guitarra:
#     def __init__(self, marca, cuerdas): 
#         self.marca = marca
#         self.cuerdas = cuerdas
#         self._precio = 100
    
#     def tocar(self):
#         print(f"Soy {self.marca} y brrn, brannn, bromm")

# main programa - instanciar / usar la clase
        
# nombre = input("Cual es el nombre de la guitarra")
# guit1 = Guitarra("les paul", 6)
# print(guit1.marca)
# print(guit1.cuerdas)

# bajo = Guitarra("bajo secillo", 4)
# bajo.cuerdas=5
# print(bajo.cuerdas)

# guit1.tocar()

# class Taza:
#     def __init__(self, liquido, cantidad):
#         self.liquido = liquido
#         self.cantidad = cantidad
    
#     def beber(self):
#         print(f"que quieres que {self.liquido} ")

# ----------------------------

# pedido = input("Que quieres que te prepare ")
# taza1 = Taza("cafe con leche", 10)
# print()

#---------------------------------

class MaquinaExpendedora:
    def __init__(self, tipo, volumen, cantidad):
        self.tipo = tipo
        self.volumen = volumen
        self.coste = cantidad

        def beber(self):
            print(f"que quieres que {self.tipo} ")

listaBebidas = []

for i in range(3):
    pedido = input("Que quieres que te prepare ")
    cuanto = input("Cuanto vas a beber ahora (0 a 100)? ")
    bebida = bebida(pedido, cuanto, 100)
    listaBebidas.append(bebida)

for bebida in listaBebidas:
    print(bebida.tipo)
    print(bebida.cantidad)
    print(bebida) #__str__
