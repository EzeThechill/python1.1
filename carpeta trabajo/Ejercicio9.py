# Gestión de los correos electrónicos
# emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]

# # Generar un informe con:
# # - los nombres de los usuarios
# # - los dominios únicos (sin repetir el dominio)

# nombres = ("maria", "jon", "david")
# # con los nombres, generar un texto en formato CSV con nuevos correos e.g maria@nazaret.eus,jon@nazaret.eus,david@nazaret.eus

print("Gestiónando correos")

correo= ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
listadenombres=[]
listadedominios=[]
for c in correo:
    x, y = c.split("@")
    listadenombres.append(x)
    listadedominios.append(y)

    # print(listadenombres)
    # print(listadedominios)
    # print(x, y)

 # Informes
sTexto= "Informe usuario \n"
for i in listadedominios:
    sTexto = sTexto + "," + i # + "/no"

print(sTexto)
setdedominios = set(listadedominios)
print(setdedominios)
    
with open("informe.txt", "w") as f:
    f.write(sTexto)


