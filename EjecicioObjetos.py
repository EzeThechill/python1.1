# class Guitarra:
#     def __init__(self, marca, cuerdas=6): 
#         self.marca = marca
#         self.cuerdas = cuerdas
#         self._precio = 100
    
#     def romperCuerdas(self, cuerdasRotas):
#         if cuerdasRotas > self.cuerdas:
#             self.cuerdas = 0
#             print("no se puede romper mas de 1")
#         else:
#             self.cuerdas = self.cuerdas - cuerdasRotas
#             print(f"Me he quedado con {self.cuerdas} cuerdas ")
            
#     def __str__(self):
#         return f"Hola Guitarra {self.marca}"
     
#     def tocar(self):
#         if self.cuerdas > 0:
#             print(f"Soy {self.marca} y brrn, brannn, bromm")
#         else:
#             print("Losiento no tengo cuerdas")

# main programa - instanciar / usar la clase
        
# nombre = input("Cual es el nombre de la guitarra")
# guit = Guitarra("les paul", 6)
# print(guit.cuerdas)
# guit.romperCuerdas(1)
# print(guit.cuerdas)
# guit.tocar()


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

#-------------------------------------------

# class Guitarra:
#     def __init__(self, marca, cuerdas=6): 
#         self.marca = marca
#         self.cuerdas = cuerdas
#         self._precio = 100
    
#     def romperCuerdas(self, cuerdasRotas):
#         if cuerdasRotas > self.cuerdas:
#             self.cuerdas = 0
#             print("no se puede romper mas de 1")
#         else:
#             self.cuerdas = self.cuerdas - cuerdasRotas
#             print(f"Me he quedado con {self.cuerdas} cuerdas ")
            
#     def __str__(self):
#         return f"Hola Guitarra {self.marca}"
     
#     def tocar(self):
#         print(f"Soy {self.marca} y brrn, brannn, bromm")

# class GuitarraElectrica(Guitarra):
#     def __init__(self, marca, cuerdas, distorsion):
#         super().__init__(marca, cuerdas)
#         self.distorsion = distorsion
    
#     def tocar(self):
#         print(f"Soy {self.marca} y brrn, brannn, bromm".upper())



# main programa - instanciar / usar la clase
        
# nombre = input("Cual es el nombre de la guitarra")
# guit = GuitarraElectrica("les paul", 6, 100)
# print(guit.marca)
# guit.romperCuerdas(1)
# print(guit.cuerdas)
# guit.tocar()

# class Madre:
#     def __init__(self, nonbre, edad):
#         self.edad = edad
    
#     def cocinar(selt):
#         print("me gusta el deporte")

# class Padre:
#     def __init__(self, ojos):
#       self.ojos = ojos

#     def cocinar(self):
#         print("me gusta cocinar")

# class Hijo(Madre, Padre):
#     def __init__(self,nombre, edad, ojos, estudios):
#         Madre.__init__(self, nombre, edad)
#         Padre.__init__(self, ojos, )
#         self.estudios = estudios

# jon= Hijo("Jon", 32, "azules", "programacion")
# jon.cocinar()
# jon.estudios()
# print()
# print()
# print()

# class Direccion:
#   def __init__(self, calle, ciudad):
#       self.calle = calle
#       self.ciudad = ciudad

#   def mostrar(self):
#       print(self.calle)
#       print(self.ciudad)

# class Persona:
#     def __init__(self, nombre, email):
#       self.nombre = nombre
#       self.email= email

#     def mostrar(self):
#       print(self.nombre + ' ' + self.email)

# # Agregar funcionalidad para usar la herencia múltiple
# class Contacto(Direccion, Persona):
#     def __init__(self, calle, ciudad, nombre, email, activo):
#       Direccion.__init__(self, calle, ciudad)
#       Persona.__init__(self, nombre, email)
#       self.activo = activo
    
#     def mostrar(self):
#        Direccion.mostrar(self)
#        Persona.mostrar(self)
#        print(self.activo)
    

# # Instanciar un contacto que es activo (True)
# jon = Contacto('Jon', 'tugrp@example.com', 'Calle 1', 'Ciudad 1', True) 
# jon.mostrar()
# e= Empleado()
# jon.mostrarEstado(e) 




# Mostrar un mensaje cuando el vehículo está conduciendo
# Por defecto, venden vehículos sin gasolina
# Cuando el nivel de gasolina es 0, el vehículo no puede conducir más
# Si esta averiado (si o no), tampoco puede conducir
# Si llenas más gasolina que el nivel máximo, mostrar un mensaje de error
# Al conducir, consume fuel


# Por ejemplo:
# rav4 = Vehiculo("Toyota", "rav4", "diesel")
# rav4.conducir()   # Lo siento, no te queda gasolina.
# rav4.actualizar_deposito(10)
# rav4.conducir()  # El rav4 está conduciendo.

class Vehiculo:
    def __init__(self, marca, modelo, tipo, fuel_maxima:100, fuel_nivel_actual:50, averiado, ruedas:4, color):
        self.marca = marca
        self.tipo = tipo
        self.fuel_maxima = fuel_maxima
        self.fuel_nivel_actual = fuel_nivel_actual
        self.averiado = averiado
        self.ruedas = ruedas
        self.color = color
    
    def conducir(self, llenar_deposito:True, nivel_de_deposito:10, Chocar:True, accidente:True):
        print("Estas conduciendo")
        

class Camion:
    def __init__(self,marca, modelo,tipo, fuel_maxima, fuel_nivel_actual, averiado, ruedas, color, cabina):
        Vehiculo.__init__(self, marca, modelo, tipo, fuel_maxima, fuel_nivel_actual, averiado, ruedas, color )
        self.cabina = cabina

    def dormir(self):
        print("Te vas a chocar si no te levantas")

    def transportar_productos(self):
        print("transportando productos fragiles")

class Moto:
    def __init__(self, marca, modelo, tipo, fuel_maxima, fuel_nivel_actual, averiado, ruedas, color, cadena, manillar):
        Vehiculo.__init__(self, marca, modelo, tipo, fuel_maxima, fuel_nivel_actual, averiado, ruedas, color)
        self.cadena = cadena
        self.manillar = manillar

    def hacer_caballito(self):
        print("Estas haciendo un caballito increible")

#--------------

Camion = Vehiculo("Toyota", "rav4")



    


