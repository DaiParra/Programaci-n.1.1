cuadrados = [x*2 for x in range(5)if(x**2)%2==0]
print(cuadrados)

#Usamos el if para achicar los resultados 
#Esto aplica para listas, conjuntos y diccionarios 
#Se pueden usar todas las condidiones que quieras, and, or

#Este es condicional a la derecha, podemos poner un condicional a la izquierda para determinar la salida, el de la derecha determina la entrada.

#estados = ["Aprobados" if n >= 6 else "Desaprobado"]
productos = {"Teclado": 120, "Mouse":80, "Monito": 450}
nuevos_precios={prod:(precio*0.9 if precio>100 else precio)for prod,precio in productos.items()}

print(nuevos_precios)