mi_archivo = open('data/data1.txt','r',encoding="utf-8")
contenido = mi_archivo.read()


mi_archivo.close()
print(contenido)


nombre = input("Introduzca su nombre : ")

archivo_escritura = open('data/data2.txt','w')
archivo_escritura.write(nombre)
archivo_escritura.close()
