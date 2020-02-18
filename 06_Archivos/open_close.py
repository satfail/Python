import json
#Setup = open, Teardown= Close
#open va a file y cuando llega al final del indent cierra
#el archivos, podemos definir estos contextManagers y modificarlos
with open('data/amigos_json.txt' , 'r') as file:
    contenido = json.load(file)#Convierte en diccionario



print(contenido['amigos'][0])


coches = [
    {'marca':'Ford', 'modelo':'Fiesta'},
    {'marca':'Ford', 'modelo':'Focus'}
]

with open('data/coches_json','w') as archivo:
    json.dump(coches,archivo)
