alumnos = {}

for i in range(3): 
    nombre =input("Nombre del alumno:")
    nota = int(input("Nota del alumno:"))
    alumnos[nombre] = nota

print(alumnos)