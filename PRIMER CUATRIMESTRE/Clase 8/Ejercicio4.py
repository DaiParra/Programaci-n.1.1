#def persona (nombre, edad): 
#    nombre = "Daiana"
#    edad = "20" 
#    if edad > 18 == True: 
#        print(True)
#    else: 
#        print (False) 

#resultado = persona 
#print(persona)

#correccion de codigo

def persona (nombre, edad): 
    mayor_edad = False
    if edad >= 18:
        mayor_edad = True
    return(nombre, edad, mayor_edad)

resultado = persona ("Daiana", 20)
print(persona)

