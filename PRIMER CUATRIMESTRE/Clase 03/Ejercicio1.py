contraseña_ingresada = input("ingresar contraseña:")
contraseña_almacenada ="1234" 
acceso_permitido = False 
#siempre a los archivos ponerle .py al final
if contraseña_almacenada == contraseña_ingresada:
    acceso_permitido = True 
    print ("Acceso permitido")
else:
    print ("Acceso denegado")
# if contraseña_almacenada != contraseña_ingresada: 
#     acceso_permitido = False
#     print("Acceso denegado")
print ("Gracias por usar el sistema seguro del banco") 
