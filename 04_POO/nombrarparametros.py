class Pelicula:
    def __init__(self,nombre,año):
        super().__init__()
        self.nombre = nombre
        self.año = año

matrix = Pelicula('The Matrix',1994)

print(matrix.nombre)