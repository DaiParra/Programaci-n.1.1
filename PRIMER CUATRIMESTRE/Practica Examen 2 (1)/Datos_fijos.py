semana = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

numero = int(input("Coloque que dia quiere ver:"))

if 1 <= numero <= 7:
    print("Día seleccionado:", semana[numero - 1])
else:
    print("Número inválido")