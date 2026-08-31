mail = input("Coloque su mail:")

mail_separado = mail.split("@")

print("usario:", mail_separado[0])
print("dominio:", mail_separado[1])