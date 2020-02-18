#Convertir txt to csv

archivo = open('data/csv_data1.txt','r')
datos = archivo.readlines()
archivo.close
#Quito el encabezado
lineas = [line.strip() for line in datos[1:]]

for linea in lineas:
    persona = linea.split(',')
    nombre = persona[0]
    edad = persona[1]
    universidad = persona[2]
    grado = persona[3]

    print(f'{nombre.title()} tiene {edad} años y estudia {grado} en {universidad.title()}')


prueba_csv_archivo = ','.join(['Juan','45','UNEX','ITI'])
print(prueba_csv_archivo)

