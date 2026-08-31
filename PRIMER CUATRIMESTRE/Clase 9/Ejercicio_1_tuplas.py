def datos(nombre,edad):
    #nombre = input("Decime tu nombre: ")
    #edad = int(input("¿Cual es tu edad?: "))

    mayor = edad >= 18

    tupla = (nombre, edad, mayor)

    return tupla

print(datos("Daiana", 19))