
class Animal:
    def __init__(self, tipo, caracteristica, peso):
        self.tipo = tipo
        self.caracteristica = caracteristica
        self.peso = 100
    
    def hablar(self):
        print("estos animales hablan")

# ----------------------------

class Gato:
    def __init__(self, nombre,):
        self.nombre = nombre
    
    def hablar(self):
        print(f"meooow de {self.nombre}")


class Perro:
    def __init__(self, nombre,):
        self.nombre = nombre
    
    def hablar(self):
        print(f"woof woooof woof de {self.nombre}")

# if __name__=="__main__":
#     listaAnimales= [Gato("loto"), Perro("rex", "hueso")]

#     for animal in listaAnimales:
#         animal.hablar()
        

        


