colores = []

for i in range(4): #no conviene por le variable en i, es mejor i y otra cosa
    color = input("Coloque su color:")
    colores.append(color) #importante que lo guardes con append en la listas

for posicion, colores in enumerate (colores, start = 1): #Recorre la lista "colores" y guarda en "posicion" la posicion y en "colores" el color 
    print(posicion, ".", colores) # en esa vuelta. “Para cada posición y color dentro de la lista colores, enumerando desde 1…” 