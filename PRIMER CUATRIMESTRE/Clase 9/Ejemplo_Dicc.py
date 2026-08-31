#EJEMPLOS PARA RECORRER EL DICCIONARIO 

persona = {
    "nombre":"Martin",
    "edad":21,
    "ciudad":"Bariloche",
}

# Recorrer por claves 
for clave in persona: 
    print(clave, persona[clave])

# Recorrer por clave y valor 
for clave, valor in persona.items():
    print(clave, valor)

# Recorrer solo las claves
for clave in persona.keys():
    print(clave)

# Recorrer solo los valores 
for valor in persona.values(): 
    print(valor)