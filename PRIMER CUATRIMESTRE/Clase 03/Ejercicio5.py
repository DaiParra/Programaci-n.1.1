#LAVAPLATOS
#Juan, Pedro y Mateo tienen que lavar 6 platos, un plato cada uno
#imprimir cada que uno de ellos lave un plato, indicando su nombre 

personas = ["Juan", "Pedro", "Mateo"] 

for i in range(6):
    print("plato", i+1, "lava", personas[i%3]) #el % sirve porque genera un patron repetitivo, es el signo q dice q sobra, 

