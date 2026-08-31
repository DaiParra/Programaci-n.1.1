#PATOVICA 
#Preguntar si tiene dni y es mayor de 18, si es true permitir acceso, sino no 

documento = input("¿Tiene documento? (si/no):") #se agrega el si/no para claridad, cosa que minimice lo q puede poner a dos valores y que sea mas claro en if 
edad = int(input("¿edad?")) #se agrega el input adentro del int porque input pide texto e int lo convierte en nro entero que guarda en edad

if documento == "si" and edad >= 18:
    print ("permitido acceso") 
else: 
    print ("no tiene acceso")