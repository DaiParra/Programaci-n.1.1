#Armar una nueva lista llamada nombres_normalizados donde cada nombre quede sin espacios sobrantes y con un formato prolijo.
nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "] 
nombres_normalizados = []
partes = nombres
a = partes[0].strip().capitalize()
b = partes[1].strip().capitalize()
c = partes[2].strip().capitalize()
d = partes[3].strip().capitalize()
e = partes[4].strip().capitalize()
normalizados = a,b,c,d,e
nombres_normalizados.append(normalizados)
print(nombres_normalizados)
