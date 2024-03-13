

sumar=lambda x, y : x+y

print(sumar(10, 6))

print((lambda x, y: x+y) (10, 1))

# def sumar(x, y):
#     return x+y

# x= sumar(10, 5)

up= lambda s : s.upper()
print(up("hola"))

hola=lambda nombre: f"kaixo {nombre} "
print(hola("juan"))


Par = (10, 12, 14)
Impar = (11, 13, 15)

par = lambda x: "Par" if x%2==0 else "Impar"

print(par(11))

def ParImpar(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "Impar"

Positivo =lambda x: "positivo" if x>0 else "Negativo"

def PosiNgativo(x):
    if x > 0 :
        return "Positivo"
    else:
        return "Negativo o zero"
    

print(Positivo(10))


