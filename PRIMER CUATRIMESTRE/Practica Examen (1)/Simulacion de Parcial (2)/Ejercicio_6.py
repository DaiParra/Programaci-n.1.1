animales = []

for i in range(3):
    animal = input("Coloque un animal: ")
    animales.append(animal)
for posicion, animales in enumerate(animales, start=1):
    print(posicion, ".", animales)