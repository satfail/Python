flag = True
contador = 0

while flag:
    print(contador)
    contador+=1
    if(contador == 5):
        flag = False

user_input = input("Introduzca p o q : ")

while user_input != 'q':
    if(user_input == 'p'):
        print("Hola")
    else:
        print("Error")
    user_input = input("Introduzca p o q")

#for similar al foreach
amigos = ["Miguel","Maria Jose", "Lucas", "Carmen"]

for friend in amigos:
    print(friend)

for index in range(2,20,3):
    print(index)


estudiantes = [
    {"nombre": "Miguel", "nota" : 90},
    {"nombre": "Maria Jose", "nota" : 91},
    {"nombre": "Lucas", "nota" : 93},
    {"nombre": "Carmen", "nota" : 99}

]

for alumno in estudiantes:
    print(alumno["nombre"] + " nota : " + str(alumno["nota"]))
