nombres = []

for i in range(5):
    nombre = input("Coloque un nombre:")
    nombres.append(nombre)
for posicion, nombre in enumerate(nombres, start=1):
    print(posicion,".", nombre)


