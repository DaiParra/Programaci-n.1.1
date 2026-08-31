
def clasificar_nota(nota): 
    if nota < 6: 
        return("Desaprobado")
    elif 6<= nota <= 8: 
        return("Aprobado")
    else: 
        return ("Excelente")
    

print(clasificar_nota(9))
print(clasificar_nota(8))
print(clasificar_nota(5))