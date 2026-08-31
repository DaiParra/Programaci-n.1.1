import json
#with open("guardia_house.json", "r") as archivo:
#    dato= json.load (archivo)

#print(values = guardia.values())
#print("nombre")
#print("prioridad")

archivo = open("guardia_house.json", "r")
datos = json.load(archivo)
archivo.close 

