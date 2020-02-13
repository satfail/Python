#No acepta duplicados, es como un mapa Id+Valor

años_amigos = {"Miguel" :33 , "Maria Jose":35 , "Lucas":3}

print(años_amigos["Miguel"])

años_amigos["Carmen"] = 1

print(años_amigos["Carmen"])


amigos = (
    {"name" : "Miguel", "edad" :33},
    {"name" : "Maria Jose", "edad" :34},
    {"name" : "Carmen", "edad" :1}
        )

print(amigos[0]["name"])

#Transformar tupla en diccionario

amigos = [("Miguel",33),("Mj",34),("Carmen",1)]
amigos = dict(amigos)
print(amigos)

