entrada = input("Coloque los nros que desee (separados por comas): ") #Pide nuemros

numeros = entrada.split(",") #Elimina las comas

numeros = [int(n) for n in numeros] #Crea una lista 

tupla = tuple(numeros) #Crea una tupla

suma_total = sum(tupla)
nro_mayor = max(tupla)
nro_menor = min(tupla)

print("La suma total es:", suma_total)
print("El nro mayor es:", nro_mayor)
print("El nro menor es:", nro_menor)