import json 
producto = {
    "nombre": "Coca",
    "precio": 950,
    "stock": 9
}

with open("producto.json", "w") as archivo: 
    json.dump(producto, archivo) 