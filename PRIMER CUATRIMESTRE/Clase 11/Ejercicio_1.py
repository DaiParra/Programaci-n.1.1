lineas = [
    " AnA ;8;7;9",
    " jUaN ;4;5;3", 
    " LucIA ;10;9;10"
]

nombres_limpios = []
for linea in lineas:
    #print(f"{linea}", type(linea))
    datos = linea.split(";")
    nombre_sucio = datos[0]
    nombres = nombre_sucio.strip().capitalize()
    #print(f"{nombre_sucio}"  "{nombre}")
    nombres_limpios.append(nombres)

idx = 0
for linea in lineas: 
    datos = linea.split(";")
    notas = [datos[1], datos[2], datos[3]]
    notas_txt = " - ".join(notas)
    print(notas, notas_txt)
    #print(f'Alumno:'  {nombres_limpios[idx]} - "Notas:" {notas_txt})
    idx+=1 
    
print(nombres_limpios) 