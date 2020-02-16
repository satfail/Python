def add ( x, y=3):
    return x+y

print(add(5,16))
print(add(5))



print (1,2,3,4,5, sep = " - ")#Hay argumentos


# funciones lambda

#normal
def dividir(x,y):
    return x/y

#lamda #parametros y return
dividiendo = lambda x,y : x/y 
print(dividiendo(12,3))


operaciones = {
    "media" : lambda total: sum(total) / len(total),
    "total" : sum, #lambda total :sum(total),
    "top" : max #lambda total :max(total)

}

estudiantes= [
    {"nombre":"Miguel", "notas": (67,79,78,90)},
    {"nombre":"Mj", "notas": (97,79,78,50)},
    {"nombre":"Carmen", "notas": (64,49,58,90)}
]

operation=input("media/total/top : ")
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    print(f"{nombre}")
    result = operaciones[operation](notas)
    print(result)








