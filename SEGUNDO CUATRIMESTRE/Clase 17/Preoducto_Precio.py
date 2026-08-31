entrada = input("Ingresar producto y precio separados por -;- : ") 
datos = entrada.split(";")

producto = datos[0]
precio = datos[1]

precio_f = float(precio)

print(f"{producto} cuesta {precio_f}$")