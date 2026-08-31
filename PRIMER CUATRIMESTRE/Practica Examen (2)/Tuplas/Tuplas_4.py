alumnos = ("Ana", "Juan", "Pedro", "Maria", "Sofia")

nombre = input("¿Que nombre quuiere verificar?")

if nombre in alumnos: 
    print("Si, esta en la lista!")
else: 
    print("Ese nombre no pertenece a la lista de alumnos.")