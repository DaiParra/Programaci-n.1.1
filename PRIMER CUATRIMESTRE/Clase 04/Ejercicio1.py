contraseña_registrada = "1234" 
contraseña_correcta = False 

while contraseña_correcta == False:
    contraseña_ingresada = input("Ingresar contraseña:") 
    if contraseña_ingresada == contraseña_registrada: 
        contraseña_correcta = True 

print("Acceso permitido") 