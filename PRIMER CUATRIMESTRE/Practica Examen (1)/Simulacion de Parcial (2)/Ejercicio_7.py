def clasificar_numero(numero): 
    if numero < 10: 
        return("chico")
    elif 10<= numero <= 50: 
        return("medio")
    else: 
        print("grande")

print(clasificar_numero(5))
print(clasificar_numero(27))
print(clasificar_numero(56))