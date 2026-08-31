numeros = () #int(input("Coloque un numero:")) Esto verde no se pone xq le pide un nro antes del while lo que hace que en el while se cancele y no lo cuente
positivos = 0

while numeros != 0: 
    numeros = int(input("Coloque otro numero:"))
    if numeros > 0: 
        positivos = positivos + 1

print("Nros positivos ingresados:", positivos)