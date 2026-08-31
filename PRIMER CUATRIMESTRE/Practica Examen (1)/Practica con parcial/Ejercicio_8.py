numeros =int(input("Agregue numeros:"))
numeros_negativos = 0

while numeros!= 0:
    numeros = int(input("Agregue otro numero:"))
    if numeros < 0:
        numeros_negativos = numeros_negativos + 1 
   
print("Numeros negativos ingresados:", numeros_negativos)    