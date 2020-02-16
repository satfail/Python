numeros = [0,1,2,3,4,5]
doble = []

for numero in numeros:
    doble.append(numero*2)

print(doble)

doble_corto = [numero*2 for numero in numeros]
#doble_corto = [numero*2 for numero in range(5)]
print(doble_corto)


edades = [33,45,50,70,80]
edad_string =  [f"Mi amigo tiene {edad} " for edad in edades]
print(edad_string)

names= ["MIGUEL", "MARIAJOSE","CARMEN","LUCAS","juan","pedro"]
lowercase = [name.lower() for name in names]
print(lowercase)


impares = [edad for edad in edades if edad % 2 == 1]
print(impares)
