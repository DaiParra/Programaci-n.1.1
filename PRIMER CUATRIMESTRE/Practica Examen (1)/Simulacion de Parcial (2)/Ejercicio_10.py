numeros = []
positivos = []
while True: 
    numero = int(input("Coloque nros:"))
    if numero == 0:
        break
    numeros.append(numero)
    if numero > 0: 
        positivos.append(numero)

print("Cantidad completa de nros:", numeros)
print("Cantidad de nros positivos:", positivos)