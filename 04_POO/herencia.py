class Estudiante:
    
    def __init__(self,nombre,notas,escuela):
        self.nombre = nombre
        self.escuela = escuela
        self.notas = notas
    def media(self):
        return sum(self.notas)/len(self.notas)

#la Herencia en Python se pasa por parámetro
class EstudianteTrabajador(Estudiante):
    def __init__(self, nombre, notas, escuela,salario):
        super().__init__(nombre, notas, escuela)
        self.salario = salario
    
    #Para que no salga el objeto al llamarlo sin ()
    #Cuando no hay argumento, lo convierto a una propiedad
    @property
    def salario_mensual(self):
        return self.salario*31


juan = EstudianteTrabajador('Juan',[40,50,45,60],'UCAM',35.5)
print(juan.notas)
juan.notas.append(99)
print(juan.notas)
print(juan.media())
print(juan.salario_mensual)


class Foo:
   #cls valor de la clase, para acceso a la clase
   @classmethod
   def hi(cls):
    print(cls.__name__)

objeto = Foo()
objeto.hi()

class Bar:
    #Relacionado con la clase
    @staticmethod
    def hi():
        print("Hello I don't have parameters.")

otro_objeto = Bar()
otro_objeto.hi()
