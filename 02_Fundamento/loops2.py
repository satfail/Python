coches = ["ok","ok","ok","ok","ok","ok","ok"]

for estado in coches:
    if estado == "error":
        print("Se paro la linea de producción")
        break
    print(estado)
else:
    print("Todos los coches estan bien")

#En python podemos poner un else a un loop y si no encuentra
#un break da la salida del else!