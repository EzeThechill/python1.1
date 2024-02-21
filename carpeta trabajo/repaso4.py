import os
directorio = input("Pon el Nombre de tu Nuevo carpeta ")
print(os.getcwd())

if os.path.exists(directorio):
    print("Ya esta Creada esa Carpeta")
else:
    print("Se creo correctamente la Carpeta")
    os.mkdir(directorio)
    os.chdir(directorio)

    with open("file1.txt", "w") as f:
        f.write("")
    with open("file2.txt", "w") as f:
        f.write("")


print(os.getcwd())



