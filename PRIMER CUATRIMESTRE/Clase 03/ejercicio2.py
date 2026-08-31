clave_almacenada = input("ingresar contraseña:")
clave_ingresada = "1234"
uso_clave_token = input("Usa clave token?")
if clave_almacenada == clave_ingresada:
    print("Acceso con clave")
elif uso_clave_token == "SI":
    print("Acceso permitido con clave token")
else:
    print("Acceso denegado")