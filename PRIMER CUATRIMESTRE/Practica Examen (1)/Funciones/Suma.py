def suma (): 
    a = int(input("Escriba el primer numero:"))
    b = int(input("Escriba el segundo numero:"))
    print(a+b)

suma()

#OTRA MANERA ES:

def sumar(a, b):
    return a + b #Te devuelve la suma de a + b

resultado = sumar(5, 3)

print(resultado)