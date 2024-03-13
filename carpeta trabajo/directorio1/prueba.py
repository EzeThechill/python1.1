import os
print(os.getcwd())
os.chdir("..")
with open("prueba2.txt", "w") as f:
    f.write("Cosas que se revelan en el avismo de tu mente")
# s=os.path.join()
    