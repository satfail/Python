amigos = ["Miguel","Maria","Carmen","Lucas"]
tiempo = [3,4,3,2]

timers = {
    amigos[i] : tiempo[i]
    for i in range(len(amigos))
    if tiempo[i] > 2
}

print(timers)