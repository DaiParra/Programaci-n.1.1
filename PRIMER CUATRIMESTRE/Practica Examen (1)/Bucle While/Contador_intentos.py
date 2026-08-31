contraseña_correcta = 1234
contraseña_pedida = int(input("Escriba la contraseña:"))

while contraseña_correcta != contraseña_pedida:
    contraseña_pedida = int(input("Contraseña incorrecta. Escriba la contraseña: ")) #Cuidado con lo almacenar los valores en la variable

print("Contraseña correcta")