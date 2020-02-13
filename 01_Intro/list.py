amigos = ["miguel","lucas","carmen"]
amigos_y_edad = [["Miguel", 33],["Lucas", 3],["Carmen", 1]]
print(amigos[2])
print(amigos_y_edad[0][1])

amigos.append("Maria Jose")
amigos.remove("miguel")
print(amigos)
amigos_y_edad.remove(amigos_y_edad[0])
print(amigos_y_edad)
lista_entera_a_string = ", ".join(amigos)
print(f"Mis amigos son : {lista_entera_a_string} ")


#Tuplas

tupla = ("Carmen","Lucas")
# no puedes hacer append, esto si
tupla = tupla+("Miguel",)
print(tupla)
