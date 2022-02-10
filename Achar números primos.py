
n = 0
cont = 0

while cont < 3000:
    contador = 0
    n += 1
    for i in range(1,n+1):
        if n % i == 0:
            contador += 1
        if contador > 2: break
    if contador == 2:
        cont += 1
        print(f"{n} - {cont}")
