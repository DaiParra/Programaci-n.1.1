materia = input("Ingrese código de materia: ")

materia = materia.strip()

if materia.count("-") == 1:
    partes = materia.split("-")
    parte_izquierda = partes[0]
    parte_derecha = partes[1]
    if not parte_izquierda.isalpha():
        print("Error: la parte izquierda debe contener solo letras.")
    if not parte_derecha.isnumeric():
        print("Error: la parte derecha debe contener solo números.")
    else:
        materia = materia.upper()
        print("Codigo de materia válido:", materia)
else: 
     print("Error: el codigo de la materia debe tener un solo guion.")