lista = []
while True: 
    nombres = input("Escriba nombre:")
    if nombres == "salir":
        break
    lista.append(nombres)

def mostrar_nombres(lista): #EN UNA FUNCION SIEMPRE CONVIENE USAR ESTE METODO PARA PONERLOS EN FILA
    for nombre in lista:
        print(nombre)


mostrar_nombres(lista)

