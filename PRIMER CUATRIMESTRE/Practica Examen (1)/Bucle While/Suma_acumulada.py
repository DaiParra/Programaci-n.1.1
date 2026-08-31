suma = 0
numero = int(input("Dame un número (0 para terminar): "))

while numero != 0: #La condicion clave esta aca, le hace la pregunta "¿0 es diferente a nro?" Si, entonces continua, cuando se No, se imprime la suma
    suma = suma + numero
    numero = int(input("Dame otro número (0 para terminar): "))

print("Suma total:", suma)