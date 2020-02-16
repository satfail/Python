def saludo():
    nombre = input("Indique su nombre : ")
    print(f"Hola {nombre}")




coche = {
    "marca" : "Ford",
    "modelo" : "Fiesta",
    "kilometros" : 23333,
    "gasolina_consumida" : 360
    }
coches = [{ "marca" : "Ford","modelo" : "Fiesta", "kilometros" : 23333,"gasolina_consumida" : 360},
            { "marca" : "Ford","modelo" : "Fiesta", "kilometros" : 213333,"gasolina_consumida" : 360},
            { "marca" : "Ford","modelo" : "Fiesta", "kilometros" :1223333,"gasolina_consumida" : 360}
]

def calcular_kpg(coche_a_calcular):
    kpg = coche_a_calcular["kilometros"] / coche_a_calcular["gasolina_consumida"]
    return kpg
    nombre = f"{coche_a_calcular['marca']} {coche_a_calcular['modelo']}"
    print(f"{nombre} hace {kpg} kilometros por litro")

for car in coches:
    kpg =calcular_kpg(car)

print(kpg)


