class Coche:
    def __init__(self,marca,modelo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo
    def __repr__(self):
        return f'<Coche {self.marca} {self.mode}'

class Garaje:
    def __init__(self):
        super().__init__()
        self.coches = []

    def __len__(self):
        return len(self.coches)

    def add_car(self,coche):

        if not isinstance(coche, Coche):
            raise TypeError(f'Intento añadir a {coche.__class__} y se necesitan Coches(Clase)')
        self.coches.append(coche)

my_garage = Garaje()

coche = Coche('Ford','Fiesta')

try:
    my_garage.add_car('Fiesta')
except TypeError:
    print('Coche incorrecto')
except ValueError:
    print('Otro error')
finally:
    print(f'El garage tiene {len(my_garage)} coches')