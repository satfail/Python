"""

--Peliculas 'a' añadir, 'l' list, 'f' buscar y 'q' salir

Tareas:
-Menu
-Añadir
-Listar
-Buscar
-Salir
"""
peliculas = []
def add_movie():
    name = input("Nombre de pelicula : ")
    director = input("Nombre de director : ")
    año = input("Año de pelicula : ")
    pelicula = {
        'nombre' : name,
        'director' : director,
        'año' : año
    }
    peliculas.append(pelicula)
    
def listar(peliculas):
    for pelicula in peliculas:
        print(pelicula)

def buscar():
    #año,nombre,director
    buscando_por = input("Por que caracteristica estas buscando? : ")
    valor_a_buscar = input(f"Valor de {buscando_por}  a buscar : ")
    movie = buscar_por_atributo(peliculas,valor_a_buscar, lambda x: x[buscando_por])
    listar(movie)

#Generica(object, valor que quieres obtener, funcion lambda en este caso x vale el valor del campo buscado)
def buscar_por_atributo(items,expected,finder):
    buscado = []

    for i in items:
        if finder(i) == expected:
            buscado.append(i)
    
    return buscado

     

def menu():
    print("a(Añadir)-l(listar)-f(buscar)-q(salir)")
    entrada = input("Introduzca el valor del menu : ")
    while(entrada != 'q'):
        if entrada == 'a':
            add_movie()
        elif entrada == 'l':
            listar(peliculas)
        elif entrada == 'f':
            buscar()
        elif entrada == 'q':
            print("Adios!")
        else:
            print("Comando erroneo")
        print("a(Añadir)-l(listar)-f(buscar)-q(salir)")
        entrada = input("Introduzca el valor del menu : ")


menu()
        
    



