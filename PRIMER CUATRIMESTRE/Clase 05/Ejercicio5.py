def pedir_comida():
    comida = "" 
    while comida == "": 
         comida = input ("Ingresa tu comida>")
    return comida 
#print(pedir_comida())

def obtener_precio(comida):
     precio = 0 
     if comida == "hamburguesa": 
          print("hamburguesa 100$") 
          precio = 100
     elif comida == "milanesa": #antes habia un if
          print("milanesa 125$") 
          precio = 120
     elif comida == "pizza":
          print ("pizza 150")
          precio =  150 
     else:
          print("No hay, buscar en otro lado") 
     return precio 

comida = pedir_comida()
print(obtener_precio(comida)) 

