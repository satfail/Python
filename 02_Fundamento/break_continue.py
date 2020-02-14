coches = ["ok","ok","ok","ok","error","ok","ok"]

for estado in coches:
    if estado == "error":
        print("Se paro la linea de producción")
        break
    print(estado)


#Saltar el coche con error
print("@@@@@@@@@@@@@@@@@@@@@")
for estado in coches:
    if estado == "error":
        print("Encontrado un cocher erróneo, seguimos")
        continue
    print(estado)