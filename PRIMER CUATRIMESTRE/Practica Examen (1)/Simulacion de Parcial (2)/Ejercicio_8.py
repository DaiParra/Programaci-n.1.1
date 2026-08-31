pares = 0
while True: 
    numero = input("Coloque numeros:")
    if numero == "fin":
        break 
    numero = int(numero) #No se pide al usuario dos veces el numero, simplemente se modifica numeros
    if numero % 2 == 0: 
        pares = pares + 1

print("Cantidad de pares:",pares)