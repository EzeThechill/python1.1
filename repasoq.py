productos = ["raqueta","balon", "guantes", "pelota"]



def convertir_m(s):
    return s.capitalize()

print(list(map(convertir_m, productos)))

for p in productos:
    print(convertir_m(p))

nuevap = [convertir_m(p) for p in productos]
print(nuevap)

captext = lambda x:x.capitalize()
print(captext("raqueta"))