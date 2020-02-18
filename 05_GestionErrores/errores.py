class MiError(TypeError):
    """
    Excepción de error de protocolo
    """
    def __init__(self, mensaje, code):
        super().__init__(f'Error: {code}: {mensaje}')
        self.code = code


err = MiError('Error de procolo',700)

print(err)

#Da una multiline que está en la clase
#También fuera de la clase, es para mostar la documentación
print(err.__doc__)

