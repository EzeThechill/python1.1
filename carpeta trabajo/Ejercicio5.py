# Actividades
# Estás trabajando en el área de pruebas para una empresa de finanzas. 
# Crear un programa para confirmar que la variable (inflacion = 3.765) es un tipo float e inmutable.
# Usar == para comprobar los cambios realizados. Documentar tu código con comentarios. 
# PISTA: usar id(), type() y/o instance().

inflacion= 5.7

print (id(inflacion))

# Con las siguientes variables, imprimir la suma de todos que son del tipo int (número entero). 
# La respuesta en este caso es 15.
# a = 5
# b = 4.32
# c = 10
# PISTA: usar if, id(), type() y/o instance().

a= 5
b= 4.32
c= 10

suma=0
if isinstance(a,int):
    suma +=a 
if isinstance(b,int):
    suma +=b
if isinstance(c,int):
    suma +=c
print(suma)

