numero_secreto = 12 
numero_propuesto = int(input("Adivina el numero:"))

while numero_secreto != numero_propuesto: 
    if numero_propuesto > numero_secreto: 
        print("mas bajo")
        numero_propuesto = int(input("Vuelva a intenar. Adivina el numero:"))
    elif numero_propuesto < numero_secreto: 
        print("mas alto")
        numero_propuesto = int(input("Vuelva a intenar. Adivina el numero:"))

print("¡NUMERO CORRECTO!")