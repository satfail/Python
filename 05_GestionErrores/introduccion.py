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
        #Si el objeto no es instancia de la clase
        if not isinstance(coche, Coche):
            raise TypeError(f'Intento añadir a {coche.__class__} y se necesitan Coches(Clase)')
            #Levanto un error
        #Si todo va ok 
        self.coches.append(coche)




my_garage = Garaje()
#my_garage.add_car("Fiesta")

coche = Coche('Ford','Fiesta')
my_garage.add_car(coche)
print(len(my_garage))



