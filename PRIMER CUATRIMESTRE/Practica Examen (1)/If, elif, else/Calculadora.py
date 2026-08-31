a = int(input("Numero 1:"))
b = int(input("Numero 2:"))
operacion = input("¿Que operacion queres hacer?")

if operacion == "suma":
    print(a+b)
elif operacion == "resta":
    print(a-b)
elif operacion == "multiplicacion":
    print(a*b)
elif operacion == "division":
    print(a/b)