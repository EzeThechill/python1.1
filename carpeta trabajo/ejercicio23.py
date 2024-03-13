frutas= ["MANZANA", "pera", "NARANJA", "uva", "MELON"]

frutas_nuevas= [fruta.lower() for fruta in frutas if frutas if fruta.isupper()]

print(frutas_nuevas)

números = [3, 54, -12, 4, -67, 99, -120]

listasPositivos= [i for i in números if i >=0]

print(listasPositivos)

numbers = [2, 6, 7, 3, 4, 8]

numbers_m = ["Par" if i%2==0 else "Impar" for i in numbers]

print(numbers_m)
# frutas_nuevas= []

# for fruta in frutas:
#     if fruta.isupper():
#         frutas_nuevas.append(fruta)


# print("Estos son nuestros productos" [frutas] )
# print(frutas_nuevas)
