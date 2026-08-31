numeros = 0
while True: 
    numero = int(input("Coloque numeros:"))
    numeros = numeros + numero
    if numero == 0: 
        break 
print(numeros)