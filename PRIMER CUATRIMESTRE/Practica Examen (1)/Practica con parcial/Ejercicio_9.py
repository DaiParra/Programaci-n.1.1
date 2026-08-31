productos = input("Seleccione su producto:")
lista_productos = []

while productos != "fin": 
    productos = input("Siga seleccionando productos:")
    if productos != "fin":
        lista_productos.append(productos)


def mostrar_pedido (): 
    for producto in lista_productos: 
        print(producto)

print("Numero de productos:", len(lista_productos))
mostrar_pedido()