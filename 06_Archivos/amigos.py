#Preguntar por 3 amigos
# Por cada uno decimos si estan cerca
# Por cada cercano, guardamos en amigoscerca.txt

# pista: readlines()

amigos = input('Introduzca amigos separados por ,').split(',')

gente = open('data/gente.txt','r',encoding="utf-8")
#el strip quita \n por cada linea en la lo leido
#funcion -en todo el foreach
gente_cerca = [line.strip() for line in gente.readlines()] #Lee creando lista
gente.close()

amigos_set = set(amigos)
gente_cerca_set = set(gente_cerca)

amigos_cerca_set = amigos_set.intersection(gente_cerca_set)

amigos_cerca_archivo = open('data/amigoscerca.txt','w',encoding="utf-8")

for amigo in amigos_cerca_set:
    print(f'{amigo} esta cerca')
    amigos_cerca_archivo.write(f'{amigo}\n')