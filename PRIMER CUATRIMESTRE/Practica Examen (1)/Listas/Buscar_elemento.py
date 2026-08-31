elementos = ["agua","tierra","aire","fuego"]

elemento_buscado = input("¿Que elemento desea buscar?")

if elemento_buscado in elementos: #la calve es el in, es "en"
    print("¡Ese elemento esta en la lista!")
else: 
    print("Ese elemento no esta en la lista")