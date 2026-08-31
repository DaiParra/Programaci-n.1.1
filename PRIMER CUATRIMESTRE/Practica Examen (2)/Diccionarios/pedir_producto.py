productos = {
    "mouse": 12000,
    "teclado": 25000,
    "monitor": 180000
}

produc_selecc = input("¿Que producto quiere seleccionar?")
if produc_selecc in productos: 
    print(productos[produc_selecc])
else: 
    print("No tenemos ese producto. Por favor elija otro.")