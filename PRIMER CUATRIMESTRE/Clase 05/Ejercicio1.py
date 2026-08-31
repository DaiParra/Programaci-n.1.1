salir =True #un flags 
i = 0
while salir:
#while True: #while infinito
    print(f"hola mundo, estoy al principio de la iteracion: {i}")
    i += 1
    if input("Ir a la proxima interacion? [si/no]") == "si": #poner una condicion, hasta que diga no se realiza 
        #break #hacemos que el while pare 
        #salir = False 
        continue #se salta a la proxima interaccion 
    if input("Desea salir? [si/no]") == "si": 
        salir = False 
    print(f"Estoy al final de la iteracion:{i-1}") 
print("Adios")