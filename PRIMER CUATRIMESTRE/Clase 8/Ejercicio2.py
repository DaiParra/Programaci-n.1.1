persona = ("Daiana" , "19")

print(persona) 

print(persona[0]) #muestra la primera variable de la tupla 
print(persona[-1]) #muestra la ultima variable de la tupla 

for x in persona: #recorre la tupla 
    print(x)

persona[0] = "Anto" #No permite que se agreguen elementos remplazandolos por otros 