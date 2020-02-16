for n in range(2,10):
    for x in range (2,n): ## hasta sqrt(n) Regla para primos
        if n % x == 0:
            print(f"{n} igual  {x} * {n/x} " )
            break
    else:
        print(f"{n} es numero primo")
