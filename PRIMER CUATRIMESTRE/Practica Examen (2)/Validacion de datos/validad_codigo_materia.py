codigo = input("Escriba el codigo de su materia: ")

if codigo.count("-"):
    partes = codigo.split("-")
    partes[0].isalpha()
    partes [1].isnumeric()
    print("La materia fue validada correctamente!")
else: 
    print("Vuelva a escribir el codigo. Esta bien escribilo bien.")