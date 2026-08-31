comandos = [" ENCENDER","apagar"," Estado","REINICIAR"," salir"]

normalizados = [comando.strip().capitalize() for comando in comandos]

print(normalizados)