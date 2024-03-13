productos = ["raqueta","balon", "guantes", "pelota"]

captext = lambda x:x.capitalize()
print(captext("raqueta"))

def convertir_m(s):
    return s.capitalize()


for p in productos:
    print(convertir_m(p))

nuevap = [convertir_m(p) for p in productos]
print(nuevap)