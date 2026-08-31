numero = input("Dame un numero:")

numero_dado = int(numero)

if numero_dado > 0: 
    print ("Es positivo")
elif numero_dado < 0: 
    print("Es negativo")
else: 
    print("Es cero")