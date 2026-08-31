pares = 0

for numero in range(5):
    numeros = int(input("Dame numeros diferentes:"))
    if numeros % 2 == 0: 
        pares = pares + 1

print(pares)