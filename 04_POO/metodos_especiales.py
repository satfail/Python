class Estudiante:
    def __init__(self,nombre):
        super().__init__()
        self.nombre = nombre
    
#Todo es un objeto en python
peliculas = ['Matrix','Buscando a Nemo']
print(peliculas.__class__)
print("Hola".__class__)

#So..
print(len(peliculas))


class Garage:
    def __init__(self):
        super().__init__()
        self.coches = []
    def __len__(self):
        return len(self.coches)
    #Para que soporte indexing
    def __getitem__(self,i):
        return self.coches[i]
    # Retorna string que reperesenta al objeto
    def __repr__(self):
        return f'Garage {self.coches}'
    def __str__(self):
        return f'Garage con {len(self)} coches'
ford = Garage()
ford.coches.append('Fiesta')
ford.coches.append('Focus')
#Hay que sobreescribir los metodos para decir donde queremos que nos digua cuantos hay
print(ford.coches)
print(len(ford.coches))
print(ford[1])

#Se pueda hace con los dos metodos definidos
#Los necesita para hacer el foreach por dentro
for coche in ford:
    print(coche)


#toString
print(ford)
#_repr para el debugging si estan las dos
# es mejor esta si solo hay uno, pero lo suyo son las 2