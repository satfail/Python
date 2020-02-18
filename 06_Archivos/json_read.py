import json

file = open('data/amigos_json.txt' , 'r')
contenido = json.load(file)#Convierte en diccionario
file.close()


print(contenido['amigos'][0])


coches = [
    {'marca':'Ford', 'modelo':'Fiesta'},
    {'marca':'Ford', 'modelo':'Focus'}
]

archivo = open('data/coches_json','w')
#No indenta pero da igual
json.dump(coches,archivo)
archivo.close()

#loads para lista a diccionario 
#dumps para pasar a tipo json listas y demas
