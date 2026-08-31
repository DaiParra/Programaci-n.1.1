tareas = []

while True: #repeti esto infinitamente
    tarea = input("Que tarea tenes que hacer: ") #guarda la respuesta en tarea
    
    if tarea == "salir":
        break #while se corta inmediatamente
    
    tareas.append(tarea)

def mostrar_tareas(tareas):
    print("Numero de tareas:",len(tareas))
    for tarea in tareas: 
        print(tarea)

mostrar_tareas(tareas)