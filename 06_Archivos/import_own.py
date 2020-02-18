#Una manera
# from funciones import file_operations
#file_operations.save('Prueba','data/test.txt')

from funciones.file_operations import save, read_file

save('Prueba','data/test.txt')
print(read_file('data/test.txt'))

