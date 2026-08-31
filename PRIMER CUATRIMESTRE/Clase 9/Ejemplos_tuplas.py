persona = ("Ana",20)

print(persona[0]) #Acceder por indice 
print(persona[-1])

nombre, edad = persona #Desempaquetar valores 
print(nombre)
print(edad)

for x in persona: #Recorrer con un for
    print(x)

persona [0] = "Pablo" #ES UNMUTABLE, esto no lo puedo hacer con la tupla