17 DE JUNIO EXAMEN - Escrito - Los temas a partir de hoy (27/05) no entran en el parcial o entran muy poco

HOY PRACTICA 
Validamos para evitar que el usuario rompa accidental o a proposito nuestro programa.

Interpretando consignas

Dato == "-1"
if Dato[0] == "":
   Dato = Dato [1:] #Esto es Slicing 

# Interpretando consignas

## Verificaciones

1. Se pide verificar que un dato es un número?

**RESPUESTA:** 
isnumeric
if dato.isnumeric():
   #codigo

NOTA: isnumeric no soporta nros negativos

2. Se pide verificar que tiene N cantidad de caracteres?

**RESPUESTA:** 
if len(Dato) == 10 #El == puede ser cualquier otra desigualdad (<,>,>=,<=, etc)
   #mi codigo 
if len(dato) >4:
   #Mi codigo


3. Se pide verificar que no sea un dato vacío?

**RESPUESTA:** 
if len(Dato) == 0
   #El dato esta vacio
o 
if Dato == ""
   #El dato esta vacio

4. Se pide verificar que un elemento más exista más de N veces?

**RESPUESTA:** 
Datos = "nombre,edad,genero" #Verificamos cuantas veces aparece la coma por ejemplo
if Datos.count(",") == 2:
   #Mi codigo 

5. Si tenemos que verificar que un texto contenga otro texto?

**RESPUESTA:** 
Se puede usar in 
Dato = "Hola mundo #El dato contiene hola
if "Hola" in Dato: 
   #Codigo 

Ahora con una lista 
Datos = ["Minipimer", "", "", ""]
if "Minipimer" in Datos: 

Funciona con set, diccionarios, tuplas, numeros, etc
## Repeticiones

1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?

**RESPUESTA:** 
Aca usamos for o while
Datos = ["1","2","3","4","5",....]
for dato in datos: 
   if dato.isnumeric():
       #Dato Validado
       Dato_n = int(dato) #El dato era caracter, ahora es nro
2. Hay que pedir"le 5 nombres al usuario. ¿Que hacemos?

**RESPUESTA:** 
Datos = []
while len(Datos) <5: 
   Datos.append(input("Coloca nombre:"))

Con el range #Ambos empiezan con lista vacia
for idx in range(5): #idx es pedido
   Datos.append(input("Coloque nombre:"))

3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?

**RESPUESTA:** 
while True: 
   use_in = input("Coloque datos:")
   if user_in == "Fin": #Siempre normalizar el fin por las diferentes formas que puede tener el usuario 
      break

Otra forma es.... 
in = ""
while in != "Fin": 
  in= input("Coloque un dato:")
## Archivos

1. Hay que leer un archivo: 

**RESPUESTA:** 
Pasos: 1. Abrir archivo 2. Lo leemos
f = open("Nombre del archivo. Ej: Archivo.txt", "r") #La r indica que lo vamos a leer 
contenido = f.read() # Extraifo el texto
contenido_l = f.readlines() #Extraigo el texto seprado por saltos de linea
2. Hay que escribir un archivo: 

**RESPUESTA:** 
f = open ("archivo.txt","w") #Con la w escribo el archivo 
f.write("Hola mundo") #En los () escribo lo que quiero implementar en el archivo 
3. ¿Hay que cerrar un archivo? SIEMPREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE 

**RESPUESTA:** 
Usamos close, si no forzamos el close hay riesgo que se pierda el archivo 
f.close() #De esta manera cerramos el archivo 


## Otros
1. Tenemos que solicitarle al usuario nombre, apellido y año de nacimiento ¿Que hacemos? 

nombre = input("Nombre:")
apellido = input("Apellido:")
nacimiento = input("")

#Conviene tambien poner un strip 

Ahora extendemos el 1 a 25 personas

datos = []
for idx in range(25): 
   nombre = input("Ingresar nombre:")
   apellido = input("Ingresar apellido:")
   año_nacimiento : input("Año de nacimiento: ")
   datos.append(
   {
    "nombre": nombre, 
    "apellido": apellido, 
    "año_nacimiento": año_nacimiento  
   })
   

2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible. #Si algo tiene una clave ya de entrada es un diccionario



