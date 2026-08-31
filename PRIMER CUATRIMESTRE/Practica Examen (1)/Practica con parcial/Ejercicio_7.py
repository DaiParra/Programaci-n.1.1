def clasificar_temperatura (temp): 
    #temp = int(input("Coloque una temperatura:"))
    if temp < 10: 
        print("frio")
    elif 10<= temp <= 25: 
        print("Templado")
    else: 
        print("Caluroso")

clasificar_temperatura(7) 
clasificar_temperatura(19)
clasificar_temperatura(48)