age = int(input("Introduzca su edad : "))
puede_entrar = age>18 and age < 40

print(f"Puede entrar {puede_entrar}")

nombre =""
apellido = "Gragera"
saludo = nombre or f"Mr.{apellido}"
print(saludo)