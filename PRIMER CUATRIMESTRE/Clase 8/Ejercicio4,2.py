def persona (nombre, edad): 
    mayor_edad = False
    if edad >= 18:
        mayor_edad = True
    return(nombre, edad, mayor_edad)

resultado = persona ("Daiana", 20)
print(persona)

