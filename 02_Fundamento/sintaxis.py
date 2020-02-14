# Asignación multiple
currencies = 0.8 , 1.2
usd, eur = currencies


amigos_y_edad = [["Miguel", 33],["Lucas", 3],["Carmen", 1]]

for nombre,edad in amigos_y_edad:
    print(f"{nombre} tiene {edad} ")

#Iterar en diccionarios key : value
amigos = {"Miguel" :33 , "Maria Jose":35 , "Lucas":3}

for edad in amigos.values():
    print(edad)

for nombre,edad in amigos.items():
    print(f"{nombre} tiene {edad} años ")


