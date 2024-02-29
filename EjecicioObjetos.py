class Guitarra:
    def __init__(self, marca, cuerdas=6): 
        self.marca = marca
        self.cuerdas = cuerdas
        self._precio = 100
    
    def romperCuerdas(self, cuerdasRotas):
        if cuerdasRotas > self.cuerdas:
            self.cuerdas = 0
            print("no se puede romper mas de 1")
        else:
            self.cuerdas = self.cuerdas - cuerdasRotas
            print(f"Me he quedado con {self.cuerdas} cuerdas ")
            
    def __str__(self):
        return f"Hola Guitarra {self.marca}"
     
    def tocar(self):
        if self.cuerdas > 0:
            print(f"Soy {self.marca} y brrn, brannn, bromm")
        else:
            print("Losiento no tengo cuerdas")

# main programa - instanciar / usar la clase
        
# nombre = input("Cual es el nombre de la guitarra")
guit = Guitarra("les paul", 6)
print(guit.cuerdas)
guit.romperCuerdas(1)
print(guit.cuerdas)
guit.tocar()


# class Taza:
#     def __init__(self, liquido, cantidad=100):
#         self.liquido = liquido
#         self.cantidad = cantidad
    
#     def beber(self, berberLiquido):
#         self.cantidad = self.cantidad - berberLiquido
#         print(f"que quieres que {self.liquido} ")

# # ----------------------------

# pedido = input("Que quieres que te prepare ")
# taza1 = Taza("cafe con leche", 10)
# print()

#---------------------------------

# class MaquinaExpendedora:
#     def __init__(self, tipo, volumen, cantidad):
#         self.tipo = tipo
#         self.volumen = volumen
#         self.coste = cantidad

#         def beber(self):
#             print(f"que quieres que {self.tipo} ")

# listaBebidas = []

# for i in range(3):
#     pedido = input("Que quieres que te prepare ")
#     cuanto = input("Cuanto vas a beber ahora (0 a 100)? ")
#     bebida = bebida(pedido, cuanto, 100)
#     listaBebidas.append(bebida)

# for bebida in listaBebidas:
#     print(bebida.tipo)
#     print(bebida.cantidad)
#     print(bebida) #__str__
