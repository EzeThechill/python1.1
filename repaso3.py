s="    122,Python,es,64,un,777,lenguaje,222,de,55,66,programación   "


s= s.strip()
listastring = s.split(",")
listadepalabras = []
for i in listastring:
    if not i.isnumeric():
        listadepalabras.append(i)

resultado = ",".join(listadepalabras)
print(resultado)
# Lo bueno

