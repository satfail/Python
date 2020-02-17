#Objetos
"""
estudiante = {
    'name' : 'Miguel',
    'notas' : [80,90,95,99,78,75]
    #'media' : #En diccionario no se puede se utilizan clases
}

def media(estudiante):
    return sum(estudiante['notas'])/len(estudiante['notas'])

print(media(estudiante))
"""

class Estudiante:
    
    def __init__(self,nombre,notas):
        self.nombre = nombre
        self.notas = notas
    def media(self):
        return sum(self.notas)/len(self.notas)

notas_uno = [80,90,95,99,78,75]
estudiante_uno = Estudiante("Miguel",notas_uno)

print(estudiante_uno.nombre)
print(estudiante_uno.notas)
#Metodo del objeto
print(estudiante_uno.media())
#Metodo estatico
print(Estudiante.media(estudiante_uno))
print(estudiante_uno.__class__)