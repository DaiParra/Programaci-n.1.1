###NIVEL 1
# frase = set()

# frase = input("Coloque una frase: ")

# for letra in frase:
#     print(letra)

frase = input("Coloque una frase: ")

letras_distintas = set()

for letra in frase:
    if letra != " ":  # para ignorar los espacios
        letras_distintas.add(letra)

print("Letras distintas:", letras_distintas)