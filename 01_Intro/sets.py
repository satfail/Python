# sets -> {}
# Solo añade elementos únicos
alumnos_ciencia = {"Miguel", "Maria Jose"}
alumnos_matematicas =  {"Miguel", "Lucas"}

alumnos_ciencia.add("Maria Jose")
alumnos_ciencia.add("Maria Jose")
alumnos_ciencia.add("Maria Jose")

print(alumnos_ciencia)

ciencia_y_no_matematicas = alumnos_ciencia.difference(alumnos_matematicas)
print(ciencia_y_no_matematicas)

#que no estan en los dos
no_en_los_dos = alumnos_ciencia.symmetric_difference(alumnos_matematicas)
print(no_en_los_dos)

#en los dos
en_los_dos = alumnos_ciencia.intersection(alumnos_matematicas)
print(en_los_dos)

todos_los_alumnos = alumnos_ciencia.union(alumnos_matematicas)
print(todos_los_alumnos)