contraseña = input("Coloque su contraseña: ")


for caracteres in contraseña:
    len(contraseña)>= 8
    contraseña.isupper()
    contraseña.isdigit()
    print("Contraseña correctamente validada!")
else: 
    print("Escribi bien la contraseña loco.")