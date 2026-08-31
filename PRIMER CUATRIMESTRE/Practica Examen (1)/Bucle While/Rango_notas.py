nota = int(input("Coloque una nota del 1 al 10"))

while nota < 1 or nota > 10: 
    nota = int(input("Nota fuera del rango, vuelva a intentarlo:"))

print("La nota es:",nota)