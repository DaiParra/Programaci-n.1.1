import json 
with open("producto.json", "r") as archivo: #lectura 
    datos = json.load(archivo) #json.load() lee archivo JSON y devuelve estructuras de python 
print(type(datos))
print(datos["nombre"])
print(type(datos["nombre"]))