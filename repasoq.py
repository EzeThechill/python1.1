import math
productos = ["raqueta","balon", "guantes", "pelota"]

def convertir_m(s):
    return s.capitalize()

print(list(map(convertir_m, productos)))
print(list(map(lambda x:x.capitalize(), productos)))

for p in productos:
    print(convertir_m(p))

nuevap = [convertir_m(p) for p in productos]
print(nuevap)

captext = lambda x:x.capitalize()
print(captext("raqueta"))

numeros=[4,5,6]
print(list(map(lambda x: x+2, numeros)))

x=(tuple(map(math.sqrt, numeros)))

print(x)

x=[4,5,6]
y=[6,3,1]
z=[8,1,2]
print(tuple(map(lambda a,b,c: a*b*c, x,y,z)))

#  python -m venv .venv   
#  .venv\Scripts\activate  

#  python  -m flask run     