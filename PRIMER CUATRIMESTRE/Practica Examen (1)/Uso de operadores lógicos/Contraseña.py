usuario_correcto = "admin"
password_correcta = "1234"
usuario_pedido = input("Ingrese su usuario:")
password_pedido = input("Ingrese la contraseña:")

if usuario_correcto == usuario_pedido and password_correcta == password_pedido: 
    print("Acceso concedido")
else: 
    print("Acceso denegado")