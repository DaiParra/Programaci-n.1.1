edad = int(input("¿Cuantos años tenes?"))
estudiante = input("¿Sos estudiante?")

if edad < 12 or estudiante == "si": 
    print("Se le aplica descuento")
else: 
    print("No tiene descuento")