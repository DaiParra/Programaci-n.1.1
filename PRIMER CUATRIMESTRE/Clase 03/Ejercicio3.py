monto = 900
es_cliente_vip = False
tiene_cupon = True 

if monto > 1000 and es_cliente_vip or tiene_cupon: 
    print ("se aplica descuento")
else:
    print("no hay descuento")