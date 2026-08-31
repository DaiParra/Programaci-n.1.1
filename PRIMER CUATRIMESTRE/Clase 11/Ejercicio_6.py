nota = input("nota parcial: ")
if nota.isnumeric() and int(nota) >= 0 and int(nota)  <= 10:
    print ("es valida")
else:
    print("no es valida")