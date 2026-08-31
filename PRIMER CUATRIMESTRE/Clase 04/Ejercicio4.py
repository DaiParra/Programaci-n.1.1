opcion = "" 
print("Selecciona la comida para llevar") 
while opcion != "Terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido:").lower() #lower es para que todo lo que escriba el usuario se ponga en minuscula 
    if opcion == "pizza":
        print("Excelente! Agregamos una pizza a tu pedido") 
    elif opcion == "terminar pedido":
        print("Cerrando pedido...") 
    else:
        print(f"Lo siento, no tenemos {opcion}, pueba con otra cosa") #nos permite poner que la opcion que puso el usuario se ponga en el texto 
print("Pedido finalizado, gracias por confiar en nosotros") 