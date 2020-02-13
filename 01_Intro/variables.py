# -*- coding: utf-8 -*-
age = 30
print(age)
age = 40
print(age)
friend_age = 50
print(friend_age)
PI=3.14159
# // division entera
integer_division = 13//5
print(integer_division)

modulo = 13%5
print(modulo)


cadena_caracteres = """Hola Mundo
Mi nombre es Miguel Angel Gragera"""
print(cadena_caracteres)
#str convierte a String
name = "Miguel"
print("Hola " + name + " " + str(age)) 
#f (funcion) y entre llaves lo que convierte
print(f"Edad: {age} ")

saludo_final = "Tenias {}, años no ?"
print(saludo_final.format(age))
nombre="Pedro"
age = 1000000
print(saludo_final.format(nombre))

#Inputs descomentar para ver

#nombre = input("Introduzca su nombre : ")
#("Hola " + nombre )

# = int(input("Introduzca su edad "))
#print(f"Tienes {age*12} meses")

age = 20


pregunta = age>=15
print(pregunta)
pregunta = age<=15
print(pregunta)