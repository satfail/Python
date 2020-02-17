class MiFloat:
    def __init__(self,cantidad):
        self.cantidad = cantidad
    def __repr__(self):
        return f'<Mi float {self.cantidad:.2f}> '
    
    @staticmethod
    #Ya no necesitamos el objeto(self)
    def suma (valor1,valor2):
        return MiFloat(valor1+valor2)
    #Sobreescritura
    @classmethod
    def suma (cls, valor1,valor2):
        return cls(valor1+valor2)



numero = MiFloat(18.3131313)
print(numero)


#Ya se parece a Java
nuevo_numero = MiFloat.suma(19.1221,0.3123123)
print(nuevo_numero)


class Euro(MiFloat):
    def __init__(self, cantidad):
        super().__init__(cantidad)
        self.simbolo = '€'

    def __repr__(self):
         return f'<Euro {self.cantidad:.2f}{self.simbolo}>'


money = Euro(18.12312)
print(money)

money2= Euro.suma(12,123.3132)
print(money2)#Ahora devuelveun Mifloat, sin la sobreescritura
#Para arreglarlo classmethod y devuelve el valor y la clase

#Static --> No van a heredar de la clase
#classmethod --> Puede que haya herencia