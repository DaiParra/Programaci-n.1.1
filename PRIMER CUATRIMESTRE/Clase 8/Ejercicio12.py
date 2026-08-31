alumnos = [
    {
         "nombre":"Joaquin",
         "notas":[8,3,6],
         "materias":{"programacion","matematica"}
    },
    { 
        "nombre":"Juan",
        "notas":[9,2,7],
        "materias": {"programacion"}

    },
    {
        "nombre":"Lucia",
        "notas":[8,4,8],
        "materias":{"programacion", "ingles"}

    }
]
for alumno in alumnos: #muestra solo los nombres
    print(alumno["nombre"])

for alumno in alumnos: 
    suma_notas = 0
    cantidad_notas = 0
    for nota in alumno["notas"]:
        suma_notas += nota
        cantidad_notas += 1 
    print(suma_notas, cantidad_notas)

promedio = suma_notas/cantidad_notas 

if promedio >= 4: 
    print(alumno["nombre"], "Aprobo", promedio)



