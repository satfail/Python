amigo = "Miguel"
user = input("Introduzca el Usuario : ")

if amigo == user :
    print(f"Bienvenido {user}")
else:
    print(f"Usuario Incorrecto")


amigos = ["Juan", "Pedro", "Ana"]
familia = ["Juan","Ana"]

if user in amigos:
    print(f"Bienvenido a la lista de amigos {user}")

elif user in familia:
    print(f"Bienvenido a la familia {user}")
else:
    print("No te conocemos")

