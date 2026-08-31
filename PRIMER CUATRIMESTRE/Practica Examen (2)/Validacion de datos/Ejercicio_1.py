alumno = input("Coloque su nombre, el codigo de la materia y sus notas en una fila separada por ;: ").split(";")

nombre = alumno[0].strip("").title()
codigo = alumno[1].strip("").upper()

if codigo.count("-") == 1:
    partes = alumno[1].split("-")
    if partes[0].isalpha() and partes[1].isnumeric():
        print("La materia fue validada correctamente!")

tupla = tuple(alumno[2])

suma = sum(int(tupla))
promedio = suma/len(tupla)

print("Alumno:", alumno[0])
print("Materia:", codigo)
print("Notas:", tupla)
print("Promedio:", promedio)