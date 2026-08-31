nombres = {"Ana","Pedro","Juan"} # Creacion del set
print(nombres)

nombres.add("Lucia") # Agregar elemento 
print(nombres)

nombres.remove("Juan") # Elimino elemento 
print(nombres)

print("Ana" in nombres) # Consultar si un elemento pertenece al set

lista_nombres = ["Ana","Juan","Ana","Lulu"] # Convertir una lista a set para eliminar repetidos 
nombres_unicos = set(lista_nombres)
print(nombres_unicos)
